from google.cloud import texttospeech
import os
import wikipediaapi
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip, TextClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from mutagen.mp3 import MP3
from PIL import Image
import bing_image_downloader.downloader as bidd
from rake_nltk import Rake
from pydub import AudioSegment
import datetime
import shutil

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + "/credentials.json"
wiki_wiki = wikipediaapi.Wikipedia(
    language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)


def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            if r != g != b: return False
    return True


def toFileName(text):
    textString = ''.join(text.title().split())
    return ''.join(filter(str.isalpha, textString))


def saveImagebySearch(keyword):
    bidd.download(keyword, limit=1, output_dir='./downloads/images/addedimages/', adult_filter_off=True,
                  force_replace=False)
    specimagefile = os.listdir("./downloads/images/addedimages/{}".format(keyword))[0]
    newimg = Image.open("./downloads/images/addedimages/{}/{}".format(keyword, specimagefile))
    imgwidth, imgheight = newimg.size
    newwidth = imgwidth * 1080 // imgheight
    if newwidth > 1920:
        newwidth = 1920
    newimg = newimg.resize((newwidth, 1080))
    if is_grey_scale("./downloads/images/addedimages/{}/{}".format(keyword, specimagefile)):
        newimg = newimg.convert('RGB')

    newimg.save("./downloads/images/addedimages/{}/{}".format(keyword, specimagefile))

    return "./downloads/images/addedimages/{}/{}".format(keyword, specimagefile)


def synthesizeText(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="en-US-Wavenet-D",
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    # audioFilename = toFileName(text)
    with open("./downloads/audio/currentaudio.mp3", "wb") as out:
        out.write(response.audio_content)

    return "./downloads/audio/currentaudio.mp3"


def wikitoDict(specwiki, wikiRenderList):
    wikiDict = {}
    for sect in specwiki.sections:
        wikiDict[sect.title] = {}
        wikiRenderList.append({"title": sect.title})
        if sect.text.strip() != "":
            wikiDict[sect.title]["text"] = sect.text.split(". ")
            for sentRender in sect.text.split(". "):
                wikiRenderList.append({"content": sentRender})

        if len(sect.sections) != 0:
            wikiDict[sect.title]["sections"] = wikitoDict(sect, wikiRenderList)

    return wikiDict


def formatdatetimetosub(dt):
    subformat = str(dt).split()[1].replace(".", ",")
    if "," not in subformat:
        subformat += ",000"
    else:
        subformat = subformat[:-3]
    return subformat


def createVidSnippet(sentences, videofilename):
    intro_silence = AudioSegment.silent(duration=5000)
    intro_silence.export("./downloads/audio/runningaudio.mp3", format='mp3')
    runningsound = AudioSegment.from_mp3("./downloads/audio/runningaudio.mp3")
    videoClipCreated = VideoFileClip(videofilename)
    clips = [videoClipCreated]
    ms = 1000.0
    runningsubstring = "1\n00:00:00,000 --> 00:00:01,000\nApple Inc.\n\n"

    i = 1
    for sentence in sentences:
        i += 1
        ogdt = datetime.datetime(1990, 12, 3, 0, 0, 0, 0) + datetime.timedelta(milliseconds=ms)
        subfilestart = formatdatetimetosub(ogdt)

        if "content" in list(sentence.keys()):
            r = Rake()
            r.extract_keywords_from_text(sentence['content'])
            rankedphrases = r.get_ranked_phrases()
            bestword = ""
            if len(rankedphrases) >= 2:
                bestword += (rankedphrases[0] + "+" + rankedphrases[1])
            elif len(rankedphrases) == 1:
                bestword += rankedphrases[0]
            elif len(rankedphrases) == 0:
                bestword = "black"

            imagefilename = saveImagebySearch(bestword)
            audiofilename = synthesizeText(sentence['content'])
            lengthofaudiofile = float(MP3(audiofilename).info.length)
            deltatime = lengthofaudiofile * 1000
            text = sentence['content']
            imageClipCreated = ImageClip(imagefilename).set_position(('center', 0)).set_duration(lengthofaudiofile)
            sound = AudioSegment.from_mp3(audiofilename)
            runningsound = runningsound + sound

            clips.append(imageClipCreated)
        if "title" in list(sentence.keys()):
            textClipCreated = TextClip(sentence['title'], font='TimesNewRoman-regular', color='white',
                                       fontsize=100).set_position('center').set_duration(2)

            clips.append(textClipCreated)
            deltatime = 2000
            text = sentence['title']

        ngdt = ogdt + datetime.timedelta(milliseconds=deltatime)
        subfileend = formatdatetimetosub(ngdt)
        runningsubstring += (str(i) + "\n" + "{} --> {}".format(subfilestart, subfileend) + "\n" + text + "\n\n")
        ms += deltatime

    with open("video_subtitles.srt", 'w') as srtfile:
        srtfile.write(runningsubstring)
    runningsound.export("./downloads/audio/runningaudio.mp3", format="mp3")
    finalaudioClipCreated = AudioFileClip("./downloads/audio/runningaudio.mp3")
    concat_clip = concatenate_videoclips(clips, method="compose").set_audio(finalaudioClipCreated)
    concat_clip.write_videofile(videofilename, fps=10)
    folder = './downloads/images/addedimages'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete')


def synthesizeText(text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="en-US-Wavenet-D",
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)

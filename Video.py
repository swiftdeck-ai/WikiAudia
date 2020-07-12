from moviepy.editor import *
import os
from google.cloud import texttospeech
import wikipediaapi
from moviepy.editor import *
from mutagen.mp3 import MP3
from PIL import Image
import bing_image_downloader.downloader as bidd
from rake_nltk import Rake
import moviepy
from pydub import AudioSegment
import datetime
import shutil
import re
import nltk.tokenize
import cv2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + "/credentials.json"


def torgbformat(filepath):
    gray = cv2.imread(filepath)
    try:
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    except:
        pass
    cv2.imwrite(filepath, gray)


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


def splitintosentences(text):
    regexsplitlist = re.split("([^0-9$][.]|[.][^0-9])", text)
    for chunk in range(len(regexsplitlist)):
        if len(regexsplitlist[chunk]) == 2:
            if regexsplitlist[chunk][1] == ".":
                try:
                    regexsplitlist[chunk - 1] += regexsplitlist[chunk][0]
                except:
                    pass
            elif regexsplitlist[chunk][0] == ".":
                try:
                    regexsplitlist[chunk + 1] = regexsplitlist[chunk][1] + regexsplitlist[chunk + 1]
                except:
                    pass

    for chunkWord in regexsplitlist:
        if re.search(r"([^0-9][.]|[.][^0-9]|[^0-9][.][^0-9])", chunkWord) != None:
            regexsplitlist.pop(regexsplitlist.index(chunkWord))

    return regexsplitlist


def saveImagebySearch(keyword):
    imageformat = ""
    numberToDownload = 1
    while not (
            imageformat.lower().endswith('jpg') or imageformat.lower().endswith('png') or imageformat.lower().endswith(
        'jpeg')):
        folder = './downloads/images'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete')
        bidd.download(keyword, limit=numberToDownload, output_dir='./downloads/images/addedimages/',
                      adult_filter_off=True, force_replace=False)
        specimagefile = os.listdir("./downloads/images/addedimages/{}".format(keyword))[numberToDownload - 1]
        imageformat = specimagefile
        numberToDownload += 1

    newimg = Image.open("./downloads/images/addedimages/{}/{}".format(keyword, imageformat))
    imgwidth, imgheight = newimg.size
    newwidth = imgwidth * 1080 // imgheight
    if newwidth > 1920:
        newwidth = 1920
    newimg = newimg.resize((newwidth, 1080))

    folder = './downloads/images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete')

    newimg.save("./downloads/images/{}".format(specimagefile))
    torgbformat("./downloads/images/{}".format(specimagefile))
    return "./downloads/images/{}".format(specimagefile)


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
        if sect.title in ['See also', 'Notes', 'References', 'External links']:
            break
        wikiRenderList.append({"title": sect.title})
        if sect.text.strip() != "":
            splittext = nltk.tokenize.sent_tokenize(sect.text)
            wikiDict[sect.title]["text"] = splittext
            for sentRender in splittext:
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


def createVidSnippet(sentences, videofilename, articleTitle, subfile):
    runningsound = AudioSegment.silent(duration=0000)
    # intro_silence.export("./downloads/audio/runningaudio.mp3", format='mp3')
    # runningsound = AudioSegment.from_mp3("./downloads/audio/runningaudio.mp3")
    clips = []
    ms = 0.0
    # runningsubstring = "1\n00:00:00,000 --> 00:00:01,000\n{}\n\n".format(articleTitle)
    runningsubstring = ""

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
            # deltatime = 2000
            text = sentence['content']
            imageClipCreated = ImageClip(imagefilename).set_position(('center', 0)).set_duration(lengthofaudiofile)
            sound = AudioSegment.from_mp3(audiofilename)
            # sound = AudioSegment.silent(duration=2000)
            runningsound = runningsound + sound

            clips.append(imageClipCreated)
        if "title" in list(sentence.keys()):
            textClipCreated = TextClip(sentence['title'], font='TimesNewRoman-regular', color='white',
                                       fontsize=100).set_position('center').set_duration(2)

            clips.append(textClipCreated)
            sound = AudioSegment.silent(duration=2000)
            runningsound = runningsound + sound
            deltatime = 2000
            text = sentence['title']

        ngdt = ogdt + datetime.timedelta(milliseconds=deltatime)
        subfileend = formatdatetimetosub(ngdt)
        runningsubstring += (str(i) + "\n" + "{} --> {}".format(subfilestart, subfileend) + "\n" + text + "\n\n")
        ms += deltatime

    with open(subfile, 'w') as srtfile:
        srtfile.write(runningsubstring)
    runningsound.export("./downloads/audio/runningaudio.mp3", format="mp3")
    finalaudioClipCreated = AudioFileClip("./downloads/audio/runningaudio.mp3")
    concat_clip = concatenate_videoclips(clips, method="compose").set_audio(finalaudioClipCreated)
    concat_clip.write_videofile(videofilename, fps=10)


def create_videos(wikipediatitle):
    wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

    p_wiki = wiki_wiki.page(wikipediatitle)

    full_orderedRenderList = [{'title': wikipediatitle}]
    full_returnedDict = wikitoDict(p_wiki, full_orderedRenderList)
    createVidSnippet(
        full_orderedRenderList,
        "fullvideo.mp4",
        wikipediatitle,
        "fullvideosubs.srt"
    )

    summary_orderedRenderList = [
        {'title': wikipediatitle},
        {"title": "Summary"},
    ]

    for summarySent in nltk.tokenize.sent_tokenize(p_wiki.summary):
        summary_orderedRenderList.append({"content": summarySent})

    createVidSnippet(
        summary_orderedRenderList,
        "summaryvideo.mp4",
        wikipediatitle,
        "summaryvideosubs.srt"
    )

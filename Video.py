# STANDARD MODULES
import datetime

# IMAGE, AUDIO, AND VIDEO CREATION MODULES
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from mutagen.mp3 import MP3
from PIL import Image, ImageDraw, ImageFont
import textwrap
import moviepy
from pydub import AudioSegment

# APPLICATION PROGRAMMING INTERFACES
import wikipediaapi

# TEXT MANIPULATION MODULES
import nltk.tokenize

# LOCAL CLASSES AND FUNCTIONS
from Thumbnail import create_thumbnails_mod
from Upload import uploadvideo
from Keywords import getkeywords
from Image import saveImagebySearch
from Narration import synthesizeText
from Wikipedia import wikitoDict
from Subtitles import formatdatetimetosub

# WEB AND COMPUTER AUTOMATION MODULES
from selenium import webdriver


def createVidSnippet(sentences, videofilename, articleTitle, subfile, driver):
    runningsound = AudioSegment.from_mp3("./Downloads/audio/twinkle.mp3") + AudioSegment.silent(4000)
    introLength = MP3("./Downloads/audio/twinkle.mp3").info.length
    clips = [
        # ImageClip("./IntroPics/WikiAudiaLogoS.png").set_position(('center', 0)).set_duration(0.9).resize((1920, 1080)),
        # ImageClip("./IntroPics/WikiAudiaLogoM.png").set_position(('center', 0)).set_duration(0.15).resize((1920, 1080)),
        # ImageClip("./IntroPics/WikiAudiaLogoL.png").set_position(('center', 0)).set_duration(introLength - 1.05).resize(
        #     (1920, 1080)),
            ImageClip("./IntroPics/IntroAnimationZero.png").set_duration(0.590),
            ImageClip("./IntroPics/IntroAnimationOne.png").set_duration(1.831),
            ImageClip("./IntroPics/IntroAnimationTwo.png").set_duration(1.581),
            ImageClip("./IntroPics/IntroAnimationThree.png").set_duration(1.197),
            ImageClip("./IntroPics/IntroAnimationFour.png").set_duration(introLength - 5.256),
            ImageClip("./IntroPics/Copyright.png").set_position(('center', 0)).set_duration(2).resize((1920, 1080)),
            ImageClip("./IntroPics/Captions.png").set_position(('center', 0)).set_duration(2).resize((1920, 1080))
        ]
    ms = (introLength + 4) * 1000
    runningsubstring = ""
    descriptionString = "Video Outline:\n\n(00:00:00) - Wikiaudia Channel Intro\n"

    i = 1
    for sentence in sentences:
        i += 1
        ogdt = datetime.datetime(1990, 12, 3, 0, 0, 0, 0) + datetime.timedelta(milliseconds=ms)
        subfilestart = formatdatetimetosub(ogdt)

        if "content" in list(sentence.keys()):
            bestword = getkeywords(sentence['content'])
            print(bestword)
            imagefilename = saveImagebySearch(bestword, articleTitle, driver)
            audiofilename = synthesizeText(sentence['content'])
            lengthofaudiofile = float(MP3(audiofilename).info.length)
            deltatime = lengthofaudiofile * 1000
            # deltatime = 2000
            text = sentence['content']
            imageClipCreated = ImageClip(imagefilename).set_position(('center', 0)).set_duration(
                lengthofaudiofile).resize((1920, 1080))
            sound = AudioSegment.from_mp3(audiofilename)
            # sound = AudioSegment.silent(2000)
            runningsound = runningsound + sound

            clips.append(imageClipCreated)
        if "title" in list(sentence.keys()):
            text = sentence['title']
            imFull = Image.new('RGB', (1920, 1080))
            dFull = ImageDraw.Draw(imFull)
            customfont = ImageFont.truetype("./Fonts/CenturyGothicBold.ttf", size=100)
            lines = textwrap.wrap(text, width=28)
            _, fixedheight = customfont.getsize("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789.")
            y_text = 540 - len(lines) * fixedheight / 2
            for line in lines:
                width, height = customfont.getsize(line)
                dFull.text(((1920 - width) / 2, y_text), line, font=customfont, fill=(255, 255, 255))
                y_text += height

            imFull.save("./Downloads/images/currentimage.png")
            textClipCreated = ImageClip("./Downloads/images/currentimage.png").set_position(('center', 0)).set_duration(
                2).resize((1920, 1080))

            clips.append(textClipCreated)
            sound = AudioSegment.silent(duration=2000)
            runningsound = runningsound + sound
            deltatime = 2000
            desctimestamp = formatdatetimetosub(ogdt)[:-4]
            descriptionString += "({}) - {}\n".format(desctimestamp, text)

        ngdt = ogdt + datetime.timedelta(milliseconds=deltatime)
        subfileend = formatdatetimetosub(ngdt)
        runningsubstring += (str(i) + "\n" + "{} --> {}".format(subfilestart, subfileend) + "\n" + " ".join(
            text.replace("\n", " ").replace("\t", " ").split()) + "\n\n")
        ms += deltatime

    clips.append(
        ImageClip("./IntroPics/Disclaimer.png").set_position(('center', 0)).set_duration(2).resize((1920, 1080)))
    runningsound = runningsound + AudioSegment.silent(duration=2000)

    with open(subfile, 'w') as srtfile:
        srtfile.write(runningsubstring)
    runningsound.export("./Downloads/audio/runningaudio.mp3", format="mp3")
    finalaudioClipCreated = AudioFileClip("./Downloads/audio/runningaudio.mp3")
    concat_clip = concatenate_videoclips(clips, method="compose").set_audio(finalaudioClipCreated).resize((1920, 1080))
    concat_clip.write_videofile(videofilename, fps=10)
    return descriptionString


def create_videos(wikipediatitle):
    wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

    p_wiki = wiki_wiki.page(wikipediatitle)

    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    full_orderedRenderList = [{'title': wikipediatitle}]
    _ = wikitoDict(p_wiki, full_orderedRenderList)
    fullVideoDescString = createVidSnippet(
        full_orderedRenderList,
        "./OutputFiles/fullvideo.mp4",
        wikipediatitle,
        "./OutputFiles/fullvideosubs.srt",
        driver
    )

    summary_orderedRenderList = [
        {'title': wikipediatitle},
        {"title": "Summary"},
    ]

    articleSummary = p_wiki.summary

    for summarySent in nltk.tokenize.sent_tokenize(articleSummary):
        summary_orderedRenderList.append({"content": summarySent})

    summaryDescString = createVidSnippet(
        summary_orderedRenderList,
        "./OutputFiles/summaryvideo.mp4",
        wikipediatitle,
        "./OutputFiles/summaryvideosubs.srt",
        driver
    )

    driver.quit()

    descriptionSummary = "\n\n\n\nSource: https://en.wikipedia.org/wiki/{}\n\n\nSummary:\n\n".format(
        "_".join(wikipediatitle.split())) + articleSummary

    descriptionSocials = "\n\n\n\n\
Follow our Socials!\n \
    \nWikiaudia Instagram: https://instagram.com/wikiaudia\n \
    \nVivek's Instagram (Co-Creator): https://instagram.com/v1v3k.k \
    \nVivek's LinkedIn (Co-Creator): https://www.linkedin.com/in/vivekkogilathota1225 \
    \nVivek's Twitter (Co-Creator): https://twitter.com/v1v3krk\n\
    \nSamrat's Instagram (Co-Creator): https://instagram.com/samrat.sahoo_ \
    \nSamrat's LinkedIn (Co-Creator): https://www.linkedin.com/in/samratsahoo \
    \nSamrat's Twitter (Co-Creator): https://twitter.com/samratsahoo2013"

    fullVideoDescString += descriptionSummary
    fullVideoDescString += descriptionSocials
    summaryDescString += descriptionSocials

    create_thumbnails_mod(wikipediatitle)
    uploadvideo("./OutputFiles/fullvideo.mp4", "./OutputFiles/fullvideosubs.srt", wikipediatitle + ": Full Video",
                fullVideoDescString, "./OutputFiles/fullvideothumbnail.png")
    uploadvideo("./OutputFiles/summaryvideo.mp4", "./OutputFiles/summaryvideosubs.srt", wikipediatitle + ": Summary",
                summaryDescString, "./OutputFiles/summaryvideothumbnail.png")

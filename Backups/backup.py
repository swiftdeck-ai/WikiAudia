# from moviepy.editor import *
# import os
# from google.cloud import texttospeech
# import wikipediaapi
# from moviepy.editor import *
# from mutagen.mp3 import MP3
# from PIL import Image
# import bing_image_downloader.downloader as bidd
# from rake_nltk import Rake
# import moviepy
# from pydub import AudioSegment
# import datetime
# import shutil
# import re
# import nltk.tokenize
# import cv2
# from Thumbnail import *
# from Upload import *
# import textwrap

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + "/credentials.json"

# chrome_options = Options()  
# chrome_options.add_argument("--headless")  
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)

# def saveImagebySearch(keyword):
#     imageformat = ""
#     numberToDownload = 1
#     while not (
#             imageformat.lower().endswith('jpg') or imageformat.lower().endswith('png')):
#         folder = './downloads/images'
#         for filename in os.listdir(folder):
#             file_path = os.path.join(folder, filename)
#             try:
#                 if os.path.isfile(file_path) or os.path.islink(file_path):
#                     os.unlink(file_path)
#                 elif os.path.isdir(file_path):
#                     shutil.rmtree(file_path)
#             except Exception as e:
#                 print('Failed to delete')
#         bidd.download(keyword, limit=numberToDownload, output_dir='./downloads/images/addedimages/',
#                       adult_filter_off=True, force_replace=False)
#         specimagefile = os.listdir("./downloads/images/addedimages/{}".format(keyword))[numberToDownload - 1]
#         imageformat = specimagefile
#         numberToDownload += 1

#     newimg = Image.open("./downloads/images/addedimages/{}/{}".format(keyword, imageformat))
#     imgwidth, imgheight = newimg.size
#     newwidth = imgwidth * 1080 // imgheight
#     if newwidth > 1920:
#         newwidth = 1920
#     newimg = newimg.resize((newwidth, 1080))
#     flankingimage1 = Image.new('RGB', ((1920-newwidth)//2,1080))
#     flankingimage2 = Image.new('RGB', ((1920-newwidth)//2,1080))
#     dst = Image.new('RGB', (flankingimage1.width + newimg.width + flankingimage2.width, newimg.height))
#     dst.paste(flankingimage1, (0, 0))
#     dst.paste(newimg, (flankingimage1.width, 0))
#     dst.paste(flankingimage2, (flankingimage1.width + newimg.width, 0))

#     folder = './downloads/images'
#     for filename in os.listdir(folder):
#         file_path = os.path.join(folder, filename)
#         try:
#             if os.path.isfile(file_path) or os.path.islink(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#         except Exception as e:
#             print('Failed to delete')

#     dst = dst.convert("RGB")
#     dst.save("./downloads/images/currentimage.png")
#     return "./downloads/images/currentimage.png"

# # def saveImagebySearch(keyword):
# #     imageformat = ""
# #     numberToDownload = 1
# #     imagefilename = ""
# #     while not (
# #             imageformat.lower() == "jpg" or imageformat.lower() == "png"):
# #         folder = './downloads/images'
# #         for filename in os.listdir(folder):
# #             file_path = os.path.join(folder, filename)
# #             try:
# #                 if os.path.isfile(file_path) or os.path.islink(file_path):
# #                     os.unlink(file_path)
# #                 elif os.path.isdir(file_path):
# #                     shutil.rmtree(file_path)
# #             except Exception as e:
# #                 print('Failed to delete')
# #         driver.get("https://www.google.com/search?q={}%20&tbm=isch&hl=en&hl=en&safe=active&safe=active&tbs=ic%3Acolor%2Citp%3Aphoto%2Cisz%3Alt%2Cislt%3Axga%2Csur%3Afc%2Ciar%3Aw&ved=0CAIQpwVqFwoTCJCq6aKfzeoCFQAAAAAdAAAAABAH&biw=1905&bih=949".format(keyword))
# #         fi = driver.find_element_by_xpath("//*[@id=\"islrg\"]/div[1]/div[{}]".format(numberToDownload))
# #         fi.click()
# #         time.sleep(1)
# #         fitwo = driver.find_element_by_xpath("//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
# #         # time.sleep(3)
# #         thelink = "data:"
# #         roundsOfSearch = 0
# #         while thelink.startswith("data:") and roundsOfSearch < 10:
# #             print(roundsOfSearch)
# #             thelink = fitwo.get_attribute("src")
# #             time.sleep(1)
# #             roundsOfSearch += 1
# #         if not thelink.startswith("data:"):
# #             urllib.request.urlretrieve(thelink, "./downloads/images/currentimage.{}".format(thelink.split(".")[-1]))
# #             # bidd.download(keyword, limit=numberToDownload, output_dir='./downloads/images/addedimages/',
# #             #               adult_filter_off=True, force_replace=False)
# #             # specimagefile = os.listdir("./downloads/images/addedimages/{}".format(keyword))[numberToDownload - 1]
# #             imageformat = thelink.split(".")[-1].lower()
# #             imagefilename = "./downloads/images/currentimage.{}".format(thelink.split(".")[-1])
# #             numberToDownload += 1

# #     print("Found Image")
# #     newimg = Image.open(imagefilename)
# #     imgwidth, imgheight = newimg.size
# #     newwidth = imgwidth * 1080 // imgheight
# #     if newwidth > 1920:
# #         newwidth = 1920
# #     newimg = newimg.resize((newwidth, 1080))
# #     flankingimage1 = Image.new('RGB', ((1920-newwidth)//2,1080))
# #     flankingimage2 = Image.new('RGB', ((1920-newwidth)//2,1080))
# #     dst = Image.new('RGB', (flankingimage1.width + newimg.width + flankingimage2.width, newimg.height))
# #     dst.paste(flankingimage1, (0, 0))
# #     dst.paste(newimg, (flankingimage1.width, 0))
# #     dst.paste(flankingimage2, (flankingimage1.width + newimg.width, 0))

# #     folder = './downloads/images'
# #     for filename in os.listdir(folder):
# #         file_path = os.path.join(folder, filename)
# #         try:
# #             if os.path.isfile(file_path) or os.path.islink(file_path):
# #                 os.unlink(file_path)
# #             elif os.path.isdir(file_path):
# #                 shutil.rmtree(file_path)
# #         except Exception as e:
# #             print('Failed to delete')

# #     dst = dst.convert("RGB")
# #     dst.save("./downloads/images/currentimage.png")
# #     return "./downloads/images/currentimage.png"


# def synthesizeText(text):
#     client = texttospeech.TextToSpeechClient()
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="en-US-Wavenet-D",
#     )
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )
#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )
#     with open("./downloads/audio/currentaudio.mp3", "wb") as out:
#         out.write(response.audio_content)

#     return "./downloads/audio/currentaudio.mp3"


# def wikitoDict(specwiki, wikiRenderList):
#     wikiDict = {}
#     for sect in specwiki.sections:
#         wikiDict[sect.title] = {}
#         if sect.title in ['See also', 'Notes', 'References', 'External links']:
#             break
#         wikiRenderList.append({"title": sect.title})
#         if sect.text.strip() != "":
#             splittext = nltk.tokenize.sent_tokenize(sect.text)
#             wikiDict[sect.title]["text"] = splittext
#             for sentRender in splittext:
#                 wikiRenderList.append({"content": sentRender})

#         if len(sect.sections) != 0:
#             wikiDict[sect.title]["sections"] = wikitoDict(sect, wikiRenderList)

#     return wikiDict


# def formatdatetimetosub(dt):
#     subformat = str(dt).split()[1].replace(".", ",")
#     if "," not in subformat:
#         subformat += ",000"
#     else:
#         subformat = subformat[:-3]
#     return subformat


# def createVidSnippet(sentences, videofilename, articleTitle, subfile):
#     runningsound = AudioSegment.from_mp3("vista.mp3")
#     introLength = MP3("vista.mp3").info.length
#     clips = [ImageClip("./IntroPics/WikiAudiaLogoS.png").set_position(('center', 0)).set_duration(0.9).resize((1920,1080)),
#         ImageClip("./IntroPics/WikiAudiaLogoM.png").set_position(('center', 0)).set_duration(0.15).resize((1920,1080)),
#         ImageClip("./IntroPics/WikiAudiaLogoL.png").set_position(('center', 0)).set_duration(introLength-1.05).resize((1920,1080))
#     ]
#     ms = introLength*1000
#     runningsubstring = ""
#     descriptionString = "Video Outline:\n\n(00:00:00) - Wikiaudia Channel Intro\n"

#     i = 1
#     for sentence in sentences:
#         i += 1
#         ogdt = datetime.datetime(1990, 12, 3, 0, 0, 0, 0) + datetime.timedelta(milliseconds=ms)
#         subfilestart = formatdatetimetosub(ogdt)

#         if "content" in list(sentence.keys()):
#             r = Rake()
#             r.extract_keywords_from_text(sentence['content'])
#             rankedphrases = r.get_ranked_phrases()
#             bestword = ""
#             if len(rankedphrases) >= 1:
#                 bestword += (rankedphrases[0])
#             elif len(rankedphrases) == 0:
#                 bestword = "black"

#             imagefilename = saveImagebySearch(bestword)
#             # audiofilename = synthesizeText(sentence['content'])
#             # lengthofaudiofile = float(MP3(audiofilename).info.length)
#             # deltatime = lengthofaudiofile * 1000
#             deltatime = 2000
#             text = sentence['content']
#             imageClipCreated = ImageClip(imagefilename).set_position(('center', 0)).set_duration(2).resize((1920,1080))
#             # sound = AudioSegment.from_mp3(audiofilename)
#             sound = AudioSegment.silent(2000)
#             runningsound = runningsound + sound

#             clips.append(imageClipCreated)
#         if "title" in list(sentence.keys()):
#             text = sentence['title']
#             imFull = Image.new('RGB',(1920,1080))
#             dFull = ImageDraw.Draw(imFull)
#             customfont = ImageFont.truetype("./Fonts/Alegreya-Bold.ttf", size=100)
#             # width_text, height_text = customfont.getsize(text)
#             # top_left_x = 960 - (width_text / 2)
#             # top_left_y = 540 - (height_text / 2)
#             # xy = top_left_x, top_left_y

#             lines = textwrap.wrap(text, width=20)
#             fixedwidth, fixedheight = customfont.getsize("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789.")
#             y_text = 540 - len(lines)*fixedheight/2
#             for line in lines:
#                 width, height = customfont.getsize(line)
#                 dFull.text(((1920 - width) / 2, y_text), line, font=customfont, fill=(255,255,255))
#                 y_text += height

#             # dFull.text(xy, text, font=customfont, fill=(255,255,255))
#             imFull.save("./downloads/images/currentimage.png")
#             textClipCreated = ImageClip("./downloads/images/currentimage.png").set_position(('center', 0)).set_duration(2).resize((1920,1080))

#             clips.append(textClipCreated)
#             sound = AudioSegment.silent(duration=2000)
#             runningsound = runningsound + sound
#             deltatime = 2000
#             desctimestamp = formatdatetimetosub(ogdt)[:-4]
#             descriptionString += "({}) - {}\n".format(desctimestamp, text)

#         ngdt = ogdt + datetime.timedelta(milliseconds=deltatime)
#         subfileend = formatdatetimetosub(ngdt)
#         runningsubstring += (str(i) + "\n" + "{} --> {}".format(subfilestart, subfileend) + "\n" + text + "\n\n")
#         ms += deltatime

#     with open(subfile, 'w') as srtfile:
#         srtfile.write(runningsubstring)
#     runningsound.export("./downloads/audio/runningaudio.mp3", format="mp3")
#     finalaudioClipCreated = AudioFileClip("./downloads/audio/runningaudio.mp3")
#     concat_clip = concatenate_videoclips(clips, method="compose").set_audio(finalaudioClipCreated).resize((1920,1080))
#     concat_clip.write_videofile(videofilename, fps=10)
#     return descriptionString


# def create_videos(wikipediatitle):
#     wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

#     p_wiki = wiki_wiki.page(wikipediatitle)

#     # full_orderedRenderList = [{'title': wikipediatitle}]
#     # full_returnedDict = wikitoDict(p_wiki, full_orderedRenderList)
#     # fullVideoDescString = createVidSnippet(
#     #     full_orderedRenderList,
#     #     "fullvideo.mp4",
#     #     wikipediatitle,
#     #     "fullvideosubs.srt"
#     # )

#     summary_orderedRenderList = [
#         {'title': wikipediatitle},
#         {"title": "Summary"},
#     ]

#     articleSummary = p_wiki.summary

#     for summarySent in nltk.tokenize.sent_tokenize(articleSummary):
#         summary_orderedRenderList.append({"content": summarySent})

#     summaryDescString = createVidSnippet(
#         summary_orderedRenderList,
#         "summaryvideo.mp4",
#         wikipediatitle,
#         "summaryvideosubs.srt"
#     )

# #     descriptionSummary = "\n\n\n\nSource: https://en.wikipedia.org/wiki/{}\n\n\nSummary:\n\n".format("_".join(wikipediatitle.split()))+articleSummary

# #     descriptionSocials = "\n\n\n\n\
# # Follow our Socials!\n \
# #     \nWikiaudia Instagram: https://instagram.com/wikiaudia\n \
# #     \nVivek's Instagram (Co-Creator): https://instagram.com/v1v3k.k \
# #     \nVivek's LinkedIn (Co-Creator): https://www.linkedin.com/in/vivekkogilathota1225 \
# #     \nVivek's Twitter (Co-Creator): https://twitter.com/v1v3krk\n\
# #     \nSamrat's Instagram (Co-Creator): https://instagram.com/samrat.sahoo_ \
# #     \nSamrats's LinkedIn (Co-Creator): https://www.linkedin.com/in/samratsahoo \
# #     \nSamrat's Twitter (Co-Creator): https://twitter.com/samratsahoo2013"

# #     fullVideoDescString += descriptionSummary
# #     fullVideoDescString += descriptionSocials
# #     summaryDescString += descriptionSocials

# #     create_thumbnails(wikipediatitle)
# #     uploadvideo("./fullvideo.mp4","./fullvideosubs.srt",wikipediatitle + ": Full Video",fullVideoDescString,"./fullvideothumbnail.png")
# #     uploadvideo("./summaryvideo.mp4","./summaryvideosubs.srt",wikipediatitle + ": Summary",summaryDescString,"./summaryvideothumbnail.png")
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

p_wiki = wiki_wiki.page("Yemeni Crisis (2011–present)")
print(p_wiki.sections)
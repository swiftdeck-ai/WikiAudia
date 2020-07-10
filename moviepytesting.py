# # from moviepy.editor import *

# # img = ['Pencils.jpg', 'testmpy.jpg']

# # clips = [ImageClip("./downloads/"+m).set_position(('center', 0)).resize(height=1080).set_duration(5)
# #       for m in img]

# # concat_clip = concatenate_videoclips(clips, method="compose")
# # concat_clip.write_videofile("video_with_python.mp4", fps=10)




# import wikipediaapi
# import pprint
# import json

# wiki_wiki = wikipediaapi.Wikipedia(
#         language='en',
#         extract_format=wikipediaapi.ExtractFormat.WIKI
# )

# p_wiki = wiki_wiki.page("Apple Inc.")

# def wikitoDict(specwiki):
#     wikiDict = {}
#     for sect in specwiki.sections:
#         wikiDict[sect.title] = {}
#         if sect.text.strip() != "":
#             wikiDict[sect.title]["text"] = sect.text

#         if len(sect.sections) != 0:
#             wikiDict[sect.title]["sections"] = wikitoDict(sect)

#     return wikiDict

# # with open("wikipediatest.txt","r") as f:

# # Prints the nicely formatted dictionary
# print(json.dumps(wikitoDict(p_wiki)['History'], indent=4))
# # print(wikitoDict(p_wiki)['History'])


# # Sets 'pretty_dict_str' to 
# # pretty_dict_str = pprint.pformat(dictionary)


# # # url = "https://www.google.com/search?q="+keyword+"&tbm=isch&hl=en&hl=en&safe=active&safe=active&tbs=itp%3Aphoto%2Cisz%3Alt%2Cislt%3Axga%2Ciar%3Aw&ved=0CAEQpwVqFwoTCIDpofW7wOoCFQAAAAAdAAAAABAD&biw=1905&bih=949"
#     # # url = "https://www.google.com/search?safe=active&tbm=isch&sxsrf=ALeKk01FwaqjtqZV7oDjVupNWUA-CQZPqQ%3A1594322475346&source=hp&biw=1920&bih=949&ei=K24HX8rdEcOEsAXg66XYCQ&q=apple+inc&oq=apple+inc&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgUIABCxA1CuCFibEGDoEGgAcAB4AIABN4gBwAOSAQE5mAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ved=0ahUKEwiKn7CG8sDqAhVDAqwKHeB1CZsQ4dUDCAc&uact=5"
#     # url = "https://www.google.com/search?q="+keyword+"&tbm=isch&ved=2ahUKEwj34LaY9MDqAhULUawKHfnaBcgQ2-cCegQIABAA&oq="+keyword+"&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzICCAAyAggAMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyBQgAELEDUME-WIRDYO9DaABwAHgAgAEsiAHBAZIBATWYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ei=anAHX_eDAYuisQX5tZfADA&safe=active&tbs=isz%3Alt%2Cislt%3Axga%2Citp%3Aphoto%2Ciar%3Aw&hl=en"
#     # # print(str(requests.get(url).text))
    
#     # # endingurl = "#imgrc=" + str(requests.get(url).content).split("data-id")[2][2:-1]
#     # # url += endingurl
#     # driver.get(url)
#     # # #imgrc=HFJO-X11dtZYCM
#     # # image = driver.find_element_by_xpath(
#     # #     "//*[@id=\"islrg\"]/div[1]/div[1]/a[1]/div[1]/img")
#     # # image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img")
#     # # image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]")
#     # # image.click()
#     # # try:
#     # # enlarged = driver.find_element_by_xpath(
#     # #     "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
#     # # except:
#     # #     driver.quit()
#     # #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     # #     url = "https://www.google.com/search?q="+keyword+"&tbm=isch&hl=en&hl=en&safe=active&safe=active&tbs=itp%3Aphoto%2Cisz%3Alt%2Cislt%3Axga%2Ciar%3Aw&ved=0CAEQpwVqFwoTCIDpofW7wOoCFQAAAAAdAAAAABAD&biw=1905&bih=949"
#     # #     driver.get(url)
#     # #     # image = driver.find_element_by_xpath(
#     # #     #     "//*[@id=\"islrg\"]/div[1]/div[1]/a[1]/div[1]/img")
#     # #     # image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]/img")
#     # #     image = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/a[1]/div[1]")
#     # #     image.click()
#     # #     enlarged = driver.find_element_by_xpath(
#     # #         "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
        
#     # actionChains = ActionChains(driver)
#     # actionChains.context_click(driver.find_elements_by_tag_name('body')).perform()
#     # # pyautogui.press(['down'], presses=10)
#     # # pyautogui.press(['enter'])
#     # # imagelocation = clipboard.paste()
#     # # urllib.request.urlretrieve(
#     # #     imagelocation, "./downloads/images/currentimage.jpg")
    

#     # # return "./downloads/images/currentimage.jpg"

import nltk.data

import re
alphabets= "([A-Za-z])"
numbers = "([0-9])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

fp = "My name is Vivek. I love to read.I am 15 years old and have $5.79."
print(re.split("([.] [A-Z])",fp))
# print('\n-----\n'.join(tokenizer.tokenize(fp)))
# print(split_into_sentences(fp))
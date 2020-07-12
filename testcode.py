# # # # import re
# # # # # alphabets= "([A-Za-z])"
# # # # # numbers = "([0-9])"
# # # # # prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# # # # # suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# # # # # starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
# # # # # acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
# # # # # websites = "[.](com|net|org|io|gov)"


# # # # # def split_into_sentences(text):
# # # # #     text = " " + text + "  "
# # # # #     text = text.replace("\n"," ")
# # # # #     text = re.sub(prefixes,"\\1<prd>",text)
# # # # #     text = re.sub(websites,"<prd>\\1",text)
# # # # #     if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
# # # # #     text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
# # # # #     text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
# # # # #     text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
# # # # #     text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
# # # # #     text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
# # # # #     text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
# # # # #     text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
# # # # #     if "”" in text: text = text.replace(".”","”.")
# # # # #     if "\"" in text: text = text.replace(".\"","\".")
# # # # #     if "!" in text: text = text.replace("!\"","\"!")
# # # # #     if "?" in text: text = text.replace("?\"","\"?")
# # # # #     text = text.replace(".",".<stop>")
# # # # #     text = text.replace("?","?<stop>")
# # # # #     text = text.replace("!","!<stop>")
# # # # #     text = text.replace("<prd>",".")
# # # # #     sentences = text.split("<stop>")
# # # # #     sentences = sentences[:-1]
# # # # #     sentences = [s.strip() for s in sentences]
# # # # #     return sentences

# # # # # # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# # # # fp = "My name is Vivek.I am 15 years old. I have $.23. Mrs. Johnson is so sweet. Apple Inc. is such a cool company. Check out weebly. com."
# # # # # # print(re.split(r'(?:(?<!\d(?=\.\d))\.|\s)+',fp))
# # # # # # print('\n-----\n'.join(tokenizer.tokenize

# # # # def splitintosentences(text):
# # # #     regexsplitlist = re.split("([^0-9$][.]|[.][^0-9])",text)
# # # #     for chunk in range(len(regexsplitlist)):
# # # #         if len(regexsplitlist[chunk]) == 2:
# # # #             if regexsplitlist[chunk][1] == ".":
# # # #                 try:
# # # #                     regexsplitlist[chunk-1] += regexsplitlist[chunk][0]
# # # #                 except:
# # # #                     pass
# # # #             elif regexsplitlist[chunk][0] == ".":
# # # #                 try:
# # # #                     regexsplitlist[chunk+1] = regexsplitlist[chunk][1] + regexsplitlist[chunk+1]
# # # #                 except:
# # # #                     pass

# # # #     for chunkWord in regexsplitlist:
# # # #         if re.search(r"([^0-9][.]|[.][^0-9]|[^0-9][.][^0-9])",chunkWord) != None:
# # # #             regexsplitlist.pop(regexsplitlist.index(chunkWord))

# # # #     return regexsplitlist
# # # # # # while fp.index(".") != None:
# # # # # print(splitintosentences(fp))
    
# # # # # from sentence_splitter import SentenceSplitter, split_text_into_sentences
# # # # # splitter = SentenceSplitter(language='en')
# # # # # print(splitter.split(text=fp))
# # # # # import segtok.segmenter

# # # # # segtok.segmenter.spl
# # # # import nltk.tokenize

# # # # print(nltk.tokenize.sent_tokenize(fp))

# # # import cv2

# # # gray = cv2.imread("./downloads/Pencils.jpg")
# # # try:
# # #     gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
# # # except:
# # #     pass
# # # cv2.imwrite("./downloads/Pencils.jpg",gray)

# # from bs4 import BeautifulSoup
# # import requests
# # import re
# # import sys
# # import os
# # import http.cookiejar
# # import json
# # import urllib.request, urllib.error, urllib.parse
# # import requests
# from PIL import Image

# # def get_soup(url,header):
# #     return BeautifulSoup(urllib.request.urlopen(
# #         urllib.request.Request(url,headers=header)),
# #         'html.parser')

# # def bing_image_search(query):
# #     query= query.split()
# #     query='+'.join(query)
# #     url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

# #     #add the directory for your image here
# #     header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
# #     soup = get_soup(url,header)
# #     image_result_raw = soup.find("a",{"class":"iusc"})

# #     m = json.loads(image_result_raw["m"])
# #     murl, turl = m["murl"],m["turl"]# mobile image, desktop image

# #     image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
# #     # with open('currentimage.{}'.format(image_name.split(".")[-1]), 'wb') as handle:
# #     #     response = requests.get(murl, stream=True)

# #     #     if not response.ok:
# #     #         print(response)

# #     #     for block in response.iter_content(1024):
# #     #         if not block:
# #     #             break

# #     #         handle.write(block)
# #     image = Image.open(urllib.request.urlopen(murl))
# #     image.save("currentimage.jpg")
# #     return (image_name,murl, turl)



# # if __name__ == "__main__":
# #     results = bing_image_search("apples")
# #     print(results)

# print(str(Image.open("./downloads/images/Image_1.gif").format))

# 676595900998-bb50t1vf9esc0nfuba74qtog77thkoib.apps.googleusercontent.com
# uyZAH5LEhXphTGNYlPIII_-_

import os

os.system("python YouTube.py --file=\"summaryvideo.mp4\" --title=\"Test Video\" --description=\"Test Description VK\" --privacyStatus=\"private\"")
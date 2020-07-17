# # # from selenium.webdriver.support import expected_conditions as EC
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # from selenium.common.exceptions import TimeoutException
# # # import pyautogui
# # # from selenium import webdriver
# # # from webdriver_manager.firefox import GeckoDriverManager
# # # from selenium.webdriver.common.keys import Keys
# # # import time
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # import urllib.request
# # # import os
# # # from selenium.webdriver.chrome.options import Options 
# # # import clipboard


# # # def getlinkfromkw(kw):
# # #     imagenumber = 1
# # #     link = ""
# # #     while True:
# # #         driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# # #         driver.get(f"https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q={kw}&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=active&tbs=sur:fc,isz:lt,islt:xga,itp:photo")
# # #         firstimageid = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{}]".format(imagenumber)).get_attribute("data-id")
# # #         # print(firstimageid)
# # #         driver.get("https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q={}&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=active&tbs=sur:fc,isz:lt,islt:xga,itp:photo#imgrc={}".format(kw,firstimageid))
# # #         largerimage = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
# # #         time.sleep(2)
# # #         action = ActionChains(driver)
# # #         action.context_click(largerimage).perform()
# # #         pyautogui.press(['down'], presses=9)
# # #         pyautogui.press(['enter'])
# # #         link = clipboard.paste()
# # #         try:
# # #             urllib.request.urlretrieve(link)
# # #             break
# # #         except:
# # #             imagenumber += 1

# # #     return link

# # # print(getlinkfromkw("programming language used"))
# import re
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer

# from nltk.corpus import stopwords
# import nltk
# import spacy


# class ExtractKeywords:

#     def extractentities(self, text):
#         spacy_nlp  = spacy.load('en_core_web_sm')

#         # parse text into spacy document
#         doc = spacy_nlp(text.strip())

#         # create sets to hold words
#         named_entities = set()
#         money_entities = set()
#         organization_entities = set()
#         location_entities = set()
#         time_indicator_entities = set()

#         for i in doc.ents:
#             entry = str(i.lemma_).lower()
#             text = text.replace(str(i).lower(), "")
#             # Time indicator entities detection
#             if i.label_ in ["TIM", "DATE"]:
#                 if len(time_indicator_entities) == 0:
#                     time_indicator_entities.add(entry)
#             # money value entities detection
#             elif i.label_ in ["MONEY"]:
#                 if len(money_entities) == 0:
#                     money_entities.add(entry)
#             # organization entities detection
#             elif i.label_ in ["ORG"]:
#                 if len(organization_entities) == 0:
#                     organization_entities.add(entry)
#             # Geographical and Geographical entities detection
#             elif i.label_ in ["GPE", "GEO"]:
#                 if len(location_entities) == 0:
#                     location_entities.add(entry)
#             # extract artifacts, events and natural phenomenon from text
#             elif i.label_ in ["ART", "EVE", "NAT", "PERSON"]:
#                 if len(named_entities) == 0:
#                     named_entities.add(entry.title())

#         return {
#             "named": list(named_entities),
#             "money": list(money_entities),
#             "location": list(location_entities),
#             "time": list(time_indicator_entities),
#             "organization": list(organization_entities)
#         }

#     def extractkeywords(self, text):
#         text = re.sub(r'\s+',' ',re.sub(r'[^\w \s]','',text) ).lower()
#         vectorizer = TfidfVectorizer()
#         vectors = vectorizer.fit_transform([text])
#         names = vectorizer.get_feature_names()
#         data = vectors.todense().tolist()
#         # Create a dataframe with the results
#         df = pd.DataFrame(data, columns=names)
#         # print(data)
#         # print(names)
#         st = set(stopwords.words('english'))
#         #remove all columns containing a stop word from the resultant dataframe. 
#         df = df[filter(lambda x: x not in list(st) , df.columns)]
#         moddict = {}
#         for key in list(dict(df).keys()):
#             moddict[key] = dict(df)[key].values[0]

#         searchstring = []
#         sortedkw = sorted(moddict.items(), key=lambda x: x[1], reverse=True)
#         for sortkw in sortedkw[:3]:
#             searchstring.append(sortkw[0])

#         return " ".join(searchstring)

    

import spacy
import pytextrank

# example text
text = "The word \"hackathon\" is a portmanteau of the words \"hack\" and \"marathon\", where \"hack\" is used in the sense of exploratory programming, not its alternate meaning as a reference to breaching computer security."

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

doc = nlp(text)

# examine the top-ranked phrases in the document
for p in doc._.phrases:
    print(p.chunks)
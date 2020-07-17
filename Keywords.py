# import re
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer

# from nltk.corpus import stopwords
# import nltk
import spacy
import pytextrank
def getkeywords(text):
    nlp = spacy.load("en_core_web_sm")
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)
    return doc._.phrases[0].chunks[0]


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

    
# def getkeywords(text):
#     keywordextractor = ExtractKeywords()
#     # text = "For Sun Microsystems, the usage referred to an event at the JavaOne conference from June 15 to June 19, 1999; there John Gage challenged attendees to write a program in Java for the new Palm V using the infrared port to communicate with other Palm users and register it on the Internet."
#     # text = "The word \"hackathon\" is a portmanteau of the words \"hack\" and \"marathon\", where \"hack\" is used in the sense of exploratory programming, not its alternate meaning as a reference to breaching computer security."
#     entitiesfromtext = keywordextractor.extractentities(text)
#     flag = True
#     entity = ""
#     for entitygroup in ["organization","named","location","time","money"]:
#         if len(entitiesfromtext[entitygroup]) != 0:
#             entity = entitiesfromtext[entitygroup][0]
#             flag = False
#             break

#     if flag:
#         return keywordextractor.extractkeywords(text)
#     else:
#         return entity
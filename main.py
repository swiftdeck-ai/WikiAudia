from __future__ import print_function

import os
import re
import sys

from GDocs import getText, addTitle, removeTitle, LOG_DOC_ID, ADD_DOC_ID
import wikipedia
from Video import create_videos
import wikipediaapi
from googletrans import Translator


def main():
    try:
        # Get list of chosen topics
        topicArray = getText(ADD_DOC_ID).strip().split('\n')
        # remove whitespace if any
        topic = topicArray[0].strip()
        # Remove topic from ADD Doc
        removeTitle(topic, ADD_DOC_ID)
        # Detect Language of Translator
        translator = Translator()
        languageTopic = translator.translate(topic).src
        if languageTopic != 'hi' and languageTopic != 'en':
            languageTopic = 'hi'
        if re.search('[a-zA-Z]', topic) is not None:
            languageTopic = 'en'
        # To check existence for Wikipedia API
        wiki_wiki = wikipediaapi.Wikipedia(language=languageTopic, extract_format=wikipediaapi.ExtractFormat.WIKI)
        page = wiki_wiki.page(topic)
        # If Add doc is empty then choose a random article
        if getText(ADD_DOC_ID).strip() == '' and topic == '':
            topic = wikipedia.random()
        # If the page does not exist, recursion
        if not page.exists():
            if languageTopic == 'hi':
                languageTopic = 'en'
                wiki_wiki = wikipediaapi.Wikipedia(language=languageTopic, extract_format=wikipediaapi.ExtractFormat.WIKI)
                page = wiki_wiki.page(topic)
                if not page.exists():
                    main()
            elif languageTopic == 'en':
                languageTopic = 'hi'
                wiki_wiki = wikipediaapi.Wikipedia(language=languageTopic, extract_format=wikipediaapi.ExtractFormat.WIKI)
                page = wiki_wiki.page(topic)
                if not page.exists():
                    main()
            else:
                main()

        # If a video over it has not already been made then make the video
        if topic not in getText(LOG_DOC_ID).split('\n'):
            addTitle(topic, LOG_DOC_ID)
            create_videos(topic, language=languageTopic)
    except Exception as e:
        exceptionType, exceptionObject, exceptionThrowback = sys.exc_info()
        fileName = os.path.split(exceptionThrowback.tb_frame.f_code.co_filename)[1]
        print(exceptionType, fileName, exceptionThrowback.tb_lineno)
        print(e)

if __name__ == "__main__":
    articles = getText(ADD_DOC_ID).strip().split('\n')
    for article in articles:
        try:
            if len(articles) == 0 or article.strip() == '':
                break
            main()
            articles = getText(ADD_DOC_ID).strip().split('\n')
        except Exception as e:
            print(e)

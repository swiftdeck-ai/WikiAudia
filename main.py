from __future__ import print_function

from GDocs import getText, addTitle, removeTitle, LOG_DOC_ID, ADD_DOC_ID
import wikipedia
from Video import *


def main():
    # Get list of chosen topics
    topicArray = getText(ADD_DOC_ID).strip().split('\n')
    # remove whitespace if any
    topic = topicArray[0].strip()
    # Remove topic from ADD Doc
    removeTitle(topic, ADD_DOC_ID)
    # If Add doc is empty then choose a random article
    if getText(ADD_DOC_ID).strip() == '' and topic == '':
        topic = wikipedia.random()
    # If a video over it has not already been made then make the video
    if topic not in getText(LOG_DOC_ID).split('\n'):
        addTitle(topic, LOG_DOC_ID)
        create_videos(topic)


if __name__ == "__main__":
    for i in range(10):
        main()
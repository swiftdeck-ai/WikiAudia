from __future__ import print_function

from GDocs import getText, addTitle, removeTitle, LOG_DOC_ID, ADD_DOC_ID
import wikipedia
from moviepy.editor import *
from video import *


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
        # Video stuff here


if __name__ == "__main__":
    img = ['Pencils.jpg']

    clips = [ImageClip("./downloads/images/" + m).set_position(('center', 0)).resize(height=1080).set_duration(1)
             for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("video_with_python_test.mp4", fps=10)
    p_wiki = wiki_wiki.page("Apple Inc.")
    orderedRenderList = [
        # {"title":"Summary"},
    ]
    # for summarySent in p_wiki.summary.split(". "):
    #     orderedRenderList.append({"content":summarySent})
    returnedDict = wikitoDict(p_wiki, orderedRenderList)
    createVidSnippet(
        orderedRenderList[:24],
        "video_with_python_test.mp4",
    )

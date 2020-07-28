import spacy
import pytextrank
import nltk
from nltk.tag import tnt
from nltk.corpus import indian
from googletrans import Translator

def getkeywords(text, title):
    nlp = spacy.load("en_core_web_sm")
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)
    try:
        return doc._.phrases[0].chunks[0]
    except:
        return title


def getKeywordsHindi(text, title):
    translator = Translator()
    text = translator.translate(text, src='hi', dest='en').text
    title = translator.translate(title, src='hi', dest='en').text
    return getkeywords(text, title)

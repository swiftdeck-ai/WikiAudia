import spacy
import pytextrank
import nltk
from mtranslate import translate
from nltk.tag import tnt
from nltk.corpus import indian


def getkeywords(text, title):
    nlp = spacy.load("en_core_web_sm")
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)
    try:
        return doc._.phrases[0].chunks[0]
    except:
        return title


def hindiModel():
    train_data = indian.tagged_sents('hindi.pos')
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger


def getKeywordsHindi(text, title):
    try:
        text = translate(text, "en", "hi")
        return getkeywords(text, title)
    except:
        return title

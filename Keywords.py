import spacy
import pytextrank


def getkeywords(text):
    nlp = spacy.load("en_core_web_sm")
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(text)
    return doc._.phrases[0].chunks[0]

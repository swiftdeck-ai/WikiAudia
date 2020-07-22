import spacy
import pytextrank
import nltk
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
        model = hindiModel()
        pos = (model.tag(nltk.word_tokenize(text)))
        grammar = r"""NP:{<NN.*>}"""
        chunkParser = nltk.RegexpParser(grammar)
        chunked = chunkParser.parse(pos)
        continuous_chunk = set()
        current_chunk = []
        for i in chunked:
            if type(i) == nltk.Tree:
                current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.add(named_entity)
                    current_chunk = []
                else:
                    continue
            return list(continuous_chunk)[0]
    except:
        return title

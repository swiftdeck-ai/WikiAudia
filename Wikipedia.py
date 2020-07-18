import nltk
from indicnlp.tokenize.sentence_tokenize import sentence_split

def wikitoDict(specwiki, wikiRenderList,language):
    wikiDict = {}
    for sect in specwiki.sections:
        wikiDict[sect.title] = {}
        if sect.title in ['See also', 'Notes', 'References', 'External links']:
            break
        wikiRenderList.append({"title": sect.title})
        if sect.text.strip() != "":
            if language == 'en':
                splittext = nltk.tokenize.sent_tokenize(sect.text)
            elif language == 'hi':
                splittext = sentence_split(sect.text, lang=language)
            wikiDict[sect.title]["text"] = splittext
            for sentRender in splittext:
                wikiRenderList.append({"content": sentRender})

        if len(sect.sections) != 0:
            wikiDict[sect.title]["sections"] = wikitoDict(sect, wikiRenderList)

    return wikiDict
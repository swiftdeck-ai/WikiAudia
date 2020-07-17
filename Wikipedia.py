import nltk

def wikitoDict(specwiki, wikiRenderList):
    wikiDict = {}
    for sect in specwiki.sections:
        wikiDict[sect.title] = {}
        if sect.title in ['See also', 'Notes', 'References', 'External links']:
            break
        wikiRenderList.append({"title": sect.title})
        if sect.text.strip() != "":
            splittext = nltk.tokenize.sent_tokenize(sect.text)
            wikiDict[sect.title]["text"] = splittext
            for sentRender in splittext:
                wikiRenderList.append({"content": sentRender})

        if len(sect.sections) != 0:
            wikiDict[sect.title]["sections"] = wikitoDict(sect, wikiRenderList)

    return wikiDict
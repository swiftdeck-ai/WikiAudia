import wikipedia

def getArticle():
    article = wikipedia.random()
    page = wikipedia.page(article)
    print(page.content)
    return article

if __name__=='__main__':
    getArticle()
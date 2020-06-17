def createArticle(contents):
    article = " ".join(content.text.strip() for content in contents)
    article = article.replace("(CNN)", "")
    article = article.replace("(CNN Business)", "")

    return article

def cleanContents(contents):
    contents = contents[12:len(contents)-3]

    if contents[0].text.strip()[0:24] == "These are external links":
        contents = contents[1:]
    
    return contents

def findContents(soup):
    results = soup.find(class_="l-container")

    if results is None:
        results = soup.find(class_="BasicArticle__main")

        if results is None:
            contents = []
        
        contents = soup.find_all(class_="Paragraph__component")
    
    else:
        contents = soup.find_all(class_="zn-body__paragraph")

    return contents

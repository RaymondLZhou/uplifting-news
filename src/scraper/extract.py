import feedparser as fp
import requests
from bs4 import BeautifulSoup
from time import sleep

def extractFields(elem):
    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    return title, description, date, link

def createSoup(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")

    return soup

def createArticle(contents):
    article = " ".join(content.text.strip() for content in contents)
    article = article.replace("(CNN)", "")
    article = article.replace("(CNN Business)", "")

    return article

def appendDict(title, description, date, link, article, newsList):
    newsDict = {
        "title": title,
        "description": description,
        "date": date,
        "link": link,
        "text": article,
    }

    newsList.append(newsDict)

    sleep(1)

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

def bbcExtract(url, newsList):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = extractFields(elem)
        soup = createSoup(link)

        results = soup.find(class_="story-body__inner")

        if results is None:
            continue

        contents = soup.find_all("p")

        if len(contents) < 16:
            continue

        contents = cleanContents(contents)
        article = createArticle(contents)

        appendDict(title, description, date, link, article, newsList)

def cnnExtract(url, newsList):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = extractFields(elem)

        description = description.split('<')[0]

        if "" in (title, description, date, link):
            continue

        if link[-5:] != ".html":
            continue

        soup = createSoup(link)
        contents = findContents(soup)
        article = createArticle(contents)

        appendDict(title, description, date, link, article, newsList)

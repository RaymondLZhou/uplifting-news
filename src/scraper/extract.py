import feedparser as fp

import parse
import clean
import add

def bbcExtract(url, newsList):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = parse.extractFields(elem)
        soup = parse.createSoup(link)

        results = soup.find(class_="story-body__inner")

        if results is None:
            continue

        contents = soup.find_all("p")

        if len(contents) < 16:
            continue

        contents = clean.cleanContents(contents)
        article = clean.createArticle(contents)

        add.appendDict(title, description, date, link, article, newsList)

def cnnExtract(url, newsList):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = parse.extractFields(elem)

        description = description.split('<')[0]

        if "" in (title, description, date, link):
            continue

        if link[-5:] != ".html":
            continue

        soup = parse.createSoup(link)
        contents = clean.findContents(soup)
        article = clean.createArticle(contents)

        add.appendDict(title, description, date, link, article, newsList)

import feedparser as fp
import json

def scrape(url):
    feed = fp.parse(url)
    newsList = []

    for elem in feed.entries:
        newsObject = {
            "title": elem.title,
            "description": elem.description,
            "date": elem.published,
            "link": elem.link
        }
        
        newsList.append(newsObject)
    
    return newsList

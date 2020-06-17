import feedparser as fp
import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

place = "http://feeds.bbci.co.uk/news/rss.xml"
feed = fp.parse(place)

newsList = []

for elem in feed.entries:

    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    url = link

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find(class_="story-body__inner")

    if results is None:
        continue

    contents = soup.find_all("p")

    if len(contents) < 16:
        continue

    contents = contents[12:len(contents)-3]

    if contents[0].text.strip()[0:24] == "These are external links":
        contents = contents[1:]

    article = " ".join(content.text.strip() for content in contents)

    newsObject = {
        "title": title,
        "description": description,
        "date": date,
        "link": link,
        "text": article,
    }
        
    newsList.append(newsObject)

    sleep(1)

place = "http://rss.cnn.com/rss/cnn_topstories.rss"
feed = fp.parse(place)

for elem in feed.entries:

    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary.split('<')[0] if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    if "" in (title, description, date, link):
        continue

    if link[-5:] != ".html":
        continue

    url = link

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find(class_="l-container")

    if results is None:
        results = soup.find(class_="BasicArticle__main")

        if results is None:
            contents = []
        
        contents = soup.find_all(class_="Paragraph__component")
    
    else:
        contents = soup.find_all(class_="zn-body__paragraph")

    article = " ".join(content.text.strip() for content in contents)
    article = article.replace("(CNN)", "")
    article = article.replace("(CNN Business)", "")

    newsObject = {
        "title": title,
        "description": description,
        "date": date,
        "link": link,
        "text": article,
    }
        
    newsList.append(newsObject)

    sleep(1)

df = pd.DataFrame(newsList)
df.to_csv("../data/feed.csv", encoding='utf-8-sig')

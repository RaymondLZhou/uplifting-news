import requests
from bs4 import BeautifulSoup
import feedparser as fp
import numpy as np
import pandas as pd
import json

url = "http://feeds.bbci.co.uk/news/rss.xml"
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

with open("raw.json", "w") as outfile:
    json.dump(newsList, outfile, ensure_ascii=False, indent=4)

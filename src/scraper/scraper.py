import requests
from bs4 import BeautifulSoup
import feedparser
import numpy as np
import pandas as pd

url = "http://feeds.bbci.co.uk/news/rss.xml"
feed = feedparser.parse(url)

for elem in feed.entries:
    print(elem.title)
    print(elem.description)
    print(elem.published)
    print(elem.link)
    print()

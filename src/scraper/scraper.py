import pandas as pd

import extract

newsList = []

url = "http://feeds.bbci.co.uk/news/rss.xml"
extract.bbcExtract(url, newsList)

url = "http://rss.cnn.com/rss/cnn_topstories.rss"
extract.cnnExtract(url, newsList)

df = pd.DataFrame(newsList)
df.to_csv("../data/feed.csv", encoding='utf-8-sig')

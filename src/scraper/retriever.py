import json
import requests
from bs4 import BeautifulSoup

with open("feed.json") as json_data:
    newsList = json.load(json_data)

articles = []

for news in newsList:
    url = news["link"]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find(class_="story-body__inner")

    if results is None:
        continue

    contents = soup.find_all("p")

    article = " ".join(content.text.strip() for content in contents)
    article = {"text": article}
    articles.append(article)

with open("articlesRaw.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)

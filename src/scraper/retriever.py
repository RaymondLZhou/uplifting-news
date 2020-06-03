import json
import requests
from bs4 import BeautifulSoup
from time import sleep

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

    if len(contents) < 16:
        continue

    contents = contents[12:len(contents)-3]

    if contents[0].text.strip()[0:24] == "These are external links":
        contents = contents[1:]

    article = " ".join(content.text.strip() for content in contents)
    article = {"text": article}
    articles.append(article)

    sleep(2)

with open("articlesRaw.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)

import json
import requests
from bs4 import BeautifulSoup
from time import sleep

with open("../data/CNNFeed.json") as json_data:
    newsList = json.load(json_data)

articles = []

for news in newsList:
    url = news["link"]
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
    article = {"text": article}
    articles.append(article)

    sleep(2)

with open("../data/CNNArticlesRaw.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)

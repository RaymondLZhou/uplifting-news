import json
import re

def clean(newsList):
    REPLACE_NO_SPACE = re.compile(r"[.;:!\'?,\"()\[\]]")
    REPLACE_WITH_SPACE = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")

    newsList = [news["text"] for news in newsList]

    newsList = [REPLACE_NO_SPACE.sub("", news.lower()) for news in newsList]
    newsList = [REPLACE_WITH_SPACE.sub(" ", news) for news in newsList]

    articles = [{"text": news} for news in newsList]

    return articles

with open("../data/BBCArticlesRaw.json") as json_data:
    newsList = json.load(json_data)

articles = clean(newsList)

with open("../data/BBCArticlesCleaned.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)


with open("../data/CNNArticlesRaw.json") as json_data:
    newsList = json.load(json_data)

articles = clean(newsList)

with open("../data/CNNArticlesCleaned.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)

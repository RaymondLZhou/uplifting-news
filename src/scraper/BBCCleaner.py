import json
import re

with open("BBCArticlesRaw.json") as json_data:
    newsList = json.load(json_data)

REPLACE_NO_SPACE = re.compile(r"[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")

newsList = [news["text"] for news in newsList]

newsList = [REPLACE_NO_SPACE.sub("", news.lower()) for news in newsList]
newsList = [REPLACE_WITH_SPACE.sub(" ", news) for news in newsList]

articles = [{"text": news} for news in newsList]

with open("BBCArticlesCleaned.json", "w") as outfile:
    json.dump(articles, outfile, indent=4)

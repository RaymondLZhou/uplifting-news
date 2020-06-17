import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def createJSON(newsList):
    sia = SentimentIntensityAnalyzer()
    sentiments = []

    for news in newsList:
        scores = sia.polarity_scores(news["title"] + news["description"])

        sentiment = {
            "title": news["title"],
            "description": news["description"],
            "date": news["date"],
            "link": news["link"],
            "positive": scores["pos"],
            "neutral": scores["neu"],
            "negative": scores["neg"],
            "overall": scores["compound"]
        }

        sentiments.append(sentiment)

    return sentiments

df = pd.read_csv("../data/feed.csv")
newsList = df.to_dict('records')
sentiments = createJSON(newsList)

sentiments.sort(key=lambda x: x['overall'])
sentiments.reverse()

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

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


with open("../data/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createJSON(newsList)

with open("../data/BBCSentiment.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)


with open("../data/CNNFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createJSON(newsList)

with open("../data/CNNSentiment.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

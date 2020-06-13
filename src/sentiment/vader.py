from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

def createJSON(newsList):
    sia = SentimentIntensityAnalyzer()
    sentiments = []

    for news in newsList:
        scores = sia.polarity_scores(news["title"] + news["description"])

        sentiment = {
            "description": news["description"],
            "positive": scores["pos"],
            "neutral": scores["neu"],
            "negative": scores["neg"],
            "overall": scores["compound"]
        }

        sentiments.append(sentiment)

    return sentiments


with open("../scraper/bbc/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createJSON(newsList)

with open("BBCSentiment.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)


with open("../scraper/cnn/CNNFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createJSON(newsList)

with open("CNNSentiment.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

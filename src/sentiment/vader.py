from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import pandas as pd

def createCSV(newsList):
    sia = SentimentIntensityAnalyzer()
    descriptions = []
    positive = []
    negative = []
    neutral = []
    overall = []

    for news in newsList:
        scores = sia.polarity_scores(news["title"] + news["description"])
        
        descriptions.append(news["description"])
        positive.append(scores["pos"])
        neutral.append(scores["neu"])
        negative.append(scores["neg"])
        overall.append(scores["compound"])

    sentiments = pd.DataFrame ({
        "description": descriptions,
        "positive": positive,
        "neutral": neutral,
        "negative": negative,
        "overall": overall,
    })

    return sentiments


with open("../scraper/bbc/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createCSV(newsList)
sentiments.to_csv("BBCSentiment.csv")

with open("../scraper/cnn/CNNFeed.json") as json_data:
    newsList = json.load(json_data)

sentiments = createCSV(newsList)
sentiments.to_csv("CNNSentiment.csv")

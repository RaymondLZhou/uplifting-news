from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import pandas as pd

with open("../scraper/bbc/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sia = SentimentIntensityAnalyzer()
descriptions = []
positive = []
negative = []
neutral = []
overall = []

for news in newsList:
    scores = sia.polarity_scores(news["description"])
    
    descriptions.append(news["description"])
    positive.append(scores["pos"])
    neutral.append(scores["neu"])
    negative.append(scores["neg"])
    overall.append(scores["compound"])

frame = pd.DataFrame ({
    "description": descriptions,
    "positive": positive,
    "neutral": neutral,
    "negative": negative,
    "overall": overall,
})

frame.to_csv("BBCSentiment.csv")

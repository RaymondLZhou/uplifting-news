from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

with open("../scraper/bbc/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sia = SentimentIntensityAnalyzer()

for news in newsList:
    scores = sia.polarity_scores(news["description"])
    print("{:-<40} {}".format(news["description"], str(scores)))
    print()

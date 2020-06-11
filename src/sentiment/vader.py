from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

with open("../scraper/bbc/BBCFeed.json") as json_data:
    newsList = json.load(json_data)

sia = SentimentIntensityAnalyzer()

news = newsList[0]["description"]

scores = sia.polarity_scores(news)

print("{:-<40} {}".format(news, str(scores)))

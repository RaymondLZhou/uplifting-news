import json
import pandas as pd

import learn

def keywords(lda):
    messages = []
    n_top_words = 6

    for _, topic in enumerate(lda.components_):
        message = ""
        message += " ".join([tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
        messages.append(message)
    
    return messages

def consolidate(scores, messages):
    sentiments = []

    for score, message in zip(scores, messages):
        sentiment = {
            "title": score["title"],
            "description": score["description"],
            "date": score["date"],
            "link": score["link"],
            "positive": score["positive"],
            "neutral": score["neutral"],
            "negative": score["negative"],
            "overall": score["overall"],
            "keywords": message,
        }

        sentiments.append(sentiment)
    
    return sentiments

def process(sentiments):
    sentiments.sort(key=lambda x: x['overall'])
    sentiments.reverse()

df = pd.read_csv("../data/feed.csv")
newsList = df.to_dict('records')

scores = learn.positivityScores(newsList)
lda, tf_feature_names = learn.train(newsList)

messages = keywords(lda)

sentiments = consolidate(scores, messages)
process(sentiments)

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

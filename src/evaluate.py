import numpy as np
import pandas as pd


def predict(model):
    df = pd.read_csv("../data/feed.csv")
    news_list = df.to_dict("records")

    text_list = [news["title"] + news["description"] + news["text"] for news in news_list]
    scores = [model.predict(np.array([text])) for text in text_list]

    sentiments = []

    for news, score in zip(news_list, scores):
        sentiment = {
            "title": news["title"],
            "link": news["link"],
            "score": score
        }

        sentiments.append(sentiment)

    sentiments.sort(key=lambda x: x["score"])
    sentiments.reverse()

    df = pd.DataFrame(sentiments)
    df.to_csv("../data/sentiment.csv", encoding="utf-8-sig")

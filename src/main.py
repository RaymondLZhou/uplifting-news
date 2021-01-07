import json

import pandas as pd

import learn
import utils

if __name__ == '__main__':
    df = pd.read_csv("../data/feed.csv")
    news_list = df.to_dict('records')

    scores = learn.get_sentiment(news_list)
    lda, tf_feature_names = learn.train(news_list)

    messages = utils.get_keywords(lda, tf_feature_names)

    sentiments = utils.consolidate(scores, messages)
    sentiments = utils.clean(sentiments)

    with open("../data/displayFeed.json", "w") as outfile:
        json.dump(sentiments, outfile, indent=4)

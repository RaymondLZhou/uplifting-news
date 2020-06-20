import json
import pandas as pd

import learn
import extract
import combine

df = pd.read_csv("../data/feed.csv")
newsList = df.to_dict('records')

scores = learn.positivityScores(newsList)
lda, tf_feature_names = learn.train(newsList)

messages = extract.keywords(lda, tf_feature_names)

sentiments = combine.consolidate(scores, messages)
sentiments = combine.process(sentiments)

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

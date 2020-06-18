import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

lemmatizer = WordNetLemmatizer()

class LemmaCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (lemmatizer.lemmatize(w) for w in analyzer(doc))

def positivityScores(newsList):
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

def train(newsList):
    articles = [news["text"] for news in newsList]
    tf_vectorizer = LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
    tf = tf_vectorizer.fit_transform(articles)

    lda = LatentDirichletAllocation(n_components=len(newsList), max_iter=5, learning_method = 'online', learning_offset = 50., random_state = 0)
    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()

    return lda, tf_feature_names

def keywords(lda):
    messages = []
    n_top_words = 6

    for index, topic in enumerate(lda.components_):
        foo = index
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

scores = positivityScores(newsList)
lda, tf_feature_names = train(newsList)

messages = keywords(lda)

sentiments = consolidate(scores, messages)
process(sentiments)

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

lemmatizer = WordNetLemmatizer()

def print_top_words(model, feature_names, n_top_words):
    for index, topic in enumerate(model.components_):
        message = "\nTopic #{}: ".format(index)
        message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
        print(message)
        print("="*70)

class LemmaCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (lemmatizer.lemmatize(w) for w in analyzer(doc))

def createJSON(newsList):
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

df = pd.read_csv("../data/feed.csv")
newsList = df.to_dict('records')

articles = [news["text"] for news in newsList]
tf_vectorizer = LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
tf = tf_vectorizer.fit_transform(articles)

lda = LatentDirichletAllocation(n_components=110, max_iter=5, learning_method = 'online', learning_offset = 50., random_state = 0)
lda.fit(tf)

n_top_words = 40
tf_feature_names = tf_vectorizer.get_feature_names()
# print_top_words(lda, tf_feature_names, n_top_words)

vader = createJSON(newsList)
messages = []

for index, topic in enumerate(lda.components_):
    message = ""
    message += " ".join([tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
    messages.append(message)

sentiments = []

for v, message in zip(vader, messages):
    sentiment = {
        "title": v["title"],
        "description": v["description"],
        "date": v["date"],
        "link": v["link"],
        "positive": v["positive"],
        "neutral": v["neutral"],
        "negative": v["negative"],
        "overall": v["overall"],
        "keywords": message,
    }

    sentiments.append(sentiment)

sentiments.sort(key=lambda x: x['overall'])
sentiments.reverse()

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(sentiments, outfile, indent=4)

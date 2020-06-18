from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.decomposition import LatentDirichletAllocation

import LemmaCountVectorizer

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
    tf_vectorizer = LemmaCountVectorizer.LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
    tf = tf_vectorizer.fit_transform(articles)

    lda = LatentDirichletAllocation(n_components=len(newsList), max_iter=5, learning_method = 'online', learning_offset = 50., random_state = 0)
    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()

    return lda, tf_feature_names

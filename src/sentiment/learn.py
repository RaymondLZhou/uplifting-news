from sklearn.decomposition import LatentDirichletAllocation

import LemmaCountVectorizer

import evaluate

def positivityScores(newsList):
    text_list = [news["title"] + news["description"] for news in newsList]
    sentiments = evaluate.predict_list(text_list)

    scores = []

    for news, sentiment in zip(newsList, sentiments):
        score = {
            "title": news["title"],
            "description": news["description"],
            "date": news["date"],
            "link": news["link"],
            "overall": sentiment
        }

        scores.append(score)

    return scores

def train(newsList):
    articles = [news["text"] for news in newsList]
    tf_vectorizer = LemmaCountVectorizer.LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
    tf = tf_vectorizer.fit_transform(articles)

    lda = LatentDirichletAllocation(n_components=len(newsList), max_iter=5, learning_method = 'online', learning_offset = 50., random_state = 0)
    lda.fit(tf)

    tf_feature_names = tf_vectorizer.get_feature_names()

    return lda, tf_feature_names

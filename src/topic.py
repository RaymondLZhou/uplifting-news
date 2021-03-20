from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

lemmatizer = WordNetLemmatizer()


class LemmaCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (lemmatizer.lemmatize(w) for w in analyzer(doc))


def train(news_list):
    articles = [news["text"] for news in news_list]
    tf_vectorizer = LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
    tf = tf_vectorizer.fit_transform(articles)

    lda = LatentDirichletAllocation(n_components=len(news_list), max_iter=5, learning_method='online',
                                    learning_offset=50., random_state=0)
    lda.fit(tf)
    tf_feature_names = tf_vectorizer.get_feature_names()

    return lda, tf_feature_names


def keywords(lda, tf_feature_names):
    messages = []
    n_top_words = 10

    for _, topic in enumerate(lda.components_):
        message = [tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1] if
                   tf_feature_names[i] not in {"say", "said"}]
        message = message[:5]
        message = ", ".join(message)

        messages.append(message)

    return messages

import json
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

with open("../data/BBCArticlesCleaned.json") as json_data:
    newsList = json.load(json_data)

lemmatizer = WordNetLemmatizer()
newsList = [news["text"] for news in newsList]

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

tf_vectorizer = LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
tf = tf_vectorizer.fit_transform(newsList)

lda = LatentDirichletAllocation(n_components=11, max_iter=5, learning_method = 'online', learning_offset = 50., random_state = 0)
lda.fit(tf)

n_top_words = 40
print("\nTopics in LDA model: ")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

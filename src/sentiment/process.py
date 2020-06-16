import json
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

with open("../data/BBCArticlesCleaned.json") as json_data:
    newsList = json.load(json_data)

lemmatizer = WordNetLemmatizer()
newsList = [news["text"] for news in newsList]

def print_top_words(model, feature_names, n_top_words):
    for index, topic in enumerate(model.components_):
        message = "\nTopic #{}:".format(index)
        message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
        print(message)
        print("="*70)

class LemmaCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (lemmatizer.lemmatize(w) for w in analyzer(doc))

tf_vectorizer = LemmaCountVectorizer(max_df=0.95, min_df=2, stop_words='english', decode_error='ignore')
tf = tf_vectorizer.fit_transform(newsList)

print(tf)

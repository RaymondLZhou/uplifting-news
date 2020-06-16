import json
import nltk

with open("../data/BBCArticlesCleaned.json") as json_data:
    newsList = json.load(json_data)

stopwords = nltk.corpus.stopwords.words('english')

first = newsList[0]["text"]
first = nltk.word_tokenize(first)
first = [word for word in first if word not in stopwords]

print(first)

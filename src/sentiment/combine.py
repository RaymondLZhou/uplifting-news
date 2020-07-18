def consolidate(scores, messages):
    sentiments = []

    for score, message in zip(scores, messages):
        sentiment = {
            "title": score["title"],
            "description": score["description"],
            "date": score["date"],
            "link": score["link"],
            "overall": score["overall"],
            "keywords": message,
        }

        sentiments.append(sentiment)
    
    return sentiments

def process(sentiments):
    sentiments.sort(key=lambda x: x['overall'])
    sentiments.reverse()
    return sentiments[:len(sentiments)//3*3]

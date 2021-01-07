def get_keywords(lda, tf_feature_names):
    messages = []
    n_top_words = 10

    for _, topic in enumerate(lda.components_):
        message = [tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1] if
                   tf_feature_names[i] not in {"say", "said"}]
        message = message[:5]
        message = ", ".join(message)

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
            "overall": score["overall"],
            "keywords": message,
        }

        sentiments.append(sentiment)

    return sentiments


def clean(sentiments):
    sentiments.sort(key=lambda x: x['overall'])
    sentiments.reverse()

    return sentiments[:len(sentiments) // 3 * 3]
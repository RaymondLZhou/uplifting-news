def keywords(lda, tf_feature_names):
    messages = []
    n_top_words = 6

    for _, topic in enumerate(lda.components_):
        message = ""
        message += " ".join([tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1]])
        messages.append(message)
    
    return messages
    
def keywords(lda, tf_feature_names):
    messages = []
    n_top_words = 10

    for _, topic in enumerate(lda.components_):
        message = [tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1 :-1] if tf_feature_names[i] not in {"say", "said"}]
        message = message[:6]
        message = ", ".join(message)

        messages.append(message)
    
    return messages
    
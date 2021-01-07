import tensorflow as tf
import tensorflow_datasets as tfds


def predict_list(text_list):
    def load_data():
        loaded_model = tf.keras.models.load_model('../data')

        _, info = tfds.load('imdb_reviews/subwords8k', with_info=True, as_supervised=True)
        loaded_encoder = info.features['text'].encoder

        print('Vocabulary size: {}'.format(loaded_encoder.vocab_size))

        return loaded_model, loaded_encoder

    def predict_text(pad=True):
        def pad_to_size(vec, size):
            zeros = [0] * (size - len(vec))
            vec.extend(zeros)
            return vec

        encoded_text = encoder.encode(text)

        if pad:
            encoded_text = pad_to_size(encoded_text, 64)

        encoded_text = tf.cast(encoded_text, tf.float32)
        prediction = model.predict(tf.expand_dims(encoded_text, 0))

        return str(prediction[0][0])

    model, encoder = load_data()
    outputs = []

    for text in text_list:
        output = predict_text()
        outputs.append(output)

    return outputs

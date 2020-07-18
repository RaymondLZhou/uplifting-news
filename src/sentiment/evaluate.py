import tensorflow as tf
import tensorflow_datasets as tfds

def load_data():
    model = tf.keras.models.load_model('../data')

    _, info = tfds.load('imdb_reviews/subwords8k', with_info=True, as_supervised=True)
    encoder = info.features['text'].encoder

    print('Vocabulary size: {}'.format(encoder.vocab_size))

    return model, encoder

def pad_to_size(vec, size):
    zeros = [0] * (size - len(vec))
    vec.extend(zeros)
    return vec

def predict_text(text, model, encoder, pad=True):
    encoded_text = encoder.encode(text)

    if pad:
        encoded_text = pad_to_size(encoded_text, 64)
    
    encoded_text = tf.cast(encoded_text, tf.float32)
    prediction = model.predict(tf.expand_dims(encoded_text, 0))

    return (prediction[0][0])

def predict_list(text_list):
    model, encoder = load_data()
    outputs = []

    for text in text_list:
        output = predict_text(text, model, encoder)
        outputs.append(output)
    
    return outputs

text_positive = 'The movie was cool. The animation and the graphics were out of this world. I would recommend this movie.'
text_negative = 'The movie was not good. The animation and the graphics were terrible. I would not recommend this movie.'

text_list = [text_positive, text_negative]

prediction = predict_list(text_list)
print(prediction)

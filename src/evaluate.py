import numpy as np


def predict(model):
    sample_text = ('The movie was cool. The animation and the graphics '
                   'were out of this world. I would recommend this movie.')
    predictions = model.predict(np.array([sample_text]))

    print(predictions)

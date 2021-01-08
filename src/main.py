import tensorflow as tf

import utilities
import visualize
import evaluate

if __name__ == '__main__':
    train_dataset, test_dataset, encoder = utilities.load_data()

    model = tf.keras.Sequential([
        encoder,
        tf.keras.layers.Embedding(
            input_dim=len(encoder.get_vocabulary()),
            output_dim=64,
            mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(1e-4),
                  metrics=['accuracy'])

    history = model.fit(train_dataset, epochs=1,
                        validation_data=test_dataset,
                        validation_steps=30)

    test_loss, test_acc = model.evaluate(test_dataset)

    visualize.display_results(test_loss, test_acc, history)

    evaluate.predict(model)

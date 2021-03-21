# Uplifting News

Positive news aggregator built on sentiment analysis in TensorFlow and Keras with an RNN to sort news feed.
Extracts keywords with scikit-learn and NLTK to perform topic modelling, web scraping with Python for data.

## Description

We train an RNN on the [IMDB large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) for sentiment analysis. 
The raw text is preprocessed, then fed into the model. The model is used to predict the positivity of a given news article, 
with the most positive being displayed first. Additionally, Latent Dirichlet Allocation is used for topic modelling and keyword extraction.

## Examples

| Article Title | Keywords | Score |
| ------------- | ------------- | ------------- |
| Rashford's free school meals victory 'chance to end holiday hunger' | school, meal, free, england, voucher | 0.936 |
| How football can help displaced people 'heal, develop and grow' | refugee, football, photo, participant, goal | 0.4019 |
| Michael Irving: Teens jailed for 'Trojan horse trap' murder | hair, twitter, footballer, sharp, post | -0.9442 |

## Getting Started

How to run the application

1. Clone the repository.
2. Open [constants.py](src/constants.py) and adjust the values as desired. 
3. Run [main.py](src/main.py) with ```python main.py```. The output data is saved in [data/sentiment.csv](data/sentiment.csv).

## Built With

* [TensorFlow](https://www.tensorflow.org/) - Deep Learning
* [NLTK](https://www.nltk.org/) - Natural Language Processing

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

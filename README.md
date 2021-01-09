# Uplifting News

React application which uses Python to scrape news articles, performing sentiment analysis to measure positivity and topic modelling to extract keywords.

## Description

We train an RNN on the [IMDB large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) for sentiment analysis. The raw text is preprocessed, then fed into the model. The model is used to predict the positivity of a given news article, with the most positive being displayed first. 

## Examples

| Article Title  | Score |
| ------------- | ------------- |
| NASA's Perseverance rover will launch to Mars next month with a global tribute to health care workers  | 4.6343  |
| How football can help displaced people heal, develop, and grow  | 2.7856  |
| Three children die and mother critical after Paisley fire  | -1.8799 |

## Getting Started

How to run the application

1. Clone the repository.
2. Open [constants.py](src/constants.py) and adjust the values as desired. 
3. Run [main.py](src/main.py) with ```python main.py```. The output image is saved in [data/sentiment.csv](data/sentiment.csv).

## Built With

* [TensorFlow](https://www.tensorflow.org/) - Deep Learning

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

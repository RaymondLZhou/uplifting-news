#!/bin/sh

python ../scraper/BBCScraper.py
python ../scraper/CNNScraper.py

python ../scraper/BBCRetriever.py
python ../scraper/CNNRetriever.py

python ../scraper/cleaner.py

python ../sentiment/vader.py

python combine.py

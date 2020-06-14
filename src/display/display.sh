#!/bin/sh

python ../scraper/BBCScraper.py
python ../scraper/CNNScraper.py

python ../sentiment/vader.py

python combine.py

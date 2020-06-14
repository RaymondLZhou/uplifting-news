#!/bin/sh

python ../scraper/BBCScraper.py
python ../scraper/CNNScraper.py

python ../sentiment/vader.py
python ../sentiment/merger.py

python combine.py

from scraper import scrape 
import json

url = "http://feeds.bbci.co.uk/news/rss.xml"
newsList = scrape(url)

with open("BBCFeed.json", "w") as outfile:
    json.dump(newsList, outfile, indent=4)

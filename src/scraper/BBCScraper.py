import feedparser as fp
import json

url = "http://feeds.bbci.co.uk/news/rss.xml"
feed = fp.parse(url)

newsList = []

for elem in feed.entries:

    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    newsObject = {
        "title": title,
        "description": description,
        "date": date,
        "link": link
    }
        
    newsList.append(newsObject)

with open("../data/BBCFeed.json", "w") as outfile:
    json.dump(newsList, outfile, indent=4)

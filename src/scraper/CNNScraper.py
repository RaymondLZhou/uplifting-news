import feedparser as fp
import json

url = "http://rss.cnn.com/rss/cnn_topstories.rss"
feed = fp.parse(url)

newsList = []

for elem in feed.entries:

    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary.split('<')[0] if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    if "" in (title, description, date, link):
        continue
    

    newsObject = {
        "title": title,
        "description": description,
        "date": date,
        "link": link
    }
        
    newsList.append(newsObject)

with open("CNNFeed.json", "w") as outfile:
    json.dump(newsList, outfile, indent=4)

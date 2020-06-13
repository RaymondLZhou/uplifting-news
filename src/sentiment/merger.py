import json

with open("../scraper/bbc/BBCFeed.json") as json_data:
    BBCFeed = json.load(json_data)

with open("BBCSentiment.json") as json_data:
    BBCSentiment = json.load(json_data)

displayFeed = []

for feed, sentiment in zip(BBCFeed, BBCSentiment):
    display = {
        "title": feed["title"],
        "description": feed["description"],
        "date": feed["date"],
        "link": feed["link"],
        "description": sentiment["description"],
        "positive": sentiment["positive"],
        "neutral": sentiment["neutral"],
        "negative": sentiment["negative"],
        "overall": sentiment["overall"]
    }

    displayFeed.append(display)

with open("BBCDisplayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)

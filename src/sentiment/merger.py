import json

def mergeFeed(information, sentiments):
    displayFeed = []

    for feed, sentiment in zip(information, sentiments):
        display = {
            "title": feed["title"],
            "description": feed["description"],
            "date": feed["date"],
            "link": feed["link"],
            "positive": sentiment["positive"],
            "neutral": sentiment["neutral"],
            "negative": sentiment["negative"],
            "overall": sentiment["overall"]
        }

        displayFeed.append(display)
    
    return displayFeed

with open("../data/BBCFeed.json") as json_data:
    BBCFeed = json.load(json_data)

with open("../data/BBCSentiment.json") as json_data:
    BBCSentiment = json.load(json_data)

displayFeed = mergeFeed(BBCFeed, BBCSentiment)

with open("../data/BBCDisplayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)


with open("../data/CNNFeed.json") as json_data:
    CNNFeed = json.load(json_data)

with open("../data/CNNSentiment.json") as json_data:
    CNNSentiment = json.load(json_data)

displayFeed = mergeFeed(CNNFeed, CNNSentiment)

with open("../data/CNNDisplayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)

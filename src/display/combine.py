import json

with open("../data/BBCSentiment.json") as json_data:
    BBCFeed = json.load(json_data)

with open("../data/CNNSentiment.json") as json_data:
    CNNFeed = json.load(json_data)

displayFeed = BBCFeed + CNNFeed
displayFeed.sort(key=lambda x: x['overall'])
displayFeed.reverse()

with open("../data/displayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)

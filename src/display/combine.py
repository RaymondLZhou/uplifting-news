import json

with open("../sentiment/BBCDisplayFeed.json") as json_data:
    BBCFeed = json.load(json_data)

with open("../sentiment/CNNDisplayFeed.json") as json_data:
    CNNFeed = json.load(json_data)

displayFeed = BBCFeed + CNNFeed
displayFeed.sort(key=lambda x: x['overall'])
displayFeed.reverse()

with open("displayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)
    
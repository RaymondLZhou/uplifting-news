import json

with open("../sentiment/BBCDisplayFeed.json") as json_data:
    BBCFeed = json.load(json_data)

with open("../sentiment/CNNDisplayFeed.json") as json_data:
    CNNFeed = json.load(json_data)

displayFeed = BBCFeed + CNNFeed

with open("DisplayFeed.json", "w") as outfile:
    json.dump(displayFeed, outfile, indent=4)
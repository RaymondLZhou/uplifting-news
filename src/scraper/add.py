from time import sleep

def appendDict(title, description, date, link, article, newsList):
    newsDict = {
        "title": title,
        "description": description,
        "date": date,
        "link": link,
        "text": article,
    }

    newsList.append(newsDict)

    sleep(1)

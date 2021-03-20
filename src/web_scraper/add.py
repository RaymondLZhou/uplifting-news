from time import sleep


def append_dict(title, description, date, link, article, newsList):
    news_dict = {
        "title": title,
        "description": description,
        "date": date,
        "link": link,
        "text": article,
    }

    newsList.append(news_dict)

    sleep(1)

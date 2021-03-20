import feedparser as fp

import parse
import clean
import add


def bbc_extract(url, news_list):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = parse.extract_fields(elem)
        soup = parse.create_soup(link)

        results = soup.find(class_="story-body__inner")

        if results is None:
            continue

        contents = soup.find_all("p")

        if len(contents) < 16:
            continue

        contents = clean.clean_contents(contents)
        article = clean.create_article(contents)

        add.append_dict(title, description, date, link, article, news_list)


def cnn_extract(url, news_list):
    feed = fp.parse(url)

    for elem in feed.entries:
        title, description, date, link = parse.extract_fields(elem)

        description = description.split('<')[0]

        if "" in (title, description, date, link):
            continue

        if link[-5:] != ".html":
            continue

        soup = parse.create_soup(link)
        contents = clean.find_contents(soup)
        article = clean.create_article(contents)

        add.append_dict(title, description, date, link, article, news_list)

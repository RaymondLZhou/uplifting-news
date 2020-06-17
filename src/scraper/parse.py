import requests
from bs4 import BeautifulSoup

def extractFields(elem):
    title = elem.title if 'title' in elem.keys() else ""
    description = elem.summary if 'summary' in elem.keys() else ""
    date = elem.published if 'published' in elem.keys() else ""
    link = elem.link if 'link' in elem.keys() else ""

    return title, description, date, link

def createSoup(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")

    return soup

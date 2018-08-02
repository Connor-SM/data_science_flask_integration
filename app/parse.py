import requests
from bs4 import BeautifulSoup


def getData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    center = list(body.children)[4]
    table = list(center.children)[0]
    return table

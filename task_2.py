import requests
from bs4 import BeautifulSoup as BS

def wiki_parsing():
    animals = []
    url = "https://inlnk.ru/jElywR"
    res = requests.get(url)
    if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        ul = soup.find('div', class_="mw-category mw-category-columns")
        li = ul.find_all('a', class_="")
        for i in li:
            title = i.text
            print(title)

wiki_parsing()

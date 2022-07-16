import requests
from bs4 import BeautifulSoup

# создаем функцию


def task():
    URL = "https://inlnk.ru/jElywR"
    data = []  # список всех животных
    for count in range(202):
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.find("div", class_="mw-category mw-category-columns"):
            for j in i.find_all('li'):
                data.append(j.get_text())
        for i in soup.find_all("a", title="Категория:Животные по алфавиту"):
            URL = "https://ru.wikipedia.org"+i.get('href')
    word = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # алфавит для счетчика
    # создаем цикл для подсчета имен по алфавиту
    for i in word:
        count = 0
        for j in data:
            if j[0] == i:
                count += 1
        print(i, ":", count)
    print(len(data))


task()

import pandas as pd
import requests
from bs4 import BeautifulSoup

# создаем функцию
def task():
    URL="https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
    data=[] #список всех животных
    for count in range(202):
        html=requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.find("div", class_="mw-category mw-category-columns"):
            for j in i.find_all('li'):
                data.append(j.get_text())
        for i in soup.find_all("a",title="Категория:Животные по алфавиту"):
            URL="https://ru.wikipedia.org"+i.get('href')

    word="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" #алфавит для счетчика
    # создаем цикл для подсчета имен по алфавиту
    for i in word:
        count=0
        for j in data:
            if j[0]==i:
                count+=1
        print(i,":",count)
    print(len(data))
    
task()
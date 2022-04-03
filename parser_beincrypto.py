import requests
from bs4 import BeautifulSoup
from time import sleep, time
from datetime import date, timedelta

import random
import os
import re



URL = 'https://beincrypto.ru/news/'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
           'accept': ACCEPT}
PROXY = {'http': 'http://161.202.226.194:8123', 'https': 'https://161.202.226.194:8123'}
#149.129.134.39:3128   http://20.97.28.47:8080 62.113.113.155:16286 95.85.24.83:8118


FILE = 'cars.csv'
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_="multi-news-card bb-1 d-lg-flex flex-lg-column mb-5")  #'div', class_='content')
    #print(items)
    print(items[1])

    urls = dict()
    for item in items:
        news = item.find('div', class_="title h-100").find_next('a')
        key = news.get_text()
        value = news.get('href')
        urls[key] = value
        print(f'news: {key}')
        print(f'http: {value}')
        print()
    return urls


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    for elem in soup.select('small'):
        print(elem)
        print('1')
        elem.decompose()
    for elem in soup.select('strong'):
        print(elem)
        print('1')
        elem.decompose()
    for elem in soup.select('div.notice'):
        print(elem)
        print('1')
        elem.decompose()
    for elem in soup.select('figure'):
        print(elem)
        print('1')
        elem.decompose()

    soup.prettify()
    title = soup.find('h1', class_='entry-title mb-3').get_text()
    data = soup.time.get_text()  #data = soup.find('time', class_='pl-md-2').get_text()
    item = soup.find('div', class_='entry-content-inner').get_text()

    print(len(item))

    #for elem in item:
    #    print(elem.text)
    #title = re.sub(r'[/|\\^:;*"?<>]', '', title)
    print(len(item))
    print(title)
    print(data)
    print(item)

    #print(type(item))
    return title #item, title

'''
def save_file(items, path):
    with open(path, 'w') as file:
        items = items.replace("\r", "").replace("\n", "")
        items = items.replace(".", ". ")[:-1]
        file.write(items)
'''


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(f'status {html.status_code}')
        urls = get_urls(html.text)  #список ссылок на новости
        print(urls['Токен Solana (SOL) пробил $90, следующая остановка — $100'])
        html = get_html(urls['Токен Solana (SOL) пробил $90, следующая остановка — $100'])
        print(f'status {html.status_code}')
        title = get_content(html.text)
    else:
        print(f'status {html.status_code}')
        '''
        urls = get_urls(html.text)  #список ссылок на новости
        sleep(random.uniform(0.99, 2.99))
        #text, title = get_content(html.text)
        #save_file(text, title + str(time()) + '.txt')

        print(len(urls))
        os.chdir('C:\\Users\\Igoryan\\Desktop\\PyTelegramBot\\parsing_text\\mk_news')
        for url in urls:
            try:
                html = get_html(url)
                if html.status_code == 200:
                    text, title = get_content(html.text)
                    save_file(text, title + ' ' + str(time()) + '.txt')
                    print(f'Loading URL: {url}')
                else:
                    print(f'ERROR: {url}')
                sleep(random.uniform(2.99, 6.99))
            except:
                print((f'ERROR SAVE DATA {url}'))
                continue
'''


if __name__ == '__main__':
    parse()

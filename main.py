''' 1.
Коды ответов 5хх указывают на непрограммные сбои, например, сбой подключения к БД или какой-либо другой сбой зависимости системы / библиотеки. 
Зачастую проблема решается повторной отправкой того же запроса.

Я бы проверила журналы ошибок и отладила код построчно, чтобы выяснить, почему сервер выдает ошибку.
'''

''' 2. '''

from typing import Callable

def create_handlers(callback: Callable) -> list:
    handlers = []
    for step in range(5):
        # в lambda захватывалась внешняя переменная step, а не ее значение в момент создания lambda,
        # поэтому callback вызывалась бы от значения 4, т.е. от последнего значения данной переменной
        handlers.append(lambda x = step: callback(x))
    return handlers


def execute_handlers(handlers: list):
    for handler in handlers:
        handler()


''' 3.'''

import requests
from lxml import html

url = 'https://greenatom.ru'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
    }

page = requests.get(url, headers=headers)

tree = html.fromstring(page.content).cssselect('*')
count_tags = len(tree)

count_att = sum([1 if tags.attrib else 0 for tags in tree])
 
print(f'Количество тегов = {count_tags}. Из них атрибуты содержит {count_att} тегов.') # 774, 478

'''4.'''

import http.client

def get_IP():
    return print(requests.get("https://ifconfig.me/ip", headers=headers).text)

def get_IP_2():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    return print(conn.getresponse().read().decode())

get_IP()   # первый вариант
get_IP_2() # второй вариант



''' 5. '''
def version_comparison(A, B):
    try:
        a = list(map(int, A.split('.')))
        b = list(map(int, B.split('.')))

        if a < b:
            return -1
        elif a == b:
            return 0
        elif a > b:
            return 1

    except:
        return "Invalid version number"
    
A = "1.2.1"
B = "2.a1.2"

a1 = "2.3.2"
b1 = "2.4.1"

a = "1.10"
b = "1.1"
print(version_comparison(A, B))   # Invalid version number
print(version_comparison(a1, b1)) # -1
print(version_comparison(a, b))   # 1
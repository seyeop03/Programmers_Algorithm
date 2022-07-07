# -*- coding: euc-kr -*-

import requests
from bs4 import BeautifulSoup

base_url = 'https://programmers.co.kr/learn/courses/2'
dirty_html = requests.get(base_url)
soup = BeautifulSoup(dirty_html.text, 'html.parser')

for i in range(18):
    index_selector = '#curriculum > div > div > div[data-index="{}"]'.format(i)
    specific_lecture_list = soup.select_one(index_selector)
    ul_num = specific_lecture_list.select('ul li')

    for j in range(len(ul_num)):
        url_selector = 'ul > li:nth-child({}) > div.lesson-detail-wrapper > div.title-wrapper > a'.format(j + 1)
        note_url = specific_lecture_list.select_one(url_selector)['href']

        note_html = requests.get(note_url)
        note_soup = BeautifulSoup(note_html.text, 'html.parser')
        if note_soup.select_one('#note') is not None:
            print(note_soup.select_one('#note'))
            print('#########################################################')
#================================================================================
#================================================================================
#================================================================================
#================================================================================
#================================================================================
import requests
from bs4 import BeautifulSoup

url = 'https://programmers.co.kr/learn/courses/2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

specific_lecture_list = soup.select_one(
    '#curriculum > div > div > div[data-index="0"]')

for i in range(5):
    url_selector = 'ul > li:nth-child({}) > div.lesson-detail-wrapper > div.title-wrapper > a'.format(i+1)
    note_url = specific_lecture_list.select_one(url_selector)['href']
    print(note_url)
    note_html = requests.get(note_url)
    note_soup = BeautifulSoup(note_html.text, 'html.parser')
    print(note_soup.select('#note'))


""" selector
#note > div.markdown.github

body > div.main > div.lesson-content-bottom > div.content-tab > div > ul > li:nth-child(1) > a

#curriculum > div > div > div:nth-child(1) > ul > li:nth-child(4) > div.lesson-detail-wrapper > div.title-wrapper > a
#curriculum > div > div > div:nth-child(1) > ul > li:nth-child(5) > div.lesson-detail-wrapper > div.title-wrapper > a
# ul > li:nth-child(4) > div.lesson-detail-wrapper > div.title-wrapper > a
"""
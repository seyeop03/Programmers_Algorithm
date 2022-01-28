import requests
from bs4 import BeautifulSoup

url = 'https://programmers.co.kr/learn/courses/2'

dirty_html = requests.get(url)
soup = BeautifulSoup(dirty_html.text, 'html.parser')

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
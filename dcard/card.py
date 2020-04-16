import urllib
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

#設定webdriver及網址
driver = webdriver.Chrome('C:/Users/Asus/Desktop/chromedriver')
url = 'https://www.dcard.tw/f'
driver.get(url)

#在搜尋框輸入文字
inputElement = driver.find_element_by_tag_name('input') #找輸入框
inputElement.send_keys('Python') #在輸入框輸入python

driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()#點擊搜尋，利用css找button的元素
time.sleep(2)

html = driver.page_source#取得網站內容(是一串網站內容文字)
soup = bs(html, 'html.parser')#解析網站

#獲取文章看板作者時間
data = soup.find_all('span', {'class': 'sc-6oxm01-2 hiTIMq'})#取得資料

meta_datas = []
for x in data:
    meta_datas.append(x.text.strip())#獲取文字
# print(meta_datas)

#將看版作者時間分類
forums = []
author = []
time = []
for i in range(len(meta_datas)):
    if i % 3 == 0:
        forums.append(meta_datas[i])
    if i % 3 == 1:
        author.append(meta_datas[i])
    if i % 3 == 2:
        time.append(meta_datas[i])

#獲取看版標題
data = soup.find_all('h2', {'class': 'sc-1v1d5rx-3'})#f12找到看版標題的
title = []
for x in data:
    title.append(x.text)
print(title)

#獲取看板相關連結
data_href = soup.find_all('a', {'class': 'sc-1v1d5rx-4 gCVegi'})#f12找到看版標題的
hrefs = []
for x in data_href:
    hrefs.append(x['href'])
print(hrefs)

#從相對連結及url及網址
links = []
for href in hrefs:
    links.append(urljoin(url, href))
print(links)

for i in range(len(forums)):
    print(forums[i], title[i], links[i])
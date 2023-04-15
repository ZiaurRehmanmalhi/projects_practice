from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()
url = "https://www.youtube.com/watch?v=zghBofrKv7s&ab_channel=EhmadZubair"
driver.get(url)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    time.sleep(1.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_content = soup.find_all('ytd-comment-thread-renderer')

data = []
for comment_data in all_content:
    user_info = comment_data.find('ytd-comment-renderer').find('a', {'id': 'author-text'})
    user_name = user_info.text.strip()
    comment_time = comment_data.find('a', {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).text
    comment_text = comment_data.find('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'}).text
    thumbnail_URL = comment_data.find('img', {'class': 'style-scope yt-img-shadow'}).get('src')
    number_of_likes = comment_data.find('span', {'class': 'style-scope ytd-comment-action-buttons-renderer'}).text.strip()

    all_data = [user_name, comment_time, comment_text, thumbnail_URL, number_of_likes]
    data.append(all_data)
    print(data)
driver.quit()

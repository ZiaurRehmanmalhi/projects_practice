from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

driver = webdriver.Chrome()
driver.get("https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&top_rated_plus=yes")
time.sleep(15)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

all_content = soup.find_all('bis_skin_checked')

data = []
for comment_data in all_content:
    # user_info = comment_data.find('ytd-comment-renderer').find('a', {'id': 'author-text'})
    # user_name = user_info.text.strip()
    name = comment_data.find('div', {'class': 'd-inline-block text-muted'})
    # comment_text = comment_data.find('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'}).text
    data.append(name)

print(data)

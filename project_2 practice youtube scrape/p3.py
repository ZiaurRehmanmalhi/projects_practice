import time
import os

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

from utils import scroll_to_page_end, extract_comment_data


url = input("Enter Any Youtube Chanel URL: ")
url += "/videos"


def create_csv(channel_url):
    channel_username = channel_url.split("com/")[-1].replace('@', '')
    if not os.path.exists(channel_username):
        os.makedirs(channel_username)
    driver = webdriver.Chrome()
    driver.get(channel_url)
    scroll_to_page_end(driver)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_content = soup.find_all('ytd-rich-grid-media')

    for video_data in all_content:
        video_title = video_data.find('a', {'id': 'video-title-link'}).text.strip()
        video_link = 'https://www.youtube.com' + video_data.find('a', {'id': 'video-title-link'}).get('href')
        driver.get(video_link)
        time.sleep(4)

        scroll_to_page_end(driver)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        data = extract_comment_data(soup)

        df = pd.DataFrame(data,
                          columns=['Username', 'Comment Time', 'Comment Text', 'Thumbnail URL', 'Number of Likes'])
        df.to_csv(os.path.join(channel_username, video_title.replace('/', '|') + '.csv'), index=False)
        driver.quit()
        print("Data successfully saved to csv files.")

    create_csv(url)


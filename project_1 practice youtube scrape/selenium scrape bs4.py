from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@zusmani78/videos")
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
videos = soup.find_all('ytd-grid-video-renderer')

titles = videos.find('a', {'id': 'video-title'}).text
views = videos.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text.strip()
duration = videos.find('span', {'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).text.strip()
upload_times = videos.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text.strip()

contents = []
for title, view, upload_time, video_duration in zip(titles, views, upload_times, duration):
    video_data = {
        "title": title.text,
        "views": view.text,
        "upload_time": upload_time.text,
        "video_duration": video_duration.text
    }
    contents.append(video_data)
# df = pd.DataFrame(data, columns=['Name', 'Views', 'Duration', 'Time Uploaded'])
# df.to_csv('youtube_videos.csv', index=False)
print(contents)
driver.quit()

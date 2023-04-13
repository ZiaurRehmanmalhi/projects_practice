from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
# url = input("Enter The Youtube videos URL : ")
url = "https://www.youtube.com/@zusmani78/videos"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_content = soup.find_all('ytd-rich-item-renderer')

data = []
for videos in all_content:
    thumbnail = videos.find('img', {"style": "background-color: transparent;"}).get('src')
    title = videos.find('yt-formatted-string', {"id": "video-title"}).text
    views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
    upload_time = videos.find('div', {"class": "style-scope ytd-video-meta-block"}).text.strip().split('\n')[-1::-3][0]
    # upload_time = videos.find('ytd-badge-supported-renderer', {"id": "video-title-link"})
    video_duration = videos.find('span', {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text.strip()

    all_data = [title, views, video_duration, thumbnail]
    data.append(all_data)

    print(upload_time)
# df = pd.DataFrame(data, columns=["Title", "Views", "Duration", "Upload Time", "Thumbnail"])
# df.to_csv("youtube_videos.csv", index=False)
driver.quit()



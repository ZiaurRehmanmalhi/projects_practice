import time
import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://www.youtube.com/@YasoobKhalid/videos")

# channel_title = driver.find_element(By.XPATH, '//yt-formatted-string[contains(@class, "ytd-channel-name")]').text
# handle = driver.find_element(By.XPATH, '//yt-formatted-string[@id="channel-handle"]').text
# subscriber_count = driver.find_element(By.XPATH, '//yt-formatted-string[@id="subscriber-count"]').text

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll to the bottom of page
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    # Wait for new videos to show up
    time.sleep(5)

    # Calculate new document height and compare it with last height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

thumbnails = driver.find_elements(By.XPATH, '//a[@id="thumbnail"]/yt-image/img')
views = driver.find_elements(By.XPATH, '//div[@id="metadata-line"]/span[1]')
titles = driver.find_elements(By.ID, "video-title")
links = driver.find_elements(By.ID, "video-title-link")

videos = []
for title, view, thumb, link in zip(titles, views, thumbnails, links):
    video_dict = {
        'title': title.text,
        'views': view.text,
        'thumbnail': thumb.get_attribute('src'),
        'link': link.get_attribute('href')
    }
    videos.append(video_dict)

print(videos)

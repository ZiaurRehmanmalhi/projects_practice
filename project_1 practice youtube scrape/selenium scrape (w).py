import time
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    time.sleep(1.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


titles = driver.find_elements(By.ID, "video-title")
views = driver.find_elements(By.XPATH, '//div[@id="metadata-line"]/span[1]')
# views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')
upload_times = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[2]')
video_durations = driver.find_elements(By.XPATH, '//*[@id="text"]')
contents = []

for title, view, upload_time, video_duration in zip(titles, views, upload_times, video_durations):
    video_data = {
        "title": title.text,
        "views": view.text,
        "upload_time": upload_time.text,
        "video_duration": video_duration.text
    }
    contents.append(video_data)

    print(contents)

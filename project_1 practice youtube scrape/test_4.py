from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://www.youtube.com/@zusmani78/videos")

scroll_distance = 2000
i = 0

while True:
    driver.execute_script("window.scrollBy(0, 2000);")
    time.sleep(0.5)
    i += 1

    # check if we've reached the end of the page
    if i >= 28:
        break

# scrape video information
video_elements = driver.find_elements_by_xpath("//div[@id='dismissible']")
video_data = []

for video in video_elements:
    name = video.find_element_by_xpath(".//a[@id='video-title']").text
    views = video.find_element_by_xpath(".//span[@class='style-scope ytd-grid-video-renderer']"
                                        "/span[contains(@aria-label, 'views')]").get_attribute('aria-label')
    duration = video.find_element_by_xpath(".//span[@class='style-scope ytd-grid-video-renderer']"
                                           "/span[contains(@class, 'ytd-thumbnail-overlay-time-status-renderer')]").text
    upload_time = video.find_element_by_xpath(".//span[@class='style-scope ytd-grid-video-renderer']"
                                              "/span[contains(@class, 'ytd-thumbnail-overlay-time-status-renderer')]"
                                              "/following-sibling::span").text
    video_data.append([name, views, duration, upload_time])

# write video data to CSV file
df = pd.DataFrame(video_data, columns=['Name', 'Views', 'Duration', 'Upload Time'])
df.to_csv('video_data.csv', index=False)

driver.quit()

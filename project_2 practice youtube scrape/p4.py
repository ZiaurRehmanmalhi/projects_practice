from selenium import webdriver
from utils import process_channel_videos

channel_url = input("Enter the URL of the YouTube channel: ")

driver = webdriver.Chrome()
process_channel_videos(channel_url, driver)
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome(executable_path="chromedriver")
wait = WebDriverWait(driver, 10)
driver.get("https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&page=1&top_rated_plus=yes")
time.sleep(15)
while True:
    last_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
    new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_scroll_height == last_scroll_height:
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "next-icon")))
            if not next_button.is_displayed():
                break
            next_button.click()
            time.sleep(2)
        except (NoSuchElementException, TimeoutException):
            break

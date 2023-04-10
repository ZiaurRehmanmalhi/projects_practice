import article as article
from article import Article
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://techwithtim.net/")

print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for articles in articles:
        header = article.find_element_by_class_name("entry-title")
        print(header.text)

finally:
    driver.quit()

main = driver.find_element_by_id("main")
print(main.text)

print(driver.page_source)
time.sleep(5)
driver.quit()

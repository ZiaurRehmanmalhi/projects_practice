import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&page=1&top_rated_plus=yes"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(URL)
time.sleep(15)
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')

# data = soup.find_all('div', {'class': 'identity-name'})    # main div
# data = soup.find_all('div', {'class': 'identity-name'})    # name
# data = soup.find_all('p', {'class': 'my-0 freelancer-title'}) # role
# data = soup.find_all('span', {'class': 'd-inline-block vertical-align-middle'})   # country
# data = soup.find_all('div', {'class': 'up-card-section d-flex'})  # link no
# data = soup.find_all('div', {'data-qa': 'rate'})  # hourly_rate
# data = soup.find_all('span', {'data-test': 'earned-amount-formatted'})  # total_earned
# data = soup.find_all('span', {'class': 'up-job-success-text'})  # job_success_score
# data = soup.find_all('span', {'class': 'status-text d-flex top-rated-badge-status'})  # badge
# data = soup.find_all('div', {'class': 'up-line-clamp-v2 clamped'})  # bio
# data = soup.find_all('div', {'class': 'd-flex align-items-center up-btn-link'})  # company_name
data = soup.find_all('div', {'class': 'ml-10 agency-box-stats'})  # company_earn
# data = soup.find_all('div', {'class': 'up-card-section up-card-hover'})  # raw_html


for freelancer in data:
    name = freelancer.text.strip()
    print(name)
driver.quit()









# ziamalhi1234@gmail.com
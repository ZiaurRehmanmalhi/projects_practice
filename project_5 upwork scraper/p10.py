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

data = soup.find_all('div', {'class': 'up-card-section up-card-hover'})    # main div

for freelancer in data:
    name = freelancer.find('div', {"class": "identity-name"}).text.strip()
    role = freelancer.find('p', {'class': 'my-0 freelancer-title'}).text.strip()

    profile_link = soup.find_all('div', {'class': 'd-flex justify-space-between align-items-start'})
    split_data = str(profile_link).split()
    sliced_data = split_data[9:10]
    split_sliced_data = sliced_data[0].split("=")
    final = split_sliced_data[1]
    final = final.replace('"', '')
    joined_final = 'https://www.upwork.com/freelancers/' + final

    country = soup.find('span', {'class': 'd-inline-block vertical-align-middle'}).text.strip()
    hourly_rate = soup.find('div', {'data-qa': 'rate'}).text.strip()
    total_earned = soup.find('span', {'data-test': 'earned-amount-formatted'}).text.strip()
    job_success_score = soup.find('span', {'class': 'up-job-success-text'}).text.strip()\
        .replace('\n', '').replace('            ', '')
    badge = soup.find('span', {'class': 'status-text d-flex top-rated-badge-status'}).text.strip()
    bio = soup.find('div', {'class': 'up-line-clamp-v2 clamped'}).text.strip()
    company_name = soup.find('div', {'class': 'd-flex align-items-center up-btn-link'}).text.strip()
    company_earn = soup.find('div', {'class': 'ml-10 agency-box-stats'}).text.strip()
    raw_html = soup.find('div', {'class': 'up-card-section up-card-hover'})

    print(joined_final)
driver.quit()


# ziamalhi1234@gmail.com
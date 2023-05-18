import time
from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&page=1&top_rated_plus=yes"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(URL)
time.sleep(15)
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')

data = soup.find_all('div', {'class': 'up-card-section up-card-hover'})    # main div

freelancers_data = []

for freelancer in data:
    name = freelancer.find('div', {"class": "identity-name"}).text.strip()
    role = freelancer.find('p', {'class': 'my-0 freelancer-title'}).text.strip()
    country = freelancer.find('span', {'class': 'd-inline-block vertical-align-middle'}).text.strip()
    hourly_rate = freelancer.find('div', {'data-qa': 'rate'}).text.strip()
    total_earned = freelancer.find('span', {'data-test': 'earned-amount-formatted'}).text.strip()
    job_success_score = freelancer.find('span', {'class': 'up-job-success-text'}).text.strip()\
        .replace('\n', '').replace('            ', '')
    badge = freelancer.find('span', {'class': 'status-text d-flex top-rated-badge-status'}).text.strip()
    bio = freelancer.find('div', {'class': 'up-line-clamp-v2 clamped'}).text.strip()
    company_name_elem = freelancer.find('div', {'class': 'd-flex align-items-center up-btn-link'})
    company_name = company_name_elem.text.strip() if company_name_elem else ""
    company_earn_elem = freelancer.find('div', {'class': 'ml-10 agency-box-stats'})
    company_earn = company_earn_elem.text.strip() if company_earn_elem else ""
    raw_html = freelancer.prettify()

    freelancer_data = {
        "Name": name,
        "Role": role,
        "Country": country,
        "Hourly Rate": hourly_rate,
        "Job Success Score": job_success_score,
        "Badge": badge,
        "Bio": bio,
        "Company Name": company_name,
        "Company Earn": company_earn,
        "Raw HTML": raw_html
    }
    freelancers_data.append(freelancer_data)

driver.quit()

print(freelancers_data)

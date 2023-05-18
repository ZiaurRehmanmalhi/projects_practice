import re
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
driver.quit()

names = soup.find_all('div', {'class': 'identity-name'})
roles = soup.find_all('p', {'class': 'my-0 freelancer-title'})
profile_links = soup.find_all('div', {'class': 'd-flex justify-space-between align-items-start'})
countries = soup.find_all('span', {'class': 'd-inline-block vertical-align-middle'})
hourly_rates = soup.find_all('div', {'data-qa': 'rate'})
total_earneds = soup.find_all('span', {'data-test': 'earned-amount-formatted'})
job_success_scores = soup.find_all('span', {'class': 'up-job-success-text'})
badges = soup.find_all('span', {'class': 'status-text d-flex top-rated-badge-status'})
bios = soup.find_all('div', {'class': 'up-line-clamp-v2 clamped'})
company_names = soup.find_all('div', {'class': 'd-flex align-items-center up-btn-link'})
company_earns = soup.find_all('div', {'class': 'ml-10 agency-box-stats'})
raw_htmls = soup.find_all('div', {'class': 'up-card-section up-card-hover'})
company_links = soup.find_all('div', {'class': 'cfe-ui-freelancer-tile-agency-box-legacy mt-5 mt-10 agency-box-legacy--link'})

# Check if all lists have the same length
if len(names) == len(roles) == len(profile_links) == len(countries) == len(hourly_rates) == len(total_earneds) == len(job_success_scores) == len(badges) == len(bios) == len(company_names) == len(company_earns) == len(raw_htmls) == len(company_links):
    for i in range(len(names)):
        name = names[i].text.strip()
        role = roles[i].text.strip()
        split_data = str(profile_links[i]).split()
        sliced_data = split_data[9:10]
        split_sliced_data = sliced_data[0].split("=")
        final = split_sliced_data[1].replace('"', '')
        joined_final = 'https://www.upwork.com/freelancers/' + final
        country = countries[i].text.strip()
        hourly_rate = hourly_rates[i].text.strip()
        total_earned = total_earneds[i].text.strip()
        score = job_success_scores[i].text.strip()
        cleaned_data = re.sub(r'\s+', ' ', ' '.join(filter(None, score.split('\n')))).strip()
        badge = badges[i].text.strip()
        bio = bios[i].text.strip()
        company_name = company_names[i].text.strip()
        company_earn = company_earns[i].text.strip()
        raw_html = raw_htmls[i].text.strip()
        split_data = str(company_links[i]).split()
        sliced_data = split_data[5:6]
        split_sliced_data = sliced_data[0].split('=')
        sliced_split_sliced_data = split_sliced_data[1:]
        cleaned_data = sliced_split_sliced_data[0].strip('[]').strip('"')
        company_link_final = 'https://www.upwork.com/agencies/' + cleaned_data

        print("Name:", name)
        print("Role:", role)
        print("Profile Link:", joined_final)
        print("Country:", country)
        print("Hourly Rate:", hourly_rate)
        print("Total Earned:", total_earned)
        print("Job Success Score:", cleaned_data)
        print("Badge:", badge)
        print("Bio:", bio)
        print("Company Name:", company_name)
        print("Company Earn:", company_earn)
        print("Raw HTML:", raw_html)
        print("Company Links:", company_link_final)
        print()
else:
    print("Lists have different lengths. Unable to process data.")

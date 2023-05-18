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
main_div = soup.find_all('div', {'class': 'up-card-section up-card-hover'})
freelancers_data = []
for div in main_div:
    names = div.find('div', {'class': 'identity-name'}).text.strip()
    roles = div.find('p', {'class': 'my-0 freelancer-title'}).text.strip()
    profile_links = div.find_all('div', {'class': 'd-flex justify-space-between align-items-start'})
    split_data = [str(element).split() for element in profile_links]
    sliced_data = split_data[0][9:10]
    split_sliced_data = sliced_data[0].split("=")
    final = split_sliced_data[1]
    finals = final.replace('"', '')
    joined_final_pl = 'https://www.upwork.com/freelancers/' + finals
    countries = div.find('span', {'class': 'd-inline-block vertical-align-middle'}).text.strip()
    hourly_rates = div.find('div', {'data-qa': 'rate'}).text.strip()
    total_earneds = div.find('span', {'data-test': 'earned-amount-formatted'}).text.strip()
    job_success_scores = div.find('span', {'class': 'up-job-success-text'}).text.strip()
    job_cleaned_data = re.sub(r'\s+', ' ', ' '.join(filter(None, job_success_scores.split('\n')))).strip()
    badges = div.find('span', {'class': 'status-text d-flex top-rated-badge-status'}).text.strip()
    bios = div.find('div', {'class': 'up-line-clamp-v2 clamped'}).text.strip()
    company_names = div.find('div', {'class': 'd-flex align-items-center up-btn-link'}).text.strip()
    company_earns = div.find('div', {'class': 'ml-10 agency-box-stats'}).text.strip()
    raw_htmls = div.find('div', {'class': 'up-card-section up-card-hover'}).prettify()
    company_links = div.find(
        'div', {'class': 'cfe-ui-freelancer-tile-agency-box-legacy mt-5 mt-10 agency-box-legacy--link'})
    split_data = str(company_links).split()
    sliced_data = split_data[5:6]
    split_sliced_data = sliced_data[0].split('=')
    sliced_split_sliced_data = split_sliced_data[1:]
    cleaned_data = sliced_split_sliced_data[0].strip('[]').strip('"')
    company_link_final = 'https://www.upwork.com/agencies/' + cleaned_data
    freelancer_data = {
            "Name": names,
            "Role": roles,
            "Profile Link": joined_final_pl,
            "Country": countries,
            "Hourly Rate": hourly_rates,
            "Total Earned": total_earneds,
            "Job Success Score": job_cleaned_data,
            "Badge": badges,
            "Bio": bios,
            "Company Name": company_names,
            "Company Earn": company_earns,
            "Raw HTML": raw_htmls,
            "company links": company_link_final
        }
    freelancers_data.append(freelancer_data)
driver.quit()

for freelancer in freelancers_data:
    print(freelancer)

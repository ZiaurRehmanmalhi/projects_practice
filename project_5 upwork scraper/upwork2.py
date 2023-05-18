from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Upwork search results page
driver.get("https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&page=1&top_rated_plus=yes")
34
# Wait for the "Next" button to appear at the bottom
next_button_locator = (By.XPATH, '//a[@class="pagination-next"]')
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(next_button_locator))

# Extract data for each person on the current page
person_locator = (By.XPATH, '//section[@class="air-card air-card-hover freelancer-tile"]')
people = driver.find_elements(*person_locator)

for person in people:
    name = person.find_element(By.CSS_SELECTOR, 'h4.freelancer-tile-name').text
    role = person.find_element(By.CSS_SELECTOR, 'p.freelancer-tile-title').text
    link = person.find_element(By.CSS_SELECTOR, 'a.freelancer-tile-name-link').get_attribute('href')
    country = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-location').text
    hourly_rate = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-rate').text
    total_earned = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-earnings').text
    job_success_score = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-job-success').text
    badge = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-top-rated').text
    bio = person.find_element(By.CSS_SELECTOR, 'div.freelancer-tile-description').text
    company = person.find_element(By.CSS_SELECTOR, 'a.freelancer-tile-company').text
    company_link = person.find_element(By.CSS_SELECTOR, 'a.freelancer-tile-company').get_attribute('href')
    company_earned = person.find_element(By.CSS_SELECTOR, 'span.freelancer-tile-company-earnings').text

    # Perform further processing or store the extracted information as needed

# Click the "Next" button to navigate to the next page
next_button = driver.find_element(*next_button_locator)
next_button.click()

# Repeat the above steps for subsequent pages until the end of the listing is reached

# Clean up and quit the driver
driver.quit()

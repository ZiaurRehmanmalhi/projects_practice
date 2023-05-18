import requests
from bs4 import BeautifulSoup
URL = "https://www.upwork.com/ab/profiles/search/?category_uid=531770282580668418&page=1&top_rated_plus=yes"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/96.0.4664.110 Safari/537.36'
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
names = soup.find_all('div', {'data-test': 'transition'})
print(response.content)
for name in names:
    title = name.find('div', {'class': 'full-width'})
    print(title)
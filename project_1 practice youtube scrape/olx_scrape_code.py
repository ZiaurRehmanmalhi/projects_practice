import pandas as pd
from tqdm import tqdm
import re
import requests
from bs4 import BeautifulSoup

category_url = "https://www.olx.com.pk/toyota-cars_c84"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/96.0.4664.110 Safari/537.36'
}

product_urls = set()

print("Extracting the product urls from listing page#: ")

page_no = 1
while True:
    url = f"{category_url}?page={page_no}"

    site = requests.get(url, headers=headers)
    if site.url != url and "page=1" not in url:
        break
    soup = BeautifulSoup(site.content, 'html.parser')
    product_eliments = (
        soup
        .find("div", {"class": re.compile("_1075545d")})
        .find("ul", {"class": re.compile("ba608fb8 de8df3a3")})
        .find_all("li", {"aria-label": re.compile("Listing")})

    )
    product_urls |= {f"https://www.olx.com.pk{p.a.attrs['href']}" for p in product_eliments if p.a}
    print(page_no, end=", ")
    page_no += 1
    break

def extract_product_details(product_url):
    site = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    title = soup.find("h1", {"class": "a38b8112"}).get_text('\n')
    name = title.find(title) if title else ""
    price = soup.find("span", {"class": "_56dab877"}).get_text(strip=True)
    miles_covered = soup.find("span", {"class": "_7f02578b"}).find("span", {"class": "fef55ec1"}).text
    model = soup.find("div", {"class": "_241b3b1e"}).find("div", {"class": "b44ca0b3"}).find(
        "span").next.next.next.next.next.next.next.next.next
    description = soup.find("div", {"class": "_0f86855a"}).get_text(strip=True)
    features = soup.find("div", {"class": "_27f9c8ac"}).get_text(' \n ')
    location = soup.find("div", {"class": "_1075545d e3cecb8b _5f872d11"}).find("span", {"class": "_8918c0a8"}).text
    primary_image_url = soup.find("div", {"class": "image-gallery-slide center"}).img.attrs['src']
    all_image_urls = soup.find("div", {"class": "image-gallery-slides"})
    all_image_links = []
    if all_image_urls is not None:
        for img in all_image_urls.find_all('img'):
            all_image_links.append(img['src'])
    else:
        ""
    all_links = '\n'.join(all_image_links[1:])

    return {
        "title": title,
        "price": price,
        "miles_covered": miles_covered,
        "model": model,
        "description": description,
        "features": features,
        "location": location,
        "primary_image_url": primary_image_url,
        "all_links": all_links,
    }
print('\n' "now extract_product_details")

product_data = []
for product_url in tqdm(list(product_urls)):
    product_data += [extract_product_details(product_url)]
df = pd.DataFrame(product_data)
df.to_csv("output.csv", index=False)
# print(product_data)

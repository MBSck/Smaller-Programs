import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup


url = "http://www.epguides.com/menu/current.shtml"
short_url = "http://www.epguides.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

results = []

for _ in range(0, 27):
    sections = soup.find("div", attrs={"class": "cont"})
    list_of_links = sections.find_all("a")

    soup.find_next()

    for link in list_of_links:
        results.append(link.get("href")[3:])

    print(results)

    print(os.path.join(short_url, results[0]))
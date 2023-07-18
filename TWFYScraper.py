import requests
from bs4 import BeautifulSoup

url = "https://www.theyworkforyou.com/pwdata/scrapedxml/debates/"
pg_text = requests.get(url)

soup = BeautifulSoup(pg_text.content, "html.parser")

results = soup.find(id = "ResultsContainer")

py_search = results.find_all("div", class_="card-content")


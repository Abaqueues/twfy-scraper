import re
import requests
import pandas as pd
import urllib3
import os
from bs4 import BeautifulSoup as bs

# Use requests library to access the website
_URL = "https://www.theyworkforyou.com/pwdata/scrapedxml/debates/"
page = requests.get(_URL)

# Define scraper parameters
_YEAR = 2023
_OUTPUT_FOLDER = "E:\\Documents\\Education\\PG University of Birmingham\\MSc Computer Science\\Summer Semester\\MSc Projects\\Project Files\\Dataset\\xml"

# Function to check whether .xml file corresponds to debates after given date
def isAfter(string):
    number = re.findall(r'\d+', string)
    if int(number[0]) > _YEAR:
        return True
    else:
        return False

# Instantiate BeautifulSoup object
soup = bs(page.content, "html.parser")

urls = []
names = []

# Loops through all classes tagged "a" and adds relevant names/URLs to list
for i, link in enumerate(soup.findAll("a")):
    _FULLURL = _URL + link.get("href")
    if _FULLURL.endswith(".xml"):
        if isAfter(_FULLURL):
            urls.append(_FULLURL)
            names.append(soup.select("a")[i].attrs["href"])

# Combines the names/URLs lists 
names_urls = zip(names, urls)

# Function to download .xml files 
def scrape_file(name, url):
    print(_OUTPUT_FOLDER + "\\" + name)
    if os.path.exists(_OUTPUT_FOLDER + "\\" + name) == True:
        print(f"File '{name}' already exists. Skipping...")
    else:
        print("Downloading %s" % url)
        r = requests.get(url)
        with open(_OUTPUT_FOLDER + name.split("/")[-1], "wb") as f:
            f.write(r.content)
            
for name, url in zip(names, urls):
    print(f"{name}" + f"{url}")
            
# Loops through and downloads the files using the URLs in the zipped list
print("Initiating scraping loop")
for name, url in list(names_urls):
    print(f"Scraping '{name}")
    scrape_file(name, url)
    
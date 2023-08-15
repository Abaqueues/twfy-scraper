import re
import requests
import pandas as pd
import urllib3
import os
from bs4 import BeautifulSoup as bs

# Use requests library to access the website
_URL = "https://www.theyworkforyou.com/pwdata/scrapedxml/debates/"
page = requests.get(_URL)

# Function to check whether .xml file corresponds to debates after 2012
year = 2012

def isAfter(string):
    number = re.findall(r'\d+', string)
    if int(number[0]) > year:
        return True
    else:
        return False

# Instantiate BeautifulSoup object
soup = bs(page.content, "html.parser")

# Loops through index table and adds relevant rows to new list
# table = soup.find("table")
# rows=list()
# for row in table.find_all("a"):
#     if (row.text).startswith("debates"):
#         if isAfter2012:
#             print(row.text)
#             rows.append(row)

urls = []
names = []

# Loops through all classes tagged "a" and adds relevant names/URLs to list
for i, link in enumerate(soup.findAll("a")):
    _FULLURL = _URL + link.get("href")
    print(_FULLURL)
    if _FULLURL.endswith(".xml"):
        if isAfter(_FULLURL):
            urls.append(_FULLURL)
            names.append(soup.select("a")[i].attrs["href"])

# Combines the names/URLs lists 
names_urls = zip(names, urls)
print(names_urls)

# Downloads the files using the URLs in the zipped list
# def file_exists(path):
#     return os.path.exists(path)

def scrape_file(name, url):
    # if file_exists(file_path):
    #     print(f"File '{name}' already exists. Skipping...")
    #     return
    print("Downloading %s" % url)
    r = requests.get(url)
    with open("E:\Documents\Education\PG University of Birmingham\MSc Computer Science\Summer Semester\MSc Projects\Project Files\Dataset\xml" + name.split("/")[-1], "wb") as f:
        f.write(r.content)

for name, url in names_urls:
    scrape_file(name, url)

# for name, url in names_urls:
#     print(url)
#     rq = urllib3.request(url)
#     res = urllib3.urlopen(rq)
#     xml = open("xmls/" + name, 'wb')
#     xml.write(res.read())
#     xml.close()    
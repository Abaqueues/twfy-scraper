# twfy-scraper

## Description
A Python webscraper that connects to the TheyWorkForYou scraped .xml index for Hansard parliamentary debates. The webscraper collates a list of debates after a given year and proceeds to download and save each of the .xml files in the list.

Development of this webscraper was necessary after numerous unsuccessful attempts to utilise the TheyWorkForYou API to gather parliamentary debate data. Further attempts using ajparsons's Python binding (twfy-python, https://github.com/ajparsons/twfy-python) were also unsuccessful - while the binding could return data using the .getMPs function call, the .getDebates function call failed to garner a response from the server.

## Usage
Modify line 13's variable according to limit (by year) the number of files you want to download from the website.

## Roadmap
Currently, the webscraper must compile the list of .xml files each time it is run. Ideally, I would like this list to be output to a .txt file - if the first result of the query is the same as the first file in the .txt file, compilation of the list can be skipped. 
# 📘 Day 22

# Python Web Scraping

# What is Web Scraping
'''
The internet is full of a huge amount of data which can be used for different purposes. To collect this data, we need to know how to scrape it from websites.

Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

In this section, we will use the BeautifulSoup and requests packages to scrape data. The version we are using is BeautifulSoup 4.

To start scraping websites, you need requests, BeautifulSoup4, and a website.

You can install the required packages by running:
pip install requests
pip install beautifulsoup4

To scrape data from websites, a basic understanding of HTML tags and CSS selectors is needed. We target content from a website using HTML tags, classes, or/and IDs. Let us import the requests and BeautifulSoup modules.
'''

import requests
from bs4 import BeautifulSoup

# Let's declare the URL variable for the website which we are going to scrape.
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Use the requests get method to fetch the data from the URL.
response = requests.get(url)

# Check the status of the response.
status = response.status_code
print(status)  # 200 means the fetching was successful

# Using BeautifulSoup to parse content from the page.
content = response.content  # We get all the content from the website.
soup = BeautifulSoup(content, 'html.parser')  # BeautifulSoup allows us to parse the content.

# Printing some parts of the parsed content.
print(soup.title)  # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text())  # UCI Machine Learning Repository: Data Sets
print(soup.body)  # Prints the whole page body.
print(response.status_code)  # Verify the status code again.

# Targeting a specific table on the page.
tables = soup.find_all('table', {'cellpadding': '3'})
# We are targeting the table with the cellpadding attribute set to 3.
table = tables[0]  # The result is a list, we are taking the first table from it.

# Extracting data from the table.
for td in table.find('tr').find_all('td'):
    print(td.text)  # Printing the text inside each cell.

# Exercise 1: Scrape the following website and store the data as a JSON file.
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Create a dictionary to hold the scraped data.
stats = {}

# Find the relevant sections containing facts and stats.
sections = soup.find_all('div', class_='facts-stat-box')

# Loop through each section and extract the title and value.
for section in sections:
    title = section.find('h3').get_text(strip=True)
    value = section.find('p').get_text(strip=True)
    stats[title] = value

# Write the data to a JSON file.
with open('bu_facts.json', 'w') as json_file:
    json.dump(stats, json_file, indent=4)

print("Data scraped and saved as bu_facts.json")

# Exercise 2: Extract the table from this URL and save it as a JSON file.
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the tables on the page.
tables = soup.find_all('table', {'cellpadding': '3'})
data = []

# Assuming the first table is the one we need.
table = tables[0]
for row in table.find_all('tr')[1:]:  # Skip the header row.
    columns = row.find_all('td')
    entry = {
        'name': columns[0].get_text(strip=True),
        'type': columns[1].get_text(strip=True),
        'tasks': columns[2].get_text(strip=True),
        'attribute_types': columns[3].get_text(strip=True),
        'instances': columns[4].get_text(strip=True),
        'attributes': columns[5].get_text(strip=True),
        'year': columns[6].get_text(strip=True)
    }
    data.append(entry)

# Save the data as a JSON file.
with open('uci_datasets.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Table data scraped and saved as uci_datasets.json")

# Exercise 3: Scrape the presidents table from Wikipedia and save it as a JSON file.
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the presidents table.
presidents_table = soup.find('table', {'class': 'wikitable'})

data = []

# Loop through each row of the table (skipping the header row).
for row in presidents_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) >= 5:  # Ensure there are enough columns to extract data.
        entry = {
            'number': columns[0].get_text(strip=True),
            'name': columns[1].get_text(strip=True),
            'birthplace': columns[2].get_text(strip=True),
            'birth_date': columns[3].get_text(strip=True),
            'death_date': columns[4].get_text(strip=True),
        }
        data.append(entry)

# Save the data as a JSON file.
with open('us_presidents.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Presidents data scraped and saved as us_presidents.json")

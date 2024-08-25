# Accessing the html content from webpage

import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []

table = soup.find('div', attrs={'id': 'all_quotes'})
# print(table)

for row in table.findAll('div', attrs = {"class": "col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top"}):
    quote = {'theme': row.h5.text, 'url': row.a['href'], 'img': row.img['src'], 'lines': row.img['alt'].split("#")[0],
             'author': row.img['alt'].split("#")[1]}
    quotes.append(quote)


for quote in quotes:
    print(quotes)

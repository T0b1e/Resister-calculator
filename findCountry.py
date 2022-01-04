import requests
from bs4 import BeautifulSoup
from requests.api import patch


r = requests.get('https://www.worldstandards.eu/electricity/plug-voltage-by-country/')
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.findAll('tbody', {'class':'row-hover'})

list = []
for x in s:
    for y in x:

        list.append(y)

print(list[1])
  
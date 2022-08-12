import requests
from bs4 import BeautifulSoup as BS
import time

url = 'https://www.currency.me.uk/convert/usd/rub'
r = requests.get(url)
soup = BS(r.text, 'lxml')
result = soup.find("span", { "class" : "mini ccyrate" }).text
print (result)
import requests
from bs4 import BeautifulSoup
page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')

soup = BeautifulSoup(page.content, 'html.parser')

print('Page Code: ', page.status_code)
print('Page Content:\n', soup.prettify()) #cantikkan output of web code


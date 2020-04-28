import requests
from bs4 import BeautifulSoup
page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
page2 = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')

# scrapping one by one
# children returns a property of list generator, need to call list function
html = list(soup.children)[2] # takes the 3rd data in the array of objects
body = list(html.children)[3]
tag = list(body.children)[1]
p_tag = tag.get_text() # finally get the wanted text data

# scrapping by get all the wanted instances
# find_all() always return in a list generator, we need to specify the array
all_p = soup.find_all('p')[0].get_text()

# looping thru instances of p tag
all_p2 = soup2.find_all('p')

for tagged in all_p2:
    #print(tagged.get_text())
    pass

# single find of instances
single_p = soup.find('p').get_text()

# scrapping from classes and ids
cl = soup2.find_all(class_='outer-text')[1].get_text()
idd = soup2.find(id='first').get_text()

print(idd)
print(cl)
print('Page Code: ', page2.status_code)
#print('Page Content:\n', soup.prettify()) # Make the output readable


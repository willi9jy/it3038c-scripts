from bs4 import BeautifulSoup4
import requests, re

r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup4(r, "lxml")
print(type(soup))
print(soup.prettify()[:100])
for link in soup.find_all('a'): print(link.get('href'))
type(soup)
<class 'bs4.BeautifulSoup')
for link in soup.find_all('a'):  
    print(link.get('href')) 
for link in soup.find_all('a', attrs={'href':re.compile("^https://github.com")}):  
    print(link)

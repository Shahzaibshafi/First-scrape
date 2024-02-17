import requests
from bs4 import BeautifulSoup

url = "https://ganjoor.net/ferdousi/shahname/aghaz/sh1"
htmlrespone = requests.get(url)

soup = BeautifulSoup(htmlrespone.content,"html.parser")
result = soup.find_all(class_="b")
poem = []
for results in result:
    poem = results.get_text()

# for x in poem:
    print(poem)
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com")

soupresponse = BeautifulSoup(response.text,"html.parser")
print(soupresponse.div)
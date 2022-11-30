

#Here i am going to show you the basics of how to scrape a website using BeautifulSoup

#  Requirments: first open your terminal on pycharm and install bs4 using: -pip install bs4
from bs4 import BeautifulSoup
# secondly install requests using the same terminal:  -pip install requests
import requests


#The website below is the website we are going to scrape
url = "https://www.wizardingworld.com/news/fantastic-beasts-secrets-of-dumbledore-to-be-released-globally-april-2022"

page = requests.get(url)
page.content

#we create the soup
soup = BeautifulSoup(page.content, "html.parser")
#Pring the soup
print(soup.text)

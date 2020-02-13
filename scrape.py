# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
#
# ^^^Above link is where I got the 'template' (what libraries to use and lines 13 &15) for my code. ^^^

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

champ = input("Champion name, spelling mistakes will screw this up >")
champ.lower()
url = 'https://www.op.gg/champion/'+ champ +'/statistics'
response = requests.get(url)
print(response) # Testing purposes, should return <Response [200]> to acknowledge a successful request
soup = BeautifulSoup(response.text, 'html.parser')


yeet = soup.findAll('td')[0:16:3] # gets first 'tbody' tag on page as it contains the data I require.
print(yeet) # Testing purpose to show that tbody does indeed contain the data.



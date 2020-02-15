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
#print(response) #Testing purposes, should return <Response [200]> to acknowledge a successful request
champPage = BeautifulSoup(response.text, 'html.parser')


counterData = champPage.findAll('td')[0:16:3] # ets first 'tbody' tag on page as it contains the data I require.
#print(yeet) #Testing purposes, to show that tbody does indeed contain the data.

for elem in counterData:
    otherChamp = elem.select('img') #Following lines turns tag elements from yeet into String elements
    if elem == counterData[0]:
        print()
        print('Countered by:')
    elif elem == counterData[3]:
        print()
        print('Counters:')
    otherChampString = str(otherChamp)
    champNameStart = otherChampString.find('champion/') + 9
    champNameEnd = otherChampString.find('.p')
    print(otherChampString[champNameStart:champNameEnd]) 


"""
yaw = yeet[0].select('img') #Following lines turns tag elements from yeet into String elements
yawString = str(yaw)

# print(type(yawString)) #Confirmation that element is indeed a string.

#Following lines finds the index positions for the start and end of a champions name
champNameStart = yawString.find('champion/') + 9
champNameEnd = yawString.find('.p')
print(yawString[champNameStart:champNameEnd])
"""


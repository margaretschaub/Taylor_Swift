from bs4 import BeautifulSoup as bs, element
import requests
import pandas as pd

# Create a list of all the pages I need to scrape

# def innerHTML(element):
#     """Returns the inner HTML of an element as a UTF-8 encoded bytestring"""
#     return element.encode_contents()

links = []
dm = []

for i in range(1):
    url = "https://www.setlist.fm/setlists/taylor-swift-3bd6bc5c.html?page=" + str(i + 1)
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    for link in soup.find_all('a', class_='summary url'):
        setlist = (link.get('href'))
        completeurl = 'http://www.setlists.fm' + setlist[2:]
        links.append(completeurl)

# Scrape every url in that list
for item in links:

    # r = requests.get(item)
    # soup = bs(r.content, "lxml")
    # tag = soup.find('li', class_='setlistParts song')
    # print(innerHTML(tag)

    extra = []

    r = requests.get(item)
    soup = bs(r.content, "lxml")
    for each in soup.find_all('li', class_='setlistParts song'):
        for each in soup.find('small'):
            extra.append(str(each.string))

    print(extra[1])

   # ['\n\n\n\n(', '<span id="id7">live debut / shortened</span>', ')\n\n']

    #Put everything in an array
    # for song in songs:
    #     dm.append([date,location,tour,song])
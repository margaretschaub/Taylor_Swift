from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Create a list of all the pages I need to scrape

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

    # 1. Scrape the date
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    for almostdate in soup.find('em', class_='link', text=True):
        date = almostdate.text[:-7]

    # 2. Scrape the location
    locationlist = []
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    div = soup.find('div', class_='setlistHeadline')
    for h1 in div.findAll("h1"):
        for span in h1.findAll("span"):
          locationlist.append(span.text.encode('utf-8'))
    location = locationlist[4]

    # 3. Scrape the tour
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    try:
        tour = soup.p.a.text
    except AttributeError:
        tour = ''

    # 4. Scrape the setlist
    songs = []
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    for songsone in soup.find_all('div', class_='songPart'):
        songstwo = songsone.text
        songs.append(songstwo.encode('utf-8').rstrip().strip())

    extra = []
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    for each in soup.find_all('li', class_='setlistParts song'):
        for each in soup.find('small'):
            extra.append(str(each.string))

    #Put everything in an array
    for song in songs:
        dm.append([date,location,tour,song])
        try:
            special = extra[1]
            dm.append(special)
        except IndexError:
            special = ''
            dm.append(special)


#Move it into a dataframe and print to a csv
df = pd.DataFrame(dm, columns=['Date', 'Location', 'Tour', 'Track','Special'])
df.to_csv(r'/Users/margaretschaub/Desktop/taylow_swift_setlist.csv')
gs
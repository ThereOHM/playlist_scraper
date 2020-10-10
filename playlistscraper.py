import requests  #Lib to make web requests
from bs4 import BeautifulSoup
from datetime import datetime


#Read in url-list
with open('url_list.txt') as url_file:
  url_data = []
  url_data = [line.rstrip() for line in url_file]

#Loop through url-list
for i in url_data:
  print(i)
  url = i

  #extract the palylist title (pos in url after 'de.'')
  station = url.split('de.')[1]
  print(station)

  #create empty data list
  data = []

  try:
    #Read in current playlist if existing
    with open('playlists/' + station + '.txt') as playlist_file:
      data = [line.rstrip() for line in playlist_file]
  except IOError:
      print('error: File does not exist')

  #print(data)
  print(len(data)) #print number of Songs in playlist

  #download content from the web url
  html = requests.get(url).text
  soup = BeautifulSoup(html, "html.parser")

  #scrape the online playlist
  table = soup.find("table", attrs={"class": "tablelist-schedule"})
  table_data = table.find_all("a")
  for link in table_data:
      #print(link.get("href"))
      #print(format(link.text))
      data.append(format(link.text)) #append online playlist to existing data

  #remove duplicate values (convert to dictionary, because dict cannot have duplicate values and convert back to list)
  data = list(dict.fromkeys(data))
  data = sorted(data) #sort alphabetically

  #print(data)
  print(len(data)) #print number of Songs in playlist

  #Save Data to playlist.txt
  playlist_file = open('playlists/' + station + '.txt','w')
  s1='\n'.join(data) #join the list to one string and wirte this string. Saves writing the list line per line
  playlist_file.write(s1)
  playlist_file.close()

  #Save statistic Data to stat.txt
  now = datetime.now() # current date and time
  date_time = now.strftime("%m/%d/%Y")

  playlist_file = open('stat.txt','a')
  s1 = date_time + '\t' + station + '\t' + str(len(data)) + '\n'
  playlist_file.write(s1)
  playlist_file.close()


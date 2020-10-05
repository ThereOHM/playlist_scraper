import requests  #Lib to make web requests
from bs4 import BeautifulSoup

url = "https://onlineradiobox.com/de/starfmhell/playlist/1?cs=de.starfmhell"


html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

#Read in current playlist
with open('starfmhell.txt') as playlist_file:
  data = []
  data = [line.rstrip() for line in playlist_file]

#print(data)
print(len(data)) #print number of Songs in playlist

# Get the online playlist
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

#Save Data to .txt
playlist_file = open('starfmhell.txt','w')
s1='\n'.join(data) #join the list to one string and wirte this string. Saves writing the list line per line
playlist_file.write(s1)
playlist_file.close()

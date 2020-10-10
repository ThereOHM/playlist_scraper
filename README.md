# Playlist Scraper

**Small Python Tool, to webscrape webradio playlists.**

:bulb: Idea:

There are plenty of good webradio stations. But I want their songs in a spotify, deezer, etc. playlist. 
But unfortunately the playlist of the most stations is resettet every couple of hours.
The Python tool scrapes the songs, makes a proper data formatting, removes double values and saves an unique playlist per station.

## How To Use:
- add the URLs of your favourite webradio stations to `url_list.txt`
- I recommend using [Onlineradiobox.com](https://onlineradiobox.com) to get the playlists, because they have the total list of each day. Example: 
`https://onlineradiobox.com/de/starfmhell/playlist/1?cs=de.starfmhell
`
- run the main.py
- the program will
	- scrape the playlist data of all stations
	- adds all the new songs to a playlist file, named by the station
	- remove duplicates and sort the songs alphabetical
	- save the playlist files
	- write some statistics to the `stat.txt` (for instance, how many new songs were added each day)

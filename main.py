# Use urllib and Beautifulsoup for webscraping
import urllib.request
from bs4 import BeautifulSoup

# Use dictionary for list of players and coordinate power levels
playerlist = {}
# Bungie site (needed when scraping profiles)
first = 'https://www.bungie.net'
# Subdirectory would be changed by clan
clan_sub_dir = '/en/ClanV2/Index?groupId=2756658'
# Open the clan page
clan_page = urllib.request.urlopen(first + clan_sub_dir)
# Beautiful soup it
soup = BeautifulSoup(clan_page, 'html.parser')
# For each div if it has a data-href (which means if person has site
for link in soup.find_all('div'):
    if link.has_attr('data-href'):
        # Open site of the member soup that, get their name, and power level
        member_site = urllib.request.urlopen(first + link.attrs['data-href'])
        second_soup = BeautifulSoup(member_site, 'html.parser')
        namey = second_soup.find('a', attrs={'href': link.attrs['data-href']})
        name = namey.text
        light_box = second_soup.find('div', attrs={'class': 'light'})
        light = light_box.text
        playerlist[name] = light
# Sort list by power levels and print it
sortedlist = sorted(playerlist.values())
sortedlist.reverse()
print(sortedlist)
for x in sortedlist:
    for y in playerlist:
        if playerlist[y] == x:
            print(y + x)
print(playerlist)

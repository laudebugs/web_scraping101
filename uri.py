import requests 
from bs4 import BeautifulSoup
import json
import csv
url = 'https://studentorg.apps.uri.edu/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

clubs = soup.find_all('div', class_="AccordionPanel")
_clubs = []
for club in clubs:
    club_info = club.find('table', id="Atable").find_all('tr')
    club_name = club_info[0].find_all('td')[1].text
    club_president = club_info[1].find_all('td')[1].text
    if club_info[3].find('a') is None:
        club_email = club_info[3].find_all('td')[1].text
    else:
        club_email = club_info[3].find('a').text
    
    _club = {}
    _club['name'] = club_name
    _club['president'] = club_president
    _club['email'] = club_email
    _clubs.append(_club)

uri_clubs_file = open('uri_clubs.csv', 'w')
writer = csv.writer(uri_clubs_file)
writer.writerow(['name', 'president', 'email'])

for club in _clubs:
    writer.writerow([club['name'], club['president'], club['email']])
uri_clubs_file.close()
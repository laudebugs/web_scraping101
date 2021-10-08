# Import the packages to use
import requests 
from bs4 import BeautifulSoup
import csv

# The URL to scrape
url = 'https://studentorg.apps.uri.edu/'

# Grab the web page
page = requests.get(url)

# Converts the web page into some soup lol - but anyway - it's an object that can be easily parsed
soup = BeautifulSoup(page.content, 'html.parser')

'''
The idea is to find the elements that you want to grab - 
typically, the clubs are in a html element with a specific class or id, 
so, here, we grab all the elements where the clubs are
'''
raw_clubs_data = soup.find_all('div', class_="AccordionPanel")
clubs = []
for a_club in raw_clubs_data:
    # For each html element containing the club information, we grab the html elements containing the info we need
    # In this case, the club information is contained in the tr elements
    club_info = a_club.find('table', id="Atable").find_all('tr')

    # We then grab all the text info we need to build a club object
    club_name = club_info[0].find_all('td')[1].text
    club_president = club_info[1].find_all('td')[1].text

    if club_info[3].find('a') is None:
        club_email = club_info[3].find_all('td')[1].text
    else:
        club_email = club_info[3].find('a').text
    
    # We create a club object to store the data
    club = {}
    club['name'] = club_name
    club['president'] = club_president
    club['email'] = club_email

    # We add the club object to the list of clubs
    clubs.append(club)

# We create a csv file to store the data
uri_clubs_file = open('uri_clubs.csv', 'w')
writer = csv.writer(uri_clubs_file)
# We write the headers
writer.writerow(['name', 'president', 'email'])

# Write each club to each row in the file
for club in clubs:
    writer.writerow([club['name'], club['president'], club['email']])
uri_clubs_file.close()

# done 💩


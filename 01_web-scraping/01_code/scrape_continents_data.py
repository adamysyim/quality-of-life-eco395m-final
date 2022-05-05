### Importing the required libraries
import requests
from bs4 import BeautifulSoup
import csv

def generate_continent_tuple(continents):
    return [(continent['City'],
             continent['Country'],
             continent['Continent']
             ) for continent in continents]


def continent_to_csv(continents, path):
    with open(path, 'w+', encoding='utf-8') as out_file:
        csv_writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)

        csv_writer.writerow(['City', 'Country', 'Continent'])
        continent_tuple_list = generate_continent_tuple(continents)
        csv_writer.writerows(continent_tuple_list)


### Scraping Cities-Continent Match Table ###
def scrape_continent(soup, path):
    ## Scraping data for each continent

    # Getting URLs for individual continent
    for row in soup.find('div', class_='select_region_links').find_all('a'):
        continent_url = row.get('href')

        data_continent = requests.get(continent_url).text
        soup = BeautifulSoup(data_continent, 'html.parser')

        continents = []
        # Looking for the table
        table = soup.find('table', id='t2')

        # Collecting data

        for row in table.tbody.find_all('tr'):
            # Find all data for each column
            columns = row.find_all('td')

            if (columns != []):
                city = columns[1].text.split(',')[0]
                country = columns[1].text.split(',')[-1].lstrip()
                continent = soup.find('h1').text.split(" ")[1][0:-1]

                continents.append({'City': city, 'Country': country, 'Continent': continent})

    # creating csv files of cities-continent match for individual continent

        continent_to_csv(continents, path.format(continent))


### Importing the required libraries
import requests
from bs4 import BeautifulSoup

### Scraping Quality of Life Index and others ###
def generate_quality_of_life_tuple(quality_of_lives):
    return [(quality_of_life['City'],
             quality_of_life['Country'],
             quality_of_life['Quality of Life Index'],
             quality_of_life['Purchasing Power Index'],
             quality_of_life['Safety Index'],
             quality_of_life['Healthcare Index'],
             quality_of_life['Cost of Living Index'],
             quality_of_life['Property Price to Income Ratio'],
             quality_of_life['Traffic Commute Time Index'],
             quality_of_life['Pollution Index'],
             quality_of_life['Climate Index'],
             ) for quality_of_life in quality_of_lives]

def quality_of_life_index_to_csv(quality_of_lives, path):
    with open(path, "w+", encoding="utf-8") as out_file:
        csv_writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)

        csv_writer.writerow(['City', 'Country', 'Quality of Life Index', 'Purchasing Power Index',
                                   'Safety Index', 'Healthcare Index', 'Cost of Living Index',
                                   'Property Price to Income Ratio', 'Traffic Commute Time Index',
                                   'Pollution Index', 'Climate Index'])
        quality_of_life_tuple_list = generate_quality_of_life_tuple(quality_of_lives)
        csv_writer.writerows(quality_of_life_tuple_list)


## Scraping yearly data for 5 years
def scrape_quality_of_life_index(url, year_latest, path):
    quality_of_lives = []
    year = int(year_latest) + 1

    for i in range(5):
        year = year - 1
        # creating url for each year
        url_yearly = url + "?title=" + str(year)
        data = requests.get(url_yearly).text

        # Creating BeautifulSoup object for each yearly data
        soup = BeautifulSoup(data, 'html.parser')

        #  Looking for the table
        table = soup.find('table', id='t2')

        # Collecting data
        for row in table.tbody.find_all('tr'):

            # Find all data for each column
            columns = row.find_all('td')

            if (columns != []):
                city = columns[1].text.split(',')[0]
                country = columns[1].text.split(',')[-1].lstrip()
                qol = columns[2].text.strip()
                pur_power = columns[3].text.strip()
                safe = columns[4].text.strip()
                health = columns[5].text.strip()
                col = columns[6].text.strip()
                property_income = columns[7].text.strip()
                traffic = columns[8].text.strip()
                pollution = columns[9].text.strip()
                climate = columns[10].text.strip()

                quality_of_lives.append({'City': city, 'Country': country, 'Quality of Life Index': qol,
                                'Purchasing Power Index': pur_power, 'Safety Index': safe,
                                'Healthcare Index': health, 'Cost of Living Index': col,
                                'Property Price to Income Ratio': property_income, 'Traffic Commute Time Index': traffic,
                                'Pollution Index': pollution, 'Climate Index': climate})
    path = path.format(year)
    quality_of_life_index_to_csv(quality_of_lives, path)


### Importing the required libraries
import requests
from bs4 import BeautifulSoup
from .scrape_quality_of_life_data import scrape_quality_of_life_index
from .scrape_continents_data import scrape_continent

BASE_DIR = "csv_data"
quality_of_life_index_csv_path = os.path.join(BASE_DIR, "quality_of_life_index_{}.csv")
continent_csv_path = os.path.join(BASE_DIR, "continent_{}.csv")
os.makedirs(BASE_DIR, exist_ok=True)

url = "https://www.numbeo.com/quality-of-life/rankings.jsp"

## Scraping data from multiple pages of the URL

# The Year of the most recent data
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
year_latest = soup.find("form", class_="changePageForm").find("option").text
scrape_quality_of_life_index(url, year_latest, quality_of_life_index_csv_path)
scrape_continent(soup, continent_csv_path )
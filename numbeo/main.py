### Importing the required libraries
import requests
from bs4 import BeautifulSoup

url = "https://www.numbeo.com/quality-of-life/rankings.jsp"

# The Year of the most recent data
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
year_latest = soup.find("form", class_="changePageForm").find("option").text

# quality-of-life-eco395m-final

## The goal of the Project
- Today, more than 50% of the world's population lives in cities. It is highly likely that your quality of life depends on what city you live. We want to find out what are the best cities to live, what are the factors that affect the quality of life in that cities, how the ranking of some of those cities change over the last 5 years. 
- Given that everyone has different preferences and needs, we focus mainly on providing individual-friendly interactive graphs and tables with search options.
- As for data analysis, we wouuld like to show the various aspects of the indexes that comprise "Quality of Life Index" described below.  

## Source of the Dataset
- Quality of Life Index (higher is better) is an estimation of overall quality of life by using an empirical formula which takes into account purchasing power index (higher is better), pollution index (lower is better), house price to income ratio (lower is better), cost of living index (lower is better), safety index (higher is better), health care index (higher is better), traffic commute time index (lower is better) and climate index (higher is better).
- These are provided by Numbeo which is the world’s largest cost of living database in the web. Numbeo is also a crowd-sourced global database of quality of life informations.

  Link: https://www.numbeo.com/quality-of-life/rankings.jsp

- Quality of life index formula:  100 + (purchasing Power Index / 2.5) - (House Price To IncomeRatio * 1.0) - (Cost of Living Index / 10) + (Safety Index / 2.0) + (HealthIndex / 2.5) - (Traffic Time Index / 2.0) - (Pollution Index * 2.0 / 3.0) + (Climate Index / 3.0)

## Summary of the Documentation of the Dataset

#### Main Index 
| Index | Description                                                |
| :---          |    :----                                                 |
| **Quality of life index formula**| 100 + (Purchasing Power Index / 2.5) - (House Price To Income Ratio * 1.0) - (Cost of Living Index / 10) + (Safety Index / 2.0) + (Health Index / 2.5) - (Traffic Time Index / 2.0) - (Pollution Index * 2.0 / 3.0) + (Climate Index / 3.0) |

#### Sub-indexes that compose the Main Index
| Index | Description                                                |
| :---          |    :----                                                 |
| **Purchasing Power Index**| relative purchasing power in buying goods and services in a given city for the average net salary in that city. If domestic purchasing power is 40, this means that the inhabitants of that city with an average salary can afford to buy on an average 60% less goods and services than New York City residents with an average salary. |
| **House Price To Income Ratio**| the basic measure for apartment purchase affordability (lower is better). It is generally calculated as the ratio of median apartment prices to median familial disposable income, expressed as years of income (although variations are used also elsewhere). |
| **Cost of Living Index**| a relative indicator of consumer goods prices, including groceries, restaurants, transportation and utilities. Cost of Living Index does not include accommodation expenses such as rent or mortgage. If a city has a Cost of Living Index of 120, it means Numbeo has estimated it is 20% more expensive than New York (excluding rent).|
| **Safety Index**| based on surveys from visitors of the website. Questions for these surveys are similar to many similar scientific and government surveys. Numbeo filters surveys to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. Survey result is scaled to [0, 100].|
| **Health Index**|based on surveys from visitors of the website. Questions for these surveys are similar to many similar scientific and government surveys. Numbeo filters surveys to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. Survey result is scaled to [0, 100]. |               
| **Traffic Time Index**| a composite index of time consumed in traffic due to job commute, estimation of time consumption dissatisfaction, CO2 consumption estimation in traffic and overall inefficiencies in the traffic system.|
| **Pollution Index**| based on surveys from visitors of the website. Questions for these surveys are similar to many similar scientific and government surveys. Numbeo filters surveys to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. Survey result is scaled to [0, 100]. |
| **Climate Index**| produced by a formula which uses dew point and temperature (and estimated avg. high humidex using those two numbers) to estimate a climate index.|

## Methodology and Description of the Project 
1. Web-scrape the data using Beautiful soup
2. Load the data on GCP database and reorganize them by using SQL  
3. Further replenish the data: adding geometrical information(longitude, latitude) for geopraphic presentation, recategorize some features for more accurate depiction of the overall information, etc.
4. Analyze the data and show different aspects of the indexes 
5. Visualize the information with reader-freiendly graphs and tables
6. Build intereactive dashboard using Streamlit

##  Findings and Analysis


## Extensions of your analysis or areas for more research must be included in your report



## Limitations of the Dataset
### Some indexes are based on surveys. Therefore in general, 
- There is always a risk that people will provide dishonest answers.
- There can be differences in how people understand the survey questions.
- Some respondents will choose answers before reading the questions.
- Surveys don’t provide the same level of personalization.

## Discussion of Extensions of Dataset that Would be Required to Improve the Analysis



## Instructions to Rerun the Analysis

#### Environment and Setup
1. Open the GCP Vertex AI. Choose the Jupyter Lab.
2. Fork and Git-Clone the repository into the Jupyter Lab

URL : https://github.com/adamysyim/quality-of-life-eco395m-final

#### How to rerun

|**Action** |**Directory**|
| :---     |    :----     |
|**0. Install** all the required packages, modules, and toolkits listed in **requirements.txt** in the terminal. Use ```Python pip3 install (packageName)``` command to install.|      |
|**1. Data Acquisition : web-scraping(Beautifulsoup)** | | 
|**Run** ```main.py``` |```../01_web-scraping/01_code```| 
|Results : csv files 
_quality_of_life_index_2018.csv, quality_of_life_index_2019.csv, quality_of_life_index_2020.csv, quality_of_life_index_2021.csv, quality_of_life_index_2022.csv, list_city_country_continent_Africa.csv, list_city_country_continent_America.csv, list_city_country_continent_Asia.csv, list_city_country_continent_Europe.csv, list_city_country_continent_Oceania.csv_ |```../01_web-scraping/02_results(csv)```|
|**2. Data Wrangling : SQL and Pandas** | |
|Go to GCP—SQL and create Database **1.** Remove headers in each csv files which are produced through web-scraping, **2.** Import no-header csv files to the Database, **3.** **Run** codes in ```data-wrangling.sql``` through DBeaver step by step as instructed in the file  | ```../02_data_wrangling/01_code(sql)```|
|Results : csv files 
_city_country_list.csv, quality_of_life_index_2018.csv, quality_of_life_index_2019.csv, quality_of_life_index_2020.csv, quality_of_life_index_2021.csv, quality_of_life_index_2022.csv, quality_of_life_index_5yrs.csv_|```../02_data_wrangling/02_data```| 
|**Run** ```data-wrangling.ipynb```|```../02_data_wrangling/03_code(pandas)``` |
|Results : csv files 
_lat_long.csv, quality_of_life_index_5yrs_original_geo.csv, quality_of_life_index_5yrs_ranking_USA.csv, quality_of_life_index_5yrs_ranking_world.csv, quality_of_life_index_5yrs_scale_geo_USA.csv, quality_of_life_index_5yrs_scale_geo.csv_|```../02_data_wrangling/04_data```|
|**3. Data Analysis and Results : Pandas**||
|**Run** ```1.Basic Statistics of the data.ipynb```, **Run** ```2._World.ipynb```, **Run** ```3._USA.ipynb```, **Run** ```4._Individual city in US.ipynb``` Each cell in jupyter notebook produces analysis result or visualization |```../03_data analysis and visualization```
|** Interactive Dashboard : Steamlit**||
|**Run** ```app.py```, the relevant command is ```streamlit run```(streamlit run does not work on GCP, you have to run it local). OR you can visit [this LINK](https://share.streamlit.io/adamysyim/quality-of-life-eco395m-final/main/app.py) to interact with the **dashboard** |```main directory```|
Link URL : https://share.streamlit.io/adamysyim/quality-of-life-eco395m-final/main/app.py

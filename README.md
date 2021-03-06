## The goal of the Project
- Today, more than 50% of the world's population lives in cities. In the US, 83% of the population lives in urban areas. Your quality of life likely depends on what city you live in. 
- Given that everyone has different preferences and needs, we focus mainly on providing user-friendly interactive graphs and tables with search options.
- As for overall data analysis, we would like to show "Quality of Life Index" of each city worldwide and USA-wide.   

  #### [Research Questions]  
- What are the best cities in the world and the US to live in?  
- What are the factors that affect the quality of life in that cities?  
- How has the ranking of some of those cities changed over the last 5 years?   
    
## Source of the Dataset
- Quality of Life Index (higher is better) is an estimation of overall quality of life by using an empirical formula that takes into account purchasing power index (higher is better), pollution index (lower is better), house price to income ratio (lower is better), cost of living index (lower is better), safety index (higher is better), health care index (higher is better), traffic commute time index (lower is better) and climate index (higher is better).
- These are provided by Numbeo which is the world’s largest cost of living database on the web. Numbeo is also a crowd-sourced global database of quality of life information.

  Link: https://www.numbeo.com/quality-of-life/rankings.jsp

## Summary of the Documentation of the Dataset

#### Main Index 
| Index | Description                                                |
| :---          |    :----                                                 |
| **Quality of life index formula**| 100 + (Purchasing Power Index / 2.5) - (House Price To Income Ratio * 1.0) - (Cost of Living Index / 10) + (Safety Index / 2.0) + (Health Index / 2.5) - (Traffic Time Index / 2.0) - (Pollution Index * 2.0 / 3.0) + (Climate Index / 3.0) |

#### Sub-indexes that compose the Main Index
| Index | Description                                                |
| :---          |    :----                                                 |
| **Purchasing Power Index**| relative purchasing power in buying goods and services in a given city for the average net salary in that city. If domestic purchasing power is 40, this means that the inhabitants of that city with an average salary can afford to buy on an average 60% less goods and services than New York City residents with an average salary. |
| **Property Price To Income Ratio**| the basic measure for apartment purchase affordability (lower is better). It is calculated as the ratio of median apartment prices to median familial disposable income, expressed as years of income (although variations are used elsewhere such as Case-Shiller Index, UK Housing Price Index, etc). |
| **Cost of Living Index**| a relative indicator of consumer goods prices, including groceries, restaurants, transportation, and utilities. The cost of Living Index does not include accommodation expenses such as rent or mortgage. If a city has a Cost of Living Index of 120, it means Numbeo has estimated it is 20% more expensive than New York (excluding rent).|
| **Safety Index**| based on surveys from visitors of the website. If the city has a high safety index, it is considered very safe. Questions for these surveys are similar to many similar scientific and government surveys. Numbeo filters survey to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. The survey result is scaled to [0, 100]. |
| **Health Index**| based on surveys from visitors of the website. Questions for these surveys are similar to many similar scientific and government surveys. Health Care Index is an estimation of the overall quality of the health care system, health care professionals, equipment, staff, doctors, cost, etc. Numbeo filters survey to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. The survey result is scaled to [0, 100]. |               
| **Traffic Time Index**| a composite index of time consumed in traffic due to job commute, estimation of time consumption dissatisfaction, CO2 consumption estimation in traffic, and overall inefficiencies in the traffic system.|
| **Pollution Index**| based on surveys from visitors of the website. Pollution Index is an estimation of the overall pollution in the city. The biggest weight is given to air pollution, than to water pollution/accessibility, the two main pollution factors. Small weight is given to other pollution types. Questions for these surveys are similar to many similar scientific and government surveys. Numbeo filters survey to eliminate potential spam, like people entering a large amount of data which are differentiating from the median value. The survey result is scaled to [0, 100]. |
| **Climate Index**| produced by a formula that uses dew point and temperature (and estimated avg. high humidex using those two numbers) to estimate a climate index.|

For consistency, we used the data since 2018 because the current formula for the Quality of Life index has been applied since then.

## Methodology and Description of the Project 
1. Web-scrape the original data using Beautiful soup
  - year by year tables
  - continent by continent tables for continent specific analysis
3. Load the data on GCP database and reorganize/merge them by using SQL  
4. Further replenish the data: 
  - add geometrical information(longitude, latitude) for geopraphic presentation
  - for ease of analysis and visualization, indexes are scaled with the min-max normalization method. Also, when scaled, all the indexes are adjusted so that a higher number reflects a better condition.
  - convert indexes to ranking 
5. Analyze the data and show different aspects of the indexes in terms of:
- Overall statistics
- World
- USA
- Visualize the information with graphs and tables with options for the reader to choose the city and year of interest
6. Build a multi-page interactive dashboard using Streamlit

##  Findings and Analysis

#### [Indexes] 
Though hypothetical at this stage, we attempted to find correlation coefficients between indexes to examine any meaningful relationships. In the meantime, we need more samples with accurate data to further develop and determine the significance of the relationship. 
- Since Purchasing Power Index, Property Price to Income Ratios, and Cost of Living Index are economic indexes sharing some features like the price of goods, services, and assets which are correlated, they have correlation coefficients of more than 0.5
  - Purchasing power index and property price to income ratios: -0.6
  - Purchasing power index and cost of living index: 0.7
- Cities with higher Purchasing Power tend to have a low Pollution Index whose correlation coefficient is -0.6.  
☞ We can hypothesize that cities with more Purchasing Power Index tend to have a high population and population density, which would result in more pollution.  



#### [World]
- The data contains Quality of Life Index and its sub-indexes across 255 cities in the world in 2022. The number of cities surveyed has grown over the last 5 years (184 in 2018)
- Most of the high ranking cities are in North America and Europe
  - Top 50 :  North America(50%), Europe(34%), Oceania(14%), Asia(0.02%)
  - Top 100 : North America(50%), Europe(37%), Oceania(8%), Asia(4%), Latin America(1%) 

<img width="709" alt="Quality of Living Index Worldwide" src="https://user-images.githubusercontent.com/97976503/167204536-6376069f-0ef9-480f-b152-71c9910d2572.png">

#### [USA] If we look at data for USA cities alone,
- There are 51 cities recorded in 2022(32 in 2018)

<img width="543" alt="Quality of Living Index USA" src="https://user-images.githubusercontent.com/97976503/167204812-7733f2cc-05d2-49ae-a931-b27277d7b0e0.png">

- For the last 5 years, the average Quality of Life Index increased by 8.5%. 
  - Purchasing Power Index decreased by 11.3% reflecting that the average net salary’s buying power of necessary goods and services has declined across those cities
  - The traffic Commute Time Index rose 64.6% contributing in large portion to the increase in the overall Quality of Life Index
- Top 5 most livable cities in 2022 are Raleigh, Columbus, Madison, Austin, and Charlotte. Whereas, the bottom 5 are: Detroit, New York, Los Angeles, Philadelphia, and Miami. Most of the low-ranking cities have poor scores on Purchasing Power Index. 

#### [Individual City] By exploring our interactive dashboard, you can choose whatever city you like and see the results. Here, we provide the result for Austin, Texas as a representative.
- Austin ranks 4th highest Quality of Life in the USA(7th in the world). For the last five years, Austin has maintained its ranking within top10 
- Compared to the US average of each index, Austin has better numbers on every index. Particularly, Austin has strong point on Purchasing Power Index, 158.21, which means the inhabitants of Austin with an average salary can afford to buy on an average 58% more goods and services than New York City residents with an average salary. Also, Austin has high points on the Safety Index which is 15% higher than the national average.

<img width="468" alt="spider chart austin" src="https://user-images.githubusercontent.com/97976503/167204745-38336b86-6749-4096-a20d-5cf23ec4ebd0.png">

- However, during the last five years, the Health Care Index showed the most decline in ranking, from 5 to 24. The pollution Index ranking also showed deterioration, from 10 to 24.

To find out more on individual cities, please visit our [DASHBOARD](https://share.streamlit.io/adamysyim/quality-of-life-eco395m-final/main/app.py)



   

## Limitations of the Dataset
- Some indexes are based on surveys. Therefore, there is always a risk that people will provide dishonest answers and there can be differences in how people understand the survey questions. Surveys don’t provide the same level of personalization.
- Some of the indexes are based on surveys that are written in English. This bias caused by largely English-speaking respondents can be corrected by having multi-language surveys.
- The distribution of ‘Property Price to Income Ratio’ has a skewness of 2.2 (Fisher's moment coefficient of skewness) which is too large. Considering the fact that relative ranking is the main purpose of this analysis, the skewness might distort the result of the analysis. We have to first see if those extreme numbers are consistent with the actual situations in those cities. If not, we have to drop those numbers for a more accurate analysis. 

## Extensions of Dataset that Would be Required to Improve the Analysis
#### [USA]
- To improve the accuracy of the indexes, particularly those data-based surveys, we can look into ‘National Health Interview Survey and match similar questions in Numbeo survey to see if they are consistent. As for ‘Pollution Index’ we can compare it with outside sources such as ‘Pollution Rankings’ researched by U.S. News.

#### [World]  
- The survey procedures should be worked on with international researchers to minimize the language bias as much as possible.  


## Areas for more research
- Data such as ‘change in population’ and ‘rate of population influx/outflux’ can be obtained from Census data to be matched with the ‘change in the ranking on Quality of Life’ of each city to see the correlation. This could be developed further into modeling.
- We can further investigate correlations between indexes. As mentioned before, cities with higher Purchasing Power tend to have a low Pollution Index. This tendency may be closely associated with city population size and population density.  
- We can add interesting the case of Bhutan. Bhutan has known as the happiest country in the world but ranks 95th out of 156 countries in the 2019 World Happiness Report. This happiness case can be worth connecting this Quality of life research.  
Source: https://www.cnn.com/2019/09/13/health/bhutan-gross-national-happiness-wellness/index.html  

# Instructions to Rerun the Analysis

#### Environment and Setup
1. Open the GCP Vertex AI. Choose the Jupyter Lab.
2. Fork and Git-Clone the repository into the Jupyter Lab

URL: https://github.com/adamysyim/eco395m-final-project--quality-of-life

## How to rerun

### 0. Installing packages
- all the required packages, modules, and toolkits are listed in **requirements.txt** in the terminal. Use ```Python pip3 install (packageName)``` command to install.

### 1. Data Acquisition : web-scraping
- **Run** ```main.py``` in ```../01_web-scraping/01_code``` 
- Resulting csv files are automatically stored in ```../01_web-scraping/02_results(csv)```

### 2. Data Wrangling: SQL and Pandas

#### [SQL]
This process is very tedious and takes some time. Please bear with us and follow the steps carefully. Or if you are short of time, you can skip this process and move directly to “02_data-wrangling/03_code(pandas)”

**A. Setting up database instance in GCP and DBeaver**

a) Create a database instance in Google Cloud Platform (GCP). If you have already done this, you can use the one you already have. Go to GCP SQL and create a PostgreSQL 13 database instance. Make sure that you whitelist the IPs in block 0.0.0.0/0. Picking the lowest spec for this instance will be sufficient for this problem. Save your password.

b) Use GCP SQL to create a database called “final”. You can do this in the "Databases" tab.

c) Connect to your database with DBeaver. Your host can be found in GCP SQL on the "Overview" tab. The port will be the default Postgres port: 5432. You can use the default Postgres username, Postgres, and the password you set in the last step. Connect with a database as ‘final’.

d) In DBeaver, Navigate to “final” > "Databases" > “final”. Right-click the database “final” -- it is the one that looks like a silo. Then select "SQL Editor" > "New SQL Script".

f) Copy the code in "02_data-wrangling/01_code/data-wrangling.sql into your SQL editor 

g) Don’t execute them all at once. You have to execute each block of code by following instructions in the SQL file

**B. Uploading no header files to database**

a)  Remove the headers from each of CSVs in ```01_web-scraping/02_results(csv)```

b) Create a bucket in GCP Cloud Storage (you can use an existing one if you like)

c) Upload your headerless CSVs to the bucket.

**C. Running SQL**

a) please execute each block of code according to instructions(commented) in the SQL file

b) export below tables and store them in ```02_data-wrangling/02_data``` as csv format
  - city_country_continent_list.csv
  - quality_of_life_index_2018.csv
  - quality_of_life_index_2019.csv
  - quality_of_life_index_2020.csv
  - quality_of_life_index_2021.csv
  - quality_of_life_index_2022.csv
  - quality_of_life_index_5yrs.csv

#### [Pandas]
- **Run** ```../02_data_wrangling/03_code(pandas)/data-wrangling.py```
  - (Reminder on the part using Geopandas to obtain the latitude and longitude of each city: due to its inherent characteristics, the process takes 2~3 minutes to complete)
- Resulting CSV files are automatically stored in ```../02_data_wrangling/04_data```

### 3. Data Analysis and Results: Pandas
(Each cell in Jupiter notebooks produces unique analysis and visualizations of the data)
- **Run** ```../03_data analysis and visualization/1.Basic Statistics of the data.ipynb```
- **Run** ```../03_data analysis and visualization/2._World.ipynb```
- **Run** ```../03_data analysis and visualization/3._USA.ipynb```
- **Run** ```../03_data analysis and visualization/4._Individual city in US.ipynb``` 

### 4. Interactive Dashboard: Steamlit**
- Visit the following [URL](https://share.streamlit.io/adamysyim/quality-of-life-eco395m-final/main/app.py)(```https://share.streamlit.io/adamysyim/quality-of-life-eco395m-final/main/app.py```) to interact with the **dashboard**
- You can **Run** ```../app.py```, the relevant command is ```streamlit run```. ```pip install streamlit``` before you run the code. Please be reminded that ```streamlit run``` doesn't work in GCP environment. You have to clone the entire repo to your local storage and run ```streamlit run app.py``` locally. 


#### Code writers 

**This is provided to help graders when assessing individual contributions to coding**

| **Directory** | **Code File** | **Writer Name** | **GitHub Account Name** |
| :---     |    :----     | :---     |    :----     |
| ```../01_web-scraping/01_code``` | ```main.py```, ```scrape_continents_data.py```, ```scrape_quality_of_life_data.py``` | Ashesh Shrestha | AsheshShrestha7 |
| ```../02_data-wrangling/01_code``` | ```data-wrangling.sql``` | Seungwoon Shin | skmanzg |
| ```../02_data-wrangling/03_code``` | ```data-wrangling.py``` | Jiyou Chen | jaredchen1124 |
| ```../03_data analysis and visualization/``` | ```01_Basic Statistics of the data.ipynb``` | Xuezhou Chong | ChloeChong01 |
| ```../03_data analysis and visualization/``` | ```02_World.ipynb```, ```03_USA.ipynb```, ```04_Individual city in US.ipynb``` | Youngseok Yim | adamysyim |
| ```../04_data analysis and visualization/``` | ```app.py```, ```multiapp.py```, ```compare.py```, ```individual.py```, ```overview.py``` | Youngseok Yim | adamysyim |

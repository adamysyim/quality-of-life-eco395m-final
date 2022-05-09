"""
<Table of Contents>

Creating longitude-latitude table for later reference
Scaling values for analysis and visualization
Creating world ranking data
Creating USA-specific data - scaled version
Creating USA-specific data - ranking version


Result data:

quality_of_life_index_5yrs_original_geo.csv
quality_of_life_index_5yrs_scale_geo.csv
quality_of_life_index_5yrs_ranking_world.csv
quality_of_life_index_5yrs_scale_geo_USA.csv
quality_of_life_index_5yrs_ranking_USA.csv
"""

import pandas as pd
import os


# create output directory

outdir = '../04_data'
if not os.path.exists(outdir):
    os.mkdir(outdir)


#### 1. Creating longitude-latitude table for later reference ####


## Importing country_city_list.csv

list_city_country_continent = pd.read_csv('../02_data/city_country_continent_list.csv')



## split America into North America and Latin America ## 

# North America
list_city_country_continent.loc[(list_city_country_continent.Country == 'United States'
                                ), 'Continent'] = 'North America'
list_city_country_continent.loc[(list_city_country_continent.Country == 'Canada'
                                ), 'Continent'] = 'North America'
# Latin America
list_city_country_continent.loc[(list_city_country_continent.Continent == 'America'
                                ), 'Continent'] = 'Latin America'



## importing the package used to obtain the latitude and longitude of each city ## 

import geopandas as gpd
from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=10, user_agent = "myGeolocator")

# Initializing the lists used to store the latitudes and longitudes

city = []
country = []
latitudes = []
longitudes = []
continent = []

# Obtaining and store the latitude and longitude of each city

for row in range(len(list_city_country_continent.index)):
    location = geolocator.geocode(
        list_city_country_continent['City'][row] + ', ' + list_city_country_continent['Country'][row]
    )
    latitudes.append(location.latitude)
    longitudes.append(location.longitude)
    city.append(list_city_country_continent['City'][row])
    country.append(list_city_country_continent['Country'][row])
    continent.append(list_city_country_continent['Continent'][row])

lat_long = pd.DataFrame({'City': city, 'Country': country, 'Continent' : continent, 
                         'Latitude': latitudes, 'Longitude': longitudes})


######### Takes some time... 2~3 minutes #########  



## adding latitude and longitude values to the original data ##

# importing original data

qol_22 = pd.read_csv('../02_data/quality_of_life_index_2022.csv')
qol_21 = pd.read_csv('../02_data/quality_of_life_index_2021.csv')
qol_20 = pd.read_csv('../02_data/quality_of_life_index_2020.csv')
qol_19 = pd.read_csv('../02_data/quality_of_life_index_2019.csv')
qol_18 = pd.read_csv('../02_data/quality_of_life_index_2018.csv')

# matching city-country and add latitude/longitude and continent

qol_22_geo = qol_22.merge(lat_long, how='inner', 
                          left_on=['City', 'Country'], right_on=['City', 'Country'])
qol_21_geo = qol_21.merge(lat_long, how='inner', 
                          left_on=['City', 'Country'], right_on=['City', 'Country'])
qol_20_geo = qol_20.merge(lat_long, how='inner', 
                          left_on=['City', 'Country'], right_on=['City', 'Country'])
qol_19_geo = qol_19.merge(lat_long, how='inner', 
                          left_on=['City', 'Country'], right_on=['City', 'Country'])
qol_18_geo = qol_18.merge(lat_long, how='inner', 
                          left_on=['City', 'Country'], right_on=['City', 'Country'])

## merging yearly dataframe across 2018-2022 ##

qol_5yrs_geo = pd.concat([qol_22_geo, qol_21_geo, qol_20_geo, qol_19_geo, qol_18_geo], 
                         axis=0, join='outer', ignore_index=True)

## exporting result dataframe to csv ##

qol_5yrs_geo.to_csv('../04_data/quality_of_life_index_5yrs_original_geo.csv', 
                    encoding='utf-8',index = False)



#### 2. Scaling values for analysis and visualization ####

# importing 2018 ~ 2022 data   
qol_22 = pd.read_csv('../02_data/quality_of_life_index_2022.csv')
qol_21 = pd.read_csv('../02_data/quality_of_life_index_2021.csv')
qol_20 = pd.read_csv('../02_data/quality_of_life_index_2020.csv')
qol_19 = pd.read_csv('../02_data/quality_of_life_index_2019.csv')
qol_18 = pd.read_csv('../02_data/quality_of_life_index_2018.csv')


## defining functions for scaling indexes through min-max normalization with range [0,100] ## 

def min_max_scaling(series):
    return (series - series.min())*100/(series.max()-series.min())

def min_max_scaling_inverse(series):
    return 100-((series - series.min())*100/(series.max()-series.min()))

def scale(qol_22):
    qol_22['Quality of Life Index'] = min_max_scaling(qol_22['Quality of Life Index'])
    qol_22['Purchasing Power Index'] = min_max_scaling(qol_22['Purchasing Power Index'])
    qol_22['Safety Index'] = min_max_scaling(qol_22['Safety Index'])
    qol_22['Healthcare Index'] = min_max_scaling(qol_22['Healthcare Index'])
    qol_22['Cost of Living Index'] = min_max_scaling_inverse(qol_22['Cost of Living Index'])
    qol_22['Property Price to Income Ratio'] = min_max_scaling_inverse(qol_22['Property Price to Income Ratio'])
    qol_22['Traffic Commute Time Index'] = min_max_scaling_inverse(qol_22['Traffic Commute Time Index'])
    qol_22['Pollution Index'] = min_max_scaling_inverse(qol_22['Pollution Index'])
    qol_22['Climate Index'] = min_max_scaling(qol_22['Climate Index'])


## scale(min-max normalization) yearly data by looping ##

list_ = [qol_22, qol_21, qol_20, qol_19, qol_18]
for df in list_:
    scale(df)


## merging yearly scaled data across 2018~2022 ##

qol_5yrs_scale = pd.concat([qol_22,qol_21, qol_20, qol_19, qol_18], axis=0, 
                           join='outer', ignore_index=True,)


## add latitude/longitude and continent by matching city-country ##

qol_5yrs_scale_geo = qol_5yrs_scale.merge(lat_long, how='inner', 
                                          left_on=['City', 'Country'], right_on=['City', 'Country'])

## exporting merged dataframe to csv ##

qol_5yrs_scale_geo.to_csv('../04_data/quality_of_life_index_5yrs_scale_geo.csv', 
                          encoding='utf-8', index = False)


#### 3. Creating world ranking data ####

# importing data

qol_scale = pd.read_csv('../04_data/quality_of_life_index_5yrs_scale_geo.csv')

qol_scale_22 = qol_scale.loc[:][qol_scale['Year'] == 2022]
qol_scale_21 = qol_scale.loc[:][qol_scale['Year'] == 2021]
qol_scale_20 = qol_scale.loc[:][qol_scale['Year'] == 2020]
qol_scale_19 = qol_scale.loc[:][qol_scale['Year'] == 2019]
qol_scale_18 = qol_scale.loc[:][qol_scale['Year'] == 2018]

# listing up columns for ranking

rankcols = ['Quality of Life Index',
       'Purchasing Power Index', 'Safety Index', 'Healthcare Index',
       'Cost of Living Index', 'Property Price to Income Ratio',
       'Traffic Commute Time Index', 'Pollution Index', 'Climate Index']

# converting values to ranking values 

qol_scale_22[rankcols] = qol_scale_22[rankcols].rank('rows', ascending=False).astype(int)
qol_scale_21[rankcols] = qol_scale_21[rankcols].rank('rows', ascending=False).astype(int)
qol_scale_20[rankcols] = qol_scale_20[rankcols].rank('rows', ascending=False).astype(int)
qol_scale_19[rankcols] = qol_scale_19[rankcols].rank('rows', ascending=False).astype(int)
qol_scale_18[rankcols] = qol_scale_18[rankcols].rank('rows', ascending=False).astype(int)

# merging

qol_5yrs_world_ranking = pd.concat([qol_scale_22, qol_scale_21, qol_scale_20, 
                                    qol_scale_19, qol_scale_18], axis=0, join='outer', 
                                   ignore_index=True,)

# exporting merged data to csv

qol_5yrs_world_ranking.to_csv('../04_data/quality_of_life_index_5yrs_ranking_world.csv', 
                              encoding='utf-8',index = False)



#### 4. Creating USA-specific data - scaled version ####

## Creating scaled data for USA cities only ##

# importing original data
qol = pd.read_csv('../04_data/quality_of_life_index_5yrs_original_geo.csv')

qol_22 = qol.loc[:][qol['Year'] == 2022]
qol_21 = qol.loc[:][qol['Year'] == 2021]
qol_20 = qol.loc[:][qol['Year'] == 2020]
qol_19 = qol.loc[:][qol['Year'] == 2019]
qol_18 = qol.loc[:][qol['Year'] == 2018]

# pick USA cities 

qol_22_us = qol_22[:].loc[(qol_22['Country'] == 'United States')]
qol_21_us = qol_21[:].loc[(qol_21['Country'] == 'United States')]
qol_20_us = qol_20[:].loc[(qol_20['Country'] == 'United States')]
qol_19_us = qol_19[:].loc[(qol_19['Country'] == 'United States')]
qol_18_us = qol_18[:].loc[(qol_18['Country'] == 'United States')]

## scaling (min-max normalization with range [0,100]) ##

list_ = [qol_22_us, qol_21_us, qol_20_us, qol_19_us, qol_18_us]

for df in list_:
    scale(df)

## merge yearly data ##

qol_5yrs_scale_us = pd.concat([qol_22_us, qol_21_us, qol_20_us, qol_19_us, qol_18_us], 
                              axis=0, join='outer', ignore_index=True,)

# exporting merged dataframe to csv

qol_5yrs_scale_us.to_csv('../04_data/quality_of_life_index_5yrs_scale_geo_USA.csv', 
                         encoding='utf-8', index = False)


#### 5. Creating USA-specific data - ranking version ####


# importing scaled data

qol_5yrs_scale_geo_USA = pd.read_csv('../04_data/quality_of_life_index_5yrs_scale_geo_USA.csv')

# dividing the data according to year

qol_22_us = qol_5yrs_scale_geo_USA[:].loc[(qol_5yrs_scale_geo_USA['Year'] == 2022)]
qol_21_us = qol_5yrs_scale_geo_USA[:].loc[(qol_5yrs_scale_geo_USA['Year'] == 2021)]
qol_20_us = qol_5yrs_scale_geo_USA[:].loc[(qol_5yrs_scale_geo_USA['Year'] == 2020)]
qol_19_us = qol_5yrs_scale_geo_USA[:].loc[(qol_5yrs_scale_geo_USA['Year'] == 2019)]
qol_18_us = qol_5yrs_scale_geo_USA[:].loc[(qol_5yrs_scale_geo_USA['Year'] == 2018)]

# listing up columns for ranking

rankcols = ['Quality of Life Index',
       'Purchasing Power Index', 'Safety Index', 'Healthcare Index',
       'Cost of Living Index', 'Property Price to Income Ratio',
       'Traffic Commute Time Index', 'Pollution Index', 'Climate Index']

# converting values to ranking values 

qol_22_us[rankcols] = qol_22_us[rankcols].rank('rows', ascending=False).astype(int)
qol_21_us[rankcols] = qol_21_us[rankcols].rank('rows', ascending=False).astype(int)
qol_20_us[rankcols] = qol_20_us[rankcols].rank('rows', ascending=False).astype(int)
qol_19_us[rankcols] = qol_19_us[rankcols].rank('rows', ascending=False).astype(int)
qol_18_us[rankcols] = qol_18_us[rankcols].rank('rows', ascending=False).astype(int)

# merging

qol_5yrs_us_ranking = pd.concat([qol_22_us, qol_21_us, qol_20_us, qol_19_us, qol_18_us], 
                                axis=0, join='outer', ignore_index=True,)

# exporting merged data to csv

qol_5yrs_us_ranking.to_csv('../04_data/quality_of_life_index_5yrs_ranking_USA.csv', 
                           encoding='utf-8', index = False)
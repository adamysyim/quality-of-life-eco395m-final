-- Table of Contents

-- 1. making city-country-continent list
-- 2. making quality_of_life_index (final results(6 tables))
-- 3. city_country_list (final result(1 table))


-- -- 1. making city-country-continent list -- -- 

-- Creating tables and import no-header csv data for each continent from GCP
-- (CSV files are the result of web-scraping)

CREATE TABLE list_city_country_continent_Africa (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    );

CREATE TABLE list_city_country_continent_America (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    ); 
   
CREATE TABLE list_city_country_continent_Asia (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    );
   
CREATE TABLE list_city_country_continent_Europe (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    );
   
CREATE TABLE list_city_country_continent_Oceania (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    );
 
   
-- For each table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Create new database
-- 3. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 4. Import each no-header csv files to match each table

   
-- creating table for the final merge   
   
CREATE TABLE list_city_country_continent_full (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50)
    ); 
    
   
   
-- merging city-country-continent list tables to "list_city_country_continent_full" table

INSERT INTO list_city_country_continent_full ("City", "Country", "Continent")
SELECT "City", "Country", "Continent" FROM list_city_country_continent_Africa;

INSERT INTO list_city_country_continent_full ("City", "Country", "Continent")
SELECT "City", "Country", "Continent" FROM list_city_country_continent_America;

INSERT INTO list_city_country_continent_full ("City", "Country", "Continent")
SELECT "City", "Country", "Continent" FROM list_city_country_continent_Asia;

INSERT INTO list_city_country_continent_full ("City", "Country", "Continent")
SELECT "City", "Country", "Continent" FROM list_city_country_continent_Europe;

INSERT INTO list_city_country_continent_full ("City", "Country", "Continent")
SELECT "City", "Country", "Continent" FROM list_city_country_continent_Oceania;



-- --  2. making quality_of_life_index (final results(6 tables)) -- --


-- creating table for quality_of_life_index_5yr  --

CREATE TABLE quality_of_life_index_5yrs (
    "City" varchar(50),
    "Country" varchar(50),
    "Continent" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2),
    "Year" char(4)
    );


-- Importing yearly index no-header data from GCP and match continent -- 
-- (CSV files are the result of web-scraping)

-- for 2022 data, create columns and import no-header files from GCP --

CREATE TABLE quality_of_life_index_2022 (
    "City" varchar(50),
    "Country" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2)
    );
   
-- For table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 3. Import each no-header csv files to match each table
   
   
-- add relevant year 

alter table quality_of_life_index_2022 add "Year" char(4);

update quality_of_life_index_2022 set "Year" = '2022';


-- match continent for each country and then insert rows into 5yr table

with qol_22_continent
as (select qol_22."City", 
        qol_22."Country", 
        coun_con."Continent", 
        qol_22."Quality of Life Index", 
        qol_22."Purchasing Power Index",
        qol_22."Safety Index", 
        qol_22."Healthcare Index", 
        qol_22."Cost of Living Index", 
        qol_22."Property Price to Income Ratio",
        qol_22."Traffic Commute Time Index", 
        qol_22."Pollution Index", 
        qol_22."Climate Index",
        qol_22."Year"
        from quality_of_life_index_2022 qol_22
        inner join (select distinct("Country"), "Continent" from list_city_country_continent_full) coun_con 
        on qol_22."Country" = coun_con."Country")
INSERT INTO quality_of_life_index_5yrs
select "City", 
       "Country", 
       "Continent", 
       "Quality of Life Index", 
       "Purchasing Power Index",
       "Safety Index", 
       "Healthcare Index", 
       "Cost of Living Index", 
       "Property Price to Income Ratio",
       "Traffic Commute Time Index", 
       "Pollution Index", 
       "Climate Index",
       "Year"
FROM qol_22_continent;
        

-- for for 2021 data, create columns and import no-header files from GCP --
        
CREATE TABLE quality_of_life_index_2021 (
    "City" varchar(50),
    "Country" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2)
    );

-- For table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 3. Import each no-header csv files to match each table 
   
   
-- add relevant year 

alter table quality_of_life_index_2021 add "Year" char(4);

update quality_of_life_index_2021 set "Year" = '2021';


-- match continent for each city and then insert rows in to 5yr table
with qol_21_continent
as (select qol_21."City", 
        qol_21."Country", 
        coun_con."Continent", 
        qol_21."Quality of Life Index", 
        qol_21."Purchasing Power Index",
        qol_21."Safety Index", 
        qol_21."Healthcare Index", 
        qol_21."Cost of Living Index", 
        qol_21."Property Price to Income Ratio",
        qol_21."Traffic Commute Time Index", 
        qol_21."Pollution Index", 
        qol_21."Climate Index",
        qol_21."Year"
        from quality_of_life_index_2021 qol_21
        inner join (select distinct("Country"), "Continent" from list_city_country_continent_full) coun_con 
        on qol_21."Country" = coun_con."Country")  
INSERT INTO quality_of_life_index_5yrs
select "City", 
       "Country", 
       "Continent", 
       "Quality of Life Index", 
       "Purchasing Power Index",
       "Safety Index", 
       "Healthcare Index", 
       "Cost of Living Index", 
       "Property Price to Income Ratio",
       "Traffic Commute Time Index", 
       "Pollution Index", 
       "Climate Index",
       "Year"
FROM qol_21_continent;
 

-- for for 2020 data, create columns and import no-header files from GCP --
        
CREATE TABLE quality_of_life_index_2020 (
    "City" varchar(50),
    "Country" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2)
    );
   
-- For table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 3. Import each no-header csv files to match each table    
   
-- add relevant year 

alter table quality_of_life_index_2020 add "Year" char(4);

update quality_of_life_index_2020 set "Year" = '2020';


-- match continent for each city and then insert rows in to 5yr table

with qol_20_continent
as (select qol_20."City", 
        qol_20."Country", 
        coun_con."Continent", 
        qol_20."Quality of Life Index", 
        qol_20."Purchasing Power Index",
        qol_20."Safety Index", 
        qol_20."Healthcare Index", 
        qol_20."Cost of Living Index", 
        qol_20."Property Price to Income Ratio",
        qol_20."Traffic Commute Time Index", 
        qol_20."Pollution Index", 
        qol_20."Climate Index",
        qol_20."Year"
        from quality_of_life_index_2020 qol_20
        inner join (select distinct("Country"), "Continent" from list_city_country_continent_full) coun_con 
        on qol_20."Country" = coun_con."Country")
INSERT INTO quality_of_life_index_5yrs
select "City", 
       "Country", 
       "Continent", 
       "Quality of Life Index", 
       "Purchasing Power Index",
       "Safety Index", 
       "Healthcare Index", 
       "Cost of Living Index", 
       "Property Price to Income Ratio",
       "Traffic Commute Time Index", 
       "Pollution Index", 
       "Climate Index",
       "Year"
FROM qol_20_continent;


-- for for 2019 data, create columns and import no-header files from GCP --
        
CREATE TABLE quality_of_life_index_2019 (
    "City" varchar(50),
    "Country" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2)
    );

-- For table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 3. Import each no-header csv files to match each table     
  
   
-- add relevant year 

alter table quality_of_life_index_2019 add "Year" char(4);

update quality_of_life_index_2019 set "Year" = '2019';


-- match continent for each city and then insert rows in to 5yr table
with qol_19_continent
as (select qol_19."City", 
        qol_19."Country", 
        coun_con."Continent", 
        qol_19."Quality of Life Index", 
        qol_19."Purchasing Power Index",
        qol_19."Safety Index", 
        qol_19."Healthcare Index", 
        qol_19."Cost of Living Index", 
        qol_19."Property Price to Income Ratio",
        qol_19."Traffic Commute Time Index", 
        qol_19."Pollution Index", 
        qol_19."Climate Index",
        qol_19."Year"
        from quality_of_life_index_2019 qol_19
        inner join (select distinct("Country"), "Continent" from list_city_country_continent_full) coun_con 
        on qol_19."Country" = coun_con."Country")       
INSERT INTO quality_of_life_index_5yrs
select "City", 
       "Country", 
       "Continent", 
       "Quality of Life Index", 
       "Purchasing Power Index",
       "Safety Index", 
       "Healthcare Index", 
       "Cost of Living Index", 
       "Property Price to Income Ratio",
       "Traffic Commute Time Index", 
       "Pollution Index", 
       "Climate Index",
       "Year"
FROM qol_19_continent;     


-- for for 2018 data, create columns and import no-header files from GCP --
        
CREATE TABLE quality_of_life_index_2018 (
    "City" varchar(50),
    "Country" varchar(50),
    "Quality of Life Index" numeric(5,2),
    "Purchasing Power Index" numeric(5,2),
    "Safety Index" numeric(5,2),
    "Healthcare Index" numeric(5,2),
    "Cost of Living Index" numeric(5,2),
    "Property Price to Income Ratio" numeric(5,2),
    "Traffic Commute Time Index" numeric(5,2),
    "Pollution Index" numeric(5,2),
    "Climate Index" numeric(5,2)
    );

-- For table above, 
-- 1. PLEASE go to GCP SQL, 
-- 2. Upload no-header csv files that are made from web-scraped csv to GCP Cloud Storage
-- 3. Import each no-header csv files to match each table    
   
   
-- add relevant year 

alter table quality_of_life_index_2018 add "Year" char(4);

update quality_of_life_index_2018 set "Year" = '2018';


-- match continent for each city and then insert rows in to 5yr table

with qol_18_continent
as (select qol_18."City", 
        qol_18."Country", 
        coun_con."Continent", 
        qol_18."Quality of Life Index", 
        qol_18."Purchasing Power Index",
        qol_18."Safety Index", 
        qol_18."Healthcare Index", 
        qol_18."Cost of Living Index", 
        qol_18."Property Price to Income Ratio",
        qol_18."Traffic Commute Time Index", 
        qol_18."Pollution Index", 
        qol_18."Climate Index",
        qol_18."Year"
        from quality_of_life_index_2018 qol_18
        inner join (select distinct("Country"), "Continent" from list_city_country_continent_full) coun_con 
        on qol_18."Country" = coun_con."Country")      
INSERT INTO quality_of_life_index_5yrs
select "City", 
       "Country", 
       "Continent", 
       "Quality of Life Index", 
       "Purchasing Power Index",
       "Safety Index", 
       "Healthcare Index", 
       "Cost of Living Index", 
       "Property Price to Income Ratio",
       "Traffic Commute Time Index", 
       "Pollution Index", 
       "Climate Index",
       "Year"
FROM qol_18_continent; 
        
        
        
-- -- 3. Creating a table for distinct values of 'city', 'country' that appear in the data -- --
-- (this data is for adding geometrical information(latitudes and longitudes) by using pandas )

select * into city_country_continent_list from (select distinct "City", "Country", "Continent" from quality_of_life_index_5yrs) a;
        
        
        
        
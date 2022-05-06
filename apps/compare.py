import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from math import pi


## page setting


def app():

    ## set the width of the sidebar
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 220px;
    }
    """,
    unsafe_allow_html=True)

    ###########################################################################################
    
    ## Side bar

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    country_list = df.Country.sort_values()
    country_list_unique = country_list.unique()
    country_1 = st.sidebar.selectbox('Select a country (for choice 1) :', country_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    city_list = df.City[df['Country'] == country_1].sort_values()
    city_list_unique = city_list.unique()
    city_1 = st.sidebar.selectbox('Select a city (for choice 1) :', city_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    year_list = df.Year.unique()
    year_list = df.loc[df['City'] == city_1].Year.unique()
    year_1 = st.sidebar.selectbox('Select year (for choice 1):', year_list)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    country_list = df.Country.sort_values()
    country_list_unique = country_list.unique()
    country_2 = st.sidebar.selectbox('Select a country (for choice 2) :', country_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    city_list = df.City[df['Country'] == country_2].sort_values()
    city_list_unique = city_list.unique()
    city_2 = st.sidebar.selectbox('Select a city (for choice 2) :', city_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    year_list = df.Year.unique()
    year_list = df.loc[df['City'] == city_2].Year.unique()
    year_2 = st.sidebar.selectbox('Select year (for choice 2):', year_list)

    ###########################################################################################
    
    ## page title

    st.title('Comparison Report for chosen cities')

    st.write('** Please select Country, City, and Year for each city of your interest on the left sidebar**')

    a1, a2, a3 = st.columns((4.2,0.8,5))

    with a1:
        st.subheader('1. ' + city_1 + ', ' + country_1 + ' (' + str(year_1) + ')')
        
    with a2:
        st.subheader('vs')    

    with a3:
        st.subheader('2. ' + city_2 + ', ' + country_2 + ' (' + str(year_2) + ')')
        

    st.markdown("""---""")

    ###########################################################################################
    st.header("""Quality of Life Index Ranking""")

    ############ obtaining world ranking 
    def get_world_ranking(city, country):
        
        # importing ranking data
        df_rank_world = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_ranking_world.csv')

        # ranking change over the year

        # extract year data for the chosen 
        chosen_row = df_rank_world.loc[(df_rank_world['City'] == city) & 
                                    (df_rank_world['Country'] == country)].sort_values(by='Year', ascending=True)

        # choose columns for display
        columnsTitles = ['Year'] + chosen_row.columns[2:-4].tolist()

        # show result
        rank_change_world = chosen_row[columnsTitles].sort_values('Year', axis = 0, ascending = False).set_index('Year').T

        ranking_world = rank_change_world.iloc[0].to_frame().T
        
        return ranking_world
    ####################################
        
        
    ############ obtaining US ranking 

    def get_usa_ranking(city, country):
        # importing ranking data
        df_rank_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_ranking_USA.csv')

        # ranking change over the year

        # extract year data for the chosen city
        chosen_row = df_rank_us.loc[(df_rank_us['City'] == city) & (df_rank_us['Country'] == country)].sort_values(by='Year', ascending=True)
    
        # choose columns for display
        columnsTitles = ['Year'] + chosen_row.columns[2:-4].tolist()

        # show result
        rank_change_us = chosen_row[columnsTitles].sort_values('Year', axis = 0, ascending = False).set_index('Year').T

        ranking_us = rank_change_us.iloc[0].to_frame().T

        return ranking_us
        
    ####################################     
    
    ## sub-section setting

    if country_1 == 'United States' and country_2 == 'United States': 

        a1, a2 = st.columns((5,5))

        with a1:
            st.write(city_1 + ', ' + country_1)
            st.write(get_usa_ranking(city_1, country_1))
            

        with a2:
            st.write(city_2 + ', ' + country_2)
            st.write(get_usa_ranking(city_2, country_2))
            
    else: 
        
        a1, a2 = st.columns((5,5))

        with a1:
            st.write(city_1 + ', ' + country_1)
            st.write(get_world_ranking(city_1, country_1))
            

        with a2:
            st.write(city_2 + ', ' + country_2)
            st.write(get_world_ranking(city_2, country_2))

    ###########################################################################################


    ###########################################################################################

    ############ obtaining spider chart(world)

    def get_radar_chart_world(city_1, country_1, year_1, city_2, country_2, year_2):
        
        ## Radar chart for individual city in the world

        # importing data

        qol = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
        qol_chosen_1 = qol.loc[(qol["City"] == city_1) & (qol['Country'] == country_1) & (qol['Year'] == year_1)]
        qol_chosen_2 = qol.loc[(qol["City"] == city_2) & (qol['Country'] == country_2) & (qol['Year'] == year_2)]

        # setting variables

        categories = ['Purchasing Power Index', 'Safety Index', 'Healthcare Index', 'Cost of Living Index',
                            'Property Price to Income Ratio', 'Traffic Commute Time Index',
                            'Pollution Index','Climate Index']
        N = len(categories)


        # getting avarage 
        qol_yr = qol[qol['Year'] == year_1]
        qol_yr_avg = qol_yr[categories].mean()


        # 1: Create background

        # the angle of each axis in the plot (divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the plot
        ax = plt.subplot(111, polar=True)

        # set the first axis to be on top
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color='grey', size=7)
        plt.ylim(0,100)

        # 2: Add plots

        # plot each individual = each line of the data

        # chosen city 1
        values = qol_chosen_1[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city_1}")
        #ax.fill(angles, values, 'b', alpha=0.1)

        # chosen city 2
        values = qol_chosen_2[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city_2}")
        #ax.fill(angles, values, 'g', alpha=0.1)

        # add legend
        plt.legend(loc='center', bbox_to_anchor=(1.6, 1))

        # add title
        plt.title(f'{city_1}, {country_1}' + '   vs   ' + f'{city_2}, {country_2} \n', fontsize=15)

        # adjust labels
        ax.tick_params(axis='both', which='major', pad=35)

        return plt

    ####################################   


    ############ obtaining spider chart(USA)

    def get_radar_chart_us(city_1, country_1, year_1, city_2, country_2, year_2):
        
        ## Radar chart for individual city in US

        # importing data

        qol_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo_USA.csv')
        qol_chosen_us_1 = qol_us.loc[(qol_us["City"] == city_1) & (qol_us['Year'] == year_1)]
        qol_chosen_us_2 = qol_us.loc[(qol_us["City"] == city_2) & (qol_us['Year'] == year_2)]

        # setting variables

        categories = ['Purchasing Power Index', 'Safety Index', 'Healthcare Index', 'Cost of Living Index',
                    'Property Price to Income Ratio', 'Traffic Commute Time Index',
                    'Pollution Index','Climate Index']
    
        N = len(categories)

        # getting avarage 
        qol_us_yr = qol_us[qol_us['Year'] == year_1]
        qol_us_yr = qol_us_yr[categories].mean()


        # 1: Create background

        # the angle of each axis in the plot (divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the plot
        ax = plt.subplot(121, polar=True)

        # set the first axis to be on top
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([20,40,60,80,100], ['20','40','60','80','100'], color='grey', size=7)
        plt.ylim(0,100)

        # 2: Add plots

        # plot each individual = each line of the data

        # chosen city 1
        values = qol_chosen_us_1[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city_1}")
        #ax.fill(angles, values, 'b', alpha=0.1)

        # chosen city 2
        values = qol_chosen_us_2[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city_2}")
        #ax.fill(angles, values, 'g', alpha=0.1)

        # add legend
        plt.legend(loc='center', bbox_to_anchor=(1.6, 1))

        # add title
        plt.title(f'{city_1}, {country_1}' + '    vs    ' + f'{city_2}, {country_2} \n', fontsize=15)

        # adjust labels
        ax.tick_params(axis='both', which='major', pad=30)

        return plt

    ####################################   
    
    ## sub-section setting

    st.markdown("""---""")

    if country_1 == 'United States' and country_2 == 'United States':  

        st.pyplot(get_radar_chart_us(city_1, country_1, year_1, city_2, country_2, year_2))
 
    else:
        
        st.pyplot(get_radar_chart_world(city_1, country_1, year_1, city_2, country_2, year_2))

    ###########################################################################################


    ###########################################################################################
    st.markdown("""---""")
    st.subheader('Ranking change for each index')
    
    ############ obtaining world ranking table 

    def get_world_rank_table(city, country):
        
        ## ranking change over the year

        df_rank_world = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_ranking_world.csv')
        
        # extract year data for the chosen city

        chosen_row = df_rank_world.loc[(df_rank_world['City'] == city) 
                                & (df_rank_world['Country'] == country)].sort_values(by='Year', ascending=True)

        # choose columns for display
        columnsTitles = ['Year'] + chosen_row.columns[3:-4].tolist()

        # show result
        rank_change_raw = chosen_row[columnsTitles].sort_values('Year', axis = 0, ascending = False).set_index('Year').T
        
        return rank_change_raw

    ####################################       

    ############ obtaining USA ranking table 

    def get_usa_rank_table(city, country):
        
        ## ranking change over the year

        df_rank_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_ranking_USA.csv')
        
        # extract year data for the chosen city

        chosen_row = df_rank_us.loc[(df_rank_us['City'] == city) 
                                & (df_rank_us['Country'] == country)].sort_values(by='Year', ascending=True)

        # choose columns for display
        columnsTitles = ['Year'] + chosen_row.columns[3:-4].tolist()

        # show result
        rank_change_raw = chosen_row[columnsTitles].sort_values('Year', axis = 0, ascending = False).set_index('Year').T
        
        return rank_change_raw

    ####################################   

    ## sub-section setting
        
    if country_1 == 'United States' and country_2 == 'United States':  

        a1, a2 = st.columns((5,5))
        
        with a1:
            st.write(get_usa_rank_table(city_1, country_1))

        with a2:
            st.write(get_usa_rank_table(city_2, country_2))    

    else:

        a1, a2 = st.columns((5,5))

        with a1:
            st.write(city_1 + ', ' + country_1)
            st.write(get_world_rank_table(city_1, country_1))
        
        with a2:
            st.write(city_2 + ', ' + country_2)
            st.write(get_world_rank_table(city_2, country_2))
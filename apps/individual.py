import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi


# page setting


def app():

    ## set the width of the sidebar
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 200px;
    }
    """,
    unsafe_allow_html=True)

    ###########################################################################################
    ## Side bar

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    country_list = df.Country.sort_values()
    country_list_unique = country_list.unique()
    country = st.sidebar.selectbox('Select a country:', country_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    city_list = df.City[df['Country'] == country].sort_values()
    city_list_unique = city_list.unique()
    city = st.sidebar.selectbox('Select a city:', city_list_unique)

    df = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    year_list = df.Year.unique()
    year_list = df.loc[df['City'] == city].Year.unique()
    year = st.sidebar.selectbox('Select year:', year_list)


    ###########################################################################################
    
    ## page title
    
    st.title('Individual City Report')

    st.write('** Please select Country, City, and Year of your interest on the left sidebar**')

    st.subheader('City' + ' : ' + city + ', ' + country)

    st.write('Year' + ' : ' + str(year))

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
    
    if country == 'United States': 

        a1, a2 = st.columns((5,5))

        with a1:
            st.write('World')
            st.write(get_world_ranking(city, country))
            

        with a2:
            st.write('USA')
            st.write(get_usa_ranking(city, country))
            

    else:
        st.write('World')
        st.write(get_world_ranking(city, country))

    ###########################################################################################
        
        
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

    ############    

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

    ## page setting 
        
    st.markdown("""---""")
    st.subheader('Ranking change for each index')

    if country == 'United States': 

        a1, a2 = st.columns((5,5))

        with a1:
            st.markdown('World')
            st.write(get_world_rank_table(city, country))

        with a2:
            st.markdown('USA')
            st.write(get_usa_rank_table(city, country))

    else:
        st.write(get_world_rank_table(city, country))

    ###########################################################################################

    ############ obtaining spider chart(world)

    def get_radar_chart_world(city, country):
        
        ## Radar chart for individual city in the world

        # importing data

        qol = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
        qol_chosen = qol.loc[(qol['City'] == city) & (qol['Country'] == country) & (qol['Year'] == year)]

        # setting variables

        categories = ['Purchasing Power Index', 'Safety Index', 'Healthcare Index', 'Cost of Living Index',
                            'Property Price to Income Ratio', 'Traffic Commute Time Index',
                            'Pollution Index','Climate Index']
        N = len(categories)


        # getting avarage 
        qol_yr = qol[qol['Year'] == year]
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

        # chosen city
        values = qol_chosen[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city}")
        ax.fill(angles, values, 'b', alpha=0.1)

        # average
        values = qol_yr_avg.values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="World Average")
        ax.fill(angles, values, 'r', alpha=0.1)

        # add legend
        plt.legend(loc='center', bbox_to_anchor=(1.6, 1))

        # add title
        plt.title(f'{city}, {country} \n', fontsize=20)

        # adjust labels
        ax.tick_params(axis='both', which='major', pad=35)

        return plt

    ############


    ############ obtaining spider chart(USA)

    def get_radar_chart_us(city, country):
        
        ## Radar chart for individual city in US

        # importing data

        qol_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo_USA.csv')
        qol_chosen_us = qol_us.loc[(qol_us["City"] == city) & (qol_us['Year'] == year)]

        # setting variables

        categories = ['Purchasing Power Index', 'Safety Index', 'Healthcare Index', 'Cost of Living Index',
                    'Property Price to Income Ratio', 'Traffic Commute Time Index',
                    'Pollution Index','Climate Index']
    
        N = len(categories)

        # getting avarage 
        qol_us_yr = qol_us[qol_us['Year'] == year]
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

        # chosen city
        values = qol_chosen_us[categories].iloc[0].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=f"{city}")
        ax.fill(angles, values, 'b', alpha=0.1)

        # average
        values = qol_us_yr.values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="US Average")
        ax.fill(angles, values, 'r', alpha=0.1)

        # add legend
        plt.legend(loc='center', bbox_to_anchor=(1.6, 1))

        # add title
        plt.title(f'{city} \n', fontsize=20)

        # adjust labels
        ax.tick_params(axis='both', which='major', pad=30)

        return plt

    ############

    ## sub-section setting

    st.markdown("""---""")

    if country != 'United States': 
        
        st.pyplot(get_radar_chart_world(city, country))

    else:
        a1, a2 = st.columns((5,5))

        with a2:
            st.markdown('USA')
            st.pyplot(get_radar_chart_us(city, country))
        
        with a1:
            st.markdown('World')
            st.pyplot(get_radar_chart_world(city, country))

    ###########################################################################################

    ############ obtaining world peer list 

    def get_peer_list_world(city, country, year):

        # showing list of peer cities

        num_peer = 2

        # importing and get 2022 data
        qol = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')


        # Sort dataframe according to Quality of Life Index
        df_peer = qol[
            (qol.Year==year)
        ].sort_values(by='Quality of Life Index', ascending=False).reset_index(drop=True)

        # reset index so that index start from 1
        df_peer.index = np.arange(1, len(df_peer)+1)

        # finding index number for chosen city 
        chosen_index = df_peer[(df_peer.City==city)].index.values.astype(int)[0]

        # list up index numbers for peer group
        index_range=[]
        for i in range(num_peer*2+1):
            index_range.append(chosen_index-num_peer)
            chosen_index += 1

        # remove irrelevant index numbers like 0, -1, -2 ...   
        index_range = [item for item in index_range if item > 0]


        display_col = ['City', 'Country', 'Quality of Life Index', 'Purchasing Power Index',
            'Safety Index', 'Healthcare Index', 'Cost of Living Index',
            'Property Price to Income Ratio', 'Traffic Commute Time Index',
            'Pollution Index', 'Climate Index']

        # display the chosen city and the peers with chosen city highlighted

        chosen_index = df_peer[(df_peer.City==city)].index.values.astype(int)[0]
        df_peer_display = df_peer.loc[index_range][display_col].style.apply(
            lambda x: ['background: lightgreen' if x.name == chosen_index else '' for i in x
                    ], axis=1).format({'Quality of Life Index': '{:,.1f}', 
                                        'Purchasing Power Index': '{:,.1f}','Safety Index': '{:,.1f}', 
                                        'Healthcare Index': '{:,.1f}', 'Cost of Living Index': '{:,.1f}',
                                        'Property Price to Income Ratio': '{:,.1f}',
                                        'Traffic Commute Time Index': '{:,.1f}','Pollution Index': '{:,.1f}',
                                        'Climate Index': '{:,.1f}'})

        return df_peer_display
        
    ############

    ############ obtaining usa peer list 

    def get_peer_list_usa(city, country, year):

        num_peer = 2
        
        # importing data

        qol_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo_USA.csv')
        
        # Sort dataframe according to Quality of Life Index
        df = qol_us[(qol_us.Year==year)
                        ].sort_values(by='Quality of Life Index', ascending=False).reset_index(drop=True)

        # reset index so that index start from 1
        df.index = np.arange(1, len(df)+1)

        # finding index number for chosen city 
        chosen_index = df[(df.City==city)].index.values.astype(int)[0]

        # list up index numbers for peer group
        index_range=[]
        for i in range(num_peer*2+1):
            index_range.append(chosen_index-num_peer)
            chosen_index += 1
        
        chosen_index_to_insert = int(np.median(index_range))

        # remove irrelevant index numbers like 0, -1, -2 and numbers that are out of the rankings...   
        index_range = [item for item in index_range if item > 0 and item <= len(df)]

        # display the chosen city and the peers with chosen city highlighted

        display_col = ['City', 'Quality of Life Index', 'Purchasing Power Index',
            'Safety Index', 'Healthcare Index', 'Cost of Living Index',
            'Property Price to Income Ratio', 'Traffic Commute Time Index',
            'Pollution Index', 'Climate Index']

        df_peer_display = df.loc[index_range][display_col].style.apply(
            lambda x: ['background: lightgreen' if x.name == chosen_index_to_insert else '' for i in x], axis=1
            ).format({'Quality of Life Index': '{:,.1f}', 'Purchasing Power Index': '{:,.1f}','Safety Index': '{:,.1f}', 
            'Healthcare Index': '{:,.1f}', 'Cost of Living Index': '{:,.1f}','Property Price to Income Ratio': '{:,.1f}',
            'Traffic Commute Time Index': '{:,.1f}','Pollution Index': '{:,.1f}', 'Climate Index': '{:,.1f}'})

        return df_peer_display
        
    ############

    ## sub-section setting

    st.markdown("""---""")
    st.subheader('Peer Cities')

    if country == 'United States': 

        a1, a2 = st.columns((5,5))

        with a1:
            st.markdown('World')
            st.write(get_peer_list_world(city, country, year))

        with a2:
            st.markdown('USA')
            st.write(get_peer_list_usa(city, country, year))

    else:
        st.write(get_peer_list_world(city, country, year))

    ###########################################################################################
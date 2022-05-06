import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd


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
    #year_list = df.Year.unique()

    # slider widget for choosing relevant year
    year = st.sidebar.slider('Choose Year between 2018 and 2022', min_value = 2018, max_value = 2022, step = 1)
    st.write('Chosen Year:', year)

    ###########################################################################################
    
    ## sub-section setting

    st.title('Overview')

    st.write('This is a overview of Quality of Life Index data' + ' (' + f'{year}' + ')')

    st.subheader('About the index')

    st.markdown("""Formula = 100 + (Purchasing Power Index / 2.5) - (House Price To Income Ratio * 1.0) 
                   - (Cost of Living Index / 10) + (Safety Index / 2.0) + (Health Index / 2.5) 
                   - (Traffic Time Index / 2.0) - (Pollution Index * 2.0 / 3.0) + (Climate Index / 3.0)""")

    st.write('For more information, visit https://www.numbeo.com/quality-of-life/indices_explained.jsp')

    st.write('** Presented indexes in this app are min-max normalized: 100 for top-most rank, 0 for bottom-most rank **')


    ###########################################################################################

    ## sub-section setting

    st.markdown("""---""")

    st.subheader('Surveyed cities' + ' (' + f'{year}' + ')')

    # importing data
    qol_scale = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')
    qol_scale = qol_scale[(qol_scale.Year==year)]

    # importing world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world[world['name']!='Antarctica']

    # Creating axes and plotting world map
    fig, ax = plt.subplots(figsize=(20, 15))
    world.plot(color='lightgrey', ax=ax)

    # Plotting Quality of Life index data with a color map
    x = qol_scale['Longitude']
    y = qol_scale['Latitude']
    z = qol_scale['Quality of Life Index']
    plt.scatter(x, y, s=0.5*z, c=z, alpha=0.9, vmin=0, vmax=100, cmap='autumn')
    plt.colorbar(label='Quality of Life Index', shrink=.56)

    # Creating axis limits and title
    plt.xlim([-180, 180])
    plt.ylim([-90, 90])
    plt.title('Quality of Living Index Worldwide \n', fontdict={'fontsize': 20})

    # removing outer axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.xticks([])
    plt.yticks([])

    st.pyplot(plt)

    #########

    qol_con = pd.read_csv('02_data-wrangling/02_data/quality_of_life_index_5yrs.csv')

    qol_con_yr = qol_con.loc[qol_con['Year'] == year]

    # counting cities by continent 

    qol_con_yr = pd.DataFrame(qol_con_yr['Continent'].value_counts())
    qol_con_yr.loc['Total'] = qol_con_yr.sum()
    
    st.write(qol_con_yr.T)


    ###########################################################################################
    
    ## sub-section setting

    st.markdown("""---""")

    st.subheader('Number of High ranking cities across continents' + ' (' + f'{year}' + ')')

    # importing data with continent information
    qol_con = pd.read_csv('02_data-wrangling/02_data/quality_of_life_index_5yrs.csv')

    # slider widget for choosing relevant year

    full_num = qol_con.loc[(qol_con['Year'] == year)]['Year'].value_counts()
    Number_of_cities = st.select_slider('Choose number of cities you want to see (Top50, Top100, Top150)', options = [50, 100, 150])

    

    qol_con_yr = qol_con.loc[qol_con['Year'] == year]

    qol_con_num = qol_con_yr.sort_values(by='Quality of Life Index', ascending=False).head(Number_of_cities)

    # counting cities by continent 

    num_city_by_continent = pd.DataFrame(qol_con_num['Continent'].value_counts())
    num_city_by_continent.loc['Total'] = num_city_by_continent.sum()
    
    st.write(num_city_by_continent.T)

    ###########################################################################################
 

    ###########################################################################################
    
    ## sub-section setting

    st.markdown("""---""")
    st.subheader('Top 10 cities in the world' + ' (' + f'{year}' + ')')

    # choose year and index
    
    index_ = 'Quality of Life Index'
    num_cities = 10

    # importing data 
    qol_scale = pd.read_csv('02_data-wrangling/04_data//quality_of_life_index_5yrs_scale_geo.csv')

    # getting the result
    qol_scale_yr = qol_scale[qol_scale['Year'] == year]
    top_world = qol_scale_yr.sort_values(by=index_, ascending=False).head(num_cities)

    # reset index so that index start from 1
    top_world.index = np.arange(1, len(top_world)+1)

    top_world = top_world[['City', 'Country', 'Quality of Life Index', 'Purchasing Power Index',
        'Safety Index', 'Healthcare Index', 'Cost of Living Index',
        'Property Price to Income Ratio', 'Traffic Commute Time Index',
        'Pollution Index', 'Climate Index']].style.apply(
            lambda x: ['background: lightgreen' if x.name == 1 else '' for i in x
                    ], axis=1).format({'Quality of Life Index': '{:,.1f}', 
                                        'Purchasing Power Index': '{:,.1f}','Safety Index': '{:,.1f}', 
                                        'Healthcare Index': '{:,.1f}', 'Cost of Living Index': '{:,.1f}',
                                        'Property Price to Income Ratio': '{:,.1f}',
                                        'Traffic Commute Time Index': '{:,.1f}','Pollution Index': '{:,.1f}',
                                        'Climate Index': '{:,.1f}'})
    st.write(top_world)

    ###########################################################################################
    
    ## sub-section setting

    st.markdown("""---""")

    st.subheader('Top 10 cities in the US' + ' (' + f'{year}' + ')')

    qol_us = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo_USA.csv')
    qol_us_yr = qol_us.loc[(qol_us['Year'] == year)]

    top10_us = qol_us_yr.sort_values(by='Quality of Life Index', ascending=False).head(10)

    # reset index so that index start from 1
    top10_us.index = np.arange(1, len(top10_us)+1)

    top10_us = top10_us[['City','Quality of Life Index', 'Purchasing Power Index',
       'Safety Index', 'Healthcare Index', 'Cost of Living Index',
       'Property Price to Income Ratio', 'Traffic Commute Time Index',
       'Pollution Index', 'Climate Index']].style.apply(
            lambda x: ['background: lightgreen' if x.name == 1  else '' for i in x
                    ], axis=1).format({'Quality of Life Index': '{:,.1f}', 
                                        'Purchasing Power Index': '{:,.1f}','Safety Index': '{:,.1f}', 
                                        'Healthcare Index': '{:,.1f}', 'Cost of Living Index': '{:,.1f}',
                                        'Property Price to Income Ratio': '{:,.1f}',
                                        'Traffic Commute Time Index': '{:,.1f}','Pollution Index': '{:,.1f}',
                                        'Climate Index': '{:,.1f}'})
    st.write(top10_us)


    ###########################################################################################
    st.markdown("""---""")

    st.subheader('Top 5 cities in each continent' + ' (' + f'{year}' + ')')
    
    def get_conti_top10_ranking(year, continent):

        numb_cities = 5 #top5

        # importing data 
        qol_scale = pd.read_csv('02_data-wrangling/04_data/quality_of_life_index_5yrs_scale_geo.csv')

        # display column

        dis_col = ['City','Country']

        # extracting cities in chosen year and continent

        qol_scale = qol_scale.loc[(qol_scale['Year']== year)]
        qol_scale = qol_scale.loc[(qol_scale['Continent']== continent)]
        qol_scale = qol_scale.sort_values(by='Quality of Life Index', ascending=False).head(numb_cities)

        # reset index so that index start from 1
        qol_scale.index = np.arange(1, len(qol_scale)+1)
        
        return qol_scale[dis_col]


    ## sub-section setting

    a1, a2, a3 = st.columns(3)

    with a1:
        st.write('America')
        st.write(get_conti_top10_ranking(year, 'America'))
        

    with a2:
        st.write('Europe')
        st.write(get_conti_top10_ranking(year, 'Europe'))

        
    with a3:
        st.write('Asia')
        st.write(get_conti_top10_ranking(year, 'Asia'))


    a1, a2, a3 = st.columns(3)

    with a1:
        st.write('Africa')
        st.write(get_conti_top10_ranking(year, 'Africa'))
        

    with a2:
        st.write('Oceania')
        st.write(get_conti_top10_ranking(year, 'Oceania'))

    with a3:
        st.write('')
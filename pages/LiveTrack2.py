import pandas as pd
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import holoviews as hv
# import datetime as dt
from streamlit_option_menu import option_menu
from datetime import date,timedelta
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import requests


# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing


#   Page configuration
st.set_page_config(
    page_title="DASHBOARD Polio",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

#AZAM CODE Feature 1 Minimalize the Defaut (ap hide kar sakty ho header and footer jis pa streamlit likha hota ha)
hide_menu_style = """
    <style>
    MainMenue {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=df_google_sheet
# @st.cache(suppress_st_warning=True)
# def printer():
#     st.write("testing")

# #loading online csv
# url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esHVLDDdUVgCxpJDsFt7gUi/data.csv"#,";")
# #s = requests.get(url).content
# df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
# df=df_google_sheet

# Ya code app ko fast karny ka lia ha
@st.experimental_memo
# @st.experimental_singleton()
def load_data():
# df=load_data.clear()
    #loading online csv
    data="https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"#,";")
    # s = requests.get(url).content
    data=pd.read_csv(data, on_bad_lines='skip', sep=";")
    df = pd.DataFrame(data)

    return df
if st.button("Click Me To Get Refresh Data"):
    # Clears all singleton caches:
#     st.experimental_singleton.clear()
    load_data.clear()
df=load_data()

start_date = st.date_input('Select start date:')
end_date = st.date_input('Select end date:')

df['Survey Day'] = pd.to_datetime(df['Survey Day'])
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Create unique List for DISTRICT
district_options = df['Enumerator Name'].unique()
# Create multiselect for DISTRICT
districts = st.multiselect('Select Vacinator Name', district_options, default = district_options)

# Filter the data based on user input
filtered_df = df[(df['Survey Day'].dt.date >= start_date) & (df['Survey Day'].dt.date <= end_date) & df['Enumerator Name'].isin(districts)]
# st.write(filtered_df)


# st.dataframe(filtered_df)
st.subheader("ALLL DATA DONWLOAD AND FILTER DATEWISE")
st.text(f"Total number of forms submitted:{df.shape[0]}")
#ya start date and end date ma jab wo date select kary ga us ki total entries ajay gai
count = filtered_df.count()[0]
st.markdown(f"<span style='color: red;'>Total count between Start Date and End Date: {count}</span>",unsafe_allow_html=True)

# today = dt.datetime.today().strftime('%Y-%m-%d')
# current_day_df = df[df['Survey Day'] == today]
# total_entries = len(current_day_df)
# st.write("Total Entries for Today:", total_entries,today)



grid_table = AgGrid(filtered_df,
                    # theme='balham',
                    enable_enterprise_modules=True,
                    fit_column_on_grid_load=True,
                    height=500,
                    width='100%')


filtered_df.rename(columns = {'_GPS_latitude':'Y'}, inplace = True)
filtered_df.rename(columns = {'_GPS_longitude':'X'}, inplace = True)
filtered_df.rename(columns = {'Enumerator Name':'ID'}, inplace = True)

filtered_df.dropna(subset=['Y'], inplace=True)
filtered_df.dropna(subset=['X'], inplace=True)
filtered_df.dropna(subset=['ID'], inplace=True)

count = filtered_df.count()[0]
st.markdown(f"<span style='color: red;'>Total count GPS Start Date and End Date Between RECEIVE: {count}</span>",unsafe_allow_html=True)
# st.write(filtered_df)

filtered_df.columns = filtered_df.columns.str.strip()
subset_of_df = filtered_df

m = folium.Map(location=[subset_of_df['Y'].mean(),
                                subset_of_df['X'].mean()],
                    zoom_start=5)

place_lat = subset_of_df['Y'].astype(float).tolist()
place_lng = subset_of_df['X'].astype(float).tolist()

points = []
# read a series of points from coordinates and assign them to points object
for i in range(len(place_lat)):
    points.append([place_lat[i], place_lng[i]])

# specify an icon of your desired shape or chosing in place for the coordinates points
# for index,lat in enumerate(place_lat):
for index,lat in enumerate(place_lat,start=1):
    folium.Marker([lat, 
                place_lng[index]],
#                 popup=('Bus Station{} \n '.format(index))
                 popup=('ID {} \n '.format(index))
                ,icon = folium.Icon(color='blue',icon_color='white',prefix='fa', icon='bus')
                ).add_to(m)

folium.PolyLine(points, color='blue' ,dash_array='5',opacity ='.85',
                tooltip='Transit Route 101'
).add_to(m)
st_folium(m, width=1500, height=950)


# st.write(printer())
    # #1ST MAP
    # some_map = folium.Map(location=[subset_of_df['Y'].mean(),subset_of_df['X'].mean()],zoom_start=5)
    # for row in subset_of_df.itertuples():
    #     some_map.add_child(folium.Marker(location=[row.Y,row.X], popup=row.ID))
    # st_folium(some_map, width=1500, height=950)


    # #2ND MAP
    # some_map_2 = folium.Map(location=[subset_of_df['Y'].mean(),
    #                                 subset_of_df['X'].mean()],
    #                                 zoom_start=10)
    # mc= MarkerCluster()
    # for row in subset_of_df.itertuples():
    #     mc.add_child(folium.Marker(location=[row.Y,row.X], popup=row.ID))
    # some_map_2.add_child(mc)
    # st_folium(some_map_2, width=1600, height=950)





    # folium.PolyLine(route_lats_longs).add_to(map_plot_route)
    # map_plot_route
    # st_folium(map_plot_route)

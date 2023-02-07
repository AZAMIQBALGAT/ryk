import pandas as pd
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import holoviews as hv
import datetime as dt
from streamlit_option_menu import option_menu
from datetime import date,timedelta
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.markdown("azam")


    # st.set_page_config(layout="wide")

    #loading online csv
    url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esHVLDDdUVgCxpJDsFt7gUi/data.csv"#,";")
    #s = requests.get(url).content
    df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
    df=df_google_sheet

    start_date = st.date_input('Select start date:')
    end_date = st.date_input('Select end date:')

    df['Survey Day'] = pd.to_datetime(df['Survey Day'])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[df['Survey Day'].between(start_date, end_date)]
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

    filtered_df.columns = filtered_df.columns.str.strip()
    subset_of_df = filtered_df

    #1ST MAP
    some_map = folium.Map(location=[subset_of_df['Y'].mean(),subset_of_df['X'].mean()],zoom_start=5)
    for row in subset_of_df.itertuples():
        some_map.add_child(folium.Marker(location=[row.Y,row.X], popup=row.ID))
    st_folium(some_map, width=1500, height=950)


    #2ND MAP
    some_map_2 = folium.Map(location=[subset_of_df['Y'].mean(),
                                    subset_of_df['X'].mean()],
                                    zoom_start=10)
    mc= MarkerCluster()
    for row in subset_of_df.itertuples():
        mc.add_child(folium.Marker(location=[row.Y,row.X], popup=row.ID))
    some_map_2.add_child(mc)
    st_folium(some_map_2, width=1600, height=950)


    # folium.PolyLine(route_lats_longs).add_to(map_plot_route)
    # map_plot_route

    # st_folium(map_plot_route)

with tab2:
    st.markdown("azam")
    st.markdown("azam iqbal2")
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


    # loading data and showing it as a table on top of the dashboard
    #https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing


    # st.set_page_config(layout="wide")

    # sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
    # df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
    # df=df_google_sheet

    #loading online csv
    url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esHVLDDdUVgCxpJDsFt7gUi/data.csv"#,";")
    #s = requests.get(url).content
    df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
    df=df_google_sheet

    st.date_input("Select start date:", key="input_1")
    st.date_input("Select end date:", key="input_2")

    # start_date = st.date_input('Select start date:')
    # end_date = st.date_input('Select end date:')

    df['Survey Day'] = pd.to_datetime(df['Survey Day'])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Create unique List for DISTRICT
    district_options = df['Enumerator Name'].unique()
    # Create multiselect for DISTRICT
    districts = st.multiselect('Select Districts', district_options, default = district_options)

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
                        key="unique_agGrid_1",
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
    for index,lat in enumerate(place_lat):
        folium.Marker([lat, 
                    place_lng[index]],
                    popup=('Bus Station{} \n '.format(index))
                    ,icon = folium.Icon(color='blue',icon_color='white',prefix='fa', icon='bus')
                    ).add_to(m)

    folium.PolyLine(points, color='blue' ,dash_array='5',opacity ='.85',
                    tooltip='Transit Route 101'
    ).add_to(m)
    st_folium(m, width=1500, height=950)
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import pandas as pd
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import holoviews as hv
import hvplot.pandas
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date,timedelta
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode




# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing




# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=df_google_sheet
#loading online csv
url="https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"#,";")
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


filtered_df.rename(columns = {'_GPS_latitude':'lat'}, inplace = True)
filtered_df.rename(columns = {'_GPS_longitude':'lon'}, inplace = True)
filtered_df.dropna(subset=['lat'], inplace=True)
filtered_df.dropna(subset=['lon'], inplace=True)
st.map(filtered_df)

# st.map(grid_table)

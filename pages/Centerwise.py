import matplotlib.pyplot as plt 
import datetime as dt
# import plotly.express as px
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
# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing




# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=df_google_sheet

#loading online csv
#loading online csv

url= "https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"
#s = requests.get(url).content
df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=df_google_sheet

# start_date = st.date_input('Select start date:')
# end_date = st.date_input('Select end date:')

# df['Survey Day'] = pd.to_datetime(df['Survey Day'])
# start_date = pd.to_datetime(start_date)
# end_date = pd.to_datetime(end_date)
# filtered_df = df[df['Survey Day'].between(start_date, end_date)]

# # st.dataframe(filtered_df)
# st.subheader("ALLL DATA DONWLOAD AND FILTER")
# st.text(f"Total number of forms submitted:{df.shape[0]}")

# today = dt.datetime.today().strftime('%Y-%m-%d')
# current_day_df = df[df['Survey Day'] == today]
# total_entries = len(current_day_df)
# st.write("Total Entries for Today:", total_entries,today)


# counts = df["UC"].value_counts()
# # Sort the counts in ascending order
# counts.sort_index(ascending=True)
# st.write(counts)




# grid_table = AgGrid(filtered_df,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')




# # create calendar widget for user to select date
# date = st.date_input("Select a date:")
# date = pd.to_datetime(date)

# # filter dataframe by selected date
# filtered_df = df[df['Survey Day'] == date]
# filtered_df['Survey Day'] = pd.to_datetime(df['Survey Day'] == date)

# # count number of UCs
# uc_count = filtered_df['UC'].value_counts().to_dict()

# # display count of UCs to user
# st.write("Number of UCs:", uc_count)

start_date = st.date_input('Select start date:')
end_date = st.date_input('Select end date:')

# convert Survey Day column to datetime type
df['Survey Day'] = pd.to_datetime(df['Survey Day'])
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
filtered_df = df[df['Survey Day'].between(start_date, end_date)]

# filter dataframe by selected date mean Single Date
# filtered_df = df[df['Survey Day'] == date]

# count number of UCs
# uc_count = filtered_df[{'UC','Monthly_Target'}]
# uc_count = filtered_df['UC'].value_counts()


# uc_count = df.groupby(['UC']).size().reset_index(name='count')
# uc_count = df.groupby(['UC', 'Monthly_Target']).size().reset_index(name='count')

# uc_count2 = df(['Monthly_Target']).size().reset_index(name='count')
# uc_count = df.pivot_table(index='UC', columns='Monthly_Target')
# st.write(uc_count)


# count number of UCs
uc_count = filtered_df['Center_Name'].value_counts()

# display count of UCs to user
st.write("Number of UCs:", uc_count)
st.bar_chart(uc_count)
# # create new dataframe with uc_count and Monthly_Target columns
# combined_df = pd.DataFrame({'uc_count': uc_count, 'Monthly_Target': monthly_target})
# st.dataframe(combined_df)
# display count of UCs to user
# st.write("Number of UCs:", uc_count)
# st.bar_chart(uc_count)

# uc_counts = df.groupby('UC').size().reset_index(name='count')

# Print the resulting DataFrame
# print(uc_counts)



import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import holoviews as hv
import hvplot.pandas
import datetime as dt
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

#loading online csv

url= "https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"
#s = requests.get(url).content
df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=df_google_sheet



today = dt.datetime.today().strftime('%Y-%m-%d')
current_day_df = df[df['Survey Day'] == today]
total_entries = len(current_day_df)
# st.write("Total Entries for Today:",today, total_entries, style={"font-size": "600pt"})
st.write("Total Entries for Today",today,total_entries,unsafe_allow_html=True)

# st.write(f"Total Entries for Today: {today}: {total_entries}", style={"font-size": "5pt"})

#st.write(text, style={"font-size": "32pt"})

# st.write[["today, total_entries"]], font_size=20, bold=True, color="red")

# st.markdown("<h1 style='font-size:20px; font-weight:bold; color:red'>Total</h1>", unsafe_allow_html=True)
# st.markdown("<font color='red'><strong><font size='36pt'>[today, total_entries]</font></strong></font>")




counts = df['Survey Day'].value_counts().sort_index(ascending=())

# Create a bar plot showing the counts
counts.plot(kind='bar')
plt.xlabel('Survey Day')
plt.ylabel('Count')

# Add event lines to the plot
# plt.eventplot(positions=list(zip(counts.index, counts)))
# Add a text label for each bar showing the count
for i, count in enumerate(counts):
    plt.text(x=i, y=count+0.5, s=count, ha='center')
    st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

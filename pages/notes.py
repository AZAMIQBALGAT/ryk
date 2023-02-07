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

st.set_option('deprecation.showPyplotGlobalUse', False)
# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing
# Use the `@st_cache.cache` decorator to cache the function's out

#   Page configuration
st.set_page_config(
    page_title="NOTES",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

#Python for Data Analysis: Exploring and Cleaning Data

sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
data= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
df=data
# st.text(df.info)
# st.text(df.describe)


categorical = df.dtypes[df.dtypes == "object"].index
st.text(categorical)

st.text(df[categorical].describe())
# st.text(categorical)
# st.markdown("azam",unsafe_allow_html=True)
# # Read in a CSV file
# df = pd.read_csv("data.csv")

# # Drop any rows with missing values
# df = df.dropna()

# # Remove any duplicates
# df = df.drop_duplicates()

# # Replace any values in the "age" column that are less than 18 with the mean age
# df.loc[df['age'] < 18, 'age'] = df['age'].mean()

# # Rename the "name" column to "full_name"
# df = df.rename(columns={'name': 'full_name'})


# grid_table = AgGrid(df,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=200,
#                     width='100%')
# st.dataframe(df)
# st.dataframe(df.info)
# df.info
# Check dimensions Rows 2004 column is 63 date is 21-1-2023 baad ma change b ho jay gay
# df.shape

# columns ka names btay ga aur  is ki data types bta da ga jo easy ho ga type kia ha us ki
#object] ya text ki data type hoti h
#int64] ya numeric values ki data type hoti h
#float_values] ya b numeric values ki data type hoti h like [0.0, 0.25, 0.5, 0.75, 1.0]
# df.dtypes 

# Check the first 5 rows
# df.head(5)

# data.describe()
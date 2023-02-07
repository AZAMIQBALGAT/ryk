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



#   Page configuration
st.set_page_config(
    page_title="Antigens",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=df_google_sheet

#loading online csv
url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esHVLDDdUVgCxpJDsFt7gUi/data.csv"#,";")
#s = requests.get(url).content
df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=df_google_sheet






# start_date = st.date_input('Select start date:')
# a = start_date
# end_date = st.date_input("Select end date")
# b =end_date
# # Date check G
# if end_date < start_date:
#     st.error("End Date cannot be before Start Date")


# df['Survey Day'] = pd.to_datetime(df['Survey Day'])
# start_date = pd.to_datetime(start_date)
# end_date = pd.to_datetime(end_date)

# # Create unique List for DISTRICT
# district_options = df['DISTRICT'].unique()
# # Create multiselect for DISTRICT
# districts = st.multiselect('Select Districts', district_options, default = district_options)


# # Filter the data based on user input
# filtered_df = df[(df['Survey Day'].dt.date >= start_date) & (df['Survey Day'].dt.date <= end_date) & df['DISTRICT'].isin(districts)]
# # st.write(filtered_df)

# st.subheader("REPORT Antigens with Charts & Data")
# st.text(f"Total number of forms submitted:{df.shape[0]}")

# #ya start date and end date ma jab wo date select kary ga us ki total entries ajay gai
# count = filtered_df.count()[0]

# # Column names ko change karna
# filtered_df.rename(columns = {'OPV-0':'OPVZero'}, inplace = True)
# filtered_df.rename(columns = {'OPV-I':'OPV1'}, inplace = True)
# filtered_df.rename(columns = {'OPV-II':'OPV2'}, inplace = True)
# filtered_df.rename(columns = {'OPV-III':'OPV3'}, inplace = True)
# filtered_df.rename(columns = {'Rotavirus-I':'Rotavirus1'}, inplace = True)
# filtered_df.rename(columns = {'Rotavirus-II':'Rotavirus2'}, inplace = True)
# filtered_df.rename(columns = {'IPV-I':'IPV1'}, inplace = True)
# filtered_df.rename(columns = {'IPV-II':'IPV2'}, inplace = True)
# filtered_df.rename(columns = {'MR-I':'MR1'}, inplace = True)
# filtered_df.rename(columns = {'MR-II':'MR2'}, inplace = True)


# BCG = filtered_df.query("BCG == 'Yes'").count()['BCG'] # st.write('BCG:', BCG)
# OPVZero = filtered_df.query("OPVZero == 'Yes'").count()['OPVZero']
# OPV1 = filtered_df.query("OPV1 == 'Yes'").count()['OPV1']
# OPV2 = filtered_df.query("OPV2 == 'Yes'").count()['OPV2']
# OPV3 = filtered_df.query("OPV3 == 'Yes'").count()['OPV3']
# Rotavirus1 = filtered_df.query("Rotavirus1 == 'Yes'").count()['Rotavirus1']
# Rotavirus2 = filtered_df.query("Rotavirus2 == 'Yes'").count()['Rotavirus2']
# IPV1 = filtered_df.query("IPV1 == 'Yes'").count()['IPV1']
# IPV2 = filtered_df.query("IPV2 == 'Yes'").count()['IPV2']
# MR1 = filtered_df.query("MR1 == 'Yes'").count()['MR1']
# MR2 = filtered_df.query("MR2 == 'Yes'").count()['MR2']

# counts_df = pd.DataFrame({'BCG': [BCG], 'OPVZero': [OPVZero], 'OPV1': [OPV1], 'OPV2': [OPV2], 'OPV3': [OPV3], 'Rotavirus1': [Rotavirus1], 'Rotavirus2': [Rotavirus2], 'IPV1': [IPV1], 'IPV2': [IPV2], 'MR1': [MR1], 'MR2': [MR2]})
# final = counts_df

# st.markdown(f"<span style='color: red;'>Total count between Start Date and End Date: {count}</span>",unsafe_allow_html=True)


# grid_table = AgGrid(final,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=140,
#                     width='100%')

# # plt.bar(['BCG', 'OPVZero', 'OPV1', 'OPV2', 'OPV3', 'Rota1','Rota2','IPV1','IPV2','MR1','MR2'], [BCG, OPVZero, OPV1, OPV2,  OPV3, Rotavirus1,Rotavirus2,IPV1,IPV2,MR1,MR2])

# # define the variables you want to display on the x-axis label
# # create the x-axis label by concatenating the variables
# # create the x-axis label by using string formatting
# # xlabel = "Date: {} To {} {}".format(a, b, districts)
# # # set the x-axis label
# # plt.xlabel(xlabel, color='red')   
# # plt.ylabel('Count of Vaccinations')

# # # Add count values on top of each bar
# # for i, v in enumerate([BCG, OPVZero, OPV1, OPV2, OPV3, Rotavirus1,Rotavirus2,IPV1,IPV2,MR1,MR2]):
# #     plt.text(i-.1, v+1, str(v), color='red', ha='center')
# #     plt.xticks(rotation=90)
# # # Display the charts
# #     # Display the selected district as a heading for the chart
# # st.pyplot()
# # ---- Plot types -------
# # fig = px.bar(final, x='BCG', y=['OPVZero','OPV1','OPV2','OPV3','Rotavirus1','Rotavirus2','IPV1','IPV2','MR1','MR2'], barmode='group')
# # fig = px.bar(final, x='BCG', y=['OPVZero','OPV1','OPV2','OPV3','Rotavirus1','Rotavirus2','IPV1','IPV2','MR1','MR2'], barmode='group')

# # fig = px.bar(['BCG', 'OPVZero', 'OPV1', 'OPV2', 'OPV3', 'Rota1','Rota2','IPV1','IPV2','MR1','MR2'], [BCG, OPVZero, OPV1, OPV2,  OPV3, Rotavirus1,Rotavirus2,IPV1,IPV2,MR1,MR2])


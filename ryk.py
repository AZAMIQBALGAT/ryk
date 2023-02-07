#import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import holoviews as hv
import hvplot.pandas
# import datetime as dt
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

st.sidebar.success("SELECT A PAGE OR REPORT.")


#loading online csv

url= "https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"
#s = requests.get(url).content
df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=df_google_sheet

# df=load_data.clear()
# df=load_data()
# st.write(df)
# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing

# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# data= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df = data




#AZAM CODE Feature 1 Minimalize the Defaut (ap hide kar sakty ho header and footer jis pa streamlit likha hota ha)
hide_menu_style = """
    <style>
    MainMenue {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# useful_data=df_google_sheet[["Enumerator Name","Enumerator Mobile","Survey Day","Union Council","UC","DISTRICT","TEHISL","Vaccination_Strategy","Monthly_Target"]]
#1- Load the CSV file and extract the unique values from the "UC" column and sort A-Z:
unique_ucs = sorted(df["Center_Name"].unique())
#2- Create the selectbox and assign it to a variable:
# uc_selectbox = st.selectbox("SELECT UC:",unique_ucs)
uc_selectbox = st.radio("SELECT CENTER:",unique_ucs)
#2.1- radio button ko horizontal to vertically ma convert kar day ga space ki bachat ho gai:
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#3- Display the data for the selected Uc:
selected_data = df[df["Center_Name"] == uc_selectbox]
#3.1 - ya extra code ha is ma jab wo uc select kary ga us ka count b ajay ga selected
count = selected_data.count()[0]
st.markdown(f"<span style='color: red;'>Total count till Date: {count}</span>",unsafe_allow_html=True)
#4- Display the data for the selected Uc IN TABLE:
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
# gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    selected_data,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    # theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=540, 
    width='100%',
    reload_data=True
)

#Column names ko change karna
selected_data.rename(columns = {'_GPS_latitude':'lat'}, inplace = True)
selected_data.rename(columns = {'_GPS_longitude':'lon'}, inplace = True)
#Column ma sa nan wali values ko khatm karna
selected_data.dropna(subset=['lat'], inplace=True)
selected_data.dropna(subset=['lon'], inplace=True)
count = selected_data.count()[0]
st.markdown(f"<span style='color: red;'>Total count GPS till Date RECEIVE: {count}</span>",unsafe_allow_html=True)
#Display the GPS IN MAPBOX
st.map(selected_data)
#Example controlers
# st.sidebar.subheader("St-AgGrid example options")

# sample_size = st.sidebar.number_input("rows", min_value=10, value=30)
# grid_height = st.sidebar.number_input("Grid height", min_value=200, max_value=800, value=300)

# return_mode = st.sidebar.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
# return_mode_value = DataReturnMode.__members__[return_mode]

# update_mode = st.sidebar.selectbox("Update Mode", list(GridUpdateMode.__members__), index=len(GridUpdateMode.__members__)-1)
# update_mode_value = GridUpdateMode.__members__[update_mode]

# #enterprise modules
# enable_enterprise_modules = st.sidebar.checkbox("Enable Enterprise Modules")
# if enable_enterprise_modules:
#     enable_sidebar =st.sidebar.checkbox("Enable grid sidebar", value=False)
# else:
#     enable_sidebar = False

# #features
# fit_columns_on_grid_load = st.sidebar.checkbox("Fit Grid Columns on Load")

# enable_selection=st.sidebar.checkbox("Enable row selection", value=True)
# if enable_selection:
#     st.sidebar.subheader("Selection options")
#     selection_mode = st.sidebar.radio("Selection Mode", ['single','multiple'], index=1)

#     use_checkbox = st.sidebar.checkbox("Use check box for selection", value=True)
#     if use_checkbox:
#         groupSelectsChildren = st.sidebar.checkbox("Group checkbox select children", value=True)
#         groupSelectsFiltered = st.sidebar.checkbox("Group checkbox includes filtered", value=True)


# enable_pagination = st.sidebar.checkbox("Enable pagination", value=False)
# if enable_pagination:
#     st.sidebar.subheader("Pagination options")
#     paginationAutoSize = st.sidebar.checkbox("Auto pagination size", value=True)
#     if not paginationAutoSize:
#         paginationPageSize = st.sidebar.number_input("Page size", value=5, min_value=0, max_value=sample_size)
#     st.sidebar.text("___")
    
# #Example controlers
# st.sidebar.subheader("St-AgGrid example options")

# with st.sidebar:
#     selected= option_menu(
#         menu_title="UC",
#         options=[unique_Uc[0],unique_Uc[1],unique_Uc[2],
#         unique_Uc[3],unique_Uc[4],unique_Uc[5],unique_Uc[6],
#         unique_Uc[7],unique_Uc[8],unique_Uc[9],
#         unique_Uc[10],unique_Uc[11],unique_Uc[12],
#         unique_Uc[13],unique_Uc[14],unique_Uc[15],
#         unique_Uc[16],unique_Uc[17]],
#     )
    
    
   
    
# if selected ==unique_Uc[0]:
#     st.header(unique_Uc[0])
#     filtered_df0=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[0]])   
#     grid_table = AgGrid(filtered_df0,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
  
    
# if selected ==unique_Uc[1]:
#     st.header(unique_Uc[1])
#     filtered_df1=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[1]])   
#     grid_table = AgGrid(filtered_df1,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
    
# if selected ==unique_Uc[2]:
#     st.header(unique_Uc[2])   
#     filtered_df2=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[2]])   
#     grid_table = AgGrid(filtered_df2,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
 
    
# if selected ==unique_Uc[3]:
#     st.header(unique_Uc[3])
#     filtered_df3=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[3]])   
#     grid_table = AgGrid(filtered_df3,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[4]:
#     st.header(unique_Uc[4])
#     filtered_df4=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[4]])   
#     grid_table = AgGrid(filtered_df4,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
       
# if selected ==unique_Uc[5]:
#     st.header(unique_Uc[5])
#     filtered_df5=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[5]])   
#     grid_table = AgGrid(filtered_df5,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[6]:
#     st.header(unique_Uc[6])
#     filtered_df6=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[6]])   
#     grid_table = AgGrid(filtered_df6,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[7]:
#     st.header(unique_Uc[7])
#     filtered_df7=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[7]])   
#     grid_table = AgGrid(filtered_df7,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')  
    
# if selected ==unique_Uc[8]:
#     st.header(unique_Uc[8])
#     filtered_df8=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[8]])   
#     grid_table = AgGrid(filtered_df8,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[9]:
#     st.header(unique_Uc[9])
#     filtered_df9=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[9]])   
#     grid_table = AgGrid(filtered_df9,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')   
    
# if selected ==unique_Uc[10]:
#     st.header(unique_Uc[10])
#     filtered_df10=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[10]])   
#     grid_table = AgGrid(filtered_df10,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')     
    
# if selected ==unique_Uc[11]:
#     st.header(unique_Uc[11])
#     filtered_df11=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[11]])   
#     grid_table = AgGrid(filtered_df11,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')  
    
# if selected ==unique_Uc[12]:
#     st.header(unique_Uc[12])
#     filtered_df12=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[12]])   
#     grid_table = AgGrid(filtered_df12,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[13]:
#     st.header(unique_Uc[13])
#     filtered_df13=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[13]])   
#     grid_table = AgGrid(filtered_df13,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')  
    
# if selected ==unique_Uc[14]:
#     st.header(unique_Uc[14])
#     filtered_df14=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[14]])   
#     grid_table = AgGrid(filtered_df14,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%') 
    
# if selected ==unique_Uc[15]:
#     st.header(unique_Uc[15])
#     filtered_df15=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[15]])   
#     grid_table = AgGrid(filtered_df15,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[16]:
#     st.header(unique_Uc[16])
#     filtered_df16=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[16]])   
#     grid_table = AgGrid(filtered_df16,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
    
# if selected ==unique_Uc[17]:
#     st.header(unique_Uc[17])
#     filtered_df17=(df_google_sheet[df_google_sheet["UC"]==unique_Uc[17]])   
#     grid_table = AgGrid(filtered_df17,
#                     # theme='balham',
#                     enable_enterprise_modules=True,
#                     fit_column_on_grid_load=True,
#                     height=500,
#                     width='100%')
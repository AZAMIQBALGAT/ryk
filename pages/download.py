import pandas as pd
import streamlit as st
import os
from datetime import date,timedelta
import datetime as dt
import urllib.request
# import pyautoit
# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing
# Use the `@st_cache.cache` decorator to cache the function's out

sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
data= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
df=data



# Iterate through each row of the dataframe
for index, row in df.iterrows():

    # Get the URL for the image
    image_url = ["https://kc.humanitarianresponse.info/media/original?media_file=prcadmin%2Fattachments%2F860d171403984e11804b06dfcfc7d70f%2F55b85e3e-a151-4e50-b012-d0c62f069b27%2F1673020074819.jpg"]
    # image_url = row["EPI CARD Picture_URL"]
    # # Get the image filename
    # image_filename = image_url.split("/")[-1]
    # Download the image
    # urllib.request.urlretrieve(image_url)
    st.download_button(image_url)
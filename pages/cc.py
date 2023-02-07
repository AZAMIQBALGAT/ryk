import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)



#   Page configuration
st.set_page_config(
    page_title="DASHBOARD Polio",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=df_google_sheet

# Load data
# loading online csv
url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esGrgdBVrATLgeXcoQEf9tX/data.csv"#,";")
#s = requests.get(url).content
df_google_sheet=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=df_google_sheet

st.title("Bar Chart of Vaccination Counts")


#  Column names ko change karna
df.rename(columns = {'OPV-0':'OPVZero'}, inplace = True)
df.rename(columns = {'OPV-I':'OPV1'}, inplace = True)
df.rename(columns = {'OPV-Il':'OPV2'}, inplace = True)
df.rename(columns = {'Rotavirus-I':'Rotavirus1'}, inplace = True)
df.rename(columns = {'Pneumococcal-I':'Pneumococcal1'}, inplace = True)
df.rename(columns = {'Pentavalent-I':'Pentavalent1'}, inplace = True)


start_date = st.date_input('Select start date:')
end_date = st.date_input('Select end date:')

df['Survey Day'] = pd.to_datetime(df['Survey Day'])
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
df = df[df['Survey Day'].between(start_date, end_date)]

# Count yes values in each column
bcg_yes = df['BCG'].eq('Yes').sum()
opvzero_yes = df['OPVZero'].eq('Yes').sum()
opv1_yes = df['OPV1'].eq('Yes').sum()
pentavalent1_yes = df['Pentavalent1'].eq('Yes').sum()
pneumococcal1_yes = df['Pneumococcal1'].eq('Yes').sum()

# Create bar chart
# counts.plot(kind='bar')
plt.bar(['BCG', 'OPVZero', 'OPV1', 'Penta1', 'Pneum1'], [bcg_yes, opvzero_yes, opv1_yes, pentavalent1_yes, pneumococcal1_yes])
plt.xlabel('Vaccinations')
plt.ylabel('Count of "Yes"')

# Add count values on top of each bar
for i, v in enumerate([bcg_yes, opvzero_yes, opv1_yes, pentavalent1_yes, pneumococcal1_yes]):
    plt.text(i-.17, v+1, str(v), color='red', fontweight='bold', ha='center')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


# # Select columns
# data = data[['Survey Day', 'BCG', 'OPVZero', 'OPV1', 'Pentavalent1', 'Pneumococcal1']]

# # Select date range
# start_date = st.date_input("Start Date")
# end_date = st.date_input("End Date")
# data = data[(data['Survey Day'] >= start_date) & (data['Survey Day'] <= end_date)]

# # Count yes values in each column
# bcg_yes = data['BCG'].eq('yes').sum()
# opvzero_yes = data['OPVZero'].eq('yes').sum()
# opv1_yes = data['OPV1'].eq('yes').sum()
# pentavalent1_yes = data['Pentavalent1'].eq('yes').sum()
# pneumococcal1_yes = data['Pneumococcal1'].eq('yes').sum()

# # Create bar chart
# plt.bar(['BCG', 'OPVZero', 'OPV1', 'Pentavalent1', 'Pneumococcal1'], [bcg_yes, opvzero_yes, opv1_yes, pentavalent1_yes, pneumococcal1_yes])
# plt.xlabel('Vaccinations')
# plt.ylabel('Count of "Yes"')
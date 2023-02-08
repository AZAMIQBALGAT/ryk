import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


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


#loading online csv
url="https://kobo.humanitarianresponse.info/api/v2/assets/aBt8DD5imGGKe8aAG8o3na/export-settings/esSYZkSfHtwYfY2tpLGyGxN/data.csv"#,";")
#s = requests.get(url).content
data=pd.read_csv(url, on_bad_lines='skip', sep=";")
pr = data.profile_report()
st_profile_report(pr)
# df.head()
# profile = ProfileReport(df, title="Pandas Profiling Report")
# profile.to_file("Anylsis")

import bar_chart_race as bcr
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import datetime as dt
import plotly.express as px
import pandas as pd
import numpy as np
import panel as pn
pn.extension ("tabulator", template="material", sizing_mode="stretch_width")
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import date,timedelta
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

st.set_option('deprecation.showPyplotGlobalUse', False)



sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
df_google_sheet= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
df=df_google_sheet


df['Survey Day'] = pd.to_datetime(df['Survey Day']).dt.date
df.rename(columns = {'OPV-0':'OPVZero'}, inplace = True)



# points = df[['Survey Day', 'BCG', 'OPVZero']]
# points.set_index('Survey Day')
# df.dtypes
# bcr.bar_chart_race(df=points[:10], filename='video.mp4')

# bcr.bar_chart_race(
#     df=df,
#     filename='covid19_horiz.mp4',
#     orientation='h',
#     sort='desc',
#     n_bars=6,
#     fixed_order=False,
#     fixed_max=True,
#     steps_per_period=10,
#     interpolate_period=False,
#     label_bars=True,
#     bar_size=.95,
#     period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
#     period_fmt='%B %d, %Y',
#     period_summary_func=lambda v, r: {'x': .99, 'y': .18,
#                                       's': f'Total deaths: {v.nlargest(6).sum():,.0f}',
#                                       'ha': 'right', 'size': 8, 'family': 'Courier New'},
#     perpendicular_bar_func='median',
#     period_length=500,
#     figsize=(5, 3),
#     dpi=144,
#     cmap='dark12',
#     title='COVID-19 Deaths by Country',
#     title_size='',
#     bar_label_size=7,
#     tick_label_size=7,
#     shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
#     scale='linear',
#     writer=None,
#     fig=None,
#     bar_kwargs={'alpha': .7},
#     filter_column_colors=False)
# import pandas as pd
# import streamlit as st
# # import folium
# # df = pd.read_csv('file.csv')

# # # Create a map using the first row's latitude and longitude values
# # m = folium.Map(location=[df.loc[0,'lat'], df.loc[0,'lon']], zoom_start=20)

# # # # Add markers for each location
# # # for i in range(0,len(df)):
# # #     folium.Marker([df.loc[i,'lat'], df.loc[i,'lon']], popup=df.loc[i,'city']).add_to(m)
# # m
# # # Display the map
# # # st.map(m)
# import folium
# import folium

# base_map = folium.Map(location=[52.2297, 21.0122], control_scale=True, zoom_start=10)

# points1 = [(52.228771, 21.003146),

#        ( 52.238025, 21.050971),
#        (52.255008, 21.036172),
#        (52.252831, 21.051385),
#        (52.219995, 20.965021)]

# for tuple_ in points1:

#     icon=folium.Icon(color='white', icon='train', icon_color="red", prefix='fa')
#     folium.Marker(tuple_, icon=icon).add_to(base_map)

# points2 = [(52.239062, 21.131601),

#        (52.204905, 21.168202),
#        (52.181296, 20.987486),
#        (52.206272, 20.914988),
#        (52.254395, 21.224107)]

# for tuple_ in points2:
#     icon=folium.Icon(color='white', icon='car', icon_color="blue", prefix='fa')
#     folium.Marker(tuple_, icon=icon).add_to(base_map)

# line_points = [(52.204905, 21.168202),(52.255008, 21.036172), (52.219995, 20.965021), (52.239062, 21.131601), (52.254395, 21.224107)]

# folium.PolyLine(locations=line_points, weight=3,color = 'yellow').add_to(base_map)


# base_map.save("example_map.html")


# Import Modules
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import requests
from io import BytesIO

# Dummy data
# data = {
#         'image_url': ['https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
#                       'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,704,1000_AL_.jpg',
#                       'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,679,1000_AL_.jpg',
#                       'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg'],
#         'name': ['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight'],
#         'year': [1994, 1972, 1974, 2008],
#         'description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
#                         'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
#                         'The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.',
#                         'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.'],
#         'rating': [9.2, 9.2, 9.0, 9.0],
#         }


# loading data and showing it as a table on top of the dashboard
#https://docs.google.com/spreadsheets/d/13ikD5WpjmapBlKY4j2dTrwsZ-du3pdfpHhjIYwugcxM/edit?usp=sharing
# Use the `@st_cache.cache` decorator to cache the function's out

# sheet_id="1yM6y7IIxSix8RGC9U0EOCXkIeNmlIAh7MdNB2Nfg494"    
# data= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")    #add this /export?format=csv
# df=data

#loading online csv
url="https://kobo.humanitarianresponse.info/api/v2/assets/aGQGms9UUYqNz6sUfwvgxu/export-settings/esHVLDDdUVgCxpJDsFt7gUi/data.csv"#,";")
#s = requests.get(url).content
data=pd.read_csv(url, on_bad_lines='skip', sep=";")
df=data


df = pd.DataFrame(data)
#st.write(df)
st.header("AgGrid table with Image Display")
render_image = JsCode('''
                      
    function renderImage(params){
    // Create a new image element
        var img = new Image();
        
        img.src = params.value;
        
        img.width = 35;
        img.height = 35;
        
        return img;
        
    }             
                      ''')

# build gridoptions object

# Build GridOptions object
options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_column('EPI CARD Picture_URL', cellRenderer = render_image)
options_builder.configure_selection(selection_mode="single", use_checkbox=True)
grid_options = options_builder.build()

# Create AgGrid component
grid = AgGrid(df, 
                gridOptions = grid_options,
                allow_unsafe_jscode=True,
                height=500, width=500, theme='streamlit')

sel_row = grid["selected_rows"]
if sel_row:
    col1, col2 = st.columns(2)
    # st.info(sel_row[0]['Child Name'])
    col1.image(sel_row[0]['EPI CARD Picture_URL'],caption = sel_row[0]['Enumerator Name'])
    col2.subheader("DISTRICT: " + str(sel_row[0]['DISTRICT']))
    col2.subheader("TEHISL: " + str(sel_row[0]['TEHISL']))
    col2.subheader("UC: " + str(sel_row[0]['UC']))
    col2.subheader("Age in Days: " + str(sel_row[0]['Age in Days']))
    col2.subheader("Age in Weeks: " + str(sel_row[0]['Age in Weeks']))
    col2.subheader("Vaccination Strategy: " + str(sel_row[0]['Vaccination_Strategy']))
    col2.subheader("Child Name: " + str(sel_row[0]['Child Name']))
    col2.subheader("Visit Status: " + str(sel_row[0]['Visit Status']))
    col2.subheader("Enumerator Name: " + str(sel_row[0]['Enumerator Name']))
    col2.subheader("Enumerator Mobile: " + str(sel_row[0]['Enumerator Mobile']))
    col2.subheader("Survey Day: " + str(sel_row[0]['Survey Day']))

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('vgsales.csv')


#------------------------------------------SIDEBAR---------------------
st.sidebar.title("REI SUPREMO DOS GAMES")
st.sidebar.image('Games_logo.png')





#['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales',
#       'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
#      dtype='object')
#-----------------------------------------------------------------------


with st.container():
    col1, col2 ,col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True, height="stretch"):
             st.markdown("### vendas globais por genero")








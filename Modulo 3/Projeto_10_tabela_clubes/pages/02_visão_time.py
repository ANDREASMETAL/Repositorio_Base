import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('Tabela_clubes.csv')
df['Idade_Media'] = df['Idade_Media'].apply(lambda x: float(x.replace(',','.')))


times = df['Clubes'].unique().tolist()

time = st.sidebar.selectbox('Time', times)

df = df[df['Clubes'] == time]


#--------------------------------------------------SIDEBAR
#clubes = df['Clubes'].unique().tolist()
#
#ftr = st.sidebar.multiselect('Clubes', clubes, clubes)
#df = df[df['Clubes'].apply(lambda x: x in  ftr)]
#
#jogadores = df['Qtd_Jogadores'].unique().tolist()
#
#jog = st.sidebar.multiselect('Qtd_Jogadores', jogadores, jogadores)
#df = df[df['Qtd_Jogadores'].apply(lambda x: x in  jog)]
#------------------------------------------------------------


with st.container():
    col1, col2, col3,col4 = st.columns(4)

    with col1:
        with st.container(border=True, height="stretch"):
            st.metric('Temporadas que participou', df['Ano'].count())

    with col2:
        with st.container(border=True, height="stretch"):
            st.metric('Quantidade total de jogadores', df['Qtd_Jogadores'].sum())

    with col3:
        with st.container(border=True, height="stretch"):
            st.metric('Idade media do Elenco', f'{df['Idade_Media'].mean():.1f}')

    with col4:
        with st.container(border=True, height="stretch"):
            st.metric('Valor total do Elenco', f'R${df['Valor_total'].sum():,}')

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(height='stretch'):
            df_aux = df.groupby('Ano')['Valor_total'].sum().reset_index()
            fig = px.line(df_aux, x='Ano', y='Valor_total', title='Valor total do clube por ano', markers=True)
            st.plotly_chart(fig)

    with col2:
        with st.container(height='stretch'):
            df_aux = df.groupby('Ano')['Vitorias'].sum().reset_index()
            fig = px.line(df_aux, x='Ano', y='Vitorias', title='Vitorias  do clube por ano', markers=True)
            
            st.plotly_chart(fig)

    with col3:
        with st.container(height='stretch'):
            df_aux = df.groupby('Ano')['Derrotas'].sum().reset_index()
            fig = px.line(df_aux, x='Ano', y='Derrotas', title='Derrotas  do clube por ano', markers=True)
            st.plotly_chart(fig)

    with col4:
        with st.container(height='stretch'):
            df_aux = df.groupby('Ano')['Empates'].sum().reset_index()
            fig = px.line(df_aux, x='Ano', y='Empates', title='Empates do clube por ano', markers=True)
            st.plotly_chart(fig)
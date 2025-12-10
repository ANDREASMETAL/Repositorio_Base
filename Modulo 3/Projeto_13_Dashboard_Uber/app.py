import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd .read_csv('uber.csv')
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['ano'] = df['pickup_datetime'].dt.year
df['mes'] = df['pickup_datetime'].dt.month
df['hora'] = df['pickup_datetime'].dt.hour


#-------------------------------------------sidebar
st.sidebar.title('Corridas uber')
st.sidebar.image('logo.png')

anos = sorted(df['ano'].unique().tolist())
ano_inicial, ano_final =st.sidebar.select_slider('Escolha o periodo', anos, value=[2009, 2015])
df = df[(df['ano']>= ano_inicial) & (df['ano']<=ano_final)]


#----------------------------------------------------body
with st.container():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st. container(border=True, height='stretch'):
            st.metric('Total corridas', df['key'].count())

    with col2:
        with st. container(border=True, height='stretch'):
            st.metric('Total Tarifa',f'${df['fare_amount'].sum():.2f}')


    with col3:
        with st. container(border=True, height='stretch'):
            st.metric('Tarifa mais Cara',f'${df['fare_amount'].max():.2f}')

    with col4:
        with st. container(border=True, height='stretch'):
            st.metric('Total Passageiros', df['passenger_count'].sum())


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        with st.container(height="stretch"):
            df_aux = df.groupby("hora")["fare_amount"].sum().reset_index()
            fig = px.line(
                df_aux,
                x="hora",
                y="fare_amount",
                title="Tarifas ao longo do dia",
                markers=True
            )
            st.plotly_chart(fig)

    with col2:
        with st.container(height="stretch"):
            df_aux = df.groupby("mes")["fare_amount"].sum().reset_index()
            fig = px.line(
                df_aux,
                x="mes",
                y="fare_amount",
                title="Preço das tarifas ao longo dos meses",
                markers=True
            )
            st.plotly_chart(fig)



mask = (
    (df['pickup_longitude']  >= -74.27) & (df['pickup_longitude']  <= -73.68) &
    (df['dropoff_longitude'] >= -74.27) & (df['dropoff_longitude'] <= -73.68) &
    (df['pickup_latitude']   >=  40.49) & (df['pickup_latitude']   <=  40.92) &
    (df['dropoff_latitude']  >=  40.49) & (df['dropoff_latitude']  <=  40.92)
)
coor = df[mask]


st.map(coor, latitude='pickup_latitude', longitude='pickup_longitude', size=1)






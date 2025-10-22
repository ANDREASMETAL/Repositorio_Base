import streamlit as st

# ---------------------------------------------- SIDEBAR

st.sidebar.title('consoles')
st.sidebar.title('Datas')





# ---------------------------------------------- PRINCIPAL
tab1, tab2, tab3, tab4, tab5 = st.tabs(['playstation one', 'Sega saturn', 'Nintendo Gamecub', 'Dreamcast','Playstation2'])

with tab1:
    st.title('Jogos De Suvival Horror')
    st.subheader('Os principais:')
    st.write('''
 - Resident Evil 1
 - Resident Evil 2
 - Resident Evil 3
 - Silent Hill
 - Alone In The Dark New Nigthmare
- Nigthmare Criatures
- Parasit Eve 1
- Parasit Eve 2
- D''')
with tab2:
    st.title('Jogos De Suvival Horror')
    st.subheader('Os principais:')
    st.write ('''
- Resident Evil 1
- Enemy Zero
- The House Of Dead
- Alone In The Dark 2''')
with tab3:
    st.title('Jogos De Suvival Horror')
    st.subheader('Os principais:')
    st.write ('''
- Resident Evil 0
- Resident Evil Remake
- Resident Evil 2
- Resident Evil 3
- Resident Evil 4
- Resident Evil COD Veronica
- Eternal Darkness''')
with tab4:
    st.title('Jogos De Suvival Horror')
    st.subheader('Os principais:')
    st.write ('''
- Resident Evil 2
- Resident Evil 3
- Resident evil COD Veronica
- Alone In The Dark New Nigthmare''')


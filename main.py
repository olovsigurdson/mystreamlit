import streamlit as st
import pandas
from weather_api import get_weather

data = {
    'Series_1': [1, 2, 3, 4, 7],
    'Series_2': [10, 30, 40, 100, 250]
}



st.title('Olovs first app')
st.subheader('Testar Streamlit!!')
st.write(f'''Första webappen
Testar!!
{get_weather()}
''')

df = pandas.DataFrame(data)
st.write(df)
st.line_chart(df)
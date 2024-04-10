import streamlit as st
import pandas as pd


st.title("DSCI 510 - Lab #12 - CAR DATA")

df = pd.read_csv('car_data.csv', sep=';')

st.dataframe(df.style.highlight_max(axis=0))

with st.sidebar:
    Car_Name = st.text_input('Car Name?', '')
    
    manual_auto = st.multiselect(
    'Manual and/or Automatic?',
    ['Manual', 'Automatic'],)
    default=['Manual', 'Automatic']
    st.write(f'Your current selection is:', manual_auto)
    
    price_range = st.slider(
    'Price Range',
    0.0, 100.0, (0.0, 20.0))
    st.write('Selected:', price_range)
    
    year = st.slider(
    'Price Range',
    1990.0, 2024.0, (2000.0, 2024.0))
    st.write('Selected:', year)
    
    st.button("Submit", type="primary")
    
    
    
    
    





    




    



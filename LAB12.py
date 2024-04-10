import streamlit as st
import pandas as pd

st.title("DSCI 510 - Lab #12 - CAR DATA")

df = pd.read_csv('car_data.csv')  # Assuming CSV file is comma-separated

# Function to apply filters and display filtered data
def filter_data(df, car_name='', transmission=['Manual', 'Automatic'], price_range=(0.0, 20.0), year_range=(2000, 2024)):
    filtered_df = df.copy()
    
    # Apply filters
    if car_name:
        filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name, case=False)]
    filtered_df = filtered_df[filtered_df['Transmission'].isin(transmission)]
    filtered_df = filtered_df[(filtered_df['Selling_Price'] >= price_range[0]) & (filtered_df['Selling_Price'] <= price_range[1])]
    filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]
    
    return filtered_df

with st.sidebar:
    # Sidebar options
    car_name = st.text_input('Car Name', '')
    transmission = st.multiselect('Manual and/or Automatic?', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])
    price_range = st.slider('Price Range', 0.0, 100.0, (0.0, 20.0))
    year_range = st.slider('Year Range', 1990, 2024, (2000, 2024))
    submit_button = st.button("Submit", type="primary")

# If the submit button is clicked
if submit_button:
    # Filter the data
    filtered_data = filter_data(df, car_name, transmission, price_range, year_range)
    
    # Display filtered data
    st.dataframe(filtered_data)
else:
    # Display original data if no filters are selected
    st.dataframe(df)
    
    
    
    
    





    




    



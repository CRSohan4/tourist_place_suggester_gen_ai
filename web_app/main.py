# !pip install streamlit

# To run the app run below command in the terminal/cmd
# `streamlit run main.py`

import streamlit as st
import utility.langchain_helper as llm_service

st.title("Plan your next trip!")

selected_country = st.sidebar.selectbox("Pick a country", ("India", "Australia", 'England', 'USA', 'New Zealand'))

if selected_country:
    response = llm_service.suggest_tourist_place_name(selected_country)
    st.write("Country: " + selected_country)
    st.header("Tourist Place: " + response['tourist_place_name'])
    
    st.write("**Description**")
    
    st.write(response["description"])

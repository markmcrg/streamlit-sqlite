import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from main import small_query_box, generate_sidebar

db_file = generate_sidebar("data_exploration")

conn = st.experimental_connection(
    "dataset",
    type="sql",
    url="sqlite:///" + db_file,
)

st.title("🚀 SQL Data Exploration")
st.write("🐧 In this section, we will learn how to use SQL to explore and answer questions about data!")
st.write("📝 Take note of the schema of the database shown on the left sidebar. You will need to know the schema in order to write queries that explore the data.")
st.write("")

tab1, tab2 = st.tabs(["dengue_cases", "volcanoes"])
# with tab1:
#     st.write("Let's start by exploring the `covid_cases` table. The table contains data about COVID-19 cases in the Philippines.")
#     st.write("* Which age group has the most COVID-19 cases?")
#     small_query_box("covid_cases", db_file)
#     show_answer = st.checkbox("Show Answer", key="covid_cases_show_answer") 
#     if show_answer: 
#         st.code("SELECT age_group, COUNT(*) AS num_cases FROM covid_cases GROUP BY age_group ORDER BY num_cases DESC LIMIT 1;", language="sql")
#         st.write("The 20-29 age group has the most COVID-19 cases.")
        
with tab1:
    st.write("Let's now explore the `dengue_cases` table. The table contains data about dengue cases in the Philippines.")
    st.write("* Which region had the most dengue cases?")

    small_query_box("dengue_cases", db_file)
    show_answer = st.checkbox("Show Answer", key="dengue_cases_show_answer")
    if show_answer: 
        st.code("SELECT Month, Year, case_count FROM dengue_cases ORDER BY case_count DESC LIMIT 5;", language="sql")
        st.write("* June 2013 had the most dengue cases.")
    
with tab2:
    st.write("Let's now explore the `volcanoes` table. The table contains data about active volcanoes in the Philippines.")
    st.write("* Which two volcanoes has the lowest elevation?")
    small_query_box("volcanoes", db_file)
    show_answer = st.checkbox("Show Answer", key="volcanoes_show_answer")
    if show_answer: 
        st.code("SELECT Name, m FROM volcanoes ORDER BY m ASC LIMIT 2;", language="sql")
        st.write("* Leonard Kniaseff and Taal has the lowest elevations.")
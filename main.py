import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.set_page_config(layout="wide", page_title="Interactive SQL")
show_pages(
    [
        Page("main.py", "What are SQL Queries?", "🤔"),
        Page("pages/basic_sql_queries.py", "Basic SQL Queries", ":star:"),
        Page("pages\more_sql_queries.py", "More SQL Queries!", ":fire:"),
        Page("pages/data_exploration.py", "SQL Data Exploration", ":rocket:")
    ]
)
st.title('🤔 What are SQL Queries?')

dataset = st.sidebar.selectbox(
    "Dataset",
    ("COVID-19 Cases in the Philippines", "Dengue Cases in the Philippines", "Active Volcanoes in the Philippines")
)
st.sidebar.subheader('Schema') 
# Add Description
if dataset == "COVID-19 Cases in the Philippines":
    db_file = "datasets/ph_covid_cases.db"
    st.sidebar.image("schema-png\covid_cases_schema.png", width=225)
elif dataset == "Dengue Cases in the Philippines":
    db_file = "datasets/ph_dengue_cases.db"
    st.sidebar.image("schema-png\dengue_cases_schema.png")
elif dataset == "Active Volcanoes in the Philippines":
    db_file = "datasets/ph_volcanoes.db"
    st.sidebar.image("schema-png\\volcanoes_schema.png")

conn = st.experimental_connection(
    "dataset",
    type="sql",
    url="sqlite:///" + db_file,
)


st.write("SQL is a language for querying data from relational databases.")
st.write("It is a powerful tool that can be used to extract, transform, and analyze data.")
st.write("SQL queries are made up of statements that are executed by the database server.")
st.write("The most common types of SQL statements are SELECT, INSERT, UPDATE, and DELETE.")

st.markdown("""
    The `SELECT` statement is used to retrieve data from a database.
    The `INSERT` statement is used to add new data to a database.
    The `UPDATE` statement is used to modify existing data in a database.
    The `DELETE` statement is used to delete data from a database.
""")

st.write("Here is an example of a simple SQL query:")
st.code("SELECT * FROM covid_cases;")
st.write("This query will return all of the rows in the `covid_cases` table.")



st.subheader("Try it out!")

query = st.text_area('Input Query', placeholder='Enter query')

if st.button('Query'):
    try:
        st.write('Result:')
        df = conn.query(query)
        st.dataframe(df, hide_index=True)
    except Exception as e:
        st.exception(e)
        
st.write("For more information about SQL, please visit the following resources:")
st.write("* [The official SQL tutorial](https://www.w3schools.com/sql/)")
st.write("* [The SQL documentation](https://www.sqlite.org/docs.html)")
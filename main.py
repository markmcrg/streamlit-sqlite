import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title

#st.set_page_config(layout="wide", page_title="Interactive SQL")

show_pages(
    [
        Page("main.py", "What are SQL Queries?", "🤔"),
        Page("pages/Basic_SQL_Queries.py", "Basic SQL Queries", ":star:"),
        Page("pages/more_sql_queries.py", "More SQL Queries!", ":fire:"),
        Page("pages/data_exploration.py", "SQL Data Exploration", ":rocket:")
    ]
)

st.title('🤔 What are SQL Queries?')

# Make sidebar reusable

dataset = st.sidebar.selectbox(
    "Dataset",
    ("COVID-19 Cases in the Philippines", "Dengue Cases in the Philippines", "Active Volcanoes in the Philippines")
)
st.sidebar.subheader('Schema') 
# Add Description
if dataset == "COVID-19 Cases in the Philippines":
    db_file = "datasets/ph_covid_cases.db"
    st.sidebar.image("schema-png/covid_cases_schema.png", width=225)
elif dataset == "Dengue Cases in the Philippines":
    db_file = "datasets/ph_dengue_cases.db"
    st.sidebar.image("schema-png/dengue_cases_schema.png")
elif dataset == "Active Volcanoes in the Philippines":
    db_file = "datasets/ph_volcanoes.db"
    st.sidebar.image("schema-png/volcanoes_schema.png")

conn = st.experimental_connection(
    "dataset",
    type="sql",
    url="sqlite:///" + db_file,
)


st.subheader('What is SQL?')
st.write('Structured Query Language (SQL) is a language used to manage data in a database.')
st.write('SQL is used for a variety of tasks, including:')
st.write('* Creating and managing databases')
st.write('* Inserting, updating, and deleting data')
st.write('* Retrieving data from databases')

st.subheader('Why is SQL used for data analytics?')
st.write('SQL is a powerful tool for data analytics because it allows you to easily retrieve and manipulate data from databases.')
st.write('This makes it possible to perform complex queries, such as joins and aggregations, to get the insights you need.')

st.subheader('How does a SQL query look like?')
st.write('A SQL query is a series of statements that are used to interact with a database.')
st.write('Each statement is made up of keywords and values.')
st.write('For example, the following query selects all of the rows from the `customers` table:')
st.code('SELECT * FROM customers;', language='sql')

st.subheader('What is a schema?')
st.write('A schema is a blueprint for a database. It defines the tables, columns, and data types that are stored in the database.')
st.write('The schema is used to ensure that the data in the database is consistent and organized.')

st.subheader('Basic syntax of SQL queries')
st.write('The basic syntax of a SQL query is as follows:')
# st.write('```sql
# SELECT [columns]
# FROM [table]
# [WHERE [conditions]]
# [ORDER BY [column]]
# ```')

st.subheader('Benefits of SQL')
st.write('There are many benefits to using SQL for data analytics, including:')
st.write('* It is a standard language, so it is portable across different databases.')
st.write('* It is a powerful language that can be used to perform complex queries.')
st.write('* It is a relatively easy language to learn.')


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
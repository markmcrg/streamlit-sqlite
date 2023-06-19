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

st.title("🤔 What are SQL Queries?")

st.subheader("💡 What is SQL? ")
st.write("SQL stands for Structured Query Language. It is a language used to communicate with databases.")

st.subheader("📊 Why is SQL used for data analytics? ")
st.write("SQL is used for data analytics because it allows you to extract data from databases and manipulate it in a way that is easy to understand and analyze.")

st.subheader("🧐 How a SQL Query looks like")
st.write("A SQL query is a set of instructions that tells the database what data you want to extract and how you want to manipulate it.")
st.write("Here is an example of a simple SQL query:")
st.code("SELECT * FROM customers;", language='sql')
st.write("💾 This query will select all of the rows from the `customers` table.")

st.subheader("🗺️ What is a schema and why is it important?")
st.write("A schema is a blueprint of a database. It defines the structure of the database, including the tables, columns, and data types.")
st.write("Schemas are important because they help to ensure that the data in a database is organized and consistent.")

st.subheader("🚀 Benefits of SQL")
st.write("There are many benefits to using SQL for data analytics, including:")
st.write("* 🛠️ It is a powerful and versatile language.")
st.write("* 📖 It is easy to learn.")
st.write("* 📉 It is a declarative language, meaning that you can focus on what you want to do rather than how to do it.")
st.write("* 🌎 It is widely supported by databases.")

st.subheader("Try it out!")

query = st.text_area('Input Query', placeholder='Enter query')

if st.button('Query'):
    try:
        st.write('Result:')
        df = conn.query(query)
        st.dataframe(df, hide_index=True)
    except Exception as e:
        st.exception(e)
        
st.write("This is just a brief introduction to SQL queries. For more information, please visit the following resources:")
st.write("* 🔗 [SQL Tutorial](https://www.w3schools.com/sql/)")
st.write("* 📘 [SQL Reference](https://www.w3schools.com/sql/sql_ref_keywords.asp)")
st.write("* 📃 [SQL Cheat Sheet](https://www.w3schools.com/sql/sql_cheatsheet.asp)")

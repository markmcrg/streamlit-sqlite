import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.title("⭐ Basic SQL Queries")
st.write("In this section, we will learn about the basic SQL queries that you will need to know in order to use SQL for data analytics.")

with st.expander("**SELECT, FROM**"):
    st.write("The `SELECT` keyword is used to select the columns that you want to return from the database.")
    st.write("The `FROM` keyword is used to specify the table that you want to select data from.")
    st.write("For example, the following query would select the `name` and `age` columns from the `customers` table:")
    st.code("SELECT name, age FROM customers;", language="sql")

with st.expander("**WHERE**"):
    st.write("The `WHERE` keyword is used to filter the rows that are returned by the query. The `WHERE` clause can contain a condition that the rows must match in order to be returned.")
    st.write("For example, the following query would select all of the customers who are over the age of 18:")
    st.code("SELECT name, age FROM customers WHERE age > 18;", language="sql")

with st.expander("**AND, OR, NOT**"):
    st.write("The `AND`, `OR`, and `NOT` keywords can be used to combine multiple conditions in the `WHERE` clause.")
    st.write("For example, the following query would select all of the customers who are over the age of 18 and from the United States:")
    st.code("SELECT name, age FROM customers WHERE age > 18 AND country = 'United States';", language="sql")

with st.expander("**ORDER BY**"):
    st.write("The `ORDER BY` keyword is used to sort the rows that are returned by the query. The `ORDER BY` clause can specify the column that you want to sort by and the order (ascending or descending) that you want the rows to be sorted in.")
    st.write("For example, the following query would sort the customers by their age in ascending order:")
    st.code("SELECT name, age FROM customers ORDER BY age ASC;", language="sql")

with st.expander("**INSERT**"):
    st.write("The `INSERT` statement is used to insert new rows into a table. The `INSERT` statement takes a list of values that you want to insert into the table.")
    st.write("For example, the following statement would insert a new customer into the `customers` table:")
    st.code("INSERT INTO customers (name, age, country) VALUES ('John Doe', 30, 'United States');", language="sql")
    
with st.expander("**UPDATE**"):
    st.write("The `UPDATE` statement is used to update existing rows in a table. The `UPDATE` statement takes a list of columns that you want to update and the new values for those columns.")
    st.write("For example, the following statement would update the age of the customer named 'John Doe' to 35:")
    st.code("UPDATE customers SET age = 35 WHERE name = 'John Doe';", language="sql")

with st.expander("**DELETE**"):
    st.write("The `DELETE` statement is used to delete rows from a table. The `DELETE` statement takes a condition that the rows must match in order to be deleted.")
    st.write("For example, the following statement would delete all of the customers who are over the age of 30:")
    st.code("DELETE FROM customers WHERE age > 30;", language="sql")
    
with st.expander("**AS**"):
    st.write("The `AS` keyword is used to give a column a new name. This can be useful for making the results of a `SELECT` statement more readable.")
    st.write("For example, the following query would select the `name` column and rename it to `customer_name`:")
    st.code("SELECT name AS customer_name FROM customers;", language="sql")


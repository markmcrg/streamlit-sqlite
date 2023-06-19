import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title
from main import small_query_box, generate_sidebar

db_file = generate_sidebar("basic_sql_queries")

st.title("⭐ Basic SQL Queries")
st.write("In this section, we will learn about the basic SQL queries that you will need to know in order to use SQL for data analytics.")

with st.expander("**SELECT, FROM**"):
    st.write("The `SELECT` keyword is used to select the columns that you want to return from the database.")
    st.write("The `FROM` keyword is used to specify the table that you want to select data from.")
    st.write("For example, the following query would select the `name` and `age` columns from the `customers` table:")
    st.code("SELECT name, age FROM customers;", language="sql")
    small_query_box("SELECT", db_file)

with st.expander("**WHERE**"):
    st.write("The `WHERE` keyword is used to filter the rows that are returned by the query. The `WHERE` clause can contain a condition that the rows must match in order to be returned.")
    st.write("For example, the following query would select all of the customers who are over the age of 18:")
    st.code("SELECT name, age FROM customers WHERE age > 18;", language="sql")
    small_query_box("WHERE", db_file)
    
with st.expander("**LIMIT**"):
    st.write("The `LIMIT` keyword is used to limit the number of rows returned by a query.")
    st.write("For example, the following query returns the first 10 rows from the `users` table:")
    st.code("SELECT * FROM users LIMIT 10")
    small_query_box("LIMIT", db_file)

with st.expander("**AND, OR, NOT**"):
    st.write("The `AND`, `OR`, and `NOT` keywords can be used to combine multiple conditions in the `WHERE` clause.")
    st.write("For example, the following query would select all of the customers who are over the age of 18 and from the United States:")
    st.code("SELECT name, age FROM customers WHERE age > 18 AND country = 'United States';", language="sql")
    small_query_box("AND", db_file)

with st.expander("**ORDER BY**"):
    st.write("The `ORDER BY` keyword is used to sort the rows that are returned by the query. The `ORDER BY` clause can specify the column that you want to sort by and the order (ascending or descending) that you want the rows to be sorted in.")
    st.write("For example, the following query would sort the customers by their age in ascending order:")
    st.code("SELECT name, age FROM customers ORDER BY age ASC;", language="sql")
    small_query_box("ORDER BY", db_file)

with st.expander("**INSERT**"):
    st.write("The `INSERT` statement is used to insert new rows into a table. The `INSERT` statement takes a list of values that you want to insert into the table.")
    st.write("For example, the following statement would insert a new customer into the `customers` table:")
    st.code("INSERT INTO customers (name, age, country) VALUES ('John Doe', 30, 'United States');", language="sql")
    small_query_box("INSERT", db_file)
    
with st.expander("**UPDATE**"):
    st.write("The `UPDATE` statement is used to update existing rows in a table. The `UPDATE` statement takes a list of columns that you want to update and the new values for those columns.")
    st.write("For example, the following statement would update the age of the customer named 'John Doe' to 35:")
    st.code("UPDATE customers SET age = 35 WHERE name = 'John Doe';", language="sql")
    small_query_box("UPDATE", db_file)

with st.expander("**DELETE**"):
    st.write("The `DELETE` statement is used to delete rows from a table. The `DELETE` statement takes a condition that the rows must match in order to be deleted.")
    st.write("For example, the following statement would delete all of the customers who are over the age of 30:")
    st.code("DELETE FROM customers WHERE age > 30;", language="sql")
    small_query_box("DELETE", db_file)
    
with st.expander("**AS**"):
    st.write("The `AS` keyword is used to give a column a new name. This can be useful for making the results of a `SELECT` statement more readable.")
    st.write("For example, the following query would select the `name` column and rename it to `customer_name`:")
    st.code("SELECT name AS customer_name FROM customers;", language="sql")
    small_query_box("AS", db_file)
    
    
st.write("")
st.subheader("💫 More SQL Queries!")
with st.expander("**DISTINCT**"):
    st.write("The `DISTINCT` keyword is used to remove duplicate rows from the results of a query.")
    st.write("For example, the following query would select all the distinct values in the `customer_name` column:")
    st.code("SELECT DISTINCT customer_name FROM customers;", language="sql") #lanuage sql and add query box and bold all
    small_query_box("DISTINCT", db_file)
    
with st.expander("**MIN/MAX**"):
    st.write("The `MIN` and `MAX` keywords are used to return the minimum and maximum values in a column.")
    st.write("For example, the following query would return the minimum and maximum values in the `customer_id` column:")
    st.code("SELECT MIN(customer_id), MAX(customer_id) FROM customers;", language="sql") 
    small_query_box("MINMAX", db_file)
    
with st.expander("**AVG**"):
    st.write("The `AVG` keyword is used to return the average value in a column.")
    st.write("For example, the following query would return the average value in the `customer_age` column:")
    st.code("SELECT AVG(customer_age) FROM customers;", language="sql") 
    small_query_box("AVG", db_file)
    
with st.expander("**COUNT**"):
    st.write("The `COUNT` keyword is used to return the number of rows in a table.")
    st.write("For example, the following query would return the number of rows in the `customers` table:")
    st.code("SELECT COUNT(*) FROM customers;", language="sql") 
    small_query_box("COUNT", db_file)
    
with st.expander("**SUM**"):
    st.write("The `SUM` keyword is used to return the sum of the values in a column.")
    st.write("For example, the following query would return the sum of the values in the `customer_spend` column:")
    st.code("SELECT SUM(customer_spend) FROM customers;", language="sql") 
    small_query_box("SUM", db_file)
    
with st.expander("**LIKE**"):
    st.write("The `LIKE` keyword is used to match a pattern in a column.")
    st.write("For example, the following query would select all the rows where the `customer_name` column contains the string `John`:")
    st.code("SELECT * FROM customers WHERE customer_name LIKE '%John%';", language="sql") 
    small_query_box("LIKE", db_file)


import pandas as pd
import numpy as np
import streamlit as st
from st_pages import Page, show_pages, add_page_title

st.title("⭐ Basic SQL Queries")

expander = st.expander("SELECT FROM")
expander2 = st.expander("WHERE")
expander3 = st.expander("AND/OR/NOT")
expander4 = st.expander("ORDER BY")
expander5 = st.expander ("INSERT INTO")

expander.write("The SELECT statement is used to select data from a database.")
expander2.write("The WHERE clause is used to filter records.")
expander3.write("The AND, OR, and NOT operators are used to filter records based on more than one condition.")
expander4.write("The ORDER BY keyword is used to sort the result-set in ascending or descending order.")
expander5.write("The INSERT INTO statement is used to insert new records in a table.")
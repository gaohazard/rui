import streamlit as st
import pandas as pd

def vlookup(table_a, table_b, join_column):
    # Perform VLOOKUP operation
    merged_table = pd.merge(table_a, table_b, on=join_column, how='left')
    return merged_table

st.title("VLOOKUP Tool")

# Upload Table A
uploaded_file_a = st.file_uploader("Upload Table A", type=["csv", "xlsx"])
if uploaded_file_a is not None:
    try:
        table_a = pd.read_csv(uploaded_file_a, encoding='utf-8', skiprows=0)  # Adjust skiprows as needed
    except Exception as e:
        st.error("Error reading Table A. Please make sure the file format is correct.")
        st.stop()

# Upload Table B
uploaded_file_b = st.file_uploader("Upload Table B", type=["csv", "xlsx"])
if uploaded_file_b is not None:
    try:
        table_b = pd.read_csv(uploaded_file_b, encoding='utf-8', skiprows=0)  # Adjust skiprows as needed
    except Exception as e:
        st.error("Error reading Table B. Please make sure the file format is correct.")
        st.stop()

if uploaded_file_a is not None and uploaded_file_b is not None:
    join_column = st.selectbox("Select the join column", table_a.columns)

    if st.button("Perform VLOOKUP"):
        merged_table = vlookup(table_a, table_b, join_column)
        st.write("Merged Table:")
        st.write(merged_table)

import streamlit as st
from openpyxl import load_workbook

def vlookup(table_a, table_b, join_column):
    # Perform VLOOKUP operation
    merged_table = []
    for row_a in table_a.iter_rows(min_row=2, values_only=True):
        for row_b in table_b.iter_rows(min_row=2, values_only=True):
            if row_a[0] == row_b[0]:
                merged_table.append(row_a + row_b[1:])
    return merged_table

st.title("VLOOKUP Tool")

# Upload Table A
uploaded_file_a = st.file_uploader("Upload Table A", type=["xlsx"])
if uploaded_file_a is not None:
    try:
        workbook_a = load_workbook(uploaded_file_a)
        sheet_a = workbook_a.active
    except Exception as e:
        st.error("Error reading Table A. Please make sure the file format is correct.")
        st.stop()

# Upload Table B
uploaded_file_b = st.file_uploader("Upload Table B", type=["xlsx"])
if uploaded_file_b is not None:
    try:
        workbook_b = load_workbook(uploaded_file_b)
        sheet_b = workbook_b.active
    except Exception as e:
        st.error("Error reading Table B. Please make sure the file format is correct.")
        st.stop()

if uploaded_file_a is not None and uploaded_file_b is not None:
    join_column = st.selectbox("Select the join column", [cell.value for cell in sheet_a[1]])

    if st.button("Perform VLOOKUP"):
        merged_table = vlookup(sheet_a, sheet_b, join_column)
        st.write("Merged Table:")
        st.write(merged_table)

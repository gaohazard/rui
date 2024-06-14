import streamlit as st
from openpyxl import load_workbook, Workbook

def vlookup_and_merge(table_a, table_b, join_column):
    merged_table = []

    # Add header row to the merged table
    merged_table.append([cell.value for cell in table_a[1]] + [cell.value for cell in table_b[1]])

    # Merge the tables based on the join column
    for row_a in table_a.iter_rows(min_row=2, values_only=True):
        for row_b in table_b.iter_rows(min_row=2, values_only=True):
            if row_a[0] == row_b[0]:
                merged_row = list(row_a) + list(row_b[1:])
                merged_table.append(merged_row)

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
        merged_table = vlookup_and_merge(sheet_a, sheet_b, join_column)

        # Create a new workbook and sheet to store the merged table
        merged_workbook = Workbook()
        merged_sheet = merged_workbook.active

        # Write the merged table to the new sheet
        for row in merged_table:
            merged_sheet.append(row)

        # Remove duplicate columns
        seen = set()
        for cell in merged_sheet[1]:
            if cell.value in seen:
                cell.value = None
            else:
                seen.add(cell.value)

        # Save the merged table to a new Excel file
        merged_file_path = "merged_table.xlsx"
        merged_workbook.save(merged_file_path)

        st.write("Merged Table:")
        st.write(merged_table)
        st.write("Merged table saved to:", merged_file_path)

        # Provide a link to download the merged Excel file
        st.markdown(f"### [Download the merged table](./{merged_file_path})")


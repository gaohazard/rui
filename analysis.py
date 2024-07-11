import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to process CSV files
def process_csv_files(path, col1, col2):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    all_data_col1 = []
    all_data_col2 = []

    total_files = len(files)
    successful_reads = 0
    failed_reads = 0

    for file in files:
        try:
            df = pd.read_csv(os.path.join(path, file), skiprows=5, low_memory=False, encoding='gbk')
            column_names = df.columns

            if col1 in column_names and col2 in column_names:
                data_col1 = pd.to_numeric(df[col1], errors='coerce')
                data_col2 = pd.to_numeric(df[col2], errors='coerce')

                all_data_col1.extend(data_col1.dropna().tolist())
                all_data_col2.extend(data_col2.dropna().tolist())

            else:
                st.write(f"Columns '{col1}' and/or '{col2}' not found in file {file}")

            successful_reads += 1

        except Exception:
            try:
                df = pd.read_csv(os.path.join(path, file), skiprows=5, low_memory=False, encoding='ISO-8859-1')
                column_names = df.columns

                if col1 in column_names and col2 in column_names:
                    data_col1 = pd.to_numeric(df[col1], errors='coerce')
                    data_col2 = pd.to_numeric(df[col2], errors='coerce')

                    all_data_col1.extend(data_col1.dropna().tolist())
                    all_data_col2.extend(data_col2.dropna().tolist())

                else:
                    st.write(f"Columns '{col1}' and/or '{col2}' not found in file {file}")
                successful_reads += 1

            except Exception as e:
                st.write(f"Error processing file {file}: {str(e)}")
                failed_reads += 1

    return all_data_col1, all_data_col2

# Streamlit app
def main():
    st.title('CSV/XLSX File Processor and Plotter')

    uploaded_files = st.file_uploader("Upload your CSV/XLSX files", type=['csv', 'xlsx'], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            df = pd.read_csv(file)
            st.write(df)

    col1 = st.text_input("Enter column 1 name")
    col2 = st.text_input("Enter column 2 name")

    if st.button("Process Files"):
        all_data_col1, all_data_col2 = process_csv_files('.', col1, col2)

        # Generate plots
        plt.figure(figsize=(10, 6))
        plt.scatter(all_data_col1, all_data_col2)
        plt.xlabel(col1)
        plt.ylabel(col2)
        st.pyplot()

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
from datetime import datetime

# Define functions for data validation
def find_duplicates(df):
    """Return all rows that are exact duplicates."""
    return df[df.duplicated()]

def count_missing(df):
    """Return a Series of missing-or-empty counts per column."""
    return df.isnull().sum() + (df == "").sum()

def find_invalid_units(df, valid_units):
    """Return rows whose 'Unit' is not in the valid_units list."""
    return df[~df['Unit'].isin(valid_units)]

def find_invalid_dates(df, col_name):
    """Return rows whose date in col_name doesn’t match any of the accepted formats."""
    def is_valid(s):
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%Y.%m.%d"):
            try:
                datetime.strptime(str(s), fmt)
                return True
            except:
                continue
        return False
    mask = df[col_name].apply(is_valid)
    return df[~mask]

# Streamlit app starts here
st.title("Material Master Data Quality Dashboard")

# File uploader
uploaded = st.file_uploader("Upload Excel or CSV", type=["xlsx", "csv"])
if uploaded is not None:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded, engine="openpyxl")
else:
    st.info("Please upload a file to begin.")
    st.stop()

# Display raw data
st.subheader("Raw Data")
st.dataframe(df)

# Display duplicate rows
st.subheader("Duplicate Rows")
dups = find_duplicates(df)
st.write(f"Found {len(dups)} duplicates")
st.dataframe(dups)

# Display missing values per column
st.subheader("Missing Values per Column")
miss = count_missing(df)
st.bar_chart(miss)

# Display invalid unit types
st.subheader("Invalid Unit Types")
invalid_units = find_invalid_units(df, valid_units=['pcs', 'kg', 'liters'])
st.write(f"Found {len(invalid_units)} invalid units")
st.dataframe(invalid_units)

# Display invalid date formats
st.subheader("Invalid Date Formats")
invalid_dates = find_invalid_dates(df, 'Created Date')
st.write(f"Found {len(invalid_dates)} invalid dates")
st.dataframe(invalid_dates)

# Sidebar filter for Material Name
st.sidebar.header("Filter Options")
material_names = df['Material Name'].unique()
selected_material = st.sidebar.selectbox("Select Material Name", material_names, key="material_selectbox")

# Filtered data
filtered_df = df[df['Material Name'] == selected_material]
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Missing values in filtered data
st.subheader("Missing Values in Filtered Data")
st.write(filtered_df.isnull().sum())

# Duplicate records in filtered data
st.subheader("Duplicate Records in Filtered Data")
st.write(filtered_df[filtered_df.duplicated()])

# Download filtered data as CSV
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv',
)

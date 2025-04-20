import pandas as pd

# Read the Excel file
df = pd.read_excel('sample_material_data.xlsx', engine='openpyxl')

# Display the first few rows
print(df.head())

import pandas as pd

# 1) Read the Excel file
df = pd.read_excel('sample_material_data.xlsx', engine='openpyxl')
print("Raw data preview:")
print(df.head(), "\n")

# 2) Check for duplicates
print("Duplicate rows:")
duplicates = df[df.duplicated()]
print(duplicates, "\n")

# 3) Check for missing values
print("Missing values per column:")
missing = df.isnull().sum() + (df == "").sum()
print(missing, "\n")

# 4) Check for invalid units
valid_units = ['pcs', 'kg', 'liters']   # adjust to your allowed list
invalid_units = df[~df['Unit'].isin(valid_units)]
print("Rows with invalid units:")
print(invalid_units, "\n")

# 5) Check for date format mismatches
from datetime import datetime

def is_valid_date(s):
    for fmt in ("%Y-%m-%d","%d/%m/%Y","%Y/%m/%d","%d-%m-%Y","%Y.%m.%d"):
        try:
            datetime.strptime(str(s), fmt)
            return True
        except:
            continue
    return False

df['Valid Date?'] = df['Created Date'].apply(is_valid_date)
invalid_dates = df[df['Valid Date?']==False]
print("Rows with invalid date formats:")
print(invalid_dates, "\n")


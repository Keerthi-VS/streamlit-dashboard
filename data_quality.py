import pandas as pd

def check_duplicates(df):
    duplicates = df[df.duplicated()]
    return duplicates

def check_missing_values(df):
    missing = df.isnull().sum()
    return missing

def check_data_types(df):
    return df.dtypes

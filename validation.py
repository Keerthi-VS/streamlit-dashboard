# utils/validation.py
import pandas as pd
from datetime import datetime

def find_duplicates(df):
    return df[df.duplicated()]

def count_missing(df):
    return df.isnull().sum() + (df == "").sum()

def find_invalid_units(df, valid_units):
    return df[~df['Unit'].isin(valid_units)]

def find_invalid_dates(df, col_name):
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

# utils/data_processing.py
import pandas as pd

def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file, engine='openpyxl')

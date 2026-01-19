import pandas as pd
import os

def load_data(file_path):
    """Load CSV and preprocess"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV not found at {file_path}")
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['CustomerID'], inplace=True)
    df['TotalSum'] = df['Quantity'] * df['UnitPrice']
    return df

import pandas as pd

def calculate_rfm(df: pd.DataFrame, reference_date: str = '2011-12-10') -> pd.DataFrame:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    snapshot_date = pd.to_datetime(reference_date)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'count',
        'TotalSum': 'sum'
    }).rename(columns={'InvoiceDate': 'Recency',
                       'InvoiceNo': 'Frequency',
                       'TotalSum': 'Monetary'})
    return rfm

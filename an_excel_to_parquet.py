# create an object oriented python function that takes an excel file and turns it into a parquet file
import pandas as pd
# import pyarrow as pa
# import pyarrow.parquet as pq
import os

def excel_to_parquet(excel_file):
    df = pd.read_excel(excel_file)
    df.to_parquet('data.parquet')
    return df

if __name__ == '__main__':
    excel_to_parquet('data.xlsx')
    

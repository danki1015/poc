import pandas as pd

def merge(df, index):
    datagabung = pd.merge(df, index, left_on='regional', right_on='Regional Name', how='left')
    return datagabung
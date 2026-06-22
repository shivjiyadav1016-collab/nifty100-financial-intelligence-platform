import pandas as pd

def clean_nav(file_path):
    # load data
    df = pd.read_csv(file_path)

    # date convert
    df['date'] = pd.to_datetime(df['date'])

    # sort
    df = df.sort_values(['amfi_code', 'date'])

    # forward fill NAV
    df['nav'] = df.groupby('amfi_code')['nav'].ffill()

    # remove duplicates
    df = df.drop_duplicates()

    # remove invalid NAV
    df = df[df['nav'] > 0]

    return df
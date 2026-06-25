import pandas as pd


def convert_numeric_columns(df):

    for column in df.columns:

        try:
            df[column] = pd.to_numeric(df[column])

        except:
            pass

    return df
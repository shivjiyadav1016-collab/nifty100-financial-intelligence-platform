import pandas as pd


def clean_missing_values(df):
    """
    Fill missing values.
    """

    return df.fillna(0)


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """

    return df.drop_duplicates()
import pandas as pd


def check_missing_values(df):

    missing_values = df.isnull().sum()

    return missing_values[missing_values > 0]


def check_duplicates(df):

    return df.duplicated().sum()


def validate_primary_key(df, columns):

    return df.duplicated(subset=columns).sum()


def dataset_summary(df):

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(check_missing_values(df))

    print("\nDuplicate Rows:")
    print(check_duplicates(df))
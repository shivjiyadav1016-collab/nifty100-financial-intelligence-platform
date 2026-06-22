def normalize_column_names(df):
    """
    Normalize dataframe column names.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def normalize_company_id(df):
    """
    Normalize company_id values.
    """

    if "company_id" in df.columns:

        df["company_id"] = (
            df["company_id"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    return df


def normalize_year(df):
    """
    Normalize year values.
    """

    if "year" in df.columns:

        df["year"] = (
            df["year"]
            .astype(str)
            .str.strip()
        )

    return df


def normalize_dataframe(df):

    df = normalize_column_names(df)
    df = normalize_company_id(df)
    df = normalize_year(df)

    return df
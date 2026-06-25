import pandas as pd
from pathlib import Path

from normaliser import normalize_dataframe
from validator import dataset_summary

# Project root directory
ROOT_DIR = Path(__file__).resolve().parents[2]

# Raw data directory
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"

# Header mapping for each dataset
HEADER_MAP = {
    "companies.xlsx": 1,
    "profitandloss.xlsx": 1,
    "balancesheet.xlsx": 1,
    "cashflow.xlsx": 1,
    "analysis.xlsx": 1,
    "documents.xlsx": 1,
    "prosandcons.xlsx": 1,

    "sectors.xlsx": 0,
    "stock_prices.xlsx": 0,
    "market_cap.xlsx": 0,
    "peer_groups.xlsx": 0,
    "financial_ratios.xlsx": 0
}

# Dataset mapping
DATA_FILES = {
    "companies": "companies.xlsx",
    "profitandloss": "profitandloss.xlsx",
    "balancesheet": "balancesheet.xlsx",
    "cashflow": "cashflow.xlsx",
    "analysis": "analysis.xlsx",
    "documents": "documents.xlsx",
    "prosandcons": "prosandcons.xlsx",
    "sectors": "sectors.xlsx",
    "stock_prices": "stock_prices.xlsx",
    "market_cap": "market_cap.xlsx",
    "peer_groups": "peer_groups.xlsx",
    "financial_ratios": "financial_ratios.xlsx"
}


def load_excel(file_name):
    """
    Load and normalize a dataset.
    """

    file_path = RAW_DATA_DIR / file_name

    header_row = HEADER_MAP[file_name]

    try:
        df = pd.read_excel(
            file_path,
            header=header_row
        )

        df = normalize_dataframe(df)

        return df

    except Exception as e:
        print(f"\nError loading {file_name}")
        print(e)

        return None


# Dictionary to store datasets
datasets = {}

# Load all datasets
for dataset_name, file_name in DATA_FILES.items():

    datasets[dataset_name] = load_excel(file_name)

    if datasets[dataset_name] is not None:

        print("\n" + "=" * 60)
        print(dataset_name.upper())
        print("=" * 60)

        print("\nColumns:")
        print(datasets[dataset_name].columns)

        dataset_summary(datasets[dataset_name])

print("\nAll datasets loaded successfully.")
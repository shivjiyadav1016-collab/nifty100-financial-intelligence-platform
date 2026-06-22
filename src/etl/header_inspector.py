import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"

FILES = [
    "sectors.xlsx",
    "stock_prices.xlsx",
    "market_cap.xlsx",
    "peer_groups.xlsx",
    "financial_ratios.xlsx"
]

for file in FILES:

    print("\n" + "="*60)
    print(file)
    print("="*60)

    path = RAW_DATA_DIR / file

    df = pd.read_excel(path, header=None)

    print(df.head(10))
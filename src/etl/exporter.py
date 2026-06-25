from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"


def export_csv(df, file_name):

    output_path = PROCESSED_DATA_DIR / file_name

    df.to_csv(output_path, index=False)

    print(f"{file_name} exported successfully")
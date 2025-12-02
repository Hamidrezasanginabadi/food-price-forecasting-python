import pandas as pd
from pathlib import Path

def load_price_data(path: str = "data/sample_prices.csv") -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path.resolve()}")

    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df

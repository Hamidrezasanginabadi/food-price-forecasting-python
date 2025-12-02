import pandas as pd

def add_lag_features(df: pd.DataFrame, col="price", lags=(1, 2, 3)) -> pd.DataFrame:
    for lag in lags:
        df[f"{col}_lag{lag}"] = df[col].shift(lag)
    return df

def add_moving_average(df: pd.DataFrame, col="price", window=7) -> pd.DataFrame:
    df[f"{col}_ma{window}"] = df[col].rolling(window).mean()
    return df

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = add_lag_features(df)
    df = add_moving_average(df)
    df = df.dropna().reset_index(drop=True)
    return df

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_test_split_time(df: pd.DataFrame, target_col="price", test_size=30):
    train = df.iloc[:-test_size]
    test = df.iloc[-test_size:]

    feature_cols = [c for c in df.columns if c not in ("date", target_col)]

    X_train = train[feature_cols]
    y_train = train[target_col]

    X_test = test[feature_cols]
    y_test = test[target_col]

    return X_train, X_test, y_train, y_test, feature_cols

def train_and_evaluate(df: pd.DataFrame, target_col="price") -> dict:
    X_train, X_test, y_train, y_test, feature_cols = train_test_split_time(df, target_col)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    return {
        "model": model,
        "rmse": rmse,
        "y_test": y_test,
        "y_pred": y_pred,
        "feature_cols": feature_cols,
    }

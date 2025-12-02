import matplotlib.pyplot as plt
import pandas as pd

def plot_forecast(dates: pd.Series, y_true, y_pred):
    plt.figure()
    plt.plot(dates, y_true, label="Actual")
    plt.plot(dates, y_pred, label="Predicted")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Food Price Forecasting")
    plt.legend()
    plt.tight_layout()
    plt.show()

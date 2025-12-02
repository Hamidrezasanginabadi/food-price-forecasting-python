from src.data_loader import load_price_data
from src.features import build_features
from src.model import train_and_evaluate
from src.visualization import plot_forecast

def main():
    df = load_price_data()
    df_features = build_features(df)
    results = train_and_evaluate(df_features)

    print(f"RMSE: {results['rmse']:.2f}")
    dates = df_features["date"].iloc[-len(results["y_test"]):]
    plot_forecast(dates, results["y_test"], results["y_pred"])

if __name__ == "__main__":
    main()

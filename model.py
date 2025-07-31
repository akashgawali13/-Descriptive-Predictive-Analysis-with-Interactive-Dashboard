import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta

def train_and_predict(df, product_line, months=3):
    df = df[df["PRODUCTLINE"] == product_line].sort_values("ORDERDATE")
    df["DateOrdinal"] = df["ORDERDATE"].map(pd.Timestamp.toordinal)
    
    X = df["DateOrdinal"].values.reshape(-1, 1)
    y = df["SALES"].values

    model = LinearRegression()
    model.fit(X, y)

    last_date = df["ORDERDATE"].max()
    future_dates = [last_date + timedelta(days=30 * i) for i in range(1, months + 1)]
    future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
    future_sales = model.predict(future_ordinals)

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted_Sales": future_sales.astype(int)
    })
    return forecast_df

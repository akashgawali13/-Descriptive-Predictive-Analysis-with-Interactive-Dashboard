import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_and_predict

# Load data
df = pd.read_csv(
    r"E:\Project\Descriptive & Predictive Analysis with Interactive Dashboard\sales_data_sample.csv",
    encoding='latin1'
)
df.columns = df.columns.str.strip()  # Clean any whitespace

# Convert date column to datetime
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

st.title("📊 Sales Dashboard - Descriptive & Predictive Analysis")

# Sidebar Filters
product_filter = st.sidebar.multiselect(
    "Select Product Line", df["PRODUCTLINE"].unique(), default=df["PRODUCTLINE"].unique()
)
region_filter = st.sidebar.multiselect(
    "Select Country", df["COUNTRY"].unique(), default=df["COUNTRY"].unique()
)

# Filtered Data
filtered_df = df[
    (df["PRODUCTLINE"].isin(product_filter)) & (df["COUNTRY"].isin(region_filter))
]

# --- Descriptive Analysis ---
st.header("📌 Descriptive Statistics")
st.write(filtered_df.describe())

# --- Visualizations ---
st.header("📈 Monthly Sales Trends")

# Set ORDERDATE as datetime index
monthly_df = filtered_df.copy()
monthly_df.set_index("ORDERDATE", inplace=True)

# Resample monthly and sum sales per product line
monthly_sales = monthly_df.groupby("PRODUCTLINE").resample("M")["SALES"].sum().reset_index()

fig1 = px.line(
    monthly_sales,
    x="ORDERDATE",
    y="SALES",
    color="PRODUCTLINE",
    title="Monthly Sales Trend by Product Line"
)
st.plotly_chart(fig1)


st.header("🛍️ Total Sales by Product Line")
fig2 = px.bar(
    filtered_df.groupby("PRODUCTLINE")["SALES"].sum().reset_index(),
    x="PRODUCTLINE",
    y="SALES",
    color="PRODUCTLINE"
)
st.plotly_chart(fig2)

st.header("🌍 Sales Distribution by Country")
fig3 = px.pie(
    filtered_df,
    values="SALES",
    names="COUNTRY",
    title="Sales by Country"
)
st.plotly_chart(fig3)

# --- Predictive Analysis ---
st.header("🔮 Predict Future Sales")
selected_product = st.selectbox("Choose Product Line", df["PRODUCTLINE"].unique())
months = st.slider("Months to Predict", 1, 12, 3)

forecast_df = train_and_predict(df, selected_product, months)
st.subheader(f"Forecast for {selected_product}")
st.write(forecast_df)

fig4 = px.line(forecast_df, x="Date", y="Predicted_Sales", title=f"{selected_product} - Sales Forecast")
st.plotly_chart(fig4)

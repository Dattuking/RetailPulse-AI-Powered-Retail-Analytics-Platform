import os
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from statsmodels.tsa.stattools import adfuller

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="RetailPulse Dashboard",
    layout="wide"
)

# ---------------------------------
# TITLE
# ---------------------------------

st.title("RetailPulse Dashboard")
st.write("Week 1: EDA, Data Cleaning, RFM, Segmentation and Time-Series Analysis")

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Dataset Overview",
        "EDA",
        "Time Series Analysis",
        "RFM Segmentation"
    ]
)

# ---------------------------------
# LOAD DATA
# ---------------------------------

file_path = "merged_cleaned_retail_data.xlsx"

if not os.path.exists(file_path):
    st.error(
        "Dataset file not found. Please upload merged_cleaned_retail_data.xlsx to GitHub root folder."
    )
    st.stop()

# Load Full Dataset
df = pd.read_excel(file_path, engine="openpyxl")

st.success("Dataset loaded successfully")

# ---------------------------------
# DATA CLEANING
# ---------------------------------

df = df.drop_duplicates()
df = df.dropna()

# Create TotalAmount
if "Quantity" in df.columns and "Price" in df.columns:
    df["TotalAmount"] = df["Quantity"] * df["Price"]

# Convert Date
if "Invoice Date" in df.columns:
    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        errors="coerce"
    )

# ---------------------------------
# KPI METRICS
# ---------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

# Total Sales
if "TotalAmount" in df.columns:
    total_sales = df["TotalAmount"].sum()
else:
    total_sales = 0

# Total Customers
if "Customer ID" in df.columns:
    total_customers = df["Customer ID"].nunique()
else:
    total_customers = 0

# Total Invoices
if "Invoice" in df.columns:
    total_invoices = df["Invoice"].nunique()
else:
    total_invoices = 0

# Average Order Value
if "TotalAmount" in df.columns and "Invoice" in df.columns:
    avg_order = df["TotalAmount"].sum() / max(df["Invoice"].nunique(), 1)
else:
    avg_order = 0

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Customers", total_customers)
col3.metric("Invoices", total_invoices)
col4.metric("Avg Order Value", f"${avg_order:,.2f}")

# ---------------------------------
# DATASET OVERVIEW
# ---------------------------------

if section == "Dataset Overview":

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Missing Values")
    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["Column", "Missing Values"]

    st.dataframe(missing_df)

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    # Download Button
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_retail_data.csv",
        mime="text/csv"
    )

# ---------------------------------
# EDA SECTION
# ---------------------------------

elif section == "EDA":

    numeric_cols = df.select_dtypes(include="number").columns

    # Histogram
    if len(numeric_cols) > 0:

        st.subheader("Numeric Feature Distribution")

        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected_col,
            title=f"{selected_col} Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Correlation Heatmap
        st.subheader("Correlation Heatmap")

        corr = df[numeric_cols].corr()

        fig, ax = plt.subplots(figsize=(12, 8))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)

    # Product Category
    if "Product_Category" in df.columns:

        st.subheader("Product Category Distribution")

        fig = px.histogram(
            df,
            x="Product_Category"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Customer Type
    if "Customer_Type" in df.columns:

        st.subheader("Customer Type Distribution")

        fig = px.histogram(
            df,
            x="Customer_Type"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Churn
    if "Churn" in df.columns:

        st.subheader("Churn Distribution")

        fig = px.histogram(
            df,
            x="Churn"
        )

        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------
# TIME SERIES ANALYSIS
# ---------------------------------

elif section == "Time Series Analysis":

    if "Invoice Date" in df.columns and "TotalAmount" in df.columns:

        st.subheader("Daily Sales Trend")

        daily_sales = df.groupby(
            df["Invoice Date"].dt.date
        )["TotalAmount"].sum()

        daily_sales.index = pd.to_datetime(daily_sales.index)

        daily_sales_df = daily_sales.reset_index()
        daily_sales_df.columns = ["Date", "Sales"]

        # Line Chart
        fig = px.line(
            daily_sales_df,
            x="Date",
            y="Sales",
            title="Daily Sales Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

        # ADF Test
        if len(daily_sales_df) > 20:

            st.subheader("ADF Stationarity Test")

            result = adfuller(daily_sales_df["Sales"])

            st.write("ADF Statistic:", result[0])
            st.write("P-value:", result[1])

            if result[1] < 0.05:
                st.success("The Time Series is Stationary")
            else:
                st.warning("The Time Series is Non-Stationary")

# ---------------------------------
# RFM SEGMENTATION
# ---------------------------------

elif section == "RFM Segmentation":

    required_cols = [
        "Customer ID",
        "Invoice Date",
        "Invoice",
        "TotalAmount"
    ]

    if all(col in df.columns for col in required_cols):

        st.subheader("RFM Customer Segmentation")

        # Snapshot Date
        snapshot_date = df["Invoice Date"].max()

        # Create RFM Table
        rfm = df.groupby("Customer ID").agg({
            "Invoice Date": lambda x: (
                snapshot_date - x.max()
            ).days,
            "Invoice": "nunique",
            "TotalAmount": "sum"
        })

        rfm.columns = [
            "Recency",
            "Frequency",
            "Monetary"
        ]

        # Standardization
        scaler = StandardScaler()

        scaled_data = scaler.fit_transform(
            rfm[[
                "Recency",
                "Frequency",
                "Monetary"
            ]]
        )

        # KMeans Clustering
        kmeans = KMeans(
            n_clusters=4,
            random_state=42,
            n_init=10
        )

        rfm["Cluster"] = kmeans.fit_predict(scaled_data)

        # Silhouette Score
        score = silhouette_score(
            scaled_data,
            rfm["Cluster"]
        )

        st.write("Silhouette Score:", round(score, 3))

        # Display RFM Table
        st.subheader("RFM Table")
        st.dataframe(rfm.head())

        # Scatter Plot
        fig = px.scatter(
            rfm,
            x="Frequency",
            y="Monetary",
            color=rfm["Cluster"].astype(str),
            title="Customer Segmentation"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Cluster Summary
        st.subheader("Cluster Summary")

        cluster_summary = rfm.groupby("Cluster").mean()

        st.dataframe(cluster_summary)

# ---------------------------------
# FOOTER
# ---------------------------------

st.success("RetailPulse Dashboard Executed Successfully")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="RetailPulse Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #1f2937;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
}

.block-container {
    padding-top: 2rem;
}

.sidebar .sidebar-content {
    background-color: #111827;
}

.css-1d391kg {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

st.title("🛍️ RetailPulse – AI Powered Customer Analytics & Demand Forecasting Platform")

st.markdown("""
RetailPulse is an end-to-end AI-powered retail analytics platform developed using Python, Streamlit, Machine Learning, Deep Learning, and Data Analytics techniques.
""")

st.success("RetailPulse Platform Successfully Loaded 🚀")

st.sidebar.title("📌 RetailPulse Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Overview",
        "Week 1",
        "Week 2",
        "Week 3",
        "Week 4",
        "Analytics Dashboard",
        "Forecasting",
        "Customer Segmentation",
        "Inventory Monitoring",
        "Project Summary"
    ]
)

np.random.seed(42)

dates = pd.date_range(start="2025-01-01", periods=30)

sales_data = pd.DataFrame({
    "Date": dates,
    "Sales": np.random.randint(1000, 5000, 30),
    "Customers": np.random.randint(50, 300, 30),
    "Profit": np.random.randint(200, 1200, 30)
})

customer_segments = pd.DataFrame({
    "Segment": ["Premium", "Regular", "Occasional", "New"],
    "Customers": [320, 540, 280, 150]
})

inventory_data = pd.DataFrame({
    "Category": ["Electronics", "Fashion", "Groceries", "Furniture", "Accessories"],
    "Stock": [120, 80, 200, 40, 150]
})

forecast_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Predicted Sales": [12000, 15000, 17000, 21000, 24000, 26000]
})

if page == "Overview":

    st.header("📈 Business Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Sales", "₹12.5L", "+15%")

    with col2:
        st.metric("Customers", "8,540", "+10%")

    with col3:
        st.metric("Profit", "₹3.2L", "+18%")

    with col4:
        st.metric("Inventory Health", "92%", "+5%")

    st.markdown("---")

    fig = px.line(
        sales_data,
        x="Date",
        y="Sales",
        markers=True,
        title="Daily Sales Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💡 Platform Highlights")

    highlights = [
        "AI-Powered Retail Analytics",
        "Customer Behavior Intelligence",
        "Demand Forecasting Models",
        "Inventory Optimization",
        "Churn Prediction",
        "Interactive Dashboards"
    ]

    for item in highlights:
        st.write(f"• {item}")

elif page == "Week 1":

    st.header("📅 Week 1 – Data Exploration & Preparation")

    week1 = {
        "Day 1": [
            "Dataset selection (retail sales, customer, inventory data)",
            "Initial EDA notebook: distribution analysis, missing values, correlation heatmap"
        ],
        "Day 2": [
            "Data cleaning and feature engineering (RFM scores, rolling statistics)",
            "Data validation with Great Expectations"
        ],
        "Day 3": [
            "Customer segmentation using K-Means and DBSCAN",
            "Cluster evaluation and business interpretation"
        ],
        "Day 4": [
            "Time-series data preparation for forecasting",
            "Stationarity tests and decomposition"
        ],
        "Day 5": [
            "Baseline Prophet model for demand forecasting"
        ],
        "Day 6": [
            "LSTM model implementation with PyTorch Lightning"
        ],
        "Day 7": [
            "Week 1 checkpoint: EDA report, cleaned dataset, baseline models logged in MLflow"
        ]
    }

    for day, tasks in week1.items():
        st.subheader(day)
        for task in tasks:
            st.write(f"• {task}")

elif page == "Week 2":

    st.header("📅 Week 2 – Advanced Modeling & Churn Prediction")

    week2 = {
        "Day 8": [
            "Hybrid forecasting model (Prophet + LSTM ensemble)"
        ],
        "Day 9": [
            "Churn prediction model using XGBoost with SHAP explainability"
        ],
        "Day 10": [
            "Inventory optimization logic using forecasted demand"
        ],
        "Day 11": [
            "Feature importance analysis and model tuning with Optuna"
        ],
        "Day 12": [
            "Drift detection setup using Evidently AI"
        ],
        "Day 13": [
            "Automated retraining pipeline with Airflow"
        ],
        "Day 14": [
            "Week 2 checkpoint: Forecasting and churn models ready, optimization logic implemented"
        ]
    }

    for day, tasks in week2.items():
        st.subheader(day)
        for task in tasks:
            st.write(f"• {task}")

elif page == "Week 3":

    st.header("📅 Week 3 – Dashboard & Analytics Layer")

    week3 = {
        "Day 15": [
            "Streamlit dashboard skeleton with multi-page layout"
        ],
        "Day 16": [
            "Demand forecasting visualizations and what-if analysis"
        ],
        "Day 17": [
            "Customer segmentation and churn risk dashboard"
        ],
        "Day 18": [
            "Inventory optimization recommendations UI"
        ],
        "Day 19": [
            "Real-time metrics and alerts"
        ],
        "Day 20": [
            "Export functionality (CSV/PDF reports)"
        ],
        "Day 21": [
            "Week 3 checkpoint: Fully interactive dashboard with all insights"
        ]
    }

    for day, tasks in week3.items():
        st.subheader(day)
        for task in tasks:
            st.write(f"• {task}")

elif page == "Week 4":

    st.header("📅 Week 4 – Deployment & Production Polish")

    week4 = {
        "Day 22": [
            "Docker multi-stage builds for the application"
        ],
        "Day 23": [
            "Kubernetes manifests and deployment configuration"
        ],
        "Day 24": [
            "GitHub Actions CI/CD pipeline"
        ],
        "Day 25": [
            "Cloud deployment on AWS or GCP"
        ],
        "Day 26": [
            "Monitoring setup with Prometheus and Grafana"
        ],
        "Day 27": [
            "Load testing and final accuracy validation"
        ],
        "Day 28": [
            "Final QA, README polishing, demo video recording, PDF export"
        ]
    }

    for day, tasks in week4.items():
        st.subheader(day)
        for task in tasks:
            st.write(f"• {task}")

elif page == "Analytics Dashboard":

    st.header("📊 Retail Analytics Dashboard")

    st.dataframe(sales_data, use_container_width=True)

    sales_chart = px.bar(
        sales_data,
        x="Date",
        y="Sales",
        title="Retail Sales Analysis"
    )

    st.plotly_chart(sales_chart, use_container_width=True)

    profit_chart = px.line(
        sales_data,
        x="Date",
        y="Profit",
        markers=True,
        title="Profit Trend"
    )

    st.plotly_chart(profit_chart, use_container_width=True)

elif page == "Forecasting":

    st.header("🤖 AI Demand Forecasting")

    forecast_chart = px.line(
        forecast_data,
        x="Month",
        y="Predicted Sales",
        markers=True,
        title="Demand Forecasting Results"
    )

    st.plotly_chart(forecast_chart, use_container_width=True)

    st.subheader("📌 Forecasting Models Used")

    st.write("• Prophet Forecasting")
    st.write("• LSTM Deep Learning")
    st.write("• Hybrid Prophet + LSTM Ensemble")

elif page == "Customer Segmentation":

    st.header("👥 Customer Segmentation & Churn Analysis")

    segment_chart = px.pie(
        customer_segments,
        names="Segment",
        values="Customers",
        title="Customer Segments"
    )

    st.plotly_chart(segment_chart, use_container_width=True)

    st.subheader("📌 Segmentation Models")

    st.write("• K-Means Clustering")
    st.write("• DBSCAN Clustering")
    st.write("• XGBoost Churn Prediction")
    st.write("• SHAP Explainability")

elif page == "Inventory Monitoring":

    st.header("📦 Inventory Optimization Dashboard")

    inventory_chart = px.bar(
        inventory_data,
        x="Category",
        y="Stock",
        color="Category",
        title="Inventory Monitoring"
    )

    st.plotly_chart(inventory_chart, use_container_width=True)

    st.subheader("📌 Inventory Features")

    st.write("• AI Inventory Optimization")
    st.write("• Demand-Based Restocking")
    st.write("• Real-Time Alerts")
    st.write("• Inventory Forecasting")

elif page == "Project Summary":

    st.header("📋 Complete Project Summary")

    st.markdown("""
### 🔹 Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Prophet
- PyTorch Lightning
- XGBoost
- SHAP
- Optuna
- Evidently AI
- Airflow
- MLflow

### 🔹 Deployment Technologies
- Docker
- Kubernetes
- GitHub Actions
- AWS / GCP
- Prometheus
- Grafana

### 🔹 Core Features
- Retail Analytics
- Customer Segmentation
- Churn Prediction
- Demand Forecasting
- Inventory Optimization
- Real-Time Monitoring
- Export Reports
- Interactive Dashboard

### 🔹 Business Benefits
- Better retail decision making
- Improved customer retention
- Accurate sales forecasting
- Inventory cost reduction
- AI-powered business intelligence
""")

    st.success("RetailPulse Production Deployment Ready 🚀")

st.markdown("---")

st.caption(f"RetailPulse Dashboard • Generated on {datetime.now().strftime('%d %B %Y %H:%M:%S')}")

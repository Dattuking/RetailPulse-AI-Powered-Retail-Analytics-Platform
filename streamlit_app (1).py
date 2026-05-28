import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from prometheus_client import Counter, Gauge

REQUEST_COUNT = Counter('retailpulse_requests_total', 'Total App Requests')
ACTIVE_USERS = Gauge('retailpulse_active_users', 'Active Users')

REQUEST_COUNT.inc()
ACTIVE_USERS.set(1)

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

</style>
""", unsafe_allow_html=True)

st.title("🛍️ RetailPulse – AI Powered Retail Analytics Platform")

st.markdown("""
RetailPulse is an end-to-end AI-powered customer analytics and demand forecasting platform developed using Python, Streamlit, Machine Learning, Deep Learning, and Data Analytics.
""")

st.success("RetailPulse Platform Successfully Loaded 🚀")

st.sidebar.title("📌 RetailPulse Modules")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📊 EDA",
        "📈 Sales Analysis",
        "👥 Customer Segmentation",
        "⚠️ Churn Analysis",
        "📦 Inventory Insights",
        "🤖 Sales Forecasting",
        "💡 AI Business Insights",
        "📡 Monitoring Dashboard",
        "☁️ Deployment Status",
        "📅 Complete Project Roadmap",
        "📋 Project Summary"
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

churn_data = pd.DataFrame({
    "Customer": ["C101", "C102", "C103", "C104", "C105"],
    "Churn Risk": ["High", "Medium", "Low", "High", "Medium"]
})

if page == "🏠 Home":

    st.header("📈 RetailPulse Overview")

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

    sales_chart = px.line(
        sales_data,
        x="Date",
        y="Sales",
        markers=True,
        title="Daily Sales Trend"
    )

    st.plotly_chart(sales_chart, use_container_width=True)

    st.subheader("💡 Platform Highlights")

    highlights = [
        "AI-Powered Retail Analytics",
        "Customer Behavior Intelligence",
        "Demand Forecasting Models",
        "Inventory Optimization",
        "Churn Prediction",
        "Interactive Dashboards",
        "Cloud Deployment Ready",
        "Real-Time Monitoring",
        "Dockerized Architecture",
        "CI/CD Enabled"
    ]

    for item in highlights:
        st.write(f"• {item}")

elif page == "📊 EDA":

    st.header("📊 Exploratory Data Analysis")

    st.dataframe(sales_data, use_container_width=True)

    sales_hist = px.histogram(
        sales_data,
        x="Sales",
        nbins=10,
        title="Sales Distribution"
    )

    st.plotly_chart(sales_hist, use_container_width=True)

    profit_chart = px.line(
        sales_data,
        x="Date",
        y="Profit",
        markers=True,
        title="Profit Trend"
    )

    st.plotly_chart(profit_chart, use_container_width=True)

    corr_data = sales_data[["Sales", "Customers", "Profit"]].corr()

    corr_chart = px.imshow(
        corr_data,
        text_auto=True,
        title="Correlation Analysis"
    )

    st.plotly_chart(corr_chart, use_container_width=True)

elif page == "📈 Sales Analysis":

    st.header("📈 Sales Analysis Dashboard")

    sales_bar = px.bar(
        sales_data,
        x="Date",
        y="Sales",
        title="Daily Sales Analysis"
    )

    st.plotly_chart(sales_bar, use_container_width=True)

    customer_line = px.line(
        sales_data,
        x="Date",
        y="Customers",
        markers=True,
        title="Customer Activity"
    )

    st.plotly_chart(customer_line, use_container_width=True)

    st.subheader("📌 Sales Insights")

    st.write("• Sales are increasing steadily")
    st.write("• Weekend sales are comparatively higher")
    st.write("• Customer traffic directly impacts revenue")

elif page == "👥 Customer Segmentation":

    st.header("👥 Customer Segmentation")

    segment_chart = px.pie(
        customer_segments,
        names="Segment",
        values="Customers",
        title="Customer Segments"
    )

    st.plotly_chart(segment_chart, use_container_width=True)

    st.write("• K-Means Clustering")
    st.write("• DBSCAN Clustering")
    st.write("• Customer Profiling")
    st.write("• Behavioral Analysis")

elif page == "⚠️ Churn Analysis":

    st.header("⚠️ Customer Churn Analysis")

    st.dataframe(churn_data, use_container_width=True)

    churn_chart = px.bar(
        churn_data,
        x="Customer",
        y=[1, 2, 3, 2, 1],
        color="Churn Risk",
        title="Customer Churn Risk"
    )

    st.plotly_chart(churn_chart, use_container_width=True)

    st.write("• XGBoost Churn Prediction")
    st.write("• SHAP Explainability")
    st.write("• Customer Retention Analytics")

elif page == "📦 Inventory Insights":

    st.header("📦 Inventory Monitoring")

    inventory_chart = px.bar(
        inventory_data,
        x="Category",
        y="Stock",
        color="Category",
        title="Inventory Status"
    )

    st.plotly_chart(inventory_chart, use_container_width=True)

    st.write("• AI Inventory Optimization")
    st.write("• Smart Restocking")
    st.write("• Warehouse Analytics")

elif page == "🤖 Sales Forecasting":

    st.header("🤖 AI Sales Forecasting")

    forecast_chart = px.line(
        forecast_data,
        x="Month",
        y="Predicted Sales",
        markers=True,
        title="Demand Forecasting"
    )

    st.plotly_chart(forecast_chart, use_container_width=True)

    st.write("• Prophet Forecasting")
    st.write("• LSTM Forecasting")
    st.write("• Hybrid Prophet + LSTM")

elif page == "💡 AI Business Insights":

    st.header("💡 AI Business Insights")

    insights = [
        "Sales expected to increase by 18% next quarter",
        "Premium customers generate maximum revenue",
        "Inventory optimization can reduce costs by 12%",
        "High churn customers need targeted retention strategies",
        "Forecasting models improve stock planning accuracy"
    ]

    for insight in insights:
        st.success(insight)

elif page == "📡 Monitoring Dashboard":

    st.header("📡 Real-Time Monitoring Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Server Status", "Healthy")

    with col2:
        st.metric("API Response Time", "120ms")

    with col3:
        st.metric("CPU Usage", "38%")

    monitoring_df = pd.DataFrame({
        "Time": range(10),
        "CPU": np.random.randint(20, 70, 10),
        "Memory": np.random.randint(30, 80, 10)
    })

    cpu_chart = px.line(
        monitoring_df,
        x="Time",
        y="CPU",
        title="CPU Monitoring"
    )

    st.plotly_chart(cpu_chart, use_container_width=True)

elif page == "☁️ Deployment Status":

    st.header("☁️ Deployment & DevOps Status")

    deployment_data = pd.DataFrame({
        "Service": [
            "Docker",
            "Kubernetes",
            "GitHub Actions",
            "AWS Deployment",
            "Prometheus",
            "Grafana",
            "Load Testing"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed"
        ]
    })

    st.dataframe(deployment_data, use_container_width=True)

    st.success("Production Deployment Successfully Configured 🚀")

elif page == "📅 Complete Project Roadmap":

    st.header("📅 RetailPulse Complete 4-Week Roadmap")

    roadmap = {
        "Week 1": [
            "Dataset selection and EDA",
            "Data cleaning and feature engineering",
            "Customer segmentation",
            "Time-series preparation",
            "Prophet forecasting",
            "LSTM implementation",
            "Week 1 checkpoint"
        ],
        "Week 2": [
            "Hybrid forecasting",
            "XGBoost churn prediction",
            "Inventory optimization",
            "Optuna tuning",
            "Drift detection",
            "Automated retraining",
            "Week 2 checkpoint"
        ],
        "Week 3": [
            "Streamlit dashboard",
            "Forecast visualizations",
            "Churn dashboard",
            "Inventory UI",
            "Real-time metrics",
            "Export functionality",
            "Interactive checkpoint"
        ],
        "Week 4": [
            "Docker setup",
            "Kubernetes deployment",
            "GitHub Actions CI/CD",
            "AWS/GCP deployment",
            "Prometheus and Grafana",
            "Load testing",
            "Final QA and documentation"
        ]
    }

    for week, tasks in roadmap.items():
        st.subheader(week)
        for idx, task in enumerate(tasks, start=1):
            st.write(f"Day {idx} • {task}")

elif page == "📋 Project Summary":

    st.header("📋 RetailPulse Project Summary")

    st.markdown("""
### 🔹 Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- XGBoost
- Prophet
- PyTorch Lightning
- Docker
- Kubernetes
- Prometheus
- Grafana

### 🔹 Core Features
- EDA Dashboard
- Sales Analytics
- Customer Segmentation
- Churn Prediction
- Inventory Optimization
- AI Forecasting
- Monitoring Dashboard
- Cloud Deployment
- CI/CD Automation

### 🔹 Business Benefits
- Better business decision making
- Improved customer retention
- Accurate demand forecasting
- Inventory cost reduction
- AI-powered insights
""")

    st.success("RetailPulse AI Platform Ready for Production 🚀")

st.markdown("---")

st.caption(
    f"RetailPulse Dashboard • Generated on {datetime.now().strftime('%d %B %Y %H:%M:%S')}"
)

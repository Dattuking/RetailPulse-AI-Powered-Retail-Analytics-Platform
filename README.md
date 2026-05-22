# RetailPulse Dashboard

RetailPulse Dashboard is an advanced retail analytics and machine learning dashboard built using Streamlit. The project provides end-to-end retail data analysis, customer segmentation, forecasting, churn prediction, inventory optimization, and model monitoring capabilities.

---

# Features

## Data Analysis
- Dataset preview
- Missing value analysis
- Summary statistics
- Correlation heatmap
- Product category analysis
- Customer type analysis
- Churn distribution analysis

## Time Series Analysis
- Daily sales trend visualization
- Stationarity testing using ADF Test
- Sales forecasting using Prophet

## Customer Segmentation
- RFM Analysis
- K-Means clustering
- Customer segmentation visualization

## Machine Learning
- Churn prediction using:
  - XGBoost
  - Random Forest
- Feature importance analysis
- SHAP explainability

## Inventory Optimization
- Recommended stock prediction
- Inventory visualization

## Hyperparameter Tuning
- Automated tuning using Optuna

## Drift Detection
- Model monitoring dashboard
- Data drift status tracking

## Automated Retraining Pipeline
- Pipeline execution monitoring
- Deployment stage visualization

---

# Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-Learn
- Prophet
- XGBoost
- SHAP
- Optuna
- Seaborn
- Matplotlib

---

# Project Structure

```bash
RetailPulse/
│
├── streamlit_app.py
├── merged_cleaned_retail_data.xlsx
├── requirements.txt
└── README.md

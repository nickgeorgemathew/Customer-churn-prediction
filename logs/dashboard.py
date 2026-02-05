import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy import create_engine,inspect
from db import engine

# Resolve path to logs.db in the same directory as dashboard.py
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "logs.db"

inspector = inspect(engine)
print("DASHBOARD DB PATH:", DB_PATH.resolve())

if "predictionlogs" not in inspector.get_table_names():
    st.warning("Prediction logs table not found yet. Waiting for inference data...")
    st.stop()

df = pd.read_sql("SELECT * FROM predictionlogs", engine)
if df["timestamp"].dtype == "object":
    df["timestamp"] = pd.to_datetime(df["timestamp"])  # Convert to datetime if needed




st.title(" Customer Churn Model Monitoring")
st.caption("Model version: v1.0 | Real-time inference analytics")

if df.empty:
    st.warning("No prediction logs available yet.")
    st.stop()

total_requests = len(df)
churn_rate = (df["prediction"] == 1).mean() * 100
avg_latency = df["latency_ms"].mean()
error_rate = df["error"].notna().mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Predictions", total_requests)
col2.metric("Predicted Churn (%)", f"{churn_rate:.2f}")
col3.metric("Avg Latency (ms)", f"{avg_latency:.1f}")
col4.metric("Error Rate (%)", f"{error_rate:.2f}")

st.divider()



st.subheader("📈 Prediction Distribution")

pred_counts = df["prediction"].value_counts().rename(
    {0: "No Churn", 1: "Churn"}
)
st.bar_chart(pred_counts)

st.divider()



st.subheader("⚠️ High-Risk Customers (Confidence > 0.8)")

high_risk = df[
    (df["prediction"] == 1) & (df["probability"] >= 0.8)
][["timestamp", "probability", "input_features"]]

st.dataframe(high_risk, use_container_width=True)

st.divider()

#latency monitoring
st.subheader("⏱ Latency Monitoring")
period = st.selectbox(
    "Choose comparison period",
    ["Yesterday", "Last 7 Days", "Last 30 Days", "Custom Range"]
)

today = pd.Timestamp.today().normalize()

if period == "Yesterday":
    start_date = today - pd.Timedelta(days=1)
   
    compare_df = df[(df["timestamp"].dt.date == start_date.date())]

elif period == "Last 7 Days":
    start_date = today - pd.Timedelta(days=7)
    end_date = today
    compare_df = df[(df["timestamp"] >= start_date) & (df["timestamp"] < end_date)]

elif period == "Last 30 Days":
    start_date = today - pd.Timedelta(days=30)
    end_date = today
    compare_df = df[(df["timestamp"] >= start_date) & (df["timestamp"] < end_date)]

elif period == "Custom Range":
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
    compare_df = df[(df["timestamp"].dt.date >= start_date) & (df["timestamp"].dt.date <= end_date)]

# Current metrics (e.g., today)
current_df = df[df["timestamp"].dt.date == today.date()]

current_churn = (current_df["prediction"] == 1).mean() * 100
current_latency = current_df["latency_ms"].mean()
current_error = current_df["error"].notna().mean() * 100
current_total = len(current_df)

# Comparison metrics
compare_churn = (compare_df["prediction"] == 1).mean() * 100
compare_latency = compare_df["latency_ms"].mean()
compare_error = compare_df["error"].notna().mean() * 100
compare_total = len(compare_df)




col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Predictions", current_total, delta=current_total - compare_total)
col2.metric("Predicted Churn (%)", f"{current_churn:.2f}", delta=f"{current_churn - compare_churn:.2f}%")
col3.metric("Avg Latency (ms)", f"{current_latency:.1f}", delta=f"{current_latency - compare_latency:.1f}")
col4.metric("Error Rate (%)", f"{current_error:.2f}", delta=f"{current_error - compare_error:.2f}%")


st.subheader(" Failed Requests")
errors = df[df["error"].notna()][
    ["timestamp", "error", "input_features"]
]

if errors.empty:
    st.success("No failed requests ")
else:
    st.dataframe(errors, use_container_width=True)
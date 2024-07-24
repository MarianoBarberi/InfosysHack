import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

def dash():
    st.title("Fraud Detection Dashboard")
    st.sidebar.header("Filters")
    date_range = st.sidebar.date_input("Date Range", [datetime.now() - timedelta(days=30), datetime.now()])

    # Calculate the number of hours between start and end date
    hours_diff = int((date_range[1] - date_range[0]).total_seconds() / 3600) + 1

    # Main content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Transaction History")
        # Simulated data - replace with actual data source
        df = pd.DataFrame({
            "Date/Time": pd.date_range(start=date_range[0], end=date_range[1], freq="H"),
            "Transaction ID": range(1000, 1000 + hours_diff),
            "Amount": np.random.randint(10, 1000, hours_diff),
            "Merchant": np.random.choice(["Amazon", "Walmart", "Target", "Best Buy"], hours_diff),
            "Status": np.random.choice(["Accepted", "Rejected"], hours_diff, p=[0.95, 0.05])
        })
        st.dataframe(df)

    with col2:
        st.subheader("Fraud Detection Statistics")
        total = len(df)
        accepted = len(df[df["Status"] == "Accepted"])
        rejected = len(df[df["Status"] == "Rejected"])
        
        st.metric("Total Transactions", total)
        st.metric("Accepted Transactions", f"{accepted} ({accepted/total:.2%})")
        st.metric("Rejected Transactions", f"{rejected} ({rejected/total:.2%})")
        st.metric("Fraud Detection Rate", f"{rejected/total:.2%}")


    st.subheader("Top Merchants by Transaction Volume")
    merchant_volume = df.groupby("Merchant")["Amount"].sum().sort_values(ascending=False)
    fig = px.bar(merchant_volume, x=merchant_volume.index, y="Amount")
    st.plotly_chart(fig, use_container_width=True)

    # System Performance Metrics
    st.subheader("System Performance Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Response Time", "50 ms")
    col2.metric("System Uptime", "99.99%")
    col3.metric("False Positive Rate", "2.3%")

    # User Activity Log
    st.subheader("User Activity Log")
    activity_log = [
        "User 'jsmith' reviewed transaction #1234",
        "User 'aharris' updated rule #56",
        "User 'mwilson' exported monthly report"
    ]

    for activity in activity_log:
        st.text(activity)
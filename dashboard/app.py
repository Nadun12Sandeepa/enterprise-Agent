import streamlit as st
import pandas as pd
import json

st.title("AI Trading Dashboard")

try:

    trades = []

    with open("logs/trades.json", "r") as f:

        for line in f:
            trades.append(json.loads(line))

    df = pd.DataFrame(trades)

    st.dataframe(df)

except:
    st.warning("No trades yet.")
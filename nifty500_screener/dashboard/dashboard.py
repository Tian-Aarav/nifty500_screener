import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Nifty 500 Screener", layout="wide")

st.title("📈 Nifty 500 Daily Screener")
st.markdown("This dashboard shows the latest **Buy/Sell/Hold** signals with key technical metrics.")

data_path = "exports/final_screener.csv"

if os.path.exists(data_path):
    df = pd.read_csv(data_path)

    st.sidebar.header("Filters")
    signal_filter = st.sidebar.multiselect("Signal", options=["BUY", "SELL", "HOLD"], default=["BUY", "SELL", "HOLD"])
    df_filtered = df[df['Signal'].isin(signal_filter)]

    st.dataframe(df_filtered, use_container_width=True)

    st.download_button("📥 Download CSV", df_filtered.to_csv(index=False), "nifty500_screen.csv")

else:
    st.error("No data file found. Please run `main.py` first to generate today's data.")
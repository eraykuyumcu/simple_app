import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
### Simple Stock Price APP

""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2010-05-31", end="2021-5-31")

st.line_chart(tickerDf.Open)

st.write("""
    ### Google Volume Historical Data
""")
st.dataframe(tickerDf.Volume)




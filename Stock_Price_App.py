import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

ALPHA_VANTAGE_API_KEY = 'MJLJ13IWEBI9YCIK'  

def fetch_stock_data(symbol, start_date, end_date):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    data = data.loc[start_date:end_date]
    return data

st.title("Stock Price Visualization App")

ticker = st.text_input("Enter Stock Ticker:", "AAPL")

start_date = st.date_input("Start Date", pd.to_datetime('2022-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('2023-01-01'))

if ticker:
    st.write(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    try:
        stock_data = fetch_stock_data(ticker, start_date, end_date)
        st.write(stock_data)

        fig, ax = plt.subplots()
        ax.plot(stock_data.index, stock_data['4. close'], label='Close Price')
        ax.set_xlabel("Date")
        ax.set_ylabel("Close Price")
        ax.legend()
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error fetching data: {e}")

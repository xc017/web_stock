import yfinance as yf
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stock Price App", layout="wide")
st.title("Stock Price App")
st.write("This app retrieves stock prices from Yahoo Finance.")
st.sidebar.header("User Input")
st.sidebar.write("Select the stock symbol and date range to view the stock prices.")
# Sidebar inputs
stock_symbol = st.sidebar.text_input("Stock Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))
# Validate date inputs
if start_date > end_date:
    st.sidebar.error("Start date must be before end date.")
# Fetch stock data
@st.cache_data
def fetch_stock_data(symbol, start, end):
    try:
        data = yf.download(symbol, start=start, end=end)
        if data.empty:
            st.error("No data found for the given stock symbol and date range.")
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None
# Fetch data
data = fetch_stock_data(stock_symbol, start_date, end_date)
if data is not None:
    # Display stock data
    st.subheader(f"Stock Data for {stock_symbol}")
    st.write(data)
    # Plot stock prices
    st.subheader("Stock Price Chart")
    st.line_chart(data['Close'])
    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())
    # Download data as CSV
    st.subheader("Download Data")
    csv = data.to_csv().encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"{stock_symbol}_stock_data.csv",
        mime="text/csv",
    )
# Footer
st.sidebar.write("Developed by xc017")
st.sidebar.write("Data source: Yahoo Finance")
# This code is a simple Streamlit app that retrieves stock prices from Yahoo Finance using the yfinance library.
# It allows users to input a stock symbol and a date range, fetches the data, and displays it in a user-friendly format.
# The app includes features like data visualization, summary statistics, and the ability to download the data as a CSV file.
# The app is designed to be easy to use and provides a clear interface for users to interact with stock data.
# The app is built using Streamlit, a popular framework for creating web applications in Python.
# The app is structured with a sidebar for user inputs and a main area for displaying the results.
# The app uses caching to improve performance when fetching data.
# The app also includes error handling to manage cases where no data is found or an error occurs during data fetching.
# The app is designed to be responsive and works well on different screen sizes.
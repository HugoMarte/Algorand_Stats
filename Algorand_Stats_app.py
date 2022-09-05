from sqlite3 import Date
#from tkinter.messagebox import YES
#from turtle import end_fill
#import tkinter as tk
import streamlit as st #For the web framework
from PIL import Image
import pandas as pd
import yfinance as yf
from urllib.request import urlopen
import plotly.express as px
import plotly.graph_objects as go

# Page layout 
st.set_page_config(layout = "wide")

#Title and subtitle
imageALG = Image.open(urlopen ("https://s2.coinmarketcap.com/static/img/coins/200x200/4030.png"))
st.image(imageALG)
st.title ("Algorand Stats")
st.markdown("""
This app retrieves cryptocurrency prices from *Yahoo Finance*
""")

# Expander bar for info
expander_info = st.expander ("App info")
expander_info.markdown (""" * **Python libraries:** pandas, streamlit, yfinance, plotly and pillow.
* Data obtaines from **Yahoo Finance**""")

# Algorand info data frames
algorand = "ALGO-USD"
ALG_data = yf.Ticker(algorand)
ALG_HIS = ALG_data.history(period="today")
ALG_1 = yf.download(algorand, start="2021-01-01", end="2022-08-29")
ALG_1 = ALG_1.drop(["Open", "High", "Low", "Close", "Adj Close"],axis=1)
ALG = yf.download(algorand, start="2021-01-01", end="2022-08-29")
ALG = ALG.drop("Volume",axis=1)
ALG_2 = yf.download(algorand, start="2021-01-01", end="2022-08-29")
ALG_2 ["Date"] = pd.date_range(start ="2021-01-01", end ="2022-08-29")
ALG_2 ["Date"] = pd.to_datetime (ALG_2 ["Date"])

# Algorand today table
st.header ("Algorand today")
st.table(ALG_HIS)
#ALG_HIS_HIST = px.histogram(ALG_HIS)
#st.plotly_chart (ALG_HIS_HIST)
#st.table(ALG_2)


# Coin selection
tickers = ("BTC-USD", "ETH-USD", "ALG-USD", "CRO-USD", "XLM-USD", "TRX-USD", "HEX-USD", "XRP-USD")
dropdown = st.multiselect("Choose your assets", tickers)

# Date selection
start = st.date_input ("start", value = pd.to_datetime ("2021-01-01"))
end = st.date_input ("end", value = pd.to_datetime ("today"))


# defining returns 
def relativeret(df):
    relative = df.pct_change() #calculates the percentage change between the current and a prior element
    cumulative = (1+relative).cumprod() - 1 # Return the cumulative product of elements along a given axis.
    cumulative = cumulative.fillna(0)
    return cumulative



#ploting the stock price
if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown,start,end) ["Adj Close"])

    # Stock price Plot display
    st.header ("Returns of {}".format(dropdown))
    st.line_chart(df)

# Algorand history plots
alg_line_plot = px.line(ALG_1)
alg_bar_plot = px.bar(ALG)
alg_candle_plot = go.Figure(data=[go.Candlestick(x=ALG_2['Date'], open=ALG_2['Open'], high=ALG_2['High'], low=ALG_2['Low'], close=ALG_2['Close'])])

# Algorand history plots display
st.title ("Algorand History")
st.header("Volume over time")
st.plotly_chart(alg_line_plot)
st.header("Algorand on the market")
st.plotly_chart(alg_bar_plot)
st.header("Algorand stats")
st.plotly_chart(alg_candle_plot)
#alg_plot_2 = px.line(ALG, animation_frame = "Date")

# Algorand_Stats
Algorand dashboard project 

## Project description

The aim of this project was to build a dashboard that allows the user to display the comparison between various cryptocurrencies in the market, based on the returns of the assets, as well as the display of Algorand current and historical data and statistics.

## Project purpose 

The purpose of this dashboard is to provide the users the information they need in order to take data driven decisions that ultimately results to the best of their interests.

## Technologies

import streamlit as st  	  		    # To build the web framework interface
from PIL import Image 		          # To display images like the algorand logo
import pandas as pd 	 		          # To create and manipulate the data frames 
import yfinance as yf			          # To harvest the information about the assets 
from urllib.request import urlopen	# To retrieve information from URL directions
import plotly.express as px		      # To generate some of the graphs and plots
import plotly.graph_objects as go	  # to generate the candlestick plot.

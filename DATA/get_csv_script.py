import pandas as pd
import yfinance as yf

symbol = "TSLA"
data = yf.download(symbol, start = "1900-01-01")
data.to_csv(f"{symbol}.csv")
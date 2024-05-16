import pandas as pd
import pandas_ta as ta
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from datetime import datetime, timedelta

# Sample crypto currencies
cryptos = [
    ('BTC', 'bitcoin.csv'),
    ('ETH', 'ethereum.csv'),
    ('XRP', 'ripple.csv'),
    ('LTC', 'litecoin.csv'),
    ('ADA', 'cardano.csv'),
    ('DOT', 'polkadot.csv'),
    ('LINK', 'chainlink.csv'),
    ('BNB', 'binancecoin.csv'),
    ('SOL', 'solana.csv'),
    ('DOGE', 'dogecoin.csv')
]

# Generating sample data for 30 days
start = datetime(2010, 1, 1)
for crypto, filename in cryptos:
    data = []
    for i in range(30):
        date = start + timedelta(days = i)
        open = round(100 + 10 * i + (i % 10) * 0.1, 2)
        high = open + round((i % 5) * 0.2, 2)
        low = open - round((i % 5) * 0.2, 2)
        close = round(open + (high - low) * 0.5, 2)
        volume = 1000000 + i * 10000

        data.append(date, crypto, open, high, low, close, volume)

    # Creating a dataframe
    dataframe = pd.DataFrame(data, columns = ['date', 'crypto', 'open', 
                                              'high', 'low', 'close', 'volume'])
    df.to_csv(filename, index = False)
'''
cryptos = ["BTC-USD", "ETH-USD", "USDT-USD", "SOL-USD", "BNB-USD", \
           "XRP-USD", "STETH-USD", "USDC-USD", "ADA-USD", "AVAX-USD", \
           "DOGE-USD", "SHIB-USD", "DOT-USD", "TON11419-USD", "WTRX-USD", \
           "TRX-USD", "LINK-USD", "WBTC-USD", "MATIC-USD", "BCH-USD"]

crypto_data = yf.download(cryptos)

for ticker in cryptos:
    # Extracting Open, High, Low, and Close prices for the ticker
    crypto_open_prices = crypto_data['Open'][ticker]
    crypto_high_prices = crypto_data['High'][ticker]
    crypto_low_prices = crypto_data['Low'][ticker]
    crypto_close_prices = crypto_data['Close'][ticker]
    crypto_volume = crypto_data['Volume'][ticker]

    # Combining the extracted data
    crypto_combined_data = pd.DataFrame({
        'Open': crypto_open_prices,
        'High': crypto_high_prices,
        'Low': crypto_low_prices,
        'Close': crypto_close_prices,
        'Volume': crypto_volume
    })

    # Saving the data to a CSV file
    crypto_combined_data.to_csv(f"{ticker}_prices.csv")


for ticker in cryptos:
    dataframe = pd.read_csv(f"{ticker}_prices.csv")

    dataframe.dropna(subset = ['Open', 'High', 'Low', 'Close', 'Volume'], \
                     how = 'all', inplace = True)
    dataframe.to_csv(f"cleaned_{ticker}_prices.csv", index = False)

Side notes:
cd DATA
python get_crypto.py
which (module)
'''

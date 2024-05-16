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
Side notes:
cd DATA
python get_crypto.py
which (module)
'''

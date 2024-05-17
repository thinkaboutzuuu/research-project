import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
start = datetime(2000, 1, 1)
end = datetime(2023, 12, 31)
days = (end - start).days + 1
for crypto, filename in cryptos:
    data = []
    for i in range(days):
        date = start + timedelta(days = i)
        open = round(100 + 10 * i + (i % 10) * 0.1, 2)
        high = open + round((i % 5) * 0.2, 2)
        low = open - round((i % 5) * 0.2, 2)
        close = round(open + (high - low) * 0.5, 2)
        volume = 1000000 + i * 10000

        data.append([date, crypto, open, high, low, close, volume])

    # Creating a dataframe
    dataframe = pd.DataFrame(data, columns = ['date', 'crypto', 'open', 
                                              'high', 'low', 'close', 'volume'])
    dataframe.to_csv(filename, index = False)
'''
path:
cd /Users/alvinkwon/Documents/GitHub/research-project/version2/DATA
python get_another_crypto.py
'''

import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split

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

    
'''
Side notes:
cd DATA
python get_crypto.py
which (module)
'''


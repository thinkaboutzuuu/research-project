import pandas as pd
import yfinance as yf

company = ["MSFT", "AAPL", "NVDA", "AMZN", "GOOG", \
           "GOOGL", "META", "TSM", "LLY", "AVGO", \
            "NVO", "TSLA", "JPM", "V", "WMT", \
                "UNH", "MA", "XOM", "ASML", "JNJ"]
data = yf.download(company)

for ticker in company:
    # Extracting Open, High, Low, and Close prices for the ticker
    open_prices = data['Open'][ticker]
    high_prices = data['High'][ticker]
    low_prices = data['Low'][ticker]
    close_prices = data['Close'][ticker]
    volume = data['Volume'][ticker]


    # Combine the extracted data into a single DataFrame
    combined_data = pd.DataFrame({
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Volume': volume
    })

    # Save the combined data to a CSV file named after the ticker
    combined_data.to_csv(f"{ticker}_prices.csv")

# Load data from CSV files
dfs = []
for ticker in company:
    # Load data from CSV file
    df = pd.read_csv(f"{ticker}_prices.csv")
    
    # Remove rows with missing values for Open, High, Low, Close, and Volume columns
    df.dropna(subset=['Open', 'High', 'Low', 'Close', 'Volume'], how='all', inplace=True)
    
    # Save cleaned data to a new CSV file
    df.to_csv(f"cleaned_{ticker}_prices.csv", index=False)

# cd DATA
# python get_csv_script.py
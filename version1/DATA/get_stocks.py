import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split

company = ["AMD", "AAPL"]
data = yf.download(company)
filter
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

# Function to split data into train, cross-validation, and test sets
def split_data(data):
    train, temp = train_test_split(data, test_size=0.4, random_state=42)
    cv, test = train_test_split(temp, test_size=0.5, random_state=42)
    return train, cv, test

# Loop through each ticker symbol
for ticker in company:
    # Load data from CSV file
    df = pd.read_csv(f"{ticker}_prices.csv")
    
    # Remove rows with missing values for Open, High, Low, Close, and Volume columns
    df.dropna(subset=['Open', 'High', 'Low', 'Close', 'Volume'], how='all', inplace=True)
    
    # Split data into train, cross-validation, and test sets
    train_df, cv_df, test_df = split_data(df)
    
    # Save split data to new CSV files
    train_df.to_csv(f"{ticker}_train.csv", index=False)
    cv_df.to_csv(f"{ticker}_cv.csv", index=False)
    test_df.to_csv(f"{ticker}_test.csv", index=False)

'''
Side notes:
cd DATA
python get_csv_script.py
which (module)
'''

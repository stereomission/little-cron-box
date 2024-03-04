from datetime import datetime
import yfinance as yf
from termcolor import colored

tickers = ['BTC-USD', 'ETH-USD', 'ETH-BTC', 'SOL-ETH']

prices_data = yf.download(tickers, period='1d')['Close']

now_time = datetime.today().strftime('%a %d %b %Y, %I:%M%p')

print(f'CRYPTO PRICES 💷: {now_time}')
print(f'================')
# Iterating through the columns (tickers) in the DataFrame
for ticker in prices_data.columns:
    price = prices_data[ticker].iloc[0]  # Assuming you're interested in the latest price
    # Format the output string
    output_string = f"{ticker}: {price:.2f}"
    # Print with color
    print(colored(output_string, 'green'))  # You can change 'green' to any other supported color

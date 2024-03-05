from datetime import datetime
import yfinance as yf

tickers = ['BTC-USD', 'ETH-USD', 'ETH-BTC', 'SOL-ETH']

output_prices_path = 'data/prices_history.txt'

prices_data = yf.download(tickers, period='1d')['Close']

now_time = datetime.today().strftime('%a %d %b %Y, %I:%M%p')

with open(output_prices_path, 'a') as file: 
    file.write(f'CRYPTO PRICES 💷: {now_time}\n')
    for ticker in prices_data.columns:
        price = prices_data[ticker].iloc[0]  # Assuming you're interested in the latest price
        # Format the output string
        output_string = f"{ticker}: {price:.2f}\n"
        # Print with color
        file.write(output_string)
    print(f"File successfully created at: {output_prices_path}")

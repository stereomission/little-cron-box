from datetime import datetime
import yfinance as yf
import dropbox

# Replace 'your_access_token' with your actual Dropbox API token
dbx = dropbox.Dropbox('sl.Bw0BDwCrQdAJZ4ybrmkP3wxatA7nNASBP-9sVU8fb7uGnKTj0_QBlbiSFc8FuUvoumPSJmNHP_dWWRx87hnB6d_S4ykcc9hjZDhccyh8RISbqxBAaXCSKY3ux-YhtK8MTD1os7Ks6YRw')

tickers = ['BTC-USD', 'ETH-USD', 'ETH-BTC', 'SOL-ETH']

prices_data = yf.download(tickers, period='1d')['Close']

now_time = datetime.today().strftime('%a %d %b %Y, %I:%M%p')

content = f'CRYPTO PRICES 💷: {now_time}\n'
for ticker in prices_data.columns:
    price = prices_data[ticker].iloc[0]
    content += f"{ticker}: {price:.2f}\n"

# Convert the string content to bytes
content_bytes = content.encode('utf-8')

# Specify the folder and the file name
folder_path = '/stock-prices-2024'  # The specific folder you want to use
file_name = 'prices_history.txt'
dropbox_path = f'{folder_path}/{file_name}'

# Upload the file to the specified folder
response = dbx.files_upload(content_bytes, dropbox_path, mode=dropbox.files.WriteMode('overwrite'))

print(f'File uploaded to Dropbox at {dropbox_path}.')

# Download the file from the specified folder
metadata, res = dbx.files_download(dropbox_path)

# Assuming you want to print the content or save it locally
data = res.content.decode("utf-8")
print(data)

# Optionally, save the content to a local file
local_file_path = 'data/prices_history.txt'
with open(local_file_path, 'w') as f:
    f.write(data)

print(f'File downloaded from Dropbox and saved to {local_file_path}.')

from flask import Flask, render_template
import os
import dropbox

# Replace 'your_access_token' with your actual Dropbox API token
dbx = dropbox.Dropbox('sl.Bw0BDwCrQdAJZ4ybrmkP3wxatA7nNASBP-9sVU8fb7uGnKTj0_QBlbiSFc8FuUvoumPSJmNHP_dWWRx87hnB6d_S4ykcc9hjZDhccyh8RISbqxBAaXCSKY3ux-YhtK8MTD1os7Ks6YRw')

# Specify the folder and the file name
folder_path = '/stock-prices-2024'  # The specific folder you want to use
file_name = 'prices_history.txt'
dropbox_path = f'{folder_path}/{file_name}'

app = Flask(__name__)

# Download the file from the specified folder
metadata, res = dbx.files_download(dropbox_path)

# Assuming you want to print the content or save it locally
data = res.content.decode("utf-8")

@app.route('/')
def show_history():
    #lines = data.split('\n')
    # Render a template with the content, or directly return it if you prefer
    return render_template('history.html', content=data)

if __name__ == '__main__':
    app.run(debug=True)
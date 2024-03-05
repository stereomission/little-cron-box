from flask import Flask, render_template
import os
import dropbox
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env into the environment

# Use the access token from the environment variable
dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))

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
from flask import Flask, render_template
import os

# Define the path to the output file
output_prices_path = 'data/prices_history.txt'

app = Flask(__name__)

@app.route('/')
def show_history():
    # Check if the output file exists
    if os.path.exists(output_prices_path):
        # Read the contents of the file
        with open(output_prices_path, 'r') as file:
            content = file.readlines()
            # Reverse the content list so the latest entry appears first
            content = content[::-1]
    else:
        content = ["No data available."]
    
    # Render a template with the content, or directly return it if you prefer
    return render_template('history.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
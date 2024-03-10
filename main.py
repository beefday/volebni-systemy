from flask import Flask, request, redirect, render_template_string
import csv

app = Flask(__name__)

with open('index.html', 'r') as f:
    HTML_FORM = f.read()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form
        with open('preferences.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data['item1'], data['item2'], data['item3'], data['item4'], data['item5'], data['item6']])
        return "Preferences saved successfully."
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(host='10.242.15.227')


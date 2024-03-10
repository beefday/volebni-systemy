from flask import Flask, request, render_template_string
import csv

def numerize(name:str):
    if name == "The Revenant":
        return 1
    elif name == "The Wolf of Wall Street":
        return 2
    elif name == "Django Unchained":
        return 3
    elif name == "Titanic":
        return 4
    elif name == "Inception":
        return 5
    elif name == "The Great Gatsby":
        return 6
    else:
        return 0

app = Flask(__name__)

with open('index.html', 'r') as f:
        HTML_FORM = f.read()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Capture the selected best movie
        best_movie = request.form.get('best_movie', 'Not specified')
        
        # Capture the rankings for both voting sections
        group1_items = [request.form.get(f'group1_item{i}', 'Not ranked') for i in range(1, 7)]
        group2_items = [request.form.get(f'group2_item{i}', 'Not ranked') for i in range(1, 7)]

        # Combine all data to write to the CSV
        data_to_write = [numerize(best_movie)] + group1_items + group2_items

        with open('preferences.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_to_write)

        return "Preferences saved successfully."

    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(host='10.242.15.227', debug=True)  # Use debug=True for development purposes only

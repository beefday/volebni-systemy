from flask import Flask, request, redirect, render_template_string
import csv

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submit Preferences</title>
</head>
<body>
    <h1>Submit Preferences</h1>
    <form method="post">
        <label for="item1">The Revenant</label>
        <input type="number" id="item1" name="item1" min="1" max="6"><br>
        <label for="item2">The Wolf of Wall Street</label>
        <input type="number" id="item2" name="item2" min="1" max="6"><br>
        <label for="item3">Django Unchained</label>
        <input type="number" id="item3" name="item3" min="1" max="6"><br>
        <label for="item4">Titanic</label>
        <input type="number" id="item4" name="item4" min="1" max="6"><br>
        <label for="item5">Inception</label>
        <input type="number" id="item5" name="item5" min="1" max="6"><br>
        <label for="item6">The Great Gatsby</label>
        <input type="number" id="item6" name="item6" min="1" max="6"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

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


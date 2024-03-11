import pandas as pd

def denumerize(number:int):
    if number == 1:
        return "The Revenant"
    elif number == 2:
        return "The Wolf of Wall Street"
    elif number == 3:
        return "Django Unchained"
    elif number == 4:
        return "Titanic"
    elif number == 5:
        return "Inception"
    elif number == 6:
        return "The Great Gatsby"
    else:
        return "Error: Invalid number."

results = pd.read_csv('preferences.csv', header=None, names=['fptp', 'group1_item1', 'group1_item2', 'group1_item3', 'group1_item4', 'group1_item5', 'group1_item6', 'group2_item1', 'group2_item2', 'group2_item3', 'group2_item4', 'group2_item5', 'group2_item6'])

print(denumerize(results['fptp'].value_counts().idxmax()))


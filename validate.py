import json

try:
    # Open the file with UTF-8 encoding
    with open("Python Codes/data_analysis.ipynb", "r", encoding="utf-8") as file:
        json.load(file)
        print("Valid JSON")
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
except UnicodeDecodeError as e:
    print("Encoding Error:", e)

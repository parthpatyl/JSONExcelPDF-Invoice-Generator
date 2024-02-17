import pandas as pd 
import openpyxl as xl
from tabula import read_pdf

file = input("Name of file: ")

if file.endswith('.xlsx'):
    df_file = pd.read_excel(file)
    print("Reading xlsx...")
elif file.endswith('.pdf'):
    df_file = read_pdf(file, pages='all')
    print("Reading PDF...")
else:
    print("FileNotSupportedError")

# Iterate through the list of DataFrames
for i, df_file in enumerate(df_file):
    # Save each DataFrame as an HTML file
    html_file_path = 'output.html'
    df_file.to_html(html_file_path)

    print(f"DataFrame saved as HTML: {html_file_path}")

css_file = 'style.css'
with open(css_file, 'r') as css_file:
        css_content = css_file.read()

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>HTML Dataframe</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    {df_file.to_html(index=False)}
</body>
</html>
"""

with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)
import json
import pandas as pandas
import openpyxl
from reportlab.platypus import SimpleDocTemplate, Table

#extractingdata
with open ('billing.json') as f:
    data = json.load(f)

df = pandas.DataFrame(data)

#excel
df.to_excel('Billing.xlsx', index=False)

# Create a PDF
pdf = SimpleDocTemplate('Billing.pdf')

# Convert DataFrame to list of lists for PDF table
data_for_pdf = [df.columns.to_list()] + df.values.tolist()

# Create a Table with the data and add some styling
table = Table(data_for_pdf)

# Add the Table to the PDF
pdf.build([table])
import openpyxl

wb = openpyxl.load_workbook('K-8 Worksheet Topics List.xlsx')
ws = wb['Grade 6']

print("Grade 6 Topics:")
print("=" * 80)
for row in ws.iter_rows(values_only=True):
    if row[0]:  # Skip empty rows
        print(row)

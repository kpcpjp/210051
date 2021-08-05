import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
num = len(wb.worksheets)
print(num)
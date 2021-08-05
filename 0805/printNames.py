import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
for ws in wb.worksheets:
	print(ws.title)
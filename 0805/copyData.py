import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
ws = wb.worksheets[1]
ws2 = wb.worksheets[2]
for i in range(1, 9):
	for j in range(1, 3):
		data = ws.cell (row = i, column = j).value
		ws2.cell(row =i,column = j).value = data
wb.save("0805.xlsx")
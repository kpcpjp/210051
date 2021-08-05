import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
ws = wb.worksheets[1]
ws.title = "hello"
wb.save("0805.xlsx")
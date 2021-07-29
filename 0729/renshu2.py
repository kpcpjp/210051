import openpyxl
wb = openpyxl.load_workbook("0729.xlsx")
ws = wb["Sheet"]
ws.cell(row = 5, column = 4).value = "hebi"
wb.save("0729.xlsx")
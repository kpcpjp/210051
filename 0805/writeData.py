import openpyxl
wb = openpyxl.load_workbook( "0805.xlsx" )
ws = wb.worksheets[0]
ws.cell( row=1,  column=1 ).value = 513
wb.save( "0805.xlsx" )
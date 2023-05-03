import xlrd
import xlwt
data=xlrd.open_workbook(r'C:\VSCODE\CUO1400W-4087.xls')
sheet=data.sheet_by_index(0) 
row_data=sheet.row_values(21)  
col_data=sheet.col_values(1)
v00=sheet.cell(1,3)
v11=sheet.cell(21,3)
v0=float(v00.value)
v1=float(v11.value)
v=v1-v0
print(v)
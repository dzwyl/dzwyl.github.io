import xlrd
import xlwt
import os
import pandas as pd
def openfile(path):
   filelist=os.listdir(path)
   for filename in filelist:
      data=xlrd.open_workbook('C:/VSCODE/AUTO-resistance/workspace/'+filename)
      return data

def resistance(path,filelist):
   data=openfile(path)
   openfile(path)
   for filename in filelist:
    sheet=data.sheet_by_index(0)
    rows=sheet.nrows                           #行数
    rowmax=rows-1
    columns=sheet.ncols                        #列数
    row_data=sheet.row_values(rowmax)
    col_data=sheet.col_values(1)
    v00=sheet.cell(1,3)
    v11=sheet.cell(rowmax,3)
    v0=float(v00.value)
    v1=float(v11.value)
    R=((v1-v0)/0.1)
    width=float(400/10000)
    thickness=float(20/10000)
    S=width*thickness
    length=0.5
    resistances=float(R*S)/length

def result(filename,resistances):
   print('样品'+filename+'的%r为:%E'%(chr(961).lower(),resistances))

def main():
   path=r'C:\VSCODE\AUTO-resistance\workspace'
   openfile(path)
   resistance(path,filelist)
   result(filename,resistances)

if __name__=="__main__":
   main()
import xlrd
import xlwt
import shutil,os
import pandas as pd
filepath=r'D:\VSCODE\AUTO-resistance\workspace'
filelist=os.listdir(filepath)
file_num=len(filelist)
workbook=xlwt.Workbook('resistance.xls')
resistance1=workbook.add_sheet('resistance')
resistance1.write(0,0,'filename')
resistance1.write(0,1,'resistance')
for index,filename in enumerate(filelist):
    data=xlrd.open_workbook('C:/VSCODE/AUTO-resistance/workspace/'+filename)
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
    print('样品'+filename+'的%r为:%E'%(chr(961).lower(),resistances))
    resistance1.write(index+1,0,filename)
    resistance1.write(index+1,1,resistances)
    workbook.save('resistance.xls')
    if index==file_num:
        break
aa=os.getcwd()
name='resistance.xls'
respath=os.path.join(aa,name)
targetpath=r'D:/VSCODE/AUTO-resistance/'
shutil.move(respath,targetpath)
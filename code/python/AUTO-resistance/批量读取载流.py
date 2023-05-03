import xlrd
import xlwt
import shutil,os
import pandas as pd
filepath='J:/copper foil/2022-9/9-23/不贴/'
filelist=os.listdir(filepath)
file_num=len(filelist)
workbook=xlwt.Workbook('载流性能.xls')
current=workbook.add_sheet('载流性能')
current.write(0,0,'filename')
current.write(0,1,'current carrying idensity')
for index,filename in enumerate(filelist):
    #print(filename)
    data=xlrd.open_workbook(r'J:/copper foil/2022-9/9-23/不贴/'+filename)
    sheet=data.sheet_by_index(0)
    rows=sheet.nrows                           #行数
    rowmax=rows-1
    for i in range(1,rows):
        idensity=sheet.cell(i,1)
        if float(idensity.value)>float(9):
            print(i)
            break
    currentcarrying=sheet.cell(i,5)
    currentcarryingidensity=float(currentcarrying.value)
    current.write(index+1,0,filename)
    current.write(index+1,1,currentcarryingidensity)
    workbook.save('载流性能.xls')
    if index==file_num:
        break
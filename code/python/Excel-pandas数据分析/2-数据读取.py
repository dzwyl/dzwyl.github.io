import pandas as pd #导入pandas库  
import csv
df=pd.read_excel('J:/py/Excel-pandas数据分析/6Cu面.xls','Run4399') #(或使用索引序号)读取指定Run4399工作表，未指定默认第一个
print(df)
print(df.index)   #Dataframe数据表格  行索引 列索引 values数据区域返回数组
print(df.columns)
print(df.values)
df.to_csv('转csv文件.csv',index=False)   #false不需要将行标题写入csv

for t,s in df.items():      # series数据结构  循环读取df表的每列数据 t列索引名称 s列数据  列数据类型
    print(t)
    print(s)
    print(type(s))
    print('-----------')

df1=pd.read_csv('J:/py/Excel-pandas数据分析/16ms-1.csv')   #支持csv格式文件
print(df1)
df1.to_excel('999.xlsx','workbook')    #保存为excel文件格式
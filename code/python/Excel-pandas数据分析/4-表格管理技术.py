import pandas as pd
import numpy as np

'''4.1 表格属性获取与修改'''
df=pd.read_excel('J:/py/Excel-pandas数据分析/6Cu面.xls','Run4399')
print(df)
print(df.size,df.shape,df.shape[0],df.shape[1])           #元素个数,行数与列数,
print(df.axes,df.axes[0],df.index,df.axes[1],df.columns)          #行索引和列索引
print(df.dtypes)     #列数据类型
print(df.values)     #以数组方式打印表格
print(df.iterrows())    #生成器按行  需要数据时才临时生成
print(df.iteritems())    #生成器按列

for t,s in df.iteritems():
    print(t)
    print(s)

for t,s in df.iterrows():
    print(t)
    print(s)

'''4.1.2 表格属性修改'''
df=pd.DataFrame(
    data=[[1,2,3],[4,5,6]],
    index=['a','b'],
    columns=['A','B','C'],
    dtype='float'
)               #创建DataFrame表格 属性 行索引，列索引，数据类型
print(df)

dt=np.dtype([('姓名','U9'),('分数','float')])  
data=np.array([('小王',98),('小李',99),('小红',97)],dtype=dt)
df=pd.DataFrame(data)              
print(df)       #dtype参数只能对整个表格设置，data只能是数组时对指定列设置格式

df=pd.read_excel(          #index_col=0将第一列作为表格行索引  header=1第二行作为表格列索引
    io='J:/py/Excel-pandas数据分析/6Cu面.xls',
    sheet_name='Run4399',
    index_col=0,
    header=1,
    dtype='float'
)          
print(df)      #df.index修改行索引  df.columns修改列索引

df['年龄']=df['年龄'].astype('float')    #修改单列数据类型
df[['年龄','出生日期']]=df[['年龄','出生日期']].astype({
    '年龄':'int',
    '出生日期':'datetime64[Y]'
})    #修改多列数据类型  设置不同数据类型    

'''4.2 表格的切片选择'''  #4.2.1 切片法
df=pd.read_excel('J:/py/Excel-pandas数据分析/切片法.xls',index_col=0)
print(df[1:3])        #使用行索引
print(df['NED001':'NED003'])     #使用行索引标签
print(df['性别'])    #使用列索引
print(df[['姓名','性别']])
print(df.性别)

print(df[1:3][['姓名','性别']])    #区域选择
print(df['NED002':'NED003'][['姓名','性别']])
print(df[df['3月']>=80][['姓名','性别']])

#4.2.2   筛选法
print(df[[True,False,False,False,True]])      #BOOL值选行，元素个数与行数相同
print(df['3月']>=80)         #条件筛选
print(df.T)      #列筛选先转置，完成后再转置

#4.2.3   loc切片法 
print(df.loc[1])        #行索引序号选择单行   返回series数据
df.index=['a','b','c','d','e']
print(df.loc['c'])          #行索引标签选择单行

print(df.loc[1:3])
df.index=['a','b','c','d','e']
print(df.loc['c':'e'])         #选择多行
print(df.loc[[1,4,3]])      #不连续选择多行  可以不按顺序

df.columns=[0,1,2,3,4,5]         #列索引是自然序号  单列
print(df.loc[:,2])
print(df.loc[:,'性别'])
print(df.loc[:,2:4])        #多列
print(df.loc[:,'姓名':'性别'])
print(df.loc[:,[2,5,0,1,4]])       #不连续多列
print(df.loc[:,['姓名','1月','性别']])
 
#4.2.4  iloc切片法   只能用索引序列  df.iloc
'''4.3 添加表格的行和列'''
df=pd.read_excel('J:/py/Excel-pandas数据分析/切片法1.xls')
s=pd.Series(
    index=['姓名','性别','1月','2月','3月'],
    data=['小王','女','23','25','65'],
    name='NED008'
)
df=df.append(s,False)        #append必须是series数据或者Dataframe
df.loc['NED999']=['小王','女','23','25','65']       #行数据直接添加
df.loc[len(df)]=['小王','女','23','25','65']
df=df.append(df)                  #向df表中添加df1表

price1=df['1月'].max()
price2=df['2月'].max()
price3=df['3月'].max()
df.loc[len(df)]=['最高价','',price1,price2,price3]

df['4月']=[1,2,3,4,5]
df.loc[:,'8月']=[23,45,67,12,32]     #添加列
df['总金额']=df['1月']+df['2月']+df['3月']
col1=[1,2,3,4,5]
col2=[23,45,67,12,32]
df.assign(五月=col1,六月=col2)
'''4.4 删除表格的行和列'''
df.drop(2,inplace=True)    #删除单行
df.drop([2,4],inplace=True)   #指定行

df=pd.read_excel('J:/py/Excel-pandas数据分析/切片法1.xls',names=range(5))  #删除列
df.drop(2,axis=1,inplace=True)
df.drop([2,4,1],axis=1,inplace=True)

df.drop(['姓名','2月'],axis=1,inplace=True)
#删除有缺失值的行和列
df.dropna(axis=0,how='all',inplace=True)   #删除整行都是缺失值的行 axis=1删除列 how='any'删除有缺失值所在行

'''4.5 表格数据的修改'''
df.loc[2,'2月']=99   #修改单值
df.iloc[2,2]=99
df.loc[3]=['小绿','男',1,2,3]    #修改单行
df.iloc[3]=['小绿','男',1,2,3]
df['3月']=[1,2,3,4,5]
df.loc[:,'2月']=[1,2,3,4,5]      #修改单列
df.iloc[:,2]=[1,2,3,4,5]
df['2月']=df['2月']*2

df.loc[[0,1],['1月','2月']]=[[1,2],[3,4]]   #修改区域
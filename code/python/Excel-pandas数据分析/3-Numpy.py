#NumPy库支持大量维度数组与矩阵运算

'''3.1.1 普通数组'''
import numpy as np
arr=np.array(['1','2','3'])
print(arr)
print(type(arr))   #将列表创建为普通数组ndarray

arra=np.array((['1','2','3'],['88','94','99']))  #二维数组  数字类型转为字符串
print(arra)
print(type(arra))

'''3.1.2 序列数组'''
arr1=np.arange(4)
arr2=np.arange(1,13)
arr3=np.arange(100,110,2)
print(arr1)
print(arr2)
print(arr3)

'''3.1.3.1 随机数组'''
rnd=np.random.rand()          #单个随机小数
arr4=np.random.rand(4)        #一维随机小数数组
arr5=np.random.rand(2,4)      #二维随机小数数组
arr6=np.random.rand(2,4,3)     #三维随机小数数组
print(rnd)
print(arr4)
print(arr5)
print(arr6)

'''3.1.3.2 随机整数数组'''
rndi=np.random.randint(1,99)          #单个随机整数   size指定维度
arr7=np.random.randint(1,99,size=(3))         #一维随机整数数组
arr8=np.random.randint(1,99,size=(3,2))      #二维随机整数数组
arr9=np.random.randint(1,99,size=(3,2,4))      #三维随机整数数组
print(rndi)
print(arr7)
print(arr8)
print(arr9)

'''3.1.4 转换数组-----'''
import pandas as pd
df=pd.read_excel('J:/py/Excel-pandas数据分析/6Cu面.xls','Run4399')   #DataFrame表格转换为数组
arr10=np.array(df)
arr11=df.to_numpy()
arr12=df.values
print(arr10)     #三种方法输出都相同

for t,s in df.items():
    print(t)
    arr13=s.values
    print(arr13)
    print('------------------')


'''3.2.1 NumPy数组预处理    类型转换'''
arr14=np.array([33,'44',55])    #转换为整数  小数  字符串
print(arr14.astype('int'))
print(arr14.astype('float'))
print(arr14.astype('str'))

arr15=np.array([0,22,55])
print(arr15.astype('datetime64[D]'))  #日期从1970-1-1开始  年Y 月M 周W 天D  小时h 分钟m 秒s 毫秒ms 微秒   时间差函数timedelta64
'''bool int整数/uint无符号整数-8/float浮点数16/32/64  str unicode'''
print(pd.to_datetime(arr15,unit='D',origin='2022-1-1'))

'''缺失值处理'''
arr16=np.array([2,3,np.nan,33,np.nan,98])    #np.nan生成缺失值  np.isnan()判断是否缺失值 返回布尔值  缺失值填充100
print(arr16)
print(np.isnan(arr16))
arr16[np.isnan(arr16)]=100
print(arr16)

'''重复值处理unique'''
arr17=np.array([9,1,2,3,1,2,9])
print(np.unique(arr17))

arr18=np.array([[2,1,1],[2,5,1],[3,1,9]])    #多维数组返回具有唯一值的一维数组
print(np.unique(arr18))

'''3.3.1 数组维度转换'''
print(arr2.reshape(3,4))    #一维转为二维，三维
print(arr2.reshape(3,2,2))

arr19=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   #多维数组转为多维数组
print(arr19.reshape(2,6))
print(arr19.reshape(2,2,3))

print(arr19.size)                    #多维数组转为一维数组  计算多维数组元素个数    直接使用内置函数flatten
print(arr19.reshape(arr19.size))
print(arr19.flatten())

'''3.3.2 数组合并'''
arr20=np.array([1,2,3])     #一维数组合并
arr21=np.array([4,5,6])
lst=[arr20,arr21]
arr22=np.concatenate(lst)
print(arr22)

arr23=np.array([[1,2,3],[4,5,6]])
arr24=np.array([[7,8,9],[10,11,12]])
lst=[arr23,arr24]
arr25=np.concatenate(lst,axis=1)    #横向合并
print(arr25)
arr26=np.concatenate(lst,axis=0)    #纵向合并
print(arr26)

'''3.4 Series数据的创建    作为DateFrame表格的列'''
s=pd.Series(['小王','小李','小红'],name='姓名')   #参数data index dtype name=None copy=False
print(s)

s=pd.Series({'A':'小王','B':'小李','C':'小红'})   #用字典创建series数据
print(s)

s=pd.Series(['小王','小李','小红'],index=['A','B','C'])   #设置索引
print(s)

s=pd.Series([3,4,8],dtype='float')   #设置数据类型
print(s)

'''3.5 DateFrame表格的创建'''
arr27=np.array([               #用numpy数组创建表格
    ['小王','男',23],
    ['小红','女',18],
    ['小兰','男',31]
])
df=pd.DataFrame(
    data=arr27,
    columns=['姓名','性别','年龄']  #设置列索引
)
print(df)

lst=[                   #用python列表创建表格
    ['小王','男',23],
    ['小红','女',18],
    ['小兰','男',31]
]
df=pd.DataFrame(
    data=lst,
    columns=['姓名','性别','年龄']
)
print(df)

dic={                             #用字典值为列表(数组，series数据都可以)创建表格
    '姓名':['小王','小红','小白'],
#字典数组数据     '姓名':np.array(['小王','小红','小白'])
#字典series数据   '姓名':pd.series(['小王','小红','小白'],['NED001','NED002','NED003'])
    '性别':['男','女','男'],
    '年龄':[23,18,31]
}
df=pd.DataFrame(
    data=dic,
    index=['NED001','NED002','NED003']
)
print(df)
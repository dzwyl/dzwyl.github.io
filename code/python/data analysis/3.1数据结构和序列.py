#3.1.1  元组tuple   一旦创建，长度固定，对象无法修改，只能在内部修改
tuple1=1,2,3
#print(tuple1)

tuple2=(1,2,3),(4,5,6)
#print(tuple2)

tuple3=tuple([3,4,5]) #序列转换为元组
#print(tuple3)

tuple4=tuple('string')
#print(tuple4)     #字符串转为元组
#print(tuple4[2])  #索引值

tuple5=tuple(['foo',[1,2],True])  #内部修改
tuple5[1].append(3)
#print(tuple5)

tup=tuple1+tuple2  #用+连接元组
#print(tup)
tup=tup*2         #用*拷贝
#print(tup)

a,b,c=tuple1  #拆包复制给变量
#print(b)

temp=a   #常用来交换变量
a=b
b=temp
#print(a,b)
a,b=b,a
#print(a,b)
a,b=3,4
#print(a,b)

seq=[(1,2,3),(4,5,6),(7,8,9)]   #拆包常用遍历元组或序列
for a,b,c in seq:
    print('a={0},b={1},c={2}'.format(a,b,c))

values=1,2,3,4,5,6,7    #*rest用来获取任意长度（想要丢弃的数据）一般用下划线
a,b,*_=values
#print(a,b)
#print(*_)


#3.1.2 列表  list
gen=range(10)    #将迭代器或者生成器转化为列表
#print(gen)
#print(list(gen))

list1=[1,2]    #append添加到尾部，insert插入,pop移除指定位置元素并返回,remove移除第一个匹配值
list1.append(4)   #用+连接两个元组，extend添加多个元素
#print(list1)
list1.insert(2,3)
#print(list1)
list1.pop(2)
#print(list1)
list1.append(1)
list1.remove(1)
#print(list1)
#print(1 in list1)

a=[2,5,7,1,4,6]  #sort排序  
a.sort()
#print(a)
b=['dd','eee','a','efef','wd']   #通过字符长度len排序
b.sort(key=len)
#print(b)

import bisect
c=[1,2,2,3,4,7]
#print(bisect.bisect(c,2))   #插入元素并保持排序
#print(bisect.bisect(c,5))
bisect.insort(c,6)          #插入相应位置
#print(c)
#print(c[1:3])               #切片
c[3:4]=[8,9]
#print(c)
#print(c[::2])
#print(c[::-1])         #翻转


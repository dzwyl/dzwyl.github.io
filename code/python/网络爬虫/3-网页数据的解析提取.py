#3-1 XPATH的使用  nodename所有子节点  /直接子节点  //子孙节点 .当前节点  ..父节点  @选取属性
#3-2 Beautiful Soup的使用
#3-3 pyquery的使用
from pyquery import PyQuery as pq
html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active">first item</li>
    </ul>
</div>
'''
doc=pq(html)
print(doc('li'))  #li节点
print(doc('#container .list li'))  #选取id为container下class为list的所有li节点
print(type(doc('#container .list li'))) 
for item in doc('#container .list li').items():
    print(item.text())  #获取节点文本内容

items=doc('.list')
print(type(items))
print(items)
lis=items.find('li')
print(type(lis))
print(lis)  #查找子节点  find查找所有子孙节点  children只查找子节点
lis=items.children()
lis=items.children('.active')  #筛选子节点中class为active的节点

items=doc('.list')
container=items.parent()  #父节点
parents=items.parents('.wrap')   #父节点的父节点
li=doc('.list .item-0.active')
print(li.siblings('.active'))   #兄弟节点

url='https://www.bilibili.com'
doc=pq(url)
print(doc('title'))   #URL初始化
doc=pq(filename='demo.html')
print(doc('li'))   #文件初始化

#遍历节点  attr获取属性  text获取文本内容
li=doc('.item.active')
print(li)
print(str(li))
print(li.html())  #调用html方法返回第一个li节点内所有HTML文本
print(li.text())  #所有li节点内纯文本内容

lis=doc('li').items()
for li in lis:
    print(li,type(li))

a=doc('.item-1 a')
print(a,type(a))
print(a.attr('href'))  #attr方法  多个节点时只调用第一个
print(a.attr.href)

a=doc('a')
for item in a.items():
    print(item.attr('href'))
    print(item.text())

#节点操作
li.removeClass('active')   #添加、移除节点内class
li.addClass('act')
li.attr('name','wenyu')  #添加name属性
li.text('changed item')  #改变文本内容
li.html('<span>changed</span>')  #li节点内部文本

#3-4 parsel的使用
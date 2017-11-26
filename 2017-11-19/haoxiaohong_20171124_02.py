# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:48:04 2017

@author: hong
"""
"""Q1：已知有序列week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    请写出两种切片命令，使得它可以得到序列['Monday','Tuseday','Wednesday','Thursday','Friday']。"""
week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday']
print week[:5]
print week[:-2]

"""Q2：若想要生成如下的列表x（1-100之间）：[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    请写出相应的列表解析表达式"""
print range(5,100)[::5]

"""Q3：熟悉并自行构造例子测试序列类型函数和方法的使用：
（1）序列：enumerate(),reversed(),sorted(),zip()
（2）字符串:join(),split(),replace(),upper()
（3）列表：append(),count(),extend(),insert()
注：元组没有自己专用的操作符和内建函数。"""
#1)序列
#enumerate()
p='basketball'
for i,t in enumerate(p):        #输出每一个位置对应的字母
    print i,t
#reversed(),sorted()            #求逆序和顺序
d=[43,33,12,63,55]
d1=[]
for n in reversed(d):          #反向排序序列，返回一个可迭代对象
    d1.append(n)           
d1
sorted(d)                       #对数据从小大排序
sorted(d,reverse=True)          #逆置排序
#zip()                          #第一个元素组成元组，第二个组成，以此类推
s,t='foo','abc'
zip(s,t)
#2)字符串
#join()                         #用冒号连接两个字符串
m=':'.join(('my name is',' join'))
m
#split()
m.split(':')                    #以冒号作为分隔符
#replace()
m.replace('name','purpose')     #把name替换成purpose
#upper()
('%s' % (m[:2]+m[12])).upper()  #将从m里选的小写字母全部转化为大写字母
#3)列表
#append()
aList=['tao',9]
aList.append('record')          #向列表中添加一个对象
aList.append(9)
aList
#count()
aList.count(9)                  #返回对象在列表中出现的次数
#extend()
aList.extend([123,'aaa'])       #接受一个列表作为参数，将列表中的每个元素添加到原列表中
aList   
#insert()
aList.insert(1,'disc')         #在索引量为1的位置插入对象
aList
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
#Q1   
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(week[0:5])
print(week[-7:-2])

#Q2
[i for i in range(5,101,5)]

#Q3
#(1)序列
a=('abc','xyz','inner','tuple')
b=('1','2','3','4')
for i in enumerate(a):
    print(i)
for t in reversed(a):
    print(t)
sorted(a)
for c,j in zip(a,b):
    print('%s %s'%(c,j))
#(2)字符串
quest='what is your favorite color?'
':'.join(quest)
quest.split()   #使用默认分隔符
quest.split(' ',1)  #分割一次
quest.replace('favorite color','quest')
quest.upper()
#(3)列表
aList=[123,'abc',4.56,['inner','list'],7-9j]
aList.append('something to see here')
aList
aList.count('abc')  #字符串'abc'是aList中的一员
aList.extend('d')
aList 
aList.insert(2,'long playing record')   
aList

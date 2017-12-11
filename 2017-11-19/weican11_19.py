# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:45:14 2017

@author: Administrator
"""
'''
Q1：已知有序列week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    请写出两种切片命令，使得它可以得到序列['Monday','Tuseday','Wednesday','Thursday','Friday']。
'''
week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(week[:5:])
print(week[0:5])
'''
Q2：若想要生成如下的列表x（1-100之间）：[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    请写出相应的列表解析表达式
'''
[x for x in range(5,105,5)]
'''
Q3：熟悉并自行构造例子测试序列类型函数和方法的使用：
（1）序列：enumerate(),reversed(),sorted(),zip()
（2）字符串:join(),split(),replace(),upper()
（3）列表：append(),count(),extend(),insert()
注：元组没有自己专用的操作符和内建函数。
'''
######enumerate()################
'''
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
'''
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print(index, item)
    
    
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
    
    

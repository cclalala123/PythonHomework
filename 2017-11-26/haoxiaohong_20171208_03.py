# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 21:18:31 2017

@author: hong
"""
#字典
#创建字典
dict={2008:52871,2009:53082,2010:54648,2011:57121,2012:58958}
print dict
#添加数据
dict[2013]=60194
dict[2014]=60710
print dict
#删除元素
del dict[2008]
del dict[2009]
print dict
#2.集合
#创建集合
a={2,3,4,6,7,8,9}
b={2,3,4,5}
print a
print b
#判断集合大小
print len(a)
print len(b)
print cmp(len(a),len(b))
#求两个集合的并，交，差，和对称差分
print a|b
print a&b
print a-b
print a^b    #只能属于集合a或b的成员，不能同时属于两个集合






# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:31:15 2017

@author: Administrator
"""

'''
1.

年份	全国粮食产量
2008	52871
2009	53082
2010	54648
2011	57121
2012	58958
2013	60194
2014	60710

以上是2008年到2014年全国产量数据，请完成以下操作：
a.	创建一个字典，将2008年到2012年数据存入；
b.	在上面字典中添加2013、2014年的数据；
c.	删除字典中2008年和2009年数据。
2.创建两个集合a={2,3,4,6,7,8,9},b={2,3,4,5}
a.判断两个集合的大小关系；
b.求两个集合的交，并，差和对称差分。
'''
#z创建字典
dict1={'2008':52871,'2009':53082,'2010':54648,'2011':57121,'2012':58958}
print(dict1)
#在字典中添加元素
dict1['2013']=60194
dict1['2014']=60710
print(dict1)
#删除字典中的元素
del dict1['2008']
del dict1['2009']
print(dict1)

#创建集合，两种方式,两种都是集合type()=set
'''
集合不能访问。与列表和元组不同，集合是无序的，也无法通过数字进行索引。此外，集合中的元素不能重复。
'''
a=set('23456789')
a1={2,3,4,5,6,7,8,9}
a2=set([2,3,4,5,6,7,8,9])
print(a,a1,a2)
b=set('2345')
b1={2,3,4,5}

print(b,b1)
print(len(a))
print(len(b))

#求两个集合的并，交，差，和对称差分
print(a|b)
print( a&b)
print (a-b)
print (a^b ) 
#对集合中的元素排序
sorted(a|b)

#删除重复元素
ar=[22,11,4,55,22,33,4]
br=set(ar)
cr=[i for i in br ]
print(cr)



#Q1
week=['Monday','Tuseday','Wednesday','Thursday','Friday','Saturday','Sunday']
#第一种方法
week[0:5]
#第二种方法
week[:-2]
['Monday', 'Tuseday', 'Wednesday', 'Thursday', 'Friday']

#Q2
list((range(5,105,5)))
list(range(101))[5::5]
s=[(x+1)*5 for x in range(20)]

#Q3
#序列
a=[5,6,4,8,3,21,1]
for index,item in enumerate(a):
    print(index,item)

a.reverse()
print(a)

a.sort()
print(a)

L=list(zip(*([1,2,3],[7,8,9])))
print(L)

'''
结果：
0 5
1 6
2 4
3 8
4 3
5 21
6 1
[1, 21, 3, 8, 4, 6, 5]
[1, 3, 4, 5, 6, 8, 21]
[(1, 7), (2, 8), (3, 9)]
'''

#字符串
a="这是梁凤的作业"
print(" ".join(a))

b='这 是 梁 凤 的 作 业'
print(b.split(' '))

c="这是是谁的作业是"
print(c.replace('是','不是',2))

d="Hello"
print(d.upper())

'''
结果：这 是 梁 凤 的 作 业
['这', '是', '梁', '凤', '的', '作', '业']
这不是不是谁的作业是
HELLO
'''

#列表
a=['h','e','l','l','o']
a.append(['!','!'])
print(a)

print(a.count('l'))

a.extend(['!','!'])
print(a)

a.insert(0,'hi')
print(a)

'''
结果：
['h', 'e', 'l', 'l', 'o', ['!', '!']]
2
['h', 'e', 'l', 'l', 'o', ['!', '!'], '!', '!']
['hi', 'h', 'e', 'l', 'l', 'o', ['!', '!'], '!', '!']
'''
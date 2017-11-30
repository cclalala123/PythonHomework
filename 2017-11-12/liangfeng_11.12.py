# Q1：

y=x=[]
x += [1]
x
[1]
y
[1]
#x本身的值被修改
x=x+[1]
x
[1,1]
y
[1]
#创建了一个新的对象指向x+[1]的和，x本身指向的地址不变。

# Q2：
#type(a)==type(b)不仅对对象的身份进行了比较，并且还再次调用了type()函数去检查对象值是否是类型本身
#type(a) is type(b)只调用一次函数对对象的身份进行比较
#选择后者的原因：如果对象的类型都不同，那么就没有必要再去检查对象值了。后者减少了不必要调用函数的次数，提高代码性能
#isinstance()函数也是可以减少程序的运行时间

# Q3:
matrix=[]
for i in range(2):
    tmp = input().split(' ')
    tmp = [int(x) for x in tmp]
    matrix.append(tmp)
#法1:
print('%d %d' % tuple(matrix[0]))
print('%d %d' % tuple(matrix[1]))
#法2
print('%d %d' % (matrix[0][0],matrix[0][1]))
print('%d %d' % (matrix[1][0],matrix[1][1]))
#法3
for i in range(2):
    for j in range(2):
        print(matrix[i][j],end=' ')
    print()
	
# Q4:
# -*- coding: utf-8 -*-

#make TextFile.py--create text file
import os
os.chdir('E:\\spyder')

ls=os.linesep

while True:
    fname=input('请输入一个未使用过的文件名：')
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break

all=[]
print("\nEnter lines ('.' by itself to quit).\n")
while True:
    entry=input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)
fobj=open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print("DONE")       

#read TextFile.py--read and display text file
fname=input('Enter filename: ')
print
try:
    fobj=open(fname,'r')
except IOError as e:
    print("*** file open error:", e)
else:
    for eachLine in fobj:
        print(eachLine,)
    fobj.close()
#
# 函数的创建
#
from asyncio import events
from multiprocessing import Event


def x2c(x):                     # 创建一个二次函数y=x^2+1
    y=x**2+1
    return y
print('the result1 is:',x2c(3))
print('<--------------------------->')

def calcu(a,b):
    c=a+b
    return c
print('the result2 is:',calcu(10,20))
print('<---------------------------------------->')

def fun(num):                   # 创建一个将列表元素分为奇数和偶数的函数
    odd=[]
    even=[]
    for i in num:
        if i%2==0:
            odd.append(i)
        elif i%2!=0:
            even.append(i)
    return odd,even
list1=[1,2,3,4,5,6,7,8,9]
print(fun(list1))
print('<----------------------------------->')

def defal(a,b=10):              # 如果没有b，则默认为10，否则返回实参的两个数值
    print(a,b)
defal(3.14)
defal(2.76,93)
print('<------------------------------------------>')

def flex(*a):                   # 位置参数个数可变的情况下使用*，返回值为元组类型
    print(a)
flex(1)
flex(1,2)
flex(1,2,3)
print('<------------------------------------------------->')

def flexw(**strg):              # 关键字参数个数可变时使用**，返回值为字典类型
    print(strg)
flexw(a=10)
flexw(a=10,b=20)
flexw(a=10,b=20,c=30)
print('<--------------------------------------------------->')

# 如果需要定义函数既有可变数量的位置形参又有可变数量的关键字形参，则只允许位置形参放在前面，关键字
# 形参放在后面，例如下式被允许，但(**a,*b)不允许
def exp(*a,**b):
    pass
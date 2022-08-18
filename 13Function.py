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


# 如果想要把主进程列表或字典的元素依次作为函数的形参，可用下述方法
def exp1(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
list2=[1,2,3]
exp1(*list2)            # 如果不加*，则list2整个列表将作为一个参数传递给形式参数a
exp1(a=10,c=20,b=30)    # 关键字实参，通过这种方式可以指定形参的值，而不是按顺序
dic1={'a':3.14,'c':2.71828,'b':5.67}
exp1(**dic1)            # 通过在字典前加**，可将字典中定义的指定参数对形参进行赋值
exp1(23,b=45,c=90)      # 支持位置实参和关键字实参混合传递
print('<------------------------------------------------>')


def exp2(a,b,*,c,d):    # 这意味着从*之后的参数必须采用关键字实参传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
exp2(43,67,c=89,d=17)


#
# 变量的作用域
#
name='Li Hua'
c=90                        # 定义全局变量可在函数内使用，但需要注意变量定义不允许在函数调用之后
def exp3(a,b):
    print(name,a+b+c)
exp3(2,3)
print('<------------------------------------------->')

def exp4(a,b):
    global c                # 通过 global 命令可使在函数内的局部变量强制为全局变量
    c=10
    print(a+b+c)
exp4(10,20)
print(c)


#
# 递归函数
#
def exp5(n):                # 阶乘函数
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n*exp5(n-1)
a=int(input('Please enter the last number: '))
print(exp5(a))
print('<---------------------------------------------->')


def exp6(n):                # 斐波那契数列函数
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==0:
        return 0
    else:
        c=exp6(n-1)+exp6(n-2)
        return c
num1=int(input('Please enter the loop number: '))
for i in range(1,num1+1):
    print(exp6(i),end='\t')
print('\t')

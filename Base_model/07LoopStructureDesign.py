#
# range() 
#
from platform import java_ver


print(range(10))        # 从0-9的整数序列
print(range(1,10))      # 从1-9的整数序列
print(range(1,10,2))    # 序列1，3，5，7，9
print(list(range(1,10,2)))
print('该整数是否在序列中',8 in range(1,10,2))

#
# Loop structure
#
# while...block, 判断语句在执行块后
r = 10
while r <= 20:
    print('r=10,r++,=',r)
    r+=1
r = False
print(r)

num1=int(input('输入起始数：'))
num2=int(input('输入终止数：'))
print('将计算该区域内的所有偶数和……')
if num1%2==0:
    num3=num1
elif num1%2==1:
    num3=num1+1
else:
    print('错误')
sum1=0
while num3<=num2:
    sum1=num3+sum1
    num3+=2
print('总和为：',sum1)

# for...in...
for item in 'python':       # 将字符串python每个字母依次取出，并赋给变量item
    print(item,type(item))
print('<----------这是一个分隔符---------->')
for i in range(1,10,2):
    print(i,type(i))
print('<----------这是一条分割线-------->')

# 使用for循环来计算0-100偶数和
sum2=0
for num in range(0,102,2):
    sum2=num+sum2
print('0-100偶数和为：',sum2)

# 100-999之间的水仙花数
for num5 in range(100,1000):
    bit1=num5//100
    bit2=num5//10%10
    bit3=num5%10
    num6=bit1**3+bit2**3+bit3**3
    if num5==num6:
        print('该数为水仙花数：',num5)
print('<-------------这是一个分隔符------------>')

# 密码
for num7 in range(3):
    pwd=int(input('please enter the password:'))
    if pwd==8888:
        print('密码正确')
        break
    else :
        print('密码错误')
else:
    print('三次密码均输入错误')
print('<------------------------>')

# 九九乘法表
for i in range(1,10):       # 行
    j=1
    while j<=i:             # 列
        result=i*j
        #print(i,'x',j,'=',result,end='\t')          # end不换行输出
        print(str(j)+'x'+str(i)+'='+str(result),end='\t')
        j+=1
    print('\n')
print('<------------------------------------>')


#
# 千年虫问题
#
year1=[82,89,87,76,82,99,00,78]
for index,value in enumerate(year1):                # 将列表中的索引和对应的值相关联
    print(index,value)
    if str(value)=='0':
        year1[index]='00'
print(year1)
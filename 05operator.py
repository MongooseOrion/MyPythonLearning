#
# How to use input() function
#
from re import A


price = input('How much is the skirt? ')
print(price, type(price))

num1 = input('please input the number 1 to sum: ')
num2 = input('please input the number 2: ')
# input() default data type is: character string
num1 = int(num1)
num2 = int(num2)
print('the result is:', num1+num2)

#
# operator
#
print(11//2)    # 整除运算
print(11%2)     # 求余
print(2**6)     # 等同于2^6

# 一正一负整除向下取整
print(5//-2)    # =-3

a=b=c=20    # abc将具有相同的内存地址

a, b, c = 30, 40, 50
print('a,b,c value is',a, b, c)
a,b=b,a     # exchange value

print(a==b)     # 比较的是值
print(a is b)   # 比较的是ID（内存地址）
print(a is not b)

# 布尔运算
# and,or,not
# in,not in
str1='Galaxy'
print('is it in str?','g' in str1)  # =false
print('is it in str?','G' in str1)  # =true

# 位运算
print('are every bit & true?',4&8)  # 'd4='b100, 'd8='b1000, 'b100&'b1000='b0000, ='d0
print('are every bit | true?',4|8)  # 'b100|'b1000='b1100, ='d12
# 左移运算
print('左移后的结果是：',4<<1)  # 左移1位, 'b100<<1='b1000='d8
print('右移后的结果是：',4>>2)  # 右移2位, 'b100>>2='b001='d1
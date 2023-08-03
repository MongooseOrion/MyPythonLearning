
# A simple of print a variable
name = 'Galaxy'
print(name)


# Get id, type and value
print('标识', id(name))   # Memory Address
print('类型', type(name))
print('值', name)


# 变量类型注解
# 语法：变量名:类型=值
var1: int = 10
var2: str = 'China'
print('var1 is:',var1)
print('var2 is:',var2)


# Data type
print(0b10001001)   # 二进制
print(0o123456)     # 八进制
print(0x2F978)      # 十六进制


# float to calculate
a = 3.1
b = 3.2678
print(round(a+b,3)) # 数据截断
from decimal import Decimal
print(Decimal('3.1')+Decimal('3.2'))


# bool
print(True+3)   # =4
print(False+3)  # =3


# Use 'and','or','not' to bool operation
print(True or False)    # =true
print(True and False)   # =false
print(not False)        # =true


# Character string
str1 = '''中国智造，
            惠及全球'''
print(str1)
print('Samsung'+'Galaxy')   # 拼接运算符


# Data type transfer
print('我叫'+'YiMo'+', '+'今年'+str(21)+'岁') 
print(float(12),int(32.111),str(56.4))      # =12.0, =32, =56.4(str type)
print(int(str(6)),bool(1),int(False))       # int(str()) only can transfer integer
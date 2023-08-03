#
# 字符串的驻留机制
# 
# 一样内容的字符串赋值的变量拥有相同的地址
a='Python'
b="Python"
c='''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

# IDE对以下含特殊符号的字符串进行了优化，以便使本来在控制台窗口显示内存地址
# 不一样的两个变量指向同一地址。在控制台两者地址不相同
chr1='abd%'
chr2='abd%'
print(chr1,id(chr1))
print(chr2,id(chr2),'\n')

# 当使用函数拼接时，因编译和运行的先后顺序，运行结果一致的字符串未必地址相同
chr3='abc'
chr4=''.join(['ab','c'])
print(chr3,id(chr3))
print(chr4,id(chr4))
print('chr3地址与chr4相同吗？',chr3 is chr4)
print('<------------------------------------------->')

#
# 字符串查找
# 
chr5='Galaxy Tab'
print(chr5.index('a'))      # 第一次出现的位置，1
print(chr5.find('a'))       # 第一次出现的位置，1
print(chr5.rindex('a'))     # 最后一次出现的位置，8
print(chr5.rfind('a'))      # 最后一次出现的位置，8

print(chr5.find('k'))       # 使用find()或rfind()函数查找不存在的字符，不报错，显示为
                            # -1
print('<-------------------------------------------->')


#
# 字符串大小写转换
#
print(chr5.upper())         # 所有字母转为大写
# 内存地址已发生改变
print(chr5.lower())         # 所有字母转为小写
print(chr5.swapcase())      # 大写转为小写，小写转为大写
print(chr5.capitalize())    # 首字母大写
chr6='hello,world'
print(chr6.title())         # 所有单词（忽略逗号）首字母大写，其余字母小写


#
# 字符串内容对齐操作
#
print(chr5.center(20,'-'))      # 该函数用于居中对齐，参数1指定宽度，若宽度小于字符串宽度，则
                                # 直接居中，否则由参数2指定的填充符左右共计填充个 参数1-字符串
                                # 宽度 个填充符。

print(chr5.ljust(20,'-'))       # 该函数用于左对齐，参数1用于指定宽度，参数2指定填充符，若参数1
                                # 大于参数2，则将 参数1-字符串宽度 个填充符加在字符串右侧，否则
                                # 直接左对齐。

print(chr5.rjust(20,'-'))       # 该函数用于右对齐，参数1用于指定宽度，参数2指定填充符，若参数1
                                # 大于参数2，则将 参数1-字符串宽度 个填充符加在字符串左侧，否则
                                # 直接右对齐。

print(chr5.zfill(20))           # 右对齐，左边用0填充，只有一个参数，用于指定宽度，如果参数小于
                                # 字符串宽度，则直接右对齐
print('-8901'.zfill(10))        # 0添加到负号后面，且只添加3个
print('<------------------------------------------------>')


#
# 字符串的分割
#
chr7='Hello world Python'
print(chr7.split())             # 不指定参数，默认按空格将字符串分为多个元素，并以列表呈现
chr8='Hello#world#Python'
print(chr8.split(sep='#'))      # 使用'sep='等式指定分隔符为','，结果与上式相同
print(chr8.split(sep='#',maxsplit=1))   # 使用'maxsplit='等式指定分隔个数，其余部分则作为一个
                                        # 整体存在列表中

print(chr8.rsplit(sep='#',maxsplit=1))  # 与split()的区别只在使用了等式'maxsplit='时从右计数


#
# 字符串的判断
#
print('init'.isidentifier())            # 判断字符串是否为合法的标识符
print('\t'.isspace())                   # 判断字符串是否为空白字符
print('abc'.isalpha())                  # 判断字符串是否全为字母
print('b000010'.isdecimal())            # 判断字符串是否全为十进制数字
print('123'.isnumeric())                # 判断字符串是否全为数字
print('123 b5'.isalpha())               # 判断字符串是否全为数字和字母


# 字符串的替换
print(chr7.replace('Python','Java'))    # 替换选定的字符串为新字符串
chr9='Do what you cant to Do'
print(chr9.replace('ou','test'))

# 字符串合并
list1=['hello','python','today']
chr10='#'.join(list1)                   # 将列表内元素连接为一个字符串，连接分隔符为‘#’，默认为
                                        # 直接连接
print(chr10,type(chr10))

tup1={'hello','python','today'}
chr11='#'.join(tup1)                    # 将元组内元素连接为一个字符串
print(chr11,type(chr11))


#
# 字符串的比较
#
chr12='apple'
chr13='banana'
print('chr12>chr13? ',chr12>chr13)      # 由于两字符串的第一位就是不同的，所以比较这一位置的字符
                                        # 在unicode编码中的数值，a<b，故而chr12<chr13

list1=['>','>=','<','<=','==','!=']     # 有这些运算符


#
# 字符串的切片操作
#
chr7='Hello world Python'
option1=chr7[:5]
option2=chr7[6:]
chr14='!'
option3=option1+option2+chr14

print(option1)
print(option2)
print(option3)

option4=chr7[1:8:2]
print(option4)
print('<-------------------------------------------->')

#
# 为字符串添加格式
#
name='Li Hua'
age=21
print('My name is %s, and I am %d years old.' % (name,age))         # 元组
print('My name is {0}, and I am {1} years old.'.format(name,age))   # 使用format()函数
print(f'My name is {name}, and I am {age} years old.')              # 使用f-string格式

# 表示数据位数，方法一
print('%10d' % 120001)      # 宽度，大于数宽度则加空格，小于数宽度则返回本身
print('%1.2f' % 12.3475)    # 小数位为几就截断几位小数位（会四舍五入）
print('%20s'%'hello world') # 多则加空格，少则返回本身

# 方法二
print('{0:0.3f} {1:0.4f}'.format(3.14123,2.71828))      # 使用format()函数以截断


#
# 字符串编码转换
#
# 编码
chr15='床前明月光'
print(chr15.encode(encoding='GBK'))             # GBK编码一个中文字符占两个字节
print(chr15.encode(encoding='UTF-8'))           # UTF-8一个中文字符占三个字节

# 解码
byte=b'\xb4\xb2\xc7\xb0\xc3\xf7\xd4\xc2\xb9\xe2'    # 某一串字符串二进制编码
print(byte.decode(encoding='GBK'))                  # 编码解码格式一定要相同


# 字符串分隔操作
def inputdata():
    indata=input('请输入年月日，以‘/’分隔：')
    year=indata[0:4]                        # 字符串可以直接像列表一样进行分隔
    month=indata[5:7]
    day=indata[8:10]
    print(year,month,day)
inputdata()
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


#
# 字符串查找
# 

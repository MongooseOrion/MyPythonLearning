# Import keyword list
import keyword
print(keyword.kwlist)       # 显示python中的所有保留字
print('<--------------------------------------------->\n')

# Watch out the file encode format, only unicode can identify zh-CN 

print(ord('a'))         # 可以显示字符a的Unicode编码数值
print(chr(97))          # 可以显示Unicode编码序列97对应的字符

print(ord('莫'))
print(chr(33707))


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
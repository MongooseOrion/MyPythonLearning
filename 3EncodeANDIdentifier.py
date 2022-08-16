# Import keyword list
import keyword
print(keyword.kwlist)       # 显示python中的所有保留字
print('<--------------------------------------------->\n')

# Watch out the file encode format, only unicode can identify zh-CN 

print(ord('a'))         # 可以显示字符a的Unicode编码数值
print(chr(97))          # 可以显示Unicode编码序列97对应的字符

print(ord('莫'))
print(chr(33707))
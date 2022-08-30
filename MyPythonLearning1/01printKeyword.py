'''
# If have '' ,will output with no calculating, or calculating
print(3+5)
print('3+5')

# Put the operator output to the file"TEXT.txt", with no ''
fp=open('D:/TEXT.txt','a+')
print(3+2, file=fp)
fp.close()

# Character string in a signal line output
print('master','output','fork')
'''

# 批量显示内容，以列表的方式
lst_name=['Li Hua','Michael','Jim','Tim','Jack']
lst_sig=['①','②','③','④','⑤']
for i in range(5):
    print(lst_sig[i],'  ',lst_name[i])
print('<----------------------------------------------------->')

# 批量显示内容，以字典的方式
dic={'①':'Li Hua','②':'Michael','③':'Jim','④':'Tim','⑤':'Jack'}
for item in dic:
    print(item,'  ',dic.get(item))
print('<------------------------------------------------------>')

# 批量显示内容，以压缩包的方式
for sig,name in zip(lst_sig,lst_name):
    print(sig,'  ',name)
print('<----------------------------------------------------->')

'''
# 设置控制台打印字符的颜色
import colorama
from colorama import init,Fore,Back,Style
init(autoreset=True)
print('\033[1;33;41m','\t中国智造，惠及全球')
'''


# 实现进位制转换功能
a=30
b=bin(a)                    # 二进制转换函数bin()输出类型为字符串
print(b)



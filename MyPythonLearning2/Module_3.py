#
# 文件读写
#
# 文件读
file=open('TextFile1.txt','r')          # 创建文件对象，'r'代表文件打开模式
print(file.readlines())                 # 以列表形式显示文件内容
file.close()

#
# 覆写模式，如果文件不存在则创建
#
file1=open('TextFile2.txt','w')
file1.write('Hello,world.\n')
file1.write('Python\n')                 # 在一次打开文件时，覆写模式不会覆写内容，而是追加
file1.close()

file1=open('TextFile2.txt','w')         # 上次的内容全部覆盖为下述内容
file1.write('2022.8.26.22H1\n')
file1.close()

#
# 追加模式
#
file1=open('TextFile2.txt','a')         
file1.write('Galaxy\n')
file1.close()

file1=open('TextFile2.txt','a')         # 追加下述内容，原来的内容不改变     
file1.write('Watch4\n')
file1.close()

#
# 二进制读写模式
#
src_file=open('alipay.ico','rb')            # 读文件，以二进制形式
target_file=open('copy_alipay.ico','wb')    # 写文件，以二进制形式
target_file.write(src_file.read())          # 将读文件的内容以二进制进行拷贝
target_file.close()
src_file.close()


#
# 一些文件命令
#
print('\n')
file=open('TextFile1.txt','r')
# print(file.read())
print(file.readline())                      # 读取一行的内容
file.close()

file=open('TextFile1.txt','w')
lst1=['Do','What','You','Cant']
file.writelines(lst1)                       # 覆写模式下将列表内容覆写为一行
file.close()

file=open('TextFile1.txt','a')
file.write('\n')
lst1=['Samsung','Galaxy','Tab','Watch']
file.writelines(lst1)                       # 追加模式，因此新建一行
file.close()

print('<---------------------------------------->')
file=open('TextFile1.txt','r')
file.seek(4)                                # 将读取起始位置（指针）重定向到第四个字节（也就是
                                            # 第五个字节开始），请注意中文占两个字节

print(file.tell())                          # 返回指针的当前位置，应当为 4
print(file.read())
print(file.tell())                          # 返回指针的当前位置，应当为字符串尾部，注意转义
                                            # 字符占2个字节，结果为 36
file.close()
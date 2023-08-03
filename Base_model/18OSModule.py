
#
# OS 模块与操作系统相关联，不同的操作系统有不同的命令，因此可能会失效
#
import os
os.system('notepad.exe')            # 调用 windows 命令

# 调用可执行文件
os.startfile('C:\\Program Files (x86)\\Tencent\\WeMeet\\wemeetapp.exe\\')

lst1=os.listdir('../MyPythonLearning1')     # 查看指定目录的所有文件
print(lst1)

os.makedirs('A/B/C')            # 创建多级目录
os.rmdir('A/B/C')               # 删除目录
os.removedirs('A/B/')           # 删除多级目录


#
# OS Path
#
import os.path
print(os.path.abspath('15Class.py'))            # 显示绝对路径 
# 判断文件是否存在，返回布尔值
print(os.path.exists('15Class.py'),os.path.exists('17ObjectClass.py'))

print(os.path.join('E:\\Document','python.py'))
print(os.path.split('E:\\Document\\python.png'))
print(os.path.splitext('python.png'))
print(os.path.basename('E:\\Document\\python.png'))
print(os.path.dirname('E:\\Document\\python.png'))
print(os.path.isdir('D:\\BaiduNetdiskDownload\\Apple.2019'),
        os.path.isdir('D:\\BaiduNetdiskDownload'))
print('<------------------------------------>\n')


#
# 列出指定目录下的所有py文件
#
import os
path=os.getcwd()
lst=os.listdir(path)                        # 在此可改为指定的路径
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
print('<------------------------------------------->\n')


#
# 列出指定目录（包括子目录）所有的py文件
#
import os
path=os.getcwd()
lst_files=os.walk(path)                         # 路径在此处指定,遍历指定目录所有文件
for dirpath,dirname,filename in lst_files:
    print(dirpath,'\n',dirname,'\n',filename)
    print('<-------------------------------------->')
    for dir in dirname:
        print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
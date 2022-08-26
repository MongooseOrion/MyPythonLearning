#
# with 语句
#
with open ('TextFile2.txt','r') as src_file:
    print(file.read())
    # 不用手动关闭，自动管理并释放资源


#
# with 语句（上下文管理器）
#
with open ('TextFile2.txt','r') as src_file:
    print(src_file.read())
    # 不用手动关闭，自动管理并释放资源


# 探究 with 语句
class MyContentMgr(object):
    def __enter__(self):
        print('This is __enter__.')
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('This is __exit__.')

    def show(self):
        print('This is show.')

with MyContentMgr() as a_file:              # 等于 a_file=MyContentMgr()
    a_file.show()
# 可以发现 with 语句自动会管理进入和退出过程


#
# 使用 with 语句进行文件复制操作
#
with open('alipay.ico','rb') as src_file:
    with open('copy_alipay_2.ico','wb') as target_file:
        target_file.write(src_file.read())





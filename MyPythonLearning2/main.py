
def add(a,b):           # 自定义函数，实现加功能
    return a+b

def div(a,b):           # 自定义函数，实现除功能
    return a/b

if __name__=='__main__':    # 此语句表明只有运行该文件时才会执行下述代码块，没有该判断则代码块
                            # 在任一引用都会被执行
    print(main.add(3,5))
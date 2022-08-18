#
# Python异常余度处理机制
#
# try...except...结构
try:
    n1=int(input('1Please enter the first number: '))
    n2=int(input('1Please enter the second number: '))
    result=n1/n2
    print('The result is: ',result)
except:
    print('Error. Please retry.')
# 在except后面可以添加指定的异常类型，当 try 代码块内的代码出现异常时，将执行except当中的代码，
# 该结构的缺点是出错了就只会执行except中的代码块，然后中止程序，不会再尝试继续运行代码块。


# try...except...else...结构
try:
    n3=int(input('2Please enter the first number: '))
    n4=int(input('2Please enter the second number: '))
except BaseException as err:
    print('Error, please retry.')
    print(err)
else:
    result=n3**2+n4*4+3
    print('The result is: ',result)


# try...except...else...finally...
try:
    n3=int(input('3Please enter the first number: '))
    n4=int(input('3Please enter the second number: '))
except BaseException as err:
    print('Error, please retry.')
    print(err)
else:
    result=n3**2+n4*4+3
    print('The result is: ',result)
finally:
    print('Finish')
# 如果不出错执行 else 代码块，如果出错执行 except 代码块。最后两者都会执行
# finally 代码块
print('<--------------------------------------------------->')


# 常见的异常类型
list_error=['ZeroDivisionError'     # 被0整除
            ,'IndexError'           # 列表索引中没有此序列（index）
            ,'KeyError'             # 字典映射中没有这个键
            ,'NameError',           # 没有声明对象
            'SyntaxError'           # 语法错误
            ,'ValueError']          # 传入无效参数
print(list_error)

# 使用 traceback 模块打印异常信息，log
import traceback
try:
    print('1.  <--------------------------------------->')
    num=10/0
except:
    traceback.print_exc()


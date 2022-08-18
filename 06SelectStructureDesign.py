
# if...else... structure
money = 1200
price = int(input('请输入取款金额：'))
if price%100==0:
    if price<=money:
        money = money-price
        print('完成')
        print('当前余额为：',money)
    else:
        print('余额不足')
        str1=input('是否需要把余额全部取出？')
        if str1=='是' or str1=='yes':
            print('成功')
            money=0
        else:
            print('已退出')
else:
    print('金额不符合要求，最少取100元')


# else if... structure
# Judge exam level
num1 = input('Please input score: ')
num1 = int(num1)
if 0<=num1<60:      # Math fulmat supported
    print('failed, Level E')
elif num1>60 and num1<70:
    print('Level D')
elif num1>70 and num1<80:
    print('Level C')
elif num1>80 and num1<90:
    print('Level B')
elif num1>90 and num1<=100:
    print('Level A')
else:
    print('Data Error')

# pass statement
# pass语句可用于占位，在执行语句块为空时使用
import random

#
# 数字竞猜游戏
#
def num_gue():
    while True:
        try:
            min=int(input('请设定区间最小数：'))
            max=int(input('请设定区间最大数：'))
            break
        except:
            print('输入不合法，请重新输入。')
    num=random.randint(min,max)
    while True:
        try:
            guess=int(input('请输入猜的数字：'))
        except:
            print('输入不合法，请重新输入。')
            continue
        if guess>num:
            print('大了。')
        elif guess<num:
            print('小了。')
        elif guess==num:
            print('正确。')
            break
        answer=input('是否需要继续猜？')
        if answer=='y':
            continue
        else:
            break
    print('正确数字是：',num)
# num_gue()


#
# 模拟登录
#
def sigin():
    lst=[{'name':'admin','pwd':123456},{'name':'user','pwd':123456}]
    for i in range(1,4):
        name=input('请输入用户名：')
        pwd=int(input('请输入密码：'))
        for item in lst:
            a=item['name']
            if name==a:
                if pwd==item['pwd']:
                    print('密码正确。')
                    return
                else:
                    print('密码错误。')
                    break
            else:
                continue
        if a!=name:
            print('用户名不存在。')
    print('已锁定。')
# sigin()


#
# 计算质数
#
def pri_num():
    a=int(input('请输入质数计算范围最小值：'))
    b=int(input('请输入质数计算范围最大值：'))
    lst=[]
    count1=0                        # 统计质数个数
    while a<=b:                   
        count2=2                    # 统计用于整除目标数的除数
        while count2<a:
            if a%count2==0:
                break
            else:
                count2+=1
        if a==count2:
            lst.append(a)
            count1+=1
        a+=1
    print('该范围内的所有质数为：',lst)
    print('质数个数为：',count1)
# pri_num()


#
# 
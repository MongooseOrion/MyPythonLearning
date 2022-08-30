
from audioop import reverse
from multiprocessing.connection import answer_challenge
from operator import itemgetter, truediv
from pickle import FALSE, TRUE
import os
import time

filename='student_info.txt'

# 主函数
def main():
    while True:
        time.sleep(0.7)
        menu()
        try:
            choice=int(input('请选择功能序号：'))           # 用户功能选择
            if choice in [0,1,2,3,4,5,6,7]:
                if choice==0:
                    answer=input('你确定要退出系统吗？ ')
                    if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
                        time.sleep(0.7)
                        print('\n已退出，谢谢你的使用。')
                        break                           # 退出系统
                    else:
                        print('输入非法，将返回主界面。')
                        continue
                elif choice==1:
                    insert()                            # 录入学生信息
                elif choice==2:
                    search()                            # 查找学生信息
                elif choice==3:
                    delete()                            # 删除学生信息
                elif choice==4:
                    modify()                            # 修改学生信息
                elif choice==5:
                    sort()                              # 排序
                elif choice==6:
                    total()                             # 统计学生总人数
                elif choice==7:
                    show()                              # 显示所有学生信息
        except:
            print('输入非法，请重新输入。')
            continue


# 菜单
def menu():
    print('\n\n============================ 学生管理系统 ==========================\n')
    time.sleep(0.7)
    print('----------------------------- 功能菜单 -----------------------------')
    print('                          1. 录入学生信息')
    print('                          2. 查找学生信息')
    print('                          3. 删除学生信息')
    print('                          4. 修改学生信息')
    print('                          5. 排序')
    print('                          6. 统计学生总人数')
    print('                          7. 显示所有学生信息')
    print('                          0. 退出系统')
    print('-------------------------------------------------------------------\n')


# 录入学生信息
def insert():
    stu_lst=[]
    while True:
        id=input('请输入待录入学生统一识别码：')
        if not id:
            break
        name=input('请输入待录入学生姓名：')
        if not name:
            break
        
        # 引入异常处理
        try:
            eng_lst=int(input('请输入待录入英语成绩：'))
            py_lst=int(input('请输入待录入 Python 成绩：'))
            java_lst=int(input('请输入待录入 Java 成绩：'))
        except:
            print('输入无效，请重新输入。')
            continue

        # 没有错误则将信息保存到字典中
        student={'id':id,'name':name,'eng_lst':eng_lst,'py_lst':py_lst,'java_lst':java_lst}
        # 将学生信息分批导入列表中
        stu_lst.append(student)
        answer=input('是否需要继续添加录入信息？ ')
        if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
            continue
        else:
            break
    # 存储信息到文件中
    save(stu_lst)
    print('学生信息录入完毕。')


# 创建/保存学生信息文件
def save(lst):
    try:
        stu_info=open(filename,'a',encoding='utf-8')
    except:
        stu_info=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_info.write(str(item)+'\n')
    stu_info.close()


# 查找学生信息
def search():
    stu_qry=[] 
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('通过统一识别码查找请按 1，通过姓名查找请按 2 。\n')
            if mode=='1':
                id=input('请输入要查询的学生的统一识别码：')
            elif mode=='2':
                name=input('请输入要查询的学生的姓名：')
            else:
                print('输入不正确，请重新输入。')
                continue
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    dic3=dict(eval(item))
                    if id!='':
                        if dic3['id']==id:
                            stu_qry.append(dic3)
                    elif name!='':
                        if dic3['name']==name:
                            stu_qry.append(dic3)
            # 显示查询结果
            show_student(stu_qry)
            # 清空列表
            stu_qry.clear()
            answer=input('是否要继续查询？ ')
            if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
                continue
            else:
                print('操作取消。')
                break
        else:
            print('库文件不存在或为空，请导入信息后重试。')
            return


# 显示查询结果的函数
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，请录入后重试。')
        return
    # 定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python 成绩','Java 成绩','总成绩'))
    # 定义内容的显示格式
    format_data='{:^6}\t{:^14}\t{:^10}\t{:^12}\t{:^12}\t{:^10}'
    for item in lst:
        try:
            print(format_data.format(item.get('id'),
                                     item.get('name'),
                                     item.get('eng_lst'),
                                     item.get('py_lst'),
                                     item.get('java_lst'),
                                     int(item.get('eng_lst'))+int(item.get('py_lst'))+int(item.get('java_lst'))
                                     ))
        except:
            print('\t','统一识别码为',item.get('id'),end='\t')
            print('该学生的某些信息为空。')
            continue


# 删除学生信息
def delete():
    while True:
        stu_id=input('请输入待删除的学生统一识别码：')
        if stu_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as rfile:
                    stu_old=rfile.readlines()
            else:
                stu_old=[] 
            flag=False                          # 标记是否删除
            if stu_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    dic1={}
                    for item in stu_old:
                        dic1=dict(eval(item))
                        if dic1['id']!=stu_id:
                            wfile.write(str(dic1)+'\n')
                        else:
                            flag=True           # 标记为已删除
                    if flag:
                        print(f'统一识别码为{stu_id}的学生信息已经被删除。')
                    else:
                        print(f'未找到统一识别码为{stu_id}的学生信息。')
            else:
                print('库文件不存在或为空，请导入信息后重试。')
                break
            show()                              # 删除之后重新显示所有学生信息
            answer=input('\n是否继续删除？ ')
            if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
                continue
            else:
                print('操作取消，将返回主界面。')
                break
        else:
            print('输入无效，请重新输入。')
            continue


# 修改学生信息
def modify():
    time.sleep(0.5)
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            stu_old=rfile.readlines()
            if not stu_old:
                print('文件为空，请尝试录入信息后再试一次。')
                return
    else:
        print('库文件不存在，请录入信息后重试。')
        return
    while True:
        stu_id=input('请输入需要修改信息的学生统一识别码：')
        if stu_id!='':
            with open(filename,'w',encoding='utf-8') as wfile:
                for item in stu_old:
                    dic2=dict(eval(item))
                    if dic2['id']==stu_id:
                        print('已找到学生信息，可以修改。')
                        while True:
                            try:
                                dic2['name']=input('请输入待修改的姓名：')
                                dic2['eng_lst']=input('请输入待修改的英语成绩：')
                                dic2['py_lst']=input('请输入待修改的 Python 成绩：')
                                dic2['java_lst']=input('请输入待修改的 Java 成绩：')
                            except:
                                print('你的输入不正确，请重新输入。')
                            else:
                                break

                        wfile.write(str(dic2)+'\n')
                        print('已经完成修改。')
                    else:
                        wfile.write(str(dic2)+'\n')
                answer=input('是否需要继续修改其他学生信息？ ')
                if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
                    modify()
                else:
                    print('操作取消，将返回至主界面。')
                    return
        else:
            print('输入无效，请重新输入。')
            continue


# 排序
def sort():
    time.sleep(0.5)
    print('\n')
    show()
    print('\n',end='')
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            stu_lst=rfile.readlines()
        stu_new=[] 
        for item in stu_lst:
            dic4=dict(eval(item))
            stu_new.append(dic4)
    else:
        print('库文件不存在，请尝试导入信息后重试。')
        return
    asc_or_desc=input('键入 0 以按升序排列所有信息，键入 1 以按降序排列所有信息。\n')
    if asc_or_desc=='0':
        asc_or_desc_bool=False 
    elif asc_or_desc=='1':
        asc_or_desc_bool=True 
    else:
        print('输入不正确，请重新输入。')
        sort()
    mode=input('请选择排序方式：键入 1 按英语成绩排序，键入 2 按 Python 成绩排序，\n\t\t键入 3 按 Java 成绩排序，键入 4 按总成绩排序。\n')
    if mode=='1':
        print('\n按照英语成绩排序。')
        stu_new.sort(key=lambda x:int(x['eng_lst']), reverse=asc_or_desc_bool)
    elif mode=='2':
        print('\n按照 Python 成绩排序。')
        stu_new.sort(key=lambda x:int(x['py_lst']), reverse=asc_or_desc_bool)
    elif mode=='3':
        print('\n按照 Java 成绩排序。')
        stu_new.sort(key=lambda x:int(x['java_lst']), reverse=asc_or_desc_bool)
    elif mode=='4':
        print('\n按照总成绩排序。')
        stu_new.sort(key=lambda x:int(x['eng_lst'])+int(x['py_lst'])+int(x['java_lst']), reverse=asc_or_desc_bool)
    else:
        print('\n输入不正确，请重新输入。')
        sort()
    show_student(stu_new)
    answer=input('\n是否需要继续按其他类别排序？ ')
    if answer=='yes' or answer=='是' or answer=='y' or answer=='Y':
        sort()
    else:
        return


# 统计学生总人数
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有 {len(students)} 名学生。')
            else:
                print('库文件为空，请尝试录入信息后重试。')
    else:
        print('库文件不存在，请尝试录入信息后重试。')


# 显示所有学生信息
def show():
    stu_lst=[] 
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            for item in students:
                stu_lst.append(eval(item))
            if stu_lst:
                show_student(stu_lst)
            else:
                print('库文件为空，请尝试导入信息后重试。')
                return
    else:
        print('库文件不存在，请尝试导入信息后重试。')
        return



if __name__=='__main__':
    main()
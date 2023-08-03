#
# 口算题卡
#
#import re
import random
import os
import time
from docx import Document

def main():
    print('\n\n#################### 欢迎使用口算题卡生成程序 v1.0 ####################\n')
    time.sleep(0.5)
    print('可以实现以下功能：')
    print('1. 自定义参与运算的数字；\n2. 自定义参与运算的数字最大是几位数（建议最大为 4 位数）；\n3. 自定义只进行加减运算或者是四则运算；\n4. 自定义生成的题目数量；\n5. 直接生成 Word 文档以便打印。\n')
    print('注意：\n1. 当算式中只有 2 个数且每个数小于等于 2 位时，除法答案将生成几余几的形式，其他情况则结果都为小数；\n2. 一页可以打印 78 个算式；\n3. 请在输入完成后按回车键。\n')
    
    time.sleep(1)
    # 避免输入错误
    while True:
        try:
            # 自定义功能
            while True:
                num_operands = int(input('请输入一个算式需要有几个数参与（例如 2+3+4，是 3 个数，必须大于 1）：\n')) 
                if num_operands < 2:
                    print('输入不正确，请重新输入。')
                else:
                    break
            while True:
                operand_digits = int(input('请输入每个数的位数（1- 一位数，2- 两位数，... 依此类推）：\n'))  
                if operand_digits > 4 and operand_digits < 1:
                    print('你输入的数字不可以，请重新输入。')
                else:
                    break
            mode = int(input('请选择是二则运算还是四则运算（1- 二则运算，2- 四则运算，其他数均为四则运算）：\n'))
            num_questions = int(input('请选择生成的题目道数：\n'))
            # 输入完成后询问是否重新输入
            redo_input = input("已保存首选项，按 'n' 可重新编辑，其他任何键均默认使用首选项设置。\n")
            if redo_input.lower() == 'n':
                continue
            else:
                break
        except:
            print('\n检测到输入错误，请重新输入。\n')
            continue
   
    count = 0
    
    expr_list = []
    result_list = []
    # 生成指定数量的算式
    while count < num_questions:
        expression, result = generate_expression(num_operands, operand_digits, mode)
        expression = expression.replace("/", "÷").replace('*', '×')
        expr_list.append(expression)
        result_list.append(result)
        count = count + 1
    
    docx_print(expr_list, '口算题卡.docx')
    print('\n\n口算题卡已经生成，你应该可以在电脑的桌面上看到。\n')
    docx_print(result_list, '答案.docx')
    print('配套答案已经生成，你应该可以在电脑的桌面上看到。\n')
    time.sleep(0.5)
    print('##### Powered by Mongoose #####\n')

    input('请按回车键退出程序。\n')



# 生成算式
def generate_expression(num_operands, operand_digits, mode):
    operators = ['+', '-']
    if mode == 1:
        pass
    else:
        operators.extend(['*', '/'])
    # 运算数
    if operand_digits < 2:
        operands = [random.randint(1, 10) for _ in range(num_operands)]
    else:
        operands = [random.randint(1, 10**operand_digits - 1) for _ in range(num_operands)] # min:10**(operand_digits-1)
    expression = str(operands[0])
    
    for i in range(1, num_operands):
        operator = random.choice(operators)
        expression += f" {operator} {operands[i]}"
        
    # 检查计算结果，它需要满足：
    # 1. 两位数或更多时不能有超过两个乘法; 2. 不能出现负数；3. 除法显示余数
    result = eval(expression)
    if num_operands > 2 or operand_digits > 2:
        while True:
            if result > 10000:
                expression = str(operands[0])
                for i in range(1, num_operands):
                    operator = random.choice(operators)
                    expression += f" {operator} {operands[i]}"
                result = eval(expression)
            else:
                break
        
    elif not isinstance(result, int):
        while True:
            if result < 0:
                expression = str(operands[0])
                for i in range(1, num_operands):
                    operator = random.choice(operators)
                    expression += f" {operator} {operands[i]}"
                result = eval(expression)
            else:
                break
        operands_lst = expression.split(sep='/')
        operands_1 = int(operands_lst[0])
        operands_2 = int(operands_lst[1])
        num_1 = operands_1 // operands_2
        num_2 = operands_1 % operands_2
        if num_2 == 0:
            result = int(num_2)
        else:
            result = ''
            result = str(num_1) + '余' + str(num_2)
    
    elif operand_digits <= 2:
        while True:
            if result < 0:
                operands = [random.randint(1, 10) for _ in range(num_operands)]
                expression = str(operands[0])
                for i in range(1, num_operands):
                    operator = random.choice(operators)
                    expression += f" {operator} {operands[i]}"
                result = eval(expression)
            else:
                break
    
    else:
        pass

    result = str(result)
    expression = expression + ' ' + '=' 
    return expression, result


def docx_print(print_list, file_name):
    # 获取 USERPROFILE 环境变量
    user_profile = os.environ.get('USERPROFILE')
    desktop_path = os.path.join(user_profile, 'Desktop')
    #file_name = '口算题卡.docx'
    file_path = os.path.join(desktop_path, file_name)

    # 分栏布局
    num_columns = 3

    # 创建一个新的docx文档对象
    doc = Document()

    num_strings = len(print_list)
    num_rows_per_page = (num_strings + num_columns - 1) // num_columns

    #for page_num in range(num_columns):

    # 创建表格
    table = doc.add_table(rows=num_rows_per_page, cols=num_columns)
    table.autofit = True

    # 迭代字符串
    for row in range(num_rows_per_page):
        for col in range(num_columns):
            string_idx = row * num_columns + col
            if string_idx < num_strings:
                cell = table.cell(row, col)
                cell.text = print_list[string_idx]

    # 保存最终结果
    doc.save(file_path)


if __name__ == "__main__":
    main()
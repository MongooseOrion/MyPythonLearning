#
# 制作一个计算器
#

import re
import sys

# 匹配乘除法
mul_div = re.compile("\d+\.*\d*[\*\/]+[\-]?\d+\.*\d*")
# 匹配加减法
plus_minus = re.compile("[\-]?\d+\.*\d*[\+\-]{1}\d+\.*\d*")
# 匹配括号
bracket = re.compile(r"\(([^()]+)\)")


def mul_div_count(str_expire):
    """
    乘除运算
    :param str_expire:表达式
    :return: 返回没有乘除的表达式/最终计算出结果
    """
    val = mul_div.search(str_expire)   # 匹配乘除号
    if not val:  # 乘除号不存在，返回输入的表达式
        return str_expire
    data = mul_div.search(str_expire).group()   # 匹配乘除号
    if len(data.split("*")) > 1:   # 当可以用乘号分割，证明有乘法运算
        part1, part2 = data.split("*")   # 以乘号作为分隔符
        value = float(part1) * float(part2)   # 计算乘法
    else:
        part1, part2 = data.split("/")   # 用除号作为分隔符
        if float(part2) == 0:   # 如果被除数为0，则退出计算
            sys.exit("计算过程中有被除数为0的存在，计算表达式失败！")
        value = float(part1) / float(part2)   # 计算除法
    # 获取第一个匹配到的乘除计算结果value，将value放回原表达式
    s1, s2 = mul_div.split(str_expire, 1)   # 分割表达式
    # 将计算结果替换回表达式，生成一个新的表达式
    next_expression = "%s%s%s" % (s1, value, s2)
    return mul_div_count(next_expression)   # 递归运算表达式


def plus_minus_count(str_expire):
    """
    加减运算
    :param str_expire: 表达式
    :return: 返回没有加减的表达式/最终计算结果
    """
    str_expire = str_expire.replace('+-', '-')   # 替换表达式里的所有'+-'
    str_expire = str_expire.replace('--', '+')   # 替换表达式里的所有'--'
    str_expire = str_expire.replace('-+', '-')   # 替换表达式里的所有'-+'
    str_expire = str_expire.replace('++', '+')   # 替换表达式里的所有'++'
    # 特殊处理加减后的表达式
    data = plus_minus.search(str_expire)   # 匹配加减号
    if not data:   # 如果不存在加减号，则证明表达式已计算完成，返回最终结果
        return str_expire
    val = plus_minus.search(str_expire).group()   # 匹配加减号
    if len(val.split('+')) > 1:   # 当可以用加号分割，证明有加法运算
        part1, part2 = val.split('+')
        value = float(part1) + float(part2)   # 计算加法
    elif val.startswith('-'):   # 如果是以'-'开头则需要单独计算
        part1, part2, part3 = val.split('-')
        value = -float(part2) - float(part3)   # 计算以负数开头的减法
    else:
        part1, part2 = val.split('-')
        value = float(part1) - float(part2)   # 计算减法
    s1, s2 = plus_minus.split(str_expire, 1)  # 分割表达式
    # 将计算结果替换回表达式，生成一个新的表达式
    next_expression = "%s%s%s" % (s1, value, s2)
    return plus_minus_count(next_expression)   # 递归运算表达式


# 定义一个方法用于去括号,并调用上述的方法进行计算
def remove_bracket(str_expire):
    """
    小括号去除运算
    :param str_expire: 表达式
    :return: 返回最终运算结果
    """
    # 判断小括号，如果不存在小括号，直接调用乘除，加减计算
    if len(bracket.findall(str_expire)) == 0:
        str_expire = mul_div_count(str_expire)
        return plus_minus_count(str_expire)   # 返回最终计算结果
    # 如果有小括号，匹配出优先级最高的小括号
    elif len(bracket.findall(str_expire)) != 0:
        while len(bracket.findall(str_expire)) != 0:
            brackets_count = bracket.search(str_expire).group()
            brackets_count = brackets_count.strip(r'\(([^()]+)\)')   # 剔除小括号
            brackets_count = mul_div_count(brackets_count)   # 计算乘除
            brackets_count = plus_minus_count(brackets_count)   # 计算加减
            part1, replace_str, part2 = re.split(
                r'\(([^()]+)\)', str_expire, 1)  # 分割表达式
            # 将小括号计算结果替换回表达式，生成一个新的表达式
            expression = '%s%s%s' % (part1, brackets_count, part2)
            return remove_bracket(expression)   # 递归去小括号运算表达式


if __name__ == "__main__":
    while True:
        str_expire = input("请输入你的公式:(q表示退出):")
        if str_expire == 'q':  # 退出计算
            sys.exit("bye-bye")
        elif len(str_expire) == 0:
            continue
        else:
            str_expire = re.sub('\s*', '', str_expire)  # 去除空格
        print("%s=%s" % (str_expire, remove_bracket(str_expire)))
        continue

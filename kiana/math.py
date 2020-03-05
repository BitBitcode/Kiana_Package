"""
【Kiana 系列库】

库名：kiana.math
简介：
    ·Kiana 系列库是 BitBitcode 自定义函数的封装库
    ·kiana.math.py 是有关一些处理日期时间的库
库函数：
    ·is_prime_number(num)
    ·bigger(num_1, num_2)
更多信息：
    ·个人邮箱：smilewwc@qq.com
    ·个人网页：https://bitbitcode.github.io/
    ·开源地址：https://github.com/BitBitcode
创建日期：2020.3.4
更新日志：

Copyright (c) BitBitcode. All rights reserved.
"""


# 定义一些常量
PI = 3.1415926  # 【π】圆周率
E = 2.7182818  # 【e】自然底数


def is_prime_number(num):
    """
    【函数】判断一个数是否为素数（Prime Number）

    :param num: 整型，输入待判断的数
    :return: 是素数返回 1，不是素数返回 0
    """
    if num <= 1:
        return 0
    elif num == 2:
        return 1
    else:
        i = 2
        signal = 1
        while i <= num / 2:
            if num % i == 0:
                signal = 0
                break
            i = i + 1
        return signal


def bigger(num_1, num_2):
    """
    【函数】判断两个数的大小

    :param num_1: 整型，输入待判断的数
    :param num_2: 整型，输入待判断的数
    :return: 返回较大的数
    """
    if num_1 >= num_2:
        return num_1
    else:
        return num_2


def average(n):
    i = 0
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sum = 0
    ave = 0
    while i < n:
        num[i] = int(input("请依次输入："))
        sum = sum + num[i]
        i = i + 1
    ave = sum / n
    return ave


# 【模块内测试代码】
if __name__ == '__main__':

    # 输出 0~100 内的素数
    x = 0
    while x < 100:
        if is_prime_number(x):
            print(x)
        x = x + 1

    print(bigger(5, 3))

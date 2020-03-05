"""
【Kiana 系列库】

库名：kiana.date
简介：
	·Kiana 系列库是 BitBitcode 自定义函数的封装库
	·kiana.date.py 是有关一些处理日期时间的库
库函数:
	·is_leap_year(y)：判断是否为闰年
	·check_date(y, m, d)：检查输入日期的有效性
更多信息：
	·个人邮箱：smilewwc@qq.com
	·个人网页：https://bitbitcode.github.io/
	·开源地址：https://github.com/BitBitcode
创建日期：2020.3.4
更新日志：

Copyright (c) BitBitcode. All rights reserved.
"""

# 来源：https://www.py.cn/jishu/jichu/13151.html


# 依赖库
import datetime


current_time = datetime.datetime.now()  # 获取原始日期时间


# （1）获取日期和时间
def get_date():
	"""
	【函数】获取日期和时间

	:return:
	"""

	# current_time.year  # 获取年
	# current_time.month  # 获取月
	# current_time.day  # 获取日
	# current_time.hour  # 获取时
	# current_time.minute  # 获取分
	# current_time.second  # 获取秒
	current_time.date()  # 获取日期

	print("原始日期时间：", current_time)

# （2）格式化
def format_date():
	# 通过datetime.datetime.now()，我们获取到的时间格式为：2019-07-06 14:55:56.873893，类型：<class 'datetime.datetime'>
	# 我们可以使用strftime()转换成我们想要的格式。处理之后的返回的值为2019-07-06、07/06等目标形式，类型为str
	date_str = current_time.strftime("%Y-%m-%d")  # 【年-月-日】形式
	# date_str = current_time.strftime("%m.%d")         #【月.日】形式

	print("格式化日期为字符串：" + date_str)

	h = str(current_time.hour)
	m = str(current_time.minute)
	s = str(current_time.second)
	print("时间字符串：" + h + ":" + m + ":" + s)  # 【时:分:秒】形式


# （3）类型转换
# 时间一般通过：时间对象，时间字符串，时间戳表示
# 通过datetime获取到的时间变量，类型为：datetime，那么datetime与str类型如何互相转换呢？
# datetime-->str
# time_str = datetime.datetime.strftime(current_time,'%Y-%m-%d %H:%M:%S')
# str-->datetime
# time_str = '2019-07-06 15:59:58'
# curr_time = datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S')


def is_leap_year(y):
	"""
	【函数】判断闰年（Leap Year）

	:param y: 整型，输入待判断的年份
	:return: 闰年返回 1，平年返回 0
	"""
	if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
		return True  	# 闰年返回 1
	else:
		return False  	# 平年返回 0


def check_date(y, m, d):
	"""
	【函数】检查输入日期日否正确

	:param y: 整型，年
	:param m: 整型，月
	:param d: 整型，日
	:return: 正确返回 1，错误返回 0
	"""
	if y > 0 and 0 < m <= 12 and 0 < d <= 31:
		if m == 2:
			if is_leap_year(y):  # 闰年 2 月
				if d > 29:
					print("【ERROR】这一年的2月只有29天！\n")
					return False
				else:
					return True
			else:  # 平年 2 月
				if d > 28:
					print("【ERROR】这一年的2月只有28天！\n")
					return False
				else:
					return True
		elif m == 4 or m == 6 or m == 9 or m == 11:
			if d == 31:
				print("【ERROR】该月份没有31天！\n")
				return False
			else:
				return True
		else:  # 1、3、5、7、8、12月
			return True
	else:
		if y < 0:
			print("【ERROR】年份应大于0！\n")
		if m <= 0 or m > 12:
			print("【ERROR】月份应在1至12之间！\n")
		if d <= 0 or d > 31:
			print("【ERROR】日应在1至31之间！\n")
		return False


# 这里放置测试代码，当且仅当直接运行模块的 .py 文件时才会执行
if __name__ == '__main__':
	while True:
		year = int(input("输入待判断年份："))
		month = int(input("输入待判断月份："))
		day = int(input("输入待判断日期："))
		print("是否闰年：", is_leap_year(year))
		print("是否正确：", check_date(year, month, day))
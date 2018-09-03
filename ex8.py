# -*- coding: utf-8 -*-

# 打印，打印

formatter = "{} {} {} {}"  # 字符串中允许有多个占位符

# 给format传递4个参数，替换其中的4个{}
print(formatter.format(1, 2, 3, 4))  # 可以传入整数
print(formatter.format("one", "two", "three", "four"))  # 也可以传入字符串
print(formatter.format(True, False, False, True))  # 也可以传入布尔型
print(formatter.format(formatter, formatter, formatter, formatter))  # 也可以传入变量
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))  # 还可以传入长文本

# -*- coding: utf-8 -*-

# 参数、解包和变量
# python ex13.py first 2nd 3rd

'''
之前我们运行Python脚本都没有添加命令行参数，如果运行这个脚本你只输了 python ex13.py那就错了
要像下面这样运行这个脚本：python ex13.py first 2nd 3rd，注意，必须传递3个命令行参数。
使用import可以让python程序实现更多的特性，我们将这些导入的特性称为模块。
'''
from sys import argv
'''
将argv解包（unpack），与其将所有参数入到同一个变量下面，不如将其赋值给4个变量。
含义:把argv中的东西取出，解包，将所有的参数依次赋值给左边的这些变量。
'''
script, first, second, third = argv

print("argv = ", repr(argv))  # 对于许多类型，repr函数尝试返回一个字符串

print("这个脚本的名称是：", script)
print("你的第一个变量是：", first)
print("你的第二个变量是：", second)
print("你的第三个变量是：", third)

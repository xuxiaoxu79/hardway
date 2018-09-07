# -*- coding: utf-8 -*-

# 到现在为止你学到了什么

'''
print('abc')  在终端打印出指定的对象，一般是字符串
print('a', 'b')  同时打印多个对象，中间用逗号分隔
print('a', 'b', sep='-')  打印多个对象时，print()默认以空格分隔，sep参数允许用户自定义
print('abc', end="")  默认情况下，print()打印完毕后会以换行符结尾，end参数允许用户自定义
f"Hello {somevar}"  这是一个格式化字符串，把变量放到指定的位置
"this {}, that {}".format('abc', '123')  格式化字符串
input([prompt])  提示用户进行输入，prompt是一个可选参数，用来设置提示的字符串

from sys import argv  从指定的模块中导入相应的功能
script, first, second = argv  这是解包(unpack)操作，将argv的值分别赋值给3个变量

#  单行注释
3个引号  多行注释

+  加号，数学中的加法，也可用于字符串相连
-  减号，数学中的减法
*  星号，数学中乘法，也可用于字符串的复制，例如：'a'*4等于'aaaa'
/  斜杠，数学中除法
%  百分号  取余数
<  小于号  逻辑比较，一般用于数值比较
>  大于号  逻辑比较，一般用于数值比较
<=  小于等于号  逻辑比较，一般用于数值比较
>=  大于等于号  逻辑比较，一般用于数值比较

=  等于号，一般用于为变量赋值
+=  将自身加上另一数值的一种简写，x += y 和 x = x + y 是一样的

\   转义符
\n  换行符
\r  回车符
\t  水平制表符

round()  四舍五入
len()  获取字符串的长度
open(filename, [mode], [encoding])  打开指定的文件，返回的是文件对象(file object)
    默认是只读方式打开文件，mode设为'w'即可在文件中写入内容
    要打开含有中文内容的文件，需要加上参数：encoding='utf-8'
文件对象拥有以下方法：
    read()  文件打开后，使用该函数可以读取文件的内容
    readline()  只读取文本文件中的一行
    write('stuff')  将"stuff"写入文件
    seek(0)  将读写位置移动到文件开头
    truncate()  清空文件
    close()  关闭文件
exists()  判断文件是否存在，需要导入 from os.path import exists
pydoc 函数名  获取函数的详细说明

def  关键字，表示定义函数
return  在函数中返回值
'''

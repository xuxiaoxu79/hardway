# -*- coding: utf-8 -*-

# 读取文件
'''
要使用 python ex15.py ex15_sample.txt 来运行程序，如果没有这个参数，程序会出错
如果被打开的文件中含有中文，open方法一定要加上 encoding="utf_8"，否则程序会出错
'''

from sys import argv

script, filename = argv

txt = open(filename, encoding="utf_8")  # 打开文件并返回相应的文件对象。
print(f"这里是你的文件：{filename}")
print(txt.read())
txt.close()

print("请再次输入你要打开的文件：")
file_again = input("> ")

txt_again = open(file_again, encoding="utf_8")

print(txt_again.read())
txt.close()

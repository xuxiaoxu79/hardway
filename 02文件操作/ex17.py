# -*- coding: utf-8 -*-

# 更多文件操作 - 将一个文件中的内容复制到另外一个文件中
# python ex17.py ex17_from.txt ex17_to.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"将 {from_file} 内容复制到 {to_file}")

# in_file = open(from_file, encoding="utf-8")  # 打开文件
# indata = in_file.read()  # 读取内容
indata = open(from_file, encoding="utf-8").read()  # 上面2行可以写成一行
# 这样的话，后面 in_file.close() 就不需要了，因为read()一旦运行，文件就会被Python关掉

print(f"源文件有 {len(indata)} 个字符")  # len返回字符串的长度

print(f"检查目标文件是否存在？ {exists(to_file)}")  # exists判断文件是否存在
print("准备好了，按回车确认，按 Ctrl+C 取消。")
input()

out_file = open(to_file, 'w', encoding="utf-8")
out_file.write(indata)

print("执行完毕！")

out_file.close()
# in_file.close()

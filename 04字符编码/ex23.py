# -*- coding: utf-8 -*-

# 字符串、字节串和字符编码
# python ex23.py utf-8 strict
'''
该脚本还可以这样运行：
python ex23.py utf-16 strict  用来和utf-8比较，看看后者节约了多少空间
python ex23.py big5 strict  会发现Python完全不买账，解决方案是运行下一行的代码
python ex23.py big5 replace  让Python替换掉Big5编码无法编码的字，无法匹配的都会被打印成问号
'''

import sys
script, encoding, error = sys.argv


# 定义这个叫main的主函数，该函数会在脚本的结尾处调用
def main(language_file, encoding, errors):
    line = language_file.readline()  # 从语言文件中读取一行
    if line:  # 当运行到文件的结尾时，readline函数会返回一个空字符串，if就是用来检查这个字符串的
        print_line(line, encoding, errors)  # 调用另一个函数来实际打印这一行，这样代码会更简单易懂
        return main(language_file, encoding, errors)  # 跳到函数顶端再运行一次，其实就是一个循环


def print_line(line, encoding, errors):
    next_lang = line.strip()  # 把每行结尾的\n删掉
    raw_bytes = next_lang.encode(encoding, errors=errors)  # 把该行编码成原始字节
    # 这是对上一行的逆操作，把前面编码的字符串进行解码操作
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)  # 将二者打印出来


languages = open("languages.txt", encoding="utf-8")  # 打开语言文件
main(languages, encoding, error)  # 执行main函数，带了需要的所有参数

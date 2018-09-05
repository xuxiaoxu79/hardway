# -*- coding: utf-8 -*-

# 提示和传递
# python ex14.py 徐小俆
'''
在运行这个脚本时，记住需要把你的名字赋给这个脚本，让argv参数接收到你的名字。
python ex14.py 徐小俆
'''

from sys import argv

script, user_name = argv
prompt = '> '  # 将用户提示符设置为变量prompt，这样就不需要在每次用到input时反复输入提示用户的字符了。

print(f"你好 {user_name}，我是 {script} 程序。")
print("我想问你几个问题。")
print(f"你喜欢我吗{user_name}？")
likes = input(prompt)

print(f"你住在哪里{user_name}？")
lives = input(prompt)

print("你拥有什么类型的电脑？")
computer = input(prompt)

print(f"""
好吧，所以你说 {likes} 我。
你住在 {lives} ，我不知道那是哪里。
你有一台 {computer} 电脑，非常棒。
""")

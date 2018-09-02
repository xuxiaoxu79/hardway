# -*- coding: utf-8 -*-

# 字符串和文本

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "biinary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# 把一个字符串放进另一个字符串
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

# 字符串相连
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)  # 字符串是可以直接通过加号进行相连的
print(w, e, sep='')  # 如果用逗号分隔，默认中间会有一个空格，加上sep=''就可以去掉这个空格

# -*- coding: utf-8 -*-

# 循环和列表

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 第一种for循环：遍历列表
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# 我们也可以通过混合列表
# 请注意我们必须使用{}，因为我们不知道它里面有什么
for i in change:
    print(f"I got {i}")

# 我们首先创建一个空列表
elements = []

# 然后使用range函数将0到5添加到列表中
for i in range(0, 6):  # range函数含首不含尾
    print(f"Adding {i} to the list.")
    # append是列表的一个方法，表示追加成员
    elements.append(i)

# 最后，我们可以将列表内容打印出来
for i in elements:
    print(f"Element was: {i}")

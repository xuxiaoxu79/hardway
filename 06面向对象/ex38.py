# -*- coding: utf-8 -*-

# 列表的操作

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("这个列表中并没有10个元素，接下来我们来解决这个问题")
stuff = ten_things.split(' ')  # 将字符串分割成列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:  # 循环到列表中有10个元素为止
    next_one = more_stuff.pop()  # 获取并删除元素
    print("即将增加: ", next_one)
    stuff.append(next_one)
    print(f"列表现在有 {len(stuff)} 个元素。")
print("我们得到了最终列表: ", stuff)

print("接下来，我们针对列表做一些操作：")
print(stuff[1])  # 打印列表中的第2个元素，序号从0开始
print(stuff[-1])  # 打印列表中倒数第1个元素
print(stuff.pop())  # 删除列表中的最后一个元素
print(' '.join(stuff))  # 将列表转换成字符串，元素之间用' '连接
print('#'.join(stuff[3:5]))  # 将列表中指定的元素转换成字符串，元素之间用'#'连接。用[3:5]来将列表切片，含首不含尾

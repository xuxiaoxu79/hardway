# -*- coding: utf-8 -*-

# 更多的变量和打印

my_name = '徐小俆'  # 姓名
my_age = 40  # 年龄
my_height = 167  # 身高cm
my_weight = 68  # 体重kg
my_eyes = '黑色'  # 眼睛的颜色
my_teeth = '白色'  # 牙齿的颜色
my_hair = '黑色'  # 头发的颜色

print(f"让我来告诉你关于 {my_name} 的情况：")
print(f"他身高 {my_height} 厘米。")
print(f"他体重 {my_weight} 公斤。")
print("实际上并不太重。")
print(f"他是 {my_eyes} 的眼睛和 {my_hair} 的头发。")
print(f"他的牙齿是 {my_teeth} 的。")

total = my_age + my_height + my_weight
print(f"如果我输入 {my_age}, {my_height} 和 {my_weight}, 就能得到合计数：{total}")

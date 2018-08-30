# -*- coding: utf-8 -*-

# 变量和命名

cars = 100  # 车
space_in_a_car = 4.0  # 每辆车可供乘坐的人数
drivers = 30  # 司机
passengers = 90  # 乘客
cars_not_driven = cars - drivers  # 缺少司机的车辆
cars_driven = drivers  # 有司机的车辆等于司机的人数
carpool_capacity = cars_driven * space_in_a_car  # 车队容量等于有司机的车辆乘以每辆车可供乘坐的人数
average_passengers_per_car = passengers / cars_driven  # 平均每辆车乘坐了多少人

print("There are", cars, "cars available.")  # 这里总共有100辆车
print("There are only", drivers, "drivers available.")  # 但这里只有30位司机
print("There will be", cars_not_driven, "empty cars today.")  # 今天将会有70辆车空着
print("We can transport", carpool_capacity, "people today.")  # 我们今天能够运送120名乘客
print("We have", passengers, "to carpool today.")  # 今天有90名乘客需要运送
# 我们需要每辆车至少装载3名乘客
print("We need to put about", average_passengers_per_car, "in each car.")

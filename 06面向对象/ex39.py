# -*- coding: utf-8 -*-

# 字典，可爱的字典

# 创建州缩写的字典
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# 创建州和一些城市的字典
cities = {
    'CA': 'San francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# 增加更多的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 打印输出一些城市
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# 打印输出一些州
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# 通过州名称在城市字典中检索
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# 打印输出所有州和名称和缩写
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# 打印输出所有州的城市
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} is abbreviated {city}")

# 同时打印输出州缩写和城市字典
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# 获取可能不存在的州的缩写
state = states.get('Texas')  # 使用get方法时，当在字典中没有找到指定的键值，返回None
if not state:
    print("Sorry, no Texas.")

# 获取城市，如果字典中不存在，则返回默认值
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

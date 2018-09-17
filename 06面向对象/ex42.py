# -*- coding: utf-8 -*-

# 对象、类及从属关系


# Animal是一个类，它继承object。通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Animal(object):
    pass


# Dog是一个类，它继承Animal类
class Dog(Animal):
    def __init__(self, name):
        # Dog类有一个name属性
        self.name = name


# Cat是一个类，它也继承Animal类
class Cat(Animal):
    def __init__(self, name):
        # Cat类有一个name属性
        self.name = name


# Person是一个类，它继承object
class Person(object):
    def __init__(self, name):
        # Person类有一个name属性
        self.name = name
        # Person类有一个pet属性，它表示此人拥有某种宠物
        self.pet = None


# Employee是一个类，它继承Person类
class Employee(Person):
    def __init__(self, name, salary):
        # 嗯这是什么奇怪的魔法，super() 函数是用于调用父类(超类)的一个方法。
        # Employee的父类是Person类，调用Person类的__init__方法
        super(Employee, self).__init__(name)
        # Employee类有一个salary属性
        self.salary = salary


# Fish是一个类
class Fish(object):
    pass


# Salmon是一个类，它继承Fish类
class Salmon(Fish):
    pass


# Halibut是一个类，它也继承Fish类
class Halibut(Fish):
    pass


# rover是一个对象，它实例化于Dog类，实例化时传入name属性值
rover = Dog("Rover")


# satan是一个对象，它实例化于Cat类，实例化时传入name属性值
satan = Cat("Satan")


# mary是一个对象，它实例化于Person类，实例化时传入name属性值
mary = Person("Mary")

# mary对象的pet属性赋值为satan对象，表示mary对象有一只名为satan的宠物
mary.pet = satan

# frank是一个对象，它实例化于Employee类，实例化时传入name和salary属性值
frank = Employee("Frank", 120000)

# frank对象的pet属性赋值为rover对象，表示frank对象有一只名为rover的宠物
frank.pet = rover

# flipper是一个对象，它实例化于Fish类
flipper = Fish()

# crouse是一个对象，它实例化于Salmon类
crouse = Salmon()

# harry是一个对象，它实例化于Halibut类
harry = Halibut()

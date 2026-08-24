class Student:
    # __init__魔术方法
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    # __str__魔术方法
    def __str__(self):
        return f"Student {self.name}, {self.age}, {self.hobby}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


"""
如果不设置str、lt、le、eq魔术方法，在输出、比较时会默认按照对象的地址进行比较
"""
stu_1 = Student("richenyv", 18, "yuki")
stu_2 = Student("cunriyang", 19, "yuki")
# 调用str方法
print(stu_1)
print(stu_2)
# 调用大于小于符号时自动调用lt\le方法
print(stu_1 < stu_2)
print(stu_1 <= stu_2)
# 调用==自动使用eq方法
print(stu_1 == stu_2)

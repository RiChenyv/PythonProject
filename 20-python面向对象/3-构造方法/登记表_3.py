class Student:
    name = None
    age = None
    hobby = None

    # 以上三行可不写

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        print("Student创建了一个对象")


stu = Student("日辰羽", 19, "Yuki")
print(stu.name)
print(stu.age)
print(stu.hobby)

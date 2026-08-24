class Student:
    name = None
    age = None
    __native_place = "河南"
    __id = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __print_id_NotHere(self):
        print("我的身份证并非4开头")

    # 公开方法可以调用私有变量和方法
    def print_yourself(self):
        if self.__native_place == "河南":
            print("我是本地人")
        else:
            self.__print_id_NotHere()
            print("我是外地人")


stu_1 = Student("richenyv", 18)
stu_1.print_yourself()

class Student:
    name = None
    age = None

    def say_hello(self, msg):
        print(f"hello,my name is {self.name} and I am {self.age},{msg}")


stu_1 = Student()
stu_1.name = "日辰羽"
stu_1.age = 19
stu_1.say_hello("很高兴认识大家")

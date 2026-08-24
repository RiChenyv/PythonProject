# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_phone = None
    age = None


# 创建对象
stu_1 = Student()
# 对对象赋值
stu_1.name = "日辰羽"
stu_1.gender = "男"
stu_1.age = 18
stu_1.nationality = "中国"
stu_1.native_phone = "北京"
# 获取信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_phone)

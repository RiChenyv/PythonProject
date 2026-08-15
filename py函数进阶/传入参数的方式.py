def user_info(name, age, gender='男'):
    print(f"your name is {name} and your age is {age} and your gender is {gender}")


# 位置参数
user_info('richenyv', 19, "man")

# 关键字参数(可以和位置参数传参混用，可以无序传参)
user_info(name="richenyv", age=19, gender="man")
user_info("richenyv", age=19, gender="man")

# 缺省参数(在函数中默认值设置一定要在最后)
user_info(name="cunriyang", age=19, gender="girl")
user_info(name="cunriyang", age=19)


# 位置不定长参数(以元组的形式出现)
def without_length(*args):
    print(args, type(args))


without_length('TOM')
without_length('TOM', 18, True)


# 关键字不定长参数
def with_lengths(**kwargs):
    print(kwargs)
    print(type(kwargs))


with_lengths(age=18, gender="man")

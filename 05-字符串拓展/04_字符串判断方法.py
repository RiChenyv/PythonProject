# 字符串判断方法：返回布尔值 True / False

# 1. isdigit()：是否全部是数字
print(f"'12345'.isdigit() = {'12345'.isdigit()}")
print(f"'123abc'.isdigit() = {'123abc'.isdigit()}")
print("————————————————————————")

# 2. isalpha()：是否全部是字母
print(f"'hello'.isalpha() = {'hello'.isalpha()}")
print(f"'hello123'.isalpha() = {'hello123'.isalpha()}")
print("————————————————————————")

# 3. isalnum()：是否全部是字母或数字
print(f"'hello123'.isalnum() = {'hello123'.isalnum()}")
print(f"'hello 123'.isalnum() = {'hello 123'.isalnum()}")
print("————————————————————————")

# 4. isspace()：是否全部是空白
print(f"'   '.isspace() = {'   '.isspace()}")
print(f"' a '.isspace() = {' a '.isspace()}")
print("————————————————————————")

# 5. isupper() / islower()：是否全大写 / 全小写
print(f"'ABC'.isupper() = {'ABC'.isupper()}")
print(f"'abc'.islower() = {'abc'.islower()}")
print("————————————————————————")

# 实际应用：验证输入是否合法
num = input("请输入一个数字：")
if num.isdigit():
    print(f"输入合法，这个数乘以2等于：{int(num) * 2}")
else:
    print("输入不合法，请输入纯数字喵！")

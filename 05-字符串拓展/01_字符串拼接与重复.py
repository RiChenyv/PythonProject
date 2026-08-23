# 字符串的拼接与重复

# 1. 使用 + 拼接字符串
str1 = "hello"
str2 = "world"
result = str1 + " " + str2
print(f"拼接结果：{result}")
print("————————————————————————")

# 2. 字符串与数字拼接需要先转换
age = 18
print("我今年" + str(age) + "岁")
print("————————————————————————")

# 3. 使用 * 重复字符串
print("*" * 10)
print("哈" * 3)
print("喵" * 5)
print("————————————————————————")

# 4. 使用 += 追加拼接
msg = "你好"
msg += "呀"
msg += "喵"
print(msg)
print("————————————————————————")

# 5. 字符串也可以使用下标和切片
my_str = "PythonProject"
print(f"第一个字符：{my_str[0]}")
print(f"前6个字符：{my_str[:6]}")
print(f"倒序：{my_str[::-1]}")

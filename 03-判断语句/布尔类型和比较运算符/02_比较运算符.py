# 比较运算符：运算结果都是布尔类型 True / False
# ==  等于
# !=  不等于
# >   大于
# <   小于
# >=  大于等于
# <=  小于等于

a = 10
b = 20

print(f"{a} == {b} : {a == b}")
print(f"{a} != {b} : {a != b}")
print(f"{a} > {b} : {a > b}")
print(f"{a} < {b} : {a < b}")
print(f"{a} >= {b} : {a >= b}")
print(f"{a} <= {b} : {a <= b}")
print("————————————————————————")

# 字符串也可以比较（按字母顺序）
print(f"'abc' == 'abc' : {'abc' == 'abc'}")
print(f"'abc' < 'abd' : {'abc' < 'abd'}")
print("————————————————————————")

# 比较运算符常用于 if 判断
age = int(input("请输入你的年龄："))
print(f"是否成年：{age >= 18}")

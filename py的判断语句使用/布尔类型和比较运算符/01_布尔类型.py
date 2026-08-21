# 布尔类型：只有两个值 True（真）和 False（假）
# 注意：True 和 False 首字母必须大写

a = True
b = False
print(f"a 的值是 {a}，类型是 {type(a)}")
print(f"b 的值是 {b}，类型是 {type(b)}")
print("————————————————————————")

# 布尔类型可以做逻辑运算
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print("————————————————————————")

# bool() 可以把其他数据转为布尔类型
# 数字 0 为 False，其他数字为 True
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool(-1) = {bool(-1)}")
print("————————————————————————")

# 字符串：空字符串为 False，非空为 True
print(f"bool('') = {bool('')}")
print(f"bool('hello') = {bool('hello')}")
print("————————————————————————")

# 判断语句的运算结果就是布尔类型
print(f"10 > 5 的结果是：{10 > 5}")

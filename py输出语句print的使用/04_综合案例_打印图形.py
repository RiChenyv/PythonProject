# 综合案例：用 print 打印各种图形

# 1. 打印直角三角形
print("————— 直角三角形 —————")
for i in range(1, 6):
    print("*" * i)
print("————————————————————————")

# 2. 打印等腰三角形
print("————— 等腰三角形 —————")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
print("————————————————————————")

# 3. 打印菱形
print("————— 菱形 —————")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
print("————————————————————————")

# 4. 打印个人信息名片
print("—————————— 个人名片 ——————————")
name = "richenyv"
age = 18
hobby = "写Python"
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"爱好：{hobby}")
print("—————————— 完 ——————————")

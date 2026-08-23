# 字符串格式化：把变量插入到字符串中

name = "richenyv"
age = 18

# 1. % 格式化（老方法）
print("我的名字是%s，今年%d岁" % (name, age))
# %s 字符串、%d 整数、%f 小数
print("价格：%.2f元" % 3.14159)
print("————————————————————————")

# 2. format() 方法（常用）
print("我的名字是{}，今年{}岁".format(name, age))
# 可以指定位置，重复使用
print("我的名字是{0}，今年{1}岁，再次叫{0}".format(name, age))
# 可以指定名称
print("我的名字是{n}，今年{a}岁".format(n=name, a=age))
print("————————————————————————")

# 3. f-string（最推荐，Python3.6+）
print(f"我的名字是{name}，今年{age}岁")
# 内部可以直接写表达式
print(f"明年我就{age + 1}岁了")
num1 = 10
num2 = 20
print(f"{num1} + {num2} = {num1 + num2}")
# 可以控制小数位数
pi = 3.1415926
print(f"圆周率保留两位：{pi:.2f}")
print("————————————————————————")

# 4. 格式化的其他玩法：补零、对齐
print(f"学号：{7:03d}")        # 003 补零
print(f"|{'居中':^10}|")       # 居中
print(f"|{'左对齐':<10}|")     # 左对齐
print(f"|{'右对齐':>10}|")     # 右对齐

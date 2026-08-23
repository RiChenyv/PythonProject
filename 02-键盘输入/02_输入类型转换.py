# 键盘输入的内容默认是字符串，参与数学运算前需要转换类型
# int() 转整数、float() 转小数、str() 转字符串

num1 = input("请输入第一个整数：")
num2 = input("请输入第二个整数：")
# 没有转换前，+ 是字符串拼接
print(f"直接相加（字符串拼接）：{num1 + num2}")

num1 = int(num1)
num2 = int(num2)
# 转换后，+ 才是数学运算
print(f"转换后相加（数学运算）：{num1 + num2}")
print("————————————————————————")

# float 转换
height = input("请输入你的身高（米）：")
height = float(height)
print(f"你的身高是：{height} 米，类型为{type(height)}")
print("————————————————————————")

# 输入小数做运算（价格 * 数量）
price = float(input("请输入苹果单价（元）："))
count = int(input("请输入购买数量："))
total = price * count
print(f"苹果单价{price}元，购买{count}个，总价为：{total}元")
print("————————————————————————")

# 也可以一步到位：input() 外面直接套转换函数
number = int(input("请输入一个整数："))
print(f"这个数乘以 10 等于：{number * 10}")

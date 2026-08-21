# 综合案例：简易加法计算器
# 输入两个数，输出它们的和

print("—————————— 简易加法计算器 ——————————")

num1 = input("请输入第一个数：")
num2 = input("请输入第二个数：")

# 支持输入小数，所以用 float 转换
num1 = float(num1)
num2 = float(num2)

result = num1 + num2
print(f"{num1} + {num2} = {result}")

print("—————————— 感谢使用 ——————————")

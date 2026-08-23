# input() 函数：从键盘接收输入
# 注意：input() 接收到的内容【永远是字符串类型】

print("请输入你的名字：")
name = input()
print(f"你好，{name}，欢迎来到Python的世界！")
print("————————————————————————")

# 也可以直接在 input() 里写提示语
age = input("请输入你的年龄：")
print(f"你的年龄是：{age}")
print("————————————————————————")

# 验证类型：input 返回的一定是 str 字符串
print(f"name 的类型是：{type(name)}")
print(f"age 的类型是：{type(age)}")
print("————————————————————————")

# 输入多个内容
hobby = input("请输入你的爱好：")
print(f"你的爱好是：{hobby}，真是个有趣的爱好呢！")

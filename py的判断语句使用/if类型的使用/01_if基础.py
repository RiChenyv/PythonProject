# if 基础语法
# if 条件:
#     条件成立时执行的代码（注意缩进！）

age = 18
if age >= 18:
    print("你已经成年啦，可以进入网吧了")

print("程序结束")
print("————————————————————————")

# if 判断也可以直接使用布尔值
if True:
    print("True 条件成立")

if False:
    print("这行不会打印")

print("————————————————————————")

# 通过 input 输入来判断
age = int(input("请输入你的年龄："))
if age >= 18:
    print("欢迎光临！")

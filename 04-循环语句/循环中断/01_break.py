# break：立即结束整个循环

# 1. 基本用法：遇到 break 直接跳出循环
print("——— 遇到 5 就停止 ———")
for i in range(1, 10):
    if i == 5:
        break
    print(i)               # 输出 1 2 3 4

print("————————————————————————")

# 2. break 用在 while 里（经典：死循环 + break 退出）
print("——— 输入 exit 退出 ———")
while True:
    word = input("请输入内容（输入exit退出）：")
    if word == "exit":
        print("已退出循环")
        break

print("————————————————————————")

# 3. break 只结束当前这一层循环（外层循环不受影响）
print("——— 内层 break 只跳内层 ———")
for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            break          # 只跳出内层 j 循环
        print(f"i={i}, j={j}")

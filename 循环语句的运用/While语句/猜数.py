import random

real_num = random.randint(1, 100)
count = 0
print("系统将生成一个随机数，其范围为1--100")
while 1:
    print("请输入你的猜测结果：")
    num = int(input())
    if num < real_num:
        count += 1
        print("猜小了")
    if num > real_num:
        count += 1
        print("猜大了")
    if num == real_num:
        count += 1
        break
    else:
        count += 1
print(f"恭喜你，猜对了，数字为{real_num}")
print(f"你猜了{count}次")

# continue：跳过本次循环，继续下一次

# 1. 基本用法：遇到 continue 跳过本次，不执行后面的代码
print("——— 跳过数字 3 ———")
for i in range(1, 6):
    if i == 3:
        continue           # 3 不打印
    print(i)               # 输出 1 2 4 5

print("————————————————————————")

# 2. 实际应用：只输出偶数（跳过奇数）
print("——— 输出 1~10 的偶数 ———")
for i in range(1, 11):
    if i % 2 != 0:
        continue           # 奇数跳过
    print(i)               # 输出 2 4 6 8 10

print("————————————————————————")

# 3. continue 只作用于当前这一层循环
print("——— 内层 continue 只跳内层 ———")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue       # 内层跳过 j=2
        print(f"i={i}, j={j}")

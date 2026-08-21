# if-else 语法：二选一
# if 条件:
#     条件成立执行的代码
# else:
#     条件不成立执行的代码

age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

print("————————————————————————")

# 例子：判断奇偶数
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")

print("————————————————————————")

# 例子：判断是否及格
score = int(input("请输入你的成绩："))
if score >= 60:
    print("恭喜，考试及格了！")
else:
    print("很遗憾，不及格，下次加油喵！")

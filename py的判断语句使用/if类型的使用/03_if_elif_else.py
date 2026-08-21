# if-elif-else 语法：多条件判断
# 从上往下依次匹配，命中一个条件就结束，后面的不再判断
# if 条件1:
#     代码1
# elif 条件2:
#     代码2
# elif 条件3:
#     代码3
# else:
#     都不满足时执行的代码

# 案例：根据分数评等级
score = int(input("请输入你的成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

print("————————————————————————")

# 案例：根据数字输出星期几
week = int(input("请输入星期几（1-7）："))
if week == 1:
    print("星期一")
elif week == 2:
    print("星期二")
elif week == 3:
    print("星期三")
elif week == 4:
    print("星期四")
elif week == 5:
    print("星期五")
elif week == 6:
    print("星期六")
elif week == 7:
    print("星期日")
else:
    print("输入错误，请输入1-7之间的数字")

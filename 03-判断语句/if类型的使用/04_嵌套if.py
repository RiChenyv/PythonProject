# 嵌套 if：if 里面再套 if
# 注意缩进！内层 if 必须在外层 if 的代码块里面

# 案例：游乐园购票
# 身高超过120cm需要买票，超过150cm可以玩刺激项目
height = int(input("请输入你的身高（cm）："))
if height > 120:
    print("你的身高超过120cm，需要购买门票")
    if height > 150:
        print("你可以玩刺激项目")
    else:
        print("你只能玩普通项目")
else:
    print("你的身高未超过120cm，可以免费游玩")

print("————————————————————————")

# 案例：登录验证（综合运用判断）
name = input("请输入用户名：")
password = input("请输入密码：")
if name == "richenyv":
    if password == "123456":
        print("登录成功，欢迎回来！")
    else:
        print("密码错误")
else:
    print("用户名不存在")

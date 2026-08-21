# 逻辑运算符：and（与）、or（或）、not（非）
# and：两边都为 True 结果才是 True
# or：  只要一边为 True 结果就是 True
# not： 取反

print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")
print("————————————————————————")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")
print("————————————————————————")
print(f"not True = {not True}")
print(f"not False = {not False}")
print("————————————————————————")

# 逻辑运算符用于多条件判断
# 案例：判断是否为闰年
# （能被4整除且不能被100整除）或者（能被400整除）
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
print("————————————————————————")

# 案例：登录验证（用户名和密码都正确才通过）
name = input("请输入用户名：")
password = input("请输入密码：")
if name == "richenyv" and password == "123456":
    print("登录成功")
else:
    print("用户名或密码错误")

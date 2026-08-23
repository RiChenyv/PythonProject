def check(temp):
    if temp <= 37.5 and temp >= 29.5:
        print(f"您的体温为{temp}，体温正常请进")
    if temp < 29.5:
        print("您的体温异常，请尽快接收治疗")
    else:
        print(f"您的体温为{temp}，疑似阳性现象，需要隔离！！！")


print("欢迎来到核酸检测平台，请出示您的健康吗和72h核酸证明，并配合体温检测")
print("请输入您的体温")
temp = input()
temp = int(temp)
check(temp)

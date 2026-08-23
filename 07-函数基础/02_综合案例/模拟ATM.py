def check():
    print("--------------余额查询--------------")
    print(f"{name},您好，您的余额为{save_money}元")


def INT_money(number):
    global save_money
    save_money += number
    print("---------------存款---------------")
    print(f"{name},您好！，您本次存款{number}元")
    print(f"您现有存款{save_money}元")


def OUT_money(number):
    global save_money
    if save_money > number:
        save_money -= number
        print("---------------取款---------------")
        print(f"{name},您好！，您本次取款{number}元")
        print(f"您现余存款{save_money}元")
    else:
        print("余额不足！！！")


print("请输入您的账户及密码")
bank = int(input())
password = str(input())
print("请输入您的用户名：")
name = str(input())
if name:
    save_money = 5000000
    chose = -1
    print(f"登陆成功，欢迎您！{name}")
    while chose != 0:

        print("----------主菜单----------")
        print("查询余额请按1")
        print("存款请按2")
        print("取款请按3")
        print("退出请按0")
        print("请输入您的选择：")
        chose = input()
        try:
            chose = int(chose)
        except ValueError:
            print("请正确输入！！")
            continue
        if int(chose) == 1:
            check()
        if int(chose) == 2:
            print("请输入本次存入总数：")
            number_input = int(input())
            INT_money(number_input)
        if int(chose) == 3:
            print("请输入本次取款金额：")
            number_output = int(input())
            OUT_money(number_output)
        if int(chose) == 0:
            chose = 0
print("您已安全退出系统，欢迎下次光临")

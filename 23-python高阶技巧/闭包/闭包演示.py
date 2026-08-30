def outer(logo):
    def inner(msg):
        print(f"{logo}|{msg}|{logo}")

    # 返回一个函数
    return inner


def outer2(logo):
    def inner(msg):
        nonlocal logo
        logo += msg
        return logo

    return inner


# fnc1是一个函数
fnc1 = outer("康神开播了")
fnc1("真的假的")
# 可重复调用
fnc1("真的假的")
# nonlocal使用
fnc2 = outer2(11)
num = fnc2(10)
print(num)

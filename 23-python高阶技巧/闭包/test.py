def acount(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"账户余额{initial_amount}，本次存入{num}")
        else:
            initial_amount -= num
            print(f"账户余额{initial_amount}，本次取出{num}")

    return atm


atm = acount()
atm(11, True)
atm(11, False)
atm(121, True)
atm(12, True)
atm(12, False)

def seelp():
    import random
    import time
    print("sleeping......")
    time.sleep(random.randint(1, 5))


def sleep_show(func):
    def inner():
        print("I will sleep")
        func()
        print("I will get up")

    return inner


fnc = sleep_show(seelp)
fnc()

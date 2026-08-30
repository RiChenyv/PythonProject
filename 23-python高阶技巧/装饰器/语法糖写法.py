def sleep_show(func):
    def inner():
        print("I will sleep")
        func()
        print("I will get up")

    return inner


@sleep_show
def sleep():
    import random
    import time
    print("sleeping......")
    time.sleep(random.randint(1, 5))


sleep()

import threading
import time


def sing(song):
    while True:
        print(song)
        time.sleep(1)


def dance(show):
    while True:
        print(show)
        time.sleep(1)


# 创建两个线程
threading_object_01 = threading.Thread(target=sing, args=("I want to sing song",), name="sing")
threading_object_02 = threading.Thread(target=dance, kwargs={"show": "I want to dance"}, name="dance")
# 启动线程
threading_object_01.start()
threading_object_02.start()

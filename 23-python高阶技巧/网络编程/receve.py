import os


def recv_msg(temp):
    while True:
        try:
            msg = temp.recv(1024)
            if not msg:
                print("对方已断开链接")
                os._exit(0)
            data = msg.decode("utf-8")
            if data == "exit":
                print("请先添加对方为好友开始聊天")
                os._exit(0)
            print(data)
        except Exception:
            print("请先添加对方为好友开始聊天")
            os._exit(0)

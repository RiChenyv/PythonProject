import socket
import threading

import receve

# 创建客户端对象
socket_user = socket.socket()
# 连接到服务器
socket_user.connect(("localhost", 8888))
threading_socket_user = threading.Thread(target=receve.recv_msg, args=(socket_user,), daemon=True).start()
while True:
    try:
        # 发送消息
        msg = input()
        if msg == "exit":
            break
        socket_user.send(msg.encode("utf-8"))
    except Exception as err:
        print("发送失败！！！！！！")
        print("请先添加对方为好友开始聊天")
        break

# 关闭客户端
socket_user.close()

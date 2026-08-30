import socket
import threading

import receve

# 创建服务端对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)  # listen方法接收一个整数，表示监听数量
# 等待客户端连接
result = socket_server.accept()  # result是一个二元元组
connection = result[0]  # 客户端和服务端的连接对象
address = result[1]  # 客户端地址信息
"""等价于
connection,address = socket_server.accept() 
accept为一个阻塞方法，如果一直未链接，程序将一直卡在这里"""
print("您已成功添加好友，现在可以开始聊天了！")
# print(f"接收到了连接信息，客户端信息为{address}")
threading.Thread(target=receve.recv_msg, args=(connection,), daemon=True).start()
while True:
    try:
        # 发送消息
        msg = input()
        if msg == 'exit':
            break
        connection.send(msg.encode("utf-8"))  # encode将字符串编码为字节对象（byte）
    except Exception as e:
        print("发送失败！！！！！！")
        print("请先添加对方为好友开始聊天")
        break
# 关闭连接
connection.close()
socket_server.close()

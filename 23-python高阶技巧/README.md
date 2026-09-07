# 🔧 23-python高阶技巧

> 记录 **Python 进阶技巧** 的学习笔记喵～
> 闭包、装饰器、多线程、网络编程、设计模式，一波全带走喵！🐱

---

## 📁 目录

```
23-python高阶技巧
├── 闭包/                      # 闭包（内层函数用外层变量）
│   ├── 闭包演示.py            # 闭包基础 + nonlocal 修改外层变量
│   └── test.py                # ⭐ 闭包实现 ATM 存取款
├── 装饰器/                    # 装饰器（给函数加功能）
│   ├── 一般写法(闭包).py      # 装饰器的闭包写法
│   └── 语法糖写法.py          # @ 语法糖写法（推荐）
├── 多线程/
│   └── test.py                # threading 创建多线程（sing/dance）
├── 网络编程/                  # socket 通信
│   ├── 服务端.py              # 服务端：bind/listen/accept
│   ├── 客户端.py              # 客户端：connect/send
│   ├── receve.py              # 接收消息的公共函数（recv/decode）
│   ├── 客户端开发/             # （空，预留）
│   └── 服务端开发/             # （空，预留）
├── 设计模式/                  # 设计模式
│   ├── 单例模式/
│   │   ├── Str_tool_py.py     # 创建好对象直接导出（模块天然单例）
│   │   └── test.py            # 验证两次 import 拿到同一个对象
│   └── 工厂模式/
│       └── test.py            # ⭐ PersonFactory 按类型造对象
└── README.md                  # 本文件
```

---

## 🔍 内容说明

### 1. 闭包（`闭包/`）

**闭包 = 内层函数 + 外层函数的变量**：内层函数可以访问外层函数的变量，即使外层函数已经结束喵！

```python
def outer(logo):
    def inner(msg):              # 内层函数用了外层变量 logo
        print(f"{logo}|{msg}|{logo}")
    return inner                 # 返回内层函数（不调用！）

fnc1 = outer("康神开播了")        # fnc1 就是一个闭包函数
fnc1("真的假的")                  # 可以反复调用
```

**修改外层变量要 `nonlocal`**：

```python
def outer2(logo):
    def inner(msg):
        nonlocal logo            # 声明 logo 是外层变量才能改
        logo += msg
        return logo
    return inner
```

> 📄 `闭包/test.py` 用闭包实现了 ATM 存取款：外层变量当「账户余额」，
> 内层函数负责存取，不用 global 也能记住余额喵！

### 2. 装饰器（`装饰器/`）

**装饰器 = 闭包的应用**：在不改原函数代码的前提下，给它「加功能」喵！

```python
# 一般写法：手动调用
def sleep_show(func):
    def inner():
        print("I will sleep")
        func()                    # 调用原函数
        print("I will get up")
    return inner

fnc = sleep_show(seelp)           # 手动装饰
fnc()
```

```python
# 语法糖写法（推荐！）：@ 符号
@sleep_show                       # 等价于 sleep = sleep_show(sleep)
def sleep():
    print("sleeping......")

sleep()                           # 直接调用，自动带装饰功能
```

> 💡 装饰器模板：外层收**函数**，内层做**增强**并调用它，返回内层喵！

### 3. 多线程（`多线程/test.py`）

```python
import threading

threading_object_01 = threading.Thread(
    target=sing,                       # 线程执行的函数
    args=("I want to sing song",),     # 位置参数（注意单元素元组要加逗号！）
    name="sing"                        # 线程名
)
threading_object_02 = threading.Thread(
    target=dance,
    kwargs={"show": "I want to dance"}  # 关键字参数
)
threading_object_01.start()            # start() 启动线程
threading_object_02.start()
```

> 💡 sing 和 dance 两个死循环函数，靠多线程**同时运行**，看起来像「边唱边跳」喵！

### 4. 网络编程（`网络编程/`）—— socket 聊天室

**服务端流程**（`服务端.py`）：

```python
import socket
socket_server = socket.socket()          # 1. 创建 socket
socket_server.bind(("localhost", 8888))  # 2. 绑定 IP 和端口
socket_server.listen(1)                  # 3. 监听（参数=最大连接数）
connection, address = socket_server.accept()  # 4. 等待客户端连接（阻塞！）
connection.send(msg.encode("utf-8"))     # 5. 发送（字符串要先 encode 成字节）
```

**客户端流程**（`客户端.py`）：

```python
socket_user = socket.socket()            # 1. 创建 socket
socket_user.connect(("localhost", 8888)) # 2. 连接服务端
socket_user.send(msg.encode("utf-8"))    # 3. 发送消息
```

**收消息公共模块**（`receve.py`）：

```python
def recv_msg(temp):
    msg = temp.recv(1024)                # 收最多 1024 字节
    data = msg.decode("utf-8")           # 字节 decode 回字符串
```

- 收发都用**线程**（daemon=True）跑着，主线程负责 `input()` 输入发送
- 输入 `exit` 双方断开喵！

### 5. 设计模式（`设计模式/`）

**单例模式**（整个程序只创建一个对象）：

```python
# Str_tool_py.py —— 创建好对象直接导出
class StrTool:
    pass

str_tool = StrTool()          # 只创建这一次

# test.py —— 每次 import 拿到的都是同一个对象
from Str_tool_py import str_tool
str1 = str_tool
str2 = str_tool
print(id(str1), id(str2))     # id 一样 = 同一个对象喵！
```

**工厂模式**（用一个工厂类统一造对象）：

```python
class PersonFactory:
    def get_person(self, p_type, name, age):
        if p_type == 'Student':
            return Student(name, age)
        elif p_type == 'Teacher':
            return Teacher(name, age)
        elif p_type == 'Worker':
            return Worker(name, age)

pf = PersonFactory()
stu = pf.get_person('Student', "richenyv", 18)   # 想造谁就传谁喵！
```

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | 闭包的定义 | `闭包/闭包演示.py` | 内层函数用外层变量并返回内层函数 = 闭包；`fnc1 = outer("...")` 后反复调用 |
| 2 | nonlocal 修改外层变量 | `闭包/闭包演示.py` | 内层想改外层变量必须 `nonlocal logo`，否则报错或只读喵 |
| 3 | 闭包实战：ATM 存取款 | `闭包/test.py` | 外层变量当余额、内层函数存取，`atm(11, True)` 存、`False` 取，不用 global |
| 4 | 装饰器（闭包写法） | `装饰器/一般写法(闭包).py` | `sleep_show(seelp)` 手动包一层，返回增强后的函数 |
| 5 | 装饰器 @ 语法糖 | `装饰器/语法糖写法.py` | `@sleep_show` 写在函数上方 = 自动装饰，直接调用原函数名即可 |
| 6 | 多线程创建与启动 | `多线程/test.py` | `Thread(target=函数, args=元组/kwargs=字典, name=名字)` + `.start()` |
| 7 | socket 服务端四步 | `网络编程/服务端.py` | `socket() → bind(ip,端口) → listen(n) → accept()`（阻塞等连接） |
| 8 | socket 客户端两步 | `网络编程/客户端.py` | `socket() → connect((ip,端口))`，然后就能 send |
| 9 | 消息编解码 | `网络编程/服务端.py` | 发送 `msg.encode("utf-8")`，接收 `recv(1024).decode("utf-8")` |
| 10 | 线程收消息 + exit 退出 | `网络编程/receve.py` | `recv_msg` 放线程里循环收；收到 `exit` / 连接断开就 `os._exit(0)` |
| 11 | 单例模式 | `设计模式/单例模式/Str_tool_py.py` | 模块里只创建一次对象并导出，import 永远拿到同一个（id 相同） |
| 12 | 工厂模式 | `设计模式/工厂模式/test.py` | `PersonFactory.get_person(类型, ...)` 按字符串类型返回不同子类对象 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ **闭包返回的是函数不是结果**：`return inner` 不要加括号（`inner()` 就变成调用执行了），调用返回的函数才执行内层喵！（`闭包/闭包演示.py`）
2. ⚠️ **内层修改外层变量必须 `nonlocal`**：不声明就直接 `logo += msg` 会报「local variable referenced before assignment」，声明了才能改喵！（`闭包/闭包演示.py`）
3. ⚠️ **args 单元素元组要加逗号**：`args=("I want to sing song",)` 少了逗号就变成字符串了，Thread 会拆错参数喵！（`多线程/test.py`）
4. ⚠️ **accept() 是阻塞方法**：服务端会一直卡在 `accept()` 等客户端连接，不连就一直不往下走，测试时先启动服务端再启动客户端喵！（`网络编程/服务端.py`）
5. ⚠️ **send/recv 要编解码配对**：发送用 `msg.encode("utf-8")`，接收要 `msg.decode("utf-8")`，漏了会报类型错误或收到乱码喵！（`网络编程/`）
6. ⚠️ **程序是死循环，要用 exit 退出**：服务端/客户端的主循环只有输入 `exit` 才 break；`receve.py` 检测到对方断开或收到 exit 会用 `os._exit(0)` 强退，别用 Ctrl+C 硬停喵！
7. ⚠️ **单例靠「模块只执行一次」**：`Str_tool_py.py` 被 import 时只运行一次，所以 `str_tool` 只有一个；但直接重复运行文件两次会创建两个，复习时理解模块机制喵！（`设计模式/单例模式/test.py`）
8. ⚠️ **工厂模式忘了 return 会拿到 None**：`get_person` 里 `if/elif` 最后没有 else 兜底，传了不认识的类型就返回 None，调用 `.name` 会 AttributeError 喵！（`设计模式/工厂模式/test.py`）

---

*本笔记由喵喵助手整理，高阶技巧全点亮喵！🐾*

# 🔄 04-循环语句

> 记录 **for / while 循环** 的学习笔记喵～
> 让代码学会「重复劳动」喵！🐱

---

## 📁 目录

```
04-循环语句
├── for循环/
│   └── for输出乘法表.py      # ⭐ for 嵌套输出九九乘法表
├── While语句/
│   └── 猜数.py              # ⭐ while 猜数字小游戏
├── 循环中断/                 # 循环控制：break / continue
│   ├── 01_break.py          # break 跳出循环
│   └── 02_continue.py       # continue 跳过本次
└── README.md                # 本文件
```

---

## 🔍 内容说明

### 1. for 循环（`for循环/for输出乘法表.py`）

```python
for number in range(1, 10):
    for index in range(1, number + 1):   # 嵌套 for
        print(f"{number}*{index}={number * index}\t", end=" ")
    print()
```

> 💡 嵌套 for 实现**九九乘法表**：外层控制行，内层控制列喵！
> `end=" "` 让输出不换行，一行输出完再 `print()` 换行喵！

### 2. while 循环（`While语句/猜数.py`）

```python
while 1:                       # 死循环 + break 退出
    num = int(input("请输入你的猜测结果："))
    if num == real_num:
        break                  # 猜对就跳出循环
```

> 💡 猜数字游戏：`random.randint(1, 100)` 生成随机数，
> 用 `while` 死循环反复猜测，猜对 `break` 退出喵！

### 3. 循环中断（`循环中断/`）

| 关键字 | 作用 |
|--------|------|
| `break` | 立即**结束整个循环** |
| `continue` | **跳过本次**循环，进入下一次 |

```python
for i in range(1, 10):
    if i == 5:
        break        # 输出 1 2 3 4 就停了
    print(i)

for i in range(1, 6):
    if i == 3:
        continue     # 跳过 3，输出 1 2 4 5
    print(i)
```

> ⚠️ `break` / `continue` 只作用于**当前这一层循环**喵！

---

## 🎓 本文件夹总结的知识点

1. 🔁 `for` 适合**遍历**（range、容器），`while` 适合**条件循环**
2. 🪆 嵌套循环：外层跑一次，内层跑一圈
3. ✂️ `break` 结束循环，`continue` 跳过本次
4. 🎮 死循环 `while 1` + `break` 是「猜数字」这类游戏的经典套路
5. 📜 `range(开始, 结束, 步长)` 生成数字序列

---

*本笔记由喵喵助手整理，循环快乐喵！🐾*

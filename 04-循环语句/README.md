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

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | for + range 遍历 | `for循环/for输出乘法表.py` | `range(1, 10)` 生成 1~9 的序列，for 逐个取数执行循环体 |
| 2 | 嵌套 for 输出九九乘法表 | `for循环/for输出乘法表.py` | 外层管行、内层管列，内层 `range(1, number + 1)` 随外层变化 |
| 3 | f-string 拼接 + `end` 不换行 | `for循环/for输出乘法表.py` | `f"{number}*{index}={number * index}"` 格式化输出，`end=" "` 让 print 不换行 |
| 4 | random.randint 生成随机数 | `While语句/猜数.py` | `random.randint(1, 100)` 返回 1~100 的随机整数，记得先 `import random` 喵 |
| 5 | while 1 死循环 + break 退出 | `While语句/猜数.py` | 条件恒真反复猜，猜对才 `break`，游戏类小程序经典套路 |
| 6 | 变量累加统计猜测次数 | `While语句/猜数.py` | 每次猜测 `count += 1`，猜对后用 f-string 输出总次数 |
| 7 | break 立即结束整个循环 | `循环中断/01_break.py` | 遇到 `break` 直接跳出，`while True` + break 实现「输入 exit 退出」 |
| 8 | continue 跳过本次循环 | `循环中断/02_continue.py` | `continue` 后面的代码不执行、直接进下一次，如跳过奇数只打印偶数 |
| 9 | break/continue 只作用于当前层 | `循环中断/01_break.py` | 嵌套循环里内层的 break/continue 不影响外层循环 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ `input()` 返回的是**字符串**，直接和数字比较会报错，必须先 `int(input())` 转成整数（`猜数.py` 里就是这么做的喵）
2. ⚠️ `range(1, 10)` 不包含 10！想输出到 9 就要写 `number + 1`，忘记 +1 九九乘法表会少一列喵
3. ⚠️ `break` / `continue` 只作用于**当前这一层**循环，嵌套时想跳出外层需要额外加标志变量喵
4. ⚠️ `continue` 之后的代码永远不执行，别把要打印的语句写在 `continue` 后面，否则等不到它喵
5. ⚠️ `while 1` 死循环一定要有退出出口（`break` 或改变条件），否则程序会无限卡住喵
6. ⚠️ 多个独立 `if` 并列（而不是 `if/elif/else` 链）时计数逻辑容易重复累加，`猜数.py` 的 count 计数就有点绕喵

---

*本笔记由喵喵助手整理，循环快乐喵！🐾*

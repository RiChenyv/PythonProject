# 🐱 PythonProject —— 喵喵的 Python 学习乐园

> 这里记录了一位小可爱从 **Python 小白** 一路打怪升级的学习足迹喵～
> 从最基础的输出与输入，到函数、异常、模块包，再到文件操作和综合案例，
> 每一步都是认真敲出来的喵！🐾

---

## 📖 项目简介

本仓库是 **Python 基础语法学习项目**，按「由浅入深」的顺序整理了各类学习笔记、
示例代码与综合练习，包含：

- ✅ 基础语法：print 输出、键盘输入、判断语句、循环语句
- ✅ 数据容器：List、Tuple、str、dict、set、序列切片
- ✅ 函数：返回值、变量作用域、嵌套调用、lambda 匿名函数
- ✅ 异常处理：`try / except / finally`
- ✅ 模块与包：`import` 的四种形式、`__init__.py`、`__all__`
- ✅ 文件操作：读取、写入、追加、`with open`
- ✅ 综合案例：错误/模块/包综合练习、模拟 ATM、账单文件处理

> 🎯 目标：**快乐学习，扎实基础，喵生圆满！**

---

## 🌳 目录结构

```
D:\PythonProject
├── .venv/                        # Python 虚拟环境（本机开发用）
├── .idea/                        # PyCharm 项目配置
├── images/                       # 学习笔记配图（截图、总结图）
│   ├── totally.jpg               # 数据容器总结图
│   ├── 文件读取操作总结_01.jpg
│   └── 微信图片_*.jpg            # 容器转换笔记图
│
├── py输出语句print的使用/         # 🖨️ print 输出语句
│   ├── 01_print基础使用.py        # print 基础用法
│   ├── 02_print的sep和end参数.py  # sep 分隔符 / end 结尾
│   ├── 03_print格式化输出.py      # %、format()、f-string
│   ├── 04_综合案例_打印图形.py    # 用 print 打印各种图形
│   └── README.md                  # print 笔记
│
├── py的判断语句使用/              # 🐾 if 判断语句
│   ├── if类型的使用/              # if / if-else / elif / 嵌套
│   └── 布尔类型和比较运算符/      # 布尔、比较、逻辑运算
│
├── 循环语句的运用/               # 🐾 循环语句
│   ├── for循环/
│   │   └── for输出乘法表.py       # for 输出九九乘法表
│   ├── While语句/
│   │   └── 猜数.py               # while 猜数字小游戏
│   └── 循环中断/                  # break / continue 循环控制
│       ├── 01_break.py           # break 跳出循环
│       └── 02_continue.py        # continue 跳过本次
│
├── 键盘输入/                     # ⌨️ 键盘输入（input 练习）
├── 字符串拓展/                   # 🔤 字符串拓展（方法练习）
│
├── python数据容器/               # 📦 五大数据容器
│   ├── List/                     # 列表：定义、常用操作、遍历
│   ├── Tuple/                    # 元组：定义与案例
│   ├── str/                      # 字符串：遍历、分割、比大小
│   ├── dict字典/                 # 字典：定义、操作、案例
│   ├── set集合/                  # 集合：定义、案例、遍历
│   ├── 序列的切片操作/           # 切片操作实战
│   ├── README.md                 # 容器通用操作笔记
│   └── 认识数据类型.md
│
├── py函数/                       # 🎯 函数基础
│   ├── 函数语法及应用.py         # 函数的定义与调用
│   ├── 函数返回值.py / 返回值none.py
│   ├── 函数的变量作用域.py / 内部定义全局变量.py
│   ├── 函数的嵌套调用.py
│   ├── 函数说明文档.py           # 函数文档字符串
│   ├── 01_案例/
│   │   └── 检查核酸.py           # 函数小案例
│   └── 02_综合案例/
│       └── 模拟ATM.py            # ⭐ 模拟 ATM 存取款系统
│
├── py函数进阶/                   # 🚀 函数进阶
│   ├── return.py                 # 多返回值
│   ├── 传入参数的方式.py         # 参数传递方式
│   └── 匿名函数/
│       ├── lambda关键字.py       # lambda 表达式
│       └── 函数逻辑传递.py
│
├── py异常/                       # ⚠️ 异常处理
│   ├── bug_past/                 # 异常案例
│   ├── catch_bug/
│   │   ├── TyrCatch.py           # try/except 捕获
│   │   └── 666.txt               # 测试文件
│   └── README.md                 # 异常语法笔记
│
├── pyMode/                       # 📦 模块导入
│   ├── import模块.py             # import / from / as 用法
│   ├── py模块.md                 # 模块学习笔记
│   └── DiyPyMode/                # 自定义模块练习
│
├── PythonPackage/                # 📦 包与导入机制
│   ├── my_package/               # 示例包（__init__.py）
│   ├── test.py                   # 包导入测试
│   └── README.md                 # ⭐ 导入机制完全指南
│
├── py的文件操作/                 # 📁 文件操作
│   ├── read/                     # 文件读取（read/readlines/readline）
│   ├── write/                    # 文件写入
│   ├── 文件的追加/               # 追加模式 a
│   ├── 综合案例.py               # ⭐ 账单分类处理
│   ├── bill.txt / bill.txt.bak / bill_test.txt
│   └── README.markdown           # 文件操作笔记
│
├── error,mode,package的综合案例/ # 🧩 综合案例（错误+模块+包）
│   ├── test.py                   # 综合调用测试
│   └── my_utils/                 # 自建工具包
│       ├── __init__.py           # 预导入 + __all__
│       ├── file_util.py          # 文件工具函数
│       └── str_util.py           # 字符串工具函数
│
├── test.txt                      # 最外层测试读取文件
└── README.md                     # 📖 本文件（就是你正在看的喵！）
```

---

## 🗺️ 学习路线图

按照学习顺序，大概是这样的喵：

```
第 1 步：基础语法
  ├── print 输出 → 键盘输入 → 判断语句 → 循环语句
  └── 字符串拓展

第 2 步：数据容器
  ├── List / Tuple / str / dict / set
  └── 序列的切片操作

第 3 步：函数
  ├── 基础：返回值、作用域、嵌套、None、文档
  └── 进阶：多返回值、参数传递、lambda

第 4 步：异常处理（try / except / finally）

第 5 步：模块与包
  ├── pyMode        → 模块的导入方式
  └── PythonPackage → 包的机制（__init__.py、__all__）

第 6 步：文件操作（读、写、追加）

第 7 步：综合案例（把所学全部串起来！）
```

> 💡 建议按这个顺序学习，前面的内容是后面案例的基础喵～

---

## ✨ 项目亮点

### ⭐ 模拟 ATM 存取款系统（`py函数/02_综合案例/模拟ATM.py`）
运用函数、`global` 全局变量、`while` 循环、异常处理实现的
简易银行系统：支持 **查询余额 / 存款 / 取款 / 退出**，取款还有余额判断喵！

### ⭐ 账单文件处理（`py的文件操作/综合案例.py`）
读取 `bill.txt` 账单，按「正式/测试」标记分类写入两个不同的文件，
是文件读写 + 字符串处理的综合练习喵！

### ⭐ 自建工具包 my_utils（`error,mode,package的综合案例/my_utils/`）
自己动手封装了 `file_util.py`（文件工具）和 `str_util.py`（字符串工具），
并通过 `__init__.py` 的 `from . import` 预导入 + `__all__` 控制导入范围，
把模块与包的知识用到了实处喵！

---

## 🚀 如何运行

1. **激活虚拟环境**（推荐使用项目自带的 `.venv`）：
   ```powershell
   # Windows
   .\.venv\Scripts\Activate.ps1
   ```
2. **直接运行任意示例**：
   ```powershell
   python .\py函数\02_综合案例\模拟ATM.py
   python .\循环语句的运用\While语句\猜数.py
   python .\error,mode,package的综合案例\test.py
   ```
3. **注意**：部分案例（如综合案例）依赖**相对路径**读取文件，
   建议直接在对应目录下运行，或把路径改成绝对路径喵～

---

## 🛠️ 环境信息

| 项目 | 说明 |
|------|------|
| 语言 | Python 3.14（虚拟环境 `.venv` 内） |
| IDE | PyCharm（`.idea/` 配置） |
| 版本控制 | Git，分支 `main` |
| 远程仓库 | https://github.com/RiChenyv/PythonProject.git |
| 第三方依赖 | 无（纯标准库学习项目） |

---

## 📌 小贴士（踩坑记录）

- 🐍 路径字符串建议用 **`r"..."` 原始字符串** 或 `/` 正斜杠，避免转义坑喵！
- 📦 `__all__` 只是名单，真正导入子模块要靠 `__init__.py` 里的 `from . import` 喵！
- 🔄 `for` 循环可以遍历所有容器，但 `set`/`dict` 不能下标索引，不能用 `while` 遍历喵！
- 🎯 函数里修改全局变量要记得 `global` 声明喵！

---

## 🐾 最后

> 感谢你看到这里喵！
> 希望这份学习笔记能帮你（或者未来的自己）快速回忆起每个知识点喵～
> 喵呜～一起加油，把 Python 学得棒棒哒！🐾

*README 由喵喵助手整理生成，祝你学习愉快喵！✨*

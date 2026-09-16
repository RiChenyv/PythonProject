# 🐱 PythonProject —— 喵喵的 Python 学习乐园

> 这里记录了一位小可爱从 **Python 小白** 一路打怪升级的学习足迹喵～
> 从最基础的输出与输入，到函数、异常、模块包，再到文件操作、
> JSON 数据可视化，最后冲进面向对象的世界喵！每一步都是认真敲出来的喵！🐾

---

## 📖 项目简介

本仓库是 **Python 学习项目**，按「由浅入深」的顺序整理了各类学习笔记、
示例代码与综合练习，包含：

- ✅ 基础语法：print 输出、键盘输入、判断语句、循环语句
- ✅ 数据容器：List、Tuple、str、dict、set、序列切片
- ✅ 函数：返回值、变量作用域、嵌套调用、lambda 匿名函数
- ✅ 异常处理：`try / except / finally`
- ✅ 模块与包：`import` 的四种形式、`__init__.py`、`__all__`
- ✅ 文件操作：读取、写入、追加、`with open`
- ✅ JSON 与数据可视化：pyecharts 折线图 / 柱状图 / 地图
- ✅ 面向对象：类与对象、封装、继承、多态、类型注解
- ✅ SQL：MySQL 语法梳理与实战案例
- ✅ 大数据：PySpark RDD 算子与实战案例
- ✅ Python 高阶技巧：闭包、装饰器、多线程、socket 网络编程、设计模式
- ✅ 综合案例：模拟 ATM、账单处理、三国新冠折线图、GDP 动态排行榜、数据分析案例

> 🎯 目标：**快乐学习，扎实基础，喵生圆满！**

---

## 🌳 目录结构

```
D:\PythonProject
├── .python-version               # 指定 Python 3.14（uv 依赖管理器用）
├── pyproject.toml                # 项目与依赖配置（uv）
├── uv.lock                       # 锁定依赖版本（由 `uv sync`/`uv lock` 生成，用于可复现构建）
├── src/pythonproject/            # 项目包（uv 脚手架，含 __init__.py 入口）
├── .venv/                        # Python 虚拟环境（本机开发用）
├── .idea/                        # PyCharm 项目配置
├── images/                       # 学习笔记配图（截图、总结图）
│   ├── totally.jpg               # 数据容器总结图
│   ├── 文件读取操作总结_01.jpg
│   └── 微信图片_*.jpg            # 容器转换笔记图
│
├── 01-print输出/                 # 🖨️ print 输出语句
│   ├── 01_print基础使用.py        # print 基础用法
│   ├── 02_print的sep和end参数.py  # sep 分隔符 / end 结尾
│   ├── 03_print格式化输出.py      # %、format()、f-string
│   ├── 04_综合案例_打印图形.py    # 用 print 打印各种图形
│   └── README.md                  # print 笔记
│
├── 02-键盘输入/                  # ⌨️ 键盘输入（input 练习）
│   ├── 01_input基础使用.py        # input 基础用法
│   ├── 02_输入类型转换.py         # int / float 类型转换
│   ├── 03_综合案例_加法计算器.py  # 简易加法计算器
│   └── README.md
│
├── 03-判断语句/                  # 🐾 if 判断语句
│   ├── if类型的使用/              # if / if-else / elif / 嵌套
│   ├── 布尔类型和比较运算符/      # 布尔、比较、逻辑运算
│   └── README.md
│
├── 04-循环语句/                  # 🔄 循环语句
│   ├── for循环/
│   │   └── for输出乘法表.py       # for 输出九九乘法表
│   ├── While语句/
│   │   └── 猜数.py               # while 猜数字小游戏
│   ├── 循环中断/                  # break / continue 循环控制
│   └── README.md
│
├── 05-字符串拓展/                # 🔤 字符串拓展（方法练习）
│   ├── 01_字符串拼接与重复.py
│   ├── 02_字符串格式化.py
│   ├── 03_字符串常用方法.py
│   ├── 04_字符串判断方法.py
│   └── README.md
│
├── 06-数据容器/                  # 📦 五大数据容器
│   ├── List/                     # 列表：定义、常用操作、遍历
│   ├── Tuple/                    # 元组：定义与案例
│   ├── str/                      # 字符串：遍历、分割、比大小
│   ├── dict字典/                 # 字典：定义、操作、案例
│   ├── set集合/                  # 集合：定义、案例、遍历
│   ├── 序列的切片操作/           # 切片操作实战
│   ├── README.md                 # 容器通用操作笔记
│   └── 认识数据类型.md
│
├── 07-函数基础/                  # 🎯 函数基础
│   ├── 函数语法及应用.py         # 函数的定义与调用
│   ├── 函数返回值.py / 返回值none.py
│   ├── 函数的变量作用域.py / 内部定义全局变量.py
│   ├── 函数的嵌套调用.py
│   ├── 函数说明文档.py           # 函数文档字符串
│   ├── 01_案例/
│   │   └── 检查核酸.py           # 函数小案例
│   ├── 02_综合案例/
│   │   └── 模拟ATM.py            # ⭐ 模拟 ATM 存取款系统
│   └── README.md
│
├── 08-函数进阶/                  # 🚀 函数进阶
│   ├── return.py                 # 多返回值
│   ├── 传入参数的方式.py         # 参数传递方式
│   ├── 匿名函数/                 # lambda 表达式
│   └── README.md
│
├── 09-异常处理/                  # ⚠️ 异常处理
│   ├── bug_past/                 # 异常案例
│   ├── catch_bug/                # try/except 捕获
│   └── README.md                 # 异常语法笔记
│
├── 10-模块导入/                  # 📦 模块导入
│   ├── import模块.py             # import / from / as 用法
│   ├── py模块.md                 # 模块学习笔记
│   ├── DiyPyMode/                # 自定义模块练习
│   └── README.md
│
├── 11-包与导入/                  # 📦 包与导入机制
│   ├── my_package/               # 示例包（__init__.py）
│   ├── test.py                   # 包导入测试
│   └── README.md                 # ⭐ 导入机制完全指南
│
├── 12-文件操作/                  # 📁 文件操作
│   ├── read/                     # 文件读取（read/readlines/readline）
│   ├── write/                    # 文件写入
│   ├── 文件的追加/               # 追加模式 a
│   ├── 综合案例.py               # ⭐ 账单分类处理
│   ├── bill.txt / bill.txt.bak / bill_test.txt
│   └── README.markdown           # 文件操作笔记
│
├── 13-JSON入门/                  # 📄 JSON 格式入门
│   ├── json数据格式.py           # dumps / loads 互相转化
│   ├── Learnjson                 # JSON 学习笔记
│   └── README.md
│
├── 14-json原始数据/              # 📊 原始数据仓库（各项目数据源头）
│   ├── 原始数据/
│   │   ├── covid19_2022_美国.txt # 新冠数据（JSON 格式）
│   │   ├── covid19_2022_日本.txt
│   │   ├── covid19_2022_印度.txt
│   │   ├── totallynum.txt        # 三国汇总数据
│   │   ├── 各国GDP_1960-2026.txt # GDP 数据（CSV 格式）
│   │   ├── 2026年1、2月销售数据.txt
│   │   └── 搜索引擎日志.txt      # 🔍 日志（时间/词/IP，\t 分隔）
│   └── 搜索引擎json数据处理返回/ # Case_03.py 的 JSON 输出（Spark 产物）
│
├── 15-可视化入门/                # 📈 pyecharts 可视化入门
│   ├── 基础折线图.py             # 四步画出折线图
│   ├── set_global_opts方法.py    # 全局配置项详解
│   └── render.html               # 生成的图表网页
│
├── 16-折线图开发/                # 📐 三国新冠数据折线图
│   ├── 折线图开发.py             # ⭐ 主程序（6 张图 Tab 切换）
│   └── render.html               # 生成的图表网页
│
├── 17-可视化柱状图/              # 📊 GDP 动态排行榜
│   ├── main.py                   # ⭐ Timeline 动态柱状图
│   └── GDP图标.html              # 生成的动态图表
│
├── 18-可视化地图/                # 🗺️ 中国地图可视化
│   ├── test.py                   # Map + VisualMap 分段配色
│   ├── render.html               # 生成的地图网页
│   └── 国内疫情地图的构建.py     # 🚧 未完成
│
├── 19-error、mode、package综合案例/  # 🧩 综合案例（错误+模块+包）
│   ├── test.py                   # 综合调用测试
│   ├── my_utils/                 # 自建工具包
│   └── README.md
│
├── 20-python面向对象/            # 🐍 面向对象（OOP）
│   ├── 学习内容/                 # 9 个主题：对象/方法/构造/封装/继承/多态...
│   ├── 练习案例/                 # 私有成员手机 + 数据分析案例
│   └── README.md
│
├── 21-SQL入门和实战/               # 🐬 MySQL 学习笔记
│   ├── README.md                 # 语法梳理 + 实战案例
│   ├── pymysql入门.py            # 🐍 Python 连接 MySQL 基础操作
│   └── 综合案例/                  # 📦 销售数据上传 MySQL 案例
│       ├── data_define.py        # Record 数据封装类
│       ├── File_define.py        # txt / JSON 文件读取器
│       ├── 综合案例.py           # ⭐ 读取 → 上传 → 验证
│       ├── 读取数据库.py         # ⭐ 从数据库读出 → 转 JSON
│       └── json数据.txt          # 读取数据库.py 的输出
│
├── 22-pyspark实战/                # 🔥 PySpark 大数据入门
│   ├── 使用pyspark/              # 环境搭建（SparkConf/Context）
│   ├── 数据输入/                  # RDD 创建（parallelize/textFile）
│   ├── 数据计算/                  # map/flatMap/reduceByKey/filter/sortBy
│   ├── 数据输出/                  # collect/count/reduce/take + saveAsTextFile
│   ├── 实战案例/                  # ⭐ 词频统计/省份汇总/搜索引擎日志分析
│   └── README.md
│
├── 23-python高阶技巧/             # 🔧 Python 高阶技巧
│   ├── 闭包/                      # 闭包 + nonlocal（ATM 案例）
│   ├── 装饰器/                    # 闭包写法 + @ 语法糖
│   ├── 多线程/                    # threading 多线程
│   ├── 网络编程/                  # ⭐ socket 聊天室（服务端/客户端）
│   ├── 设计模式/                  # 单例模式 + 工厂模式
│   └── README.md
│
├── test1/ test2/                  # 📁 PySpark saveAsTextFile 输出目录
│   └── README.md                 # 输出说明
│
├── test.txt                      # 最外层测试读取文件
└── README.md                     # 📖 本文件（就是你正在看的喵！）
```

---

## 🗺️ 学习路线图

按照学习顺序，大概是这样的喵：

```
第 1 步：基础语法
  ├── 01-print输出 → 02-键盘输入 → 03-判断语句 → 04-循环语句
  └── 05-字符串拓展

第 2 步：数据容器（06-数据容器）
  ├── List / Tuple / str / dict / set
  └── 序列的切片操作

第 3 步：函数
  ├── 07-函数基础：返回值、作用域、嵌套、None、文档
  └── 08-函数进阶：多返回值、参数传递、lambda

第 4 步：异常处理（09-异常处理，try / except / finally）

第 5 步：模块与包
  ├── 10-模块导入  → 模块的导入方式
  └── 11-包与导入  → 包的机制（__init__.py、__all__）

第 6 步：文件操作（12-文件操作，读、写、追加）

第 7 步：JSON 与数据可视化
  ├── 13-JSON入门      → JSON 格式与 dumps/loads
  ├── 14-json原始数据  → 原始数据仓库（新冠 + GDP + 销售数据）
  ├── 15-可视化入门    → pyecharts 入门
  ├── 16-折线图开发    → 三国新冠数据折线图
  ├── 17-可视化柱状图  → GDP 动态排行榜（Timeline）
  └── 18-可视化地图    → 中国地图可视化（Map）

第 8 步：面向对象（20-python面向对象）
  ├── 学习内容：对象 / 成员方法 / 构造 / 魔术方法 / 封装 / 继承 / 多态 / 类型注解
  └── 练习案例：数据分析案例（销售额柱状图）

第 9 步：SQL 数据库（21-SQL入门和实战）
  └── MySQL 语法梳理：DDL / DML / DQL / 约束 / 多表查询 / 事务 + pymysql 实战案例

第 10 步：大数据（22-pyspark实战）
  └── PySpark 入门：RDD 创建 + 六大算子 + saveAsTextFile 输出 + 词频统计/省份汇总/搜索引擎日志分析

第 11 步：Python 高阶技巧（23-python高阶技巧）
  └── 闭包 → 装饰器 → 多线程 → socket 网络编程 → 设计模式（单例/工厂）

第 12 步：综合案例（19-error、mode、package综合案例，把所学全部串起来！）
```

> 💡 建议按这个顺序学习，前面的内容是后面案例的基础喵～

---

## ✨ 项目亮点

### ⭐ 模拟 ATM 存取款系统（`07-函数基础/02_综合案例/模拟ATM.py`）
运用函数、`global` 全局变量、`while` 循环、异常处理实现的
简易银行系统：支持 **查询余额 / 存款 / 取款 / 退出**，取款还有余额判断喵！

### ⭐ 账单文件处理（`12-文件操作/综合案例.py`）
读取 `bill.txt` 账单，按「正式/测试」标记分类写入两个不同的文件，
是文件读写 + 字符串处理的综合练习喵！

### ⭐ 三国新冠数据折线图（`16-折线图开发/折线图开发.py`）
读取美、日、印三国 2022 年新冠 **JSON 数据**，用 pyecharts 批量绘制
「确诊 / 新增 / 死亡」折线图，还能用 `Tab` 按钮切换对比喵！

### ⭐ GDP 动态排行榜（`17-可视化柱状图/main.py`）
读取 1960~2026 各国 GDP 数据，用 `Timeline` 时间线自动播放
**每年全球前八** 的横向柱状图，数据处理 + 排序 + 动态可视化一步到位喵！

### ⭐ 中国地图可视化（`18-可视化地图/test.py`）
用 `Map` + `VisualMapOpts` 分段配色画出中国地图，
数值区间自动上色，是地图可视化的入门案例喵！

### ⭐ 数据分析案例（`20-python面向对象/练习案例/数据分析案例/数据分析案例.py`）
用**面向对象思想**（抽象类 + 多态）读取 txt / JSON 两种格式的销售数据，
封装成对象再汇总绘图，是 OOP + 数据分析 + 可视化的综合实战喵！

### ⭐ pymysql 数据库实战（`21-SQL入门和实战/`）
让 Python 与 MySQL 真正联动喵！
- [`pymysql入门.py`](21-SQL入门和实战/pymysql入门.py)：连接测试、查询、插入一条龙
- [`综合案例/`](21-SQL入门和实战/综合案例/综合案例.py)：读取销售数据 → 封装成对象 → **批量上传 MySQL** → SELECT 验证，
  是 SQL + 面向对象 + 文件处理的综合实战喵！

### ⭐ PySpark 大数据实战（`22-pyspark实战/`）
用 PySpark 处理大数据喵！
- [`Case_01.py`](22-pyspark实战/实战案例/Case_01.py)：`flatMap 切词 → map (词,1) → reduceByKey` 经典**词频统计**
- [`Case_2.py`](22-pyspark实战/实战案例/Case_2.py)：解析 JSON 销售数据，`reduceByKey` **按省份汇总销售额**
- [`Case_03.py`](22-pyspark实战/实战案例/Case_03.py)：**搜索引擎日志分析**——热门搜索时段/热门搜索词/各词最热时段 + `map 构造字典 → saveAsTextFile` 输出 JSON，
  是 RDD 算子 + 数据处理的大数据实战喵！

### ⭐ socket 聊天室（`23-python高阶技巧/网络编程/`）
用 socket + threading 实现**双人聊天**喵！
- [`服务端.py`](23-python高阶技巧/网络编程/服务端.py)：`bind → listen → accept` 等连接
- [`客户端.py`](23-python高阶技巧/网络编程/客户端.py)：`connect` 连上就聊
- `receve.py`：线程循环收消息，输入 `exit` 断开，
  是网络编程 + 多线程 + 闭包的综合实战喵！

### ⭐ 自建工具包 my_utils（`19-error、mode、package综合案例/my_utils/`）
自己动手封装了 `file_util.py`（文件工具）和 `str_util.py`（字符串工具），
并通过 `__init__.py` 的 `from . import` 预导入 + `__all__` 控制导入范围喵！

---

## 🚀 如何运行

### 方式一：用 uv（推荐）

```powershell
uv sync                       # 按 pyproject.toml / uv.lock 创建 .venv 并安装依赖
                              # 镜像已设为清华 TUNA（见 pyproject.toml 的 [[tool.uv.index]]）
uv run pythonproject          # 运行项目包入口（src/pythonproject/__init__.py 的 main）
uv run python .\07-函数基础\02_综合案例\模拟ATM.py   # 用 uv 环境跑任意示例
```

### 方式二：手动激活 `.venv`（传统方式）

1. **激活虚拟环境**（推荐使用项目自带的 `.venv`）：
   ```powershell
   # Windows
   .\.venv\Scripts\Activate.ps1
   ```
2. **直接运行任意示例**：
   ```powershell
   python .\07-函数基础\02_综合案例\模拟ATM.py
   python .\04-循环语句\While语句\猜数.py
   python .\16-折线图开发\折线图开发.py      # 需要 pyecharts
   python .\20-python面向对象\练习案例\数据分析案例\数据分析案例.py
   python .\21-SQL入门和实战\综合案例\综合案例.py   # 需要 pymysql + 本机 MySQL 服务
   ```
3. **注意**：部分案例（如综合案例、可视化项目）依赖**绝对路径**读取数据文件，
   运行前请确认路径中的 `D:\PythonProject\...` 指向正确喵～

---

## 🛠️ 环境信息

| 项目 | 说明 |
|------|------|
| 语言 | Python 3.14（`.python-version` 指定，虚拟环境 `.venv` 内） |
| 依赖管理 | [uv](https://docs.astral.sh/uv/)（`pyproject.toml`，src 布局可安装包，`uv.lock` 锁定版本） |
| IDE | PyCharm（`.idea/` 配置） |
| 版本控制 | Git，分支 `main` |
| 远程仓库 | https://github.com/RiChenyv/PythonProject.git |
| 第三方依赖 | pyecharts 2.1.0（数据可视化）、pymysql（连接 MySQL）、pyspark 4.2.0（大数据） |

---

## 📌 小贴士（踩坑记录）

- 🐍 路径字符串建议用 **`r"..."` 原始字符串** 或 `/` 正斜杠，避免转义坑喵！
- 📦 `__all__` 只是名单，真正导入子模块要靠 `__init__.py` 里的 `from . import` 喵！
- 🔄 `for` 循环可以遍历所有容器，但 `set`/`dict` 不能下标索引，不能用 `while` 遍历喵！
- 🎯 函数里修改全局变量要记得 `global` 声明喵！
- 🧬 类里成员方法第一个参数一定是 `self`，私有成员用 `__` 开头喵！

---

## 🐾 最后

> 感谢你看到这里喵！
> 希望这份学习笔记能帮你（或者未来的自己）快速回忆起每个知识点喵～
> 喵呜～一起加油，把 Python 学得棒棒哒！🐾

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！按学习路线 01→22 把整个项目的核心知识点浓缩成一张表，每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | 基础输入输出 | `01-print输出/01_print基础使用.py` | `print()` 逗号多参、`sep`/`end` 控制分隔与结尾；`input()` 永远返回字符串，参与运算前要 `int()`/`float()` 转换喵 |
| 2 | 判断语句 | `03-判断语句/if类型的使用/03_if_elif_else.py` | `if`-`elif`-`else` 从上往下命中即止；布尔 `True/False`、比较运算、`and`/`or`/`not` 逻辑运算（闰年判断）喵 |
| 3 | 循环与中断 | `04-循环语句/循环中断/01_break.py` | `for`+`range`、`while` 遍历；`break` 结束整个循环、`continue` 跳过本次，只作用于当前层喵 |
| 4 | 字符串拓展 | `05-字符串拓展/03_字符串常用方法.py` | `strip`/`split`/`join`/`replace`/`find`/`count` 全家桶；`isdigit()` 校验输入；f-string 格式化最推荐喵 |
| 5 | 数据容器 | `06-数据容器/List/02_list常用操作.py` | List 可变 / Tuple 不可变 / set 去重无序 / dict 键值对；序列切片 `[起:止:步]`；set/dict 不能下标索引喵 |
| 6 | 函数 | `07-函数基础/函数语法及应用.py` | `def` 定义、`return` 返回值、无 return 返回 `None`；局部/全局变量、`global` 声明；进阶见 08 的 lambda 喵 |
| 7 | 异常处理 | `09-异常处理/catch_bug/TyrCatch.py` | `try`/`except`/`else`/`finally` 四件套；`except Exception` 兜底；异常会沿调用链一路往上抛喵 |
| 8 | 模块与包 | `11-包与导入/test.py` | `import` 四种形式；包 = 文件夹 + `__init__.py`；`__all__` 只是名单，真正导入靠 `from . import` 喵 |
| 9 | 文件操作 | `12-文件操作/综合案例.py` | `r`/`w`/`a` 三种模式、`with open` 自动关闭、`read`/`readlines`/`readline` 区分、别忘了 `encoding="utf-8"` 喵 |
| 10 | JSON 与可视化 | `16-折线图开发/折线图开发.py` | `json.dumps`/`loads` 互转（`ensure_ascii=False` 保中文）；pyecharts `Line`/`Bar`/`Map`/`Timeline` 画图、`Tab` 多图切换喵 |
| 11 | 面向对象 | `20-python面向对象/学习内容/6-继承/phone_1.0.py` | `__init__` 构造、`__` 私有成员、多继承、`super()` 调父类、多态；数据分析案例用抽象类 + 多态实战喵 |
| 12 | SQL 与大数据 | `21-SQL入门和实战/pymysql入门.py` | pymysql 连接 → 游标 → `execute` → `fetchall` 上传数据；PySpark RDD `flatMap→map→reduceByKey` 词频统计喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ **Windows 路径转义**：全项目大量硬编码 `D:/PythonProject/...` 或 `r"D:\..."` 绝对路径，忘写 `r` 前缀时 `\t`、`\n`、`\1` 会被当成转义符；而且换台电脑目录一变就 `FileNotFoundError`，建议改用相对路径或 `Path(__file__)` 喵（见 `17-可视化柱状图/main.py`、`22-pyspark实战/数据输入/rdd.py`）。
2. ⚠️ **`input()` 永远返回字符串**：01~04 文件夹几乎所有案例都要先 `int()`/`float()` 转换再比较或运算，忘了转直接 `age >= 18` 就报错；转换前最好先用 `isdigit()` 校验输入喵。
3. ⚠️ **文件读写三连坑**：`w` 模式会清空原内容、`write()` 不自动换行要自己拼 `'\n'`、`read()` 完指针到末尾再 `readlines()` 读到空；读中文文件不写 `encoding="utf-8"` 会乱码，`12-文件操作/综合案例.py` 还把输出文件名写成了 `bill_test.txt.`（末尾多个点）喵！
4. ⚠️ **函数作用域与 None**：函数里改全局变量要先 `global` 声明（`07-函数基础/02_综合案例/模拟ATM.py` 的正确示范），忘了声明只会新建局部变量、外面根本改不到；没写 `return` 的函数返回的是 `None`，别拿它当数字继续运算喵。
5. ⚠️ **模块包的「名单」陷阱**：`__all__` 只是导出名单，不写 `from . import` 照样导不进子模块（`19-error、mode、package综合案例/my_utils/__init__.py` 的正确写法是两行都写）；目录名带数字/连字符（如 `11-包与导入`）不能直接写进 `import`，要用 `importlib.import_module` 绕开喵。
6. ⚠️ **编码与密码安全**：JSON 读写都要 `ensure_ascii=False` 保中文、文件读写统一 `utf-8`；数据库密码已改为从环境变量 `MYSQL_PASSWD` 读取（`21-SQL入门和实战/pymysql入门.py`、`综合案例/综合案例.py`、`读取数据库.py`），不再明文写死，SQL 也别用 f-string 硬拼（防注入）喵！

*README 由喵喵助手整理生成，祝你学习愉快喵！✨*

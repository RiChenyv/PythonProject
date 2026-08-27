# 🔥 22-pyspark实战 —— PySpark 大数据入门

> 记录 **PySpark** 的学习实战喵～
> 从环境搭建到 RDD 算子，再到实战案例，向大数据世界进发喵！🐱

---

## 📁 目录

```
22-pyspark实战
├── 使用pyspark/
│   └── 学习引入.py            # ⭐ 环境搭建（SparkConf + SparkContext）
├── 数据输入/
│   └── rdd.py                 # RDD 创建（parallelize / textFile）
├── 数据计算/                  # RDD 算子练习
│   ├── MAP方法的使用.py        # map 一对一映射
│   ├── FlatMap方法的使用.py    # flatMap 扁平化
│   ├── ReduceByKey.py         # reduceByKey 按键聚合
│   ├── distinct方法的使用/
│   │   └── distinct使用.py     # distinct 去重
│   ├── filterf方法/
│   │   └── filter方法使用.py   # filter 过滤
│   └── sortBy算子的使用/
│       └── sortBy算子的使用.py # sortBy 排序
├── 实战案例/
│   ├── Case_01.py             # ⭐ 词频统计（文本）
│   └── Case_2.py              # ⭐ 按省份汇总销售额（JSON）
└── README.md                  # 本文件
```

---

## 🔍 内容说明

### 1. 环境搭建（`使用pyspark/学习引入.py`）

```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark")
sc = SparkContext(conf=conf)
print(sc.version)   # 测试是否成功
sc.stop()
```

- `setMaster("local[*]")`：本地模式运行（`*` 表示用满所有 CPU 核）
- `setAppName("名字")`：给任务起名字
- `SparkContext`（sc）：一切操作的入口，用完记得 `sc.stop()` 喵！

> ⚠️ **踩坑提醒**：部分机器需要设置 Python 解释器路径喵：
> ```python
> import os
> os.environ['PYSPARK_PYTHON'] = r"C:\...\python.exe"  # 指向你的 Python
> ```

### 2. RDD 创建（`数据输入/rdd.py`）

RDD = 弹性分布式数据集，Spark 的基本数据单位喵！

| 方法 | 作用 | 例子 |
|------|------|------|
| `sc.parallelize(集合)` | 从内存集合创建 | `[1,2,3]`、字典、字符串 |
| `sc.textFile(路径)` | 从文件创建（**按行**读取） | 读取销售数据 txt |

```python
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])     # 从列表创建
rdd2 = sc.parallelize({"key": 1, "key2": 2})  # 从字典创建
rdd3 = sc.textFile(r"D:\...\2026年1月销售数据.txt")  # 从文件创建
print(rdd.collect())   # collect() 把 RDD 收回到本地查看
```

### 3. RDD 算子（`数据计算/`）—— 重点喵！

| 算子 | 作用 | 例子 |
|------|------|------|
| `map(函数)` | **一对一**转换每个元素 | `rdd.map(lambda x: x * 10)` |
| `flatMap(函数)` | 先映射再**解嵌套**（扁平化） | `rdd.flatMap(lambda x: x.split(" "))` |
| `reduceByKey(函数)` | 按键**分组聚合**（kv 数据） | `rdd.reduceByKey(lambda a, b: a + b)` |
| `distinct()` | **去重** | `rdd.distinct()` |
| `filter(函数)` | **过滤**（保留 True 的） | `rdd.filter(lambda x: x % 2 == 0)` |
| `sortBy(函数)` | **排序**（ascending 升降序、numPartitions 分区） | `rdd.sortBy(lambda x: x[1], ascending=True)` |

> 💡 **map vs flatMap 喵**：
> - `map`：1 个元素 → 1 个元素（一对一）
> - `flatMap`：1 个元素 → 多个元素（先 split 再摊平，比如一句话拆成多个单词喵！）

---

## 🏆 实战案例

### 📝 Case_01.py —— 词频统计（文本）

对销售数据 txt 做**分词统计**，经典 WordCount 流程喵：

```python
rdd = sc.textFile(r"D:\...\2026年1月销售数据.txt")
# ① 按逗号切分并摊平（每行 → 多个词）
world_rdd = rdd.flatMap(lambda x: x.split(","))
# ② 每个词变成 (词, 1)
world_with_one_rdd = world_rdd.map(lambda word: (word, 1))
# ③ 按键聚合求和（统计每个词出现次数）
result_rdd = world_with_one_rdd.reduceByKey(lambda x, y: x + y)
print(result_rdd.collect())
```

> 🐱 口诀：**flatMap 切词 → map 变 (词,1) → reduceByKey 求和** 喵！

### 📊 Case_2.py —— 按省份汇总销售额（JSON）

对 2 月销售数据（JSON 格式）做**分组统计**喵：

```python
rdd_init = sc.textFile(r"D:\...\2026年2月销售数据.txt")
# ① 过滤掉 JSON 的括号行 [ ] 和空行
json_rdd = rdd_init.filter(lambda line: line.strip() not in ["[", "]", ""]) \
    .map(lambda line: json.loads(line.strip().rstrip(",")))
# ② 取出 (省份, 销售额)
dict_rdd = json_rdd.map(lambda line: (line["销售省份"], round(line["销售额"], 2)))
# ③ 按键聚合：各省份销售额求和
city_with_money_rdd = dict_rdd.reduceByKey(lambda x, y: x + y)
print([(p, f"{m:.2f}") for p, m in city_with_money_rdd.collect()])
```

> 💡 亮点：先 `filter` 清掉 JSON 的括号行，再用 `json.loads` 解析，
> 最后 `reduceByKey` 完成「按省份分组求和」喵！

> 📌 数据来源：[`14-json原始数据/原始数据/`](../14-json原始数据/README.md) 的销售数据文件喵！

---

## 🚀 如何运行

```powershell
# 需要 pyspark（已安装在 .venv 里喵）
.\.venv\Scripts\python.exe .\22-pyspark实战\实战案例\Case_01.py
.\.venv\Scripts\python.exe .\22-pyspark实战\实战案例\Case_2.py
```

> ⚠️ 首次运行会启动 Spark，速度稍慢，耐心等待喵！
> 如果报 Python 解释器错误，记得在代码里设置 `os.environ['PYSPARK_PYTHON']` 喵！

---

## 🎓 本文件夹总结的知识点

1. 🔥 `SparkConf` + `SparkContext` 搭建 PySpark 环境（local 模式）
2. 📦 RDD 创建：`parallelize`（内存）/ `textFile`（文件，按行读）
3. ⚙️ 六大算子：`map` / `flatMap` / `reduceByKey` / `distinct` / `filter` / `sortBy`
4. 📊 `collect()` 收结果，`sc.stop()` 关环境
5. 🏆 WordCount 经典流程：`flatMap 切词 → map (词,1) → reduceByKey 求和`

---

*本笔记由喵喵助手整理，大数据之路启航喵！🐾*

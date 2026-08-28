# 📊 17-可视化柱状图 —— GDP 动态排行榜

> 用 **pyecharts 柱状图 + 时间线** 做全球 GDP 动态排行榜喵！
> 每一年全球前八的 GDP 排行，自动播放动画喵！🐱

---

## 📁 目录

```
17-可视化柱状图
├── main.py               # ⭐ 主程序：GDP 动态柱状图
├── GDP图标.html          # 生成的动态图表网页
└── README.md             # 本文件
```

> 📌 数据来源：[`14-json原始数据/原始数据/各国GDP_1960-2026.txt`](../14-json原始数据/README.md)

---

## 🔍 内容说明

### 1. 数据准备（`main.py` 前半部分）

- 按行读取 `各国GDP_1960-2026.txt`（CSV 格式），`pop(0)` 删掉表头
- `for` 循环逐行处理，`split(",")` 取出 `年份 / GDP / 国家`
- 用 **字典** 按年份归类：`data_dict[year] = [[国家, GDP], ...]`
- `try/except KeyError` 处理「年份第一次出现」的情况喵！

```python
try:
    data_dict[year].append([country, GDP])
except KeyError:          # year 第一次出现时还没有 key
    data_dict[year] = []
    data_dict[year].append([country, GDP])
```

### 2. 动态柱状图（`main.py` 后半部分）

```
每年数据 → 按 GDP 从大到小排序 → 取前 8 → 横向柱状图 → 加入时间线
```

- `data_dict[year].sort(key=lambda x: x[1], reverse=True)` 按 GDP 降序
- 取前八名，`x_data` / `y_data` 收集数据
- `bar.reversal_axis()` 变成**横向柱状图**（数据要先 reverse 喵！）
- `Timeline` 时间线：按年份自动播放，`play_interval=1000` 每秒一帧
- `ThemeType.LIGHT` 设置明亮主题

```python
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType

time = Timeline({"theme": ThemeType.LIGHT})
time.add(bar, str(year))   # 每年一张图
time.add_schema(play_interval=1000, is_auto_play=True, is_loop_play=True)
time.render("GDP图标.html")
```

### 3. 生成结果（`GDP图标.html`）

浏览器打开即可看到 **1960~2026 全球前八 GDP 动态排行**，
自动播放、可暂停、可拖拽时间轴喵！

---

## 🚀 如何运行

```powershell
# 需要 pyecharts（已安装在 .venv 里喵）
.\.venv\Scripts\python.exe .\17-可视化柱状图\main.py
# 生成后浏览器打开 17-可视化柱状图\GDP图标.html
```

---

## 🎓 本文件夹总结的知识点

1. 📄 CSV 数据处理：`readlines` + `split(",")` + `strip()`
2. 🔀 字典按 key 归类数据，`try/except KeyError` 初始化
3. 📊 pyecharts `Bar` 柱状图：`reversal_axis()` 横向显示
4. 🎞️ `Timeline` 时间线：图表动起来！`add_schema` 控制播放
5. 🎨 `ThemeType` 换主题，`LabelOpts` 控制标签位置

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | CSV 文件读取 | `main.py` | `open(r"路径", encoding="utf-8")` + `readlines()` 按行读，`pop(0)` 删掉表头行 |
| 2 | 逐行清洗与拆分 | `main.py` | `strip()` 去掉换行，`split(",")` 按逗号拆，再按下标取出 年份[0] / GDP[1] / 国家[3] |
| 3 | 字典按年份归类 | `main.py` | `data_dict[year].append([国家, GDP])`，配合 `try/except KeyError` 处理年份第一次出现 |
| 4 | 年份排序 | `main.py` | `sorted(data_dict.keys())` 让年份从小到大，时间线的播放顺序全靠它 |
| 5 | 按 GDP 降序取前八 | `main.py` | `sort(key=lambda x: x[1], reverse=True)` 后切片 `[0:8]`，下标 1 才是 GDP 喵！ |
| 6 | 组装 x/y 轴数据 | `main.py` | 循环把国家名加入 `x_data`、GDP 数值加入 `y_data` |
| 7 | 横向柱状图 | `main.py` | 数据先 `reverse()` 再 `bar.reversal_axis()`，`LabelOpts(position="right")` 让标签在右侧 |
| 8 | 图表全局设置 | `main.py` | `TitleOpts` 用 f-string 生成动态标题，`ToolboxOpts(is_show=True)` 开启工具栏 |
| 9 | Timeline 时间线 | `main.py` | `Timeline({"theme": ThemeType.LIGHT})` 建时间线，`time.add(bar, str(year))` 逐年加图 |
| 10 | 播放控制与导出 | `main.py` | `add_schema(play_interval=1000, is_auto_play=True, is_loop_play=True)`，最后 `render("GDP图标.html")` 生成网页 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ **忘写 `r` 的路径转义坑**：`open(r"D:\...")` 的原始字符串前缀 `r` 不能省，不然 `\1`、`\0` 会被当成转义字符，路径直接报错喵！
2. ⚠️ **不写 `encoding="utf-8"` 的编码坑**：Windows 默认按 GBK 读文件，碰到中文或特殊符号会乱码甚至抛 `UnicodeDecodeError`，读 CSV 一定要带上 `encoding="utf-8"` 喵！
3. ⚠️ **漏掉 `try/except KeyError`**：年份第一次进字典时还没有这个 key，直接 `append` 会崩；except 里要先建空列表再 `append`，顺序写反照样报错喵！
4. ⚠️ **横向柱状图忘了先 `reverse()`**：`reversal_axis()` 之前不把 x/y 数据逆置，排行榜会倒着显示，第一名跑到最底下喵！
5. ⚠️ **`split(",")` 取错下标**：原始 CSV 每列位置固定，年份是 `[0]`、GDP 是 `[1]`、国家是 `[3]`，取错列整组数据就全乱了喵！
6. ⚠️ **排序的 key 选错列**：`sort(key=lambda x: x[1])` 排的是 GDP 不是国家名，也别忘 `reverse=True`，否则会变成从小到大、排行榜变垫底榜喵！

---

*本笔记由喵喵助手整理，动态图表好酷喵！🐾*

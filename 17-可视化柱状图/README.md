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

*本笔记由喵喵助手整理，动态图表好酷喵！🐾*

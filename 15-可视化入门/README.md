# 📈 15-可视化入门 —— pyecharts 入门

> 记录 **pyecharts 数据可视化** 的入门案例喵～
> 几行代码就能画出漂亮的交互式图表喵！🐱

---

## 📁 目录

```
15-可视化入门
├── 基础折线图.py           # ⭐ pyecharts 最简入门
├── set_global_opts方法.py  # 全局配置项详解
├── render.html             # 生成的图表网页
└── README.md               # 本文件
```

---

## 🔍 内容说明

### 1. 基础折线图（`基础折线图.py`）

pyecharts 最简流程，只有 **4 步**喵：

```python
from pyecharts.charts import Line

line = Line()  # 1. 创建图表对象
line.add_xaxis(["中国", "美国", "英国"])  # 2. 添加 X 轴数据
line.add_yaxis("GDP", [30, 20, 10])  # 3. 添加 Y 轴数据（一条线）
line.render()  # 4. 生成网页图表
```

运行后会生成 `render.html`，浏览器打开就能看到交互式折线图喵！

### 2. 全局配置（`set_global_opts方法.py`）

`set_global_opts()` 用来设置图表的全局配置，本案例用到：

| 配置项             | 作用                                           |
|-----------------|----------------------------------------------|
| `TitleOpts`     | 标题：`title` 标题文字、`pos_left` 位置、`pos_top` 顶部偏移 |
| `LegendOpts`    | 图例：`is_show=True` 显示图例                       |
| `ToolboxOpts`   | 工具箱：保存图片、缩放等工具                               |
| `VisualMapOpts` | 视觉映射：颜色渐变表示数值大小                              |

```python
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_top="0%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
```

> 💡 更多配置项还有 `DataZoomOpts`（区域缩放）、
> `TooltipOpts`（提示框）等，用到再查文档喵！

---

## 🚀 如何运行

```powershell
# 需要 pyecharts（已安装在 .venv 里喵）
.\.venv\Scripts\python.exe .\15-可视化入门\基础折线图.py
.\.venv\Scripts\python.exe .\15-可视化入门\set_global_opts方法.py
# 生成后浏览器打开 15-可视化入门\render.html
```

---

## 🎓 本文件夹总结的知识点

1. 📈 pyecharts 四步曲：创建对象 → X 轴 → Y 轴 → `render()`
2. ⚙️ `set_global_opts()` 做全局美化
3. 🖼️ `render()` 生成 `render.html`，浏览器即开即看
4. 🚀 更大规模的实战（多国数据批量绘图）见
   [`16-折线图开发/README.md`](../16-折线图开发/README.md) 喵！

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | 导入 Line 图表类 | `基础折线图.py` | `from pyecharts.charts import Line`，Line 在 `pyecharts.charts` 里喵 |
| 2 | 创建图表对象 | `基础折线图.py` | `line = Line()`，所有操作都从它开始喵 |
| 3 | 添加 X 轴数据 | `基础折线图.py` | `line.add_xaxis(["中国","美国","英国"])`，传的是标签列表 |
| 4 | 添加 Y 轴数据（系列） | `基础折线图.py` | `line.add_yaxis("GDP", [30, 20, 10])`，系列名 + 数值列表，一次调用就是一条线 |
| 5 | 生成网页图表 | `基础折线图.py` | `line.render()` 生成 `render.html`，浏览器打开就能看到交互图喵 |
| 6 | 全局配置入口 | `set_global_opts方法.py` | `line.set_global_opts(...)` 集中管理全局美化配置 |
| 7 | 标题 TitleOpts | `set_global_opts方法.py` | `title="GDP展示"`、`pos_left="center"`、`pos_top="0%"` 控制标题文字与位置 |
| 8 | 图例 LegendOpts | `set_global_opts方法.py` | `LegendOpts(is_show=True)` 显示图例 |
| 9 | 工具箱 ToolboxOpts | `set_global_opts方法.py` | `ToolboxOpts(is_show=True)` 提供保存图片、缩放等交互工具 |
| 10 | 视觉映射 VisualMapOpts | `set_global_opts方法.py` | `VisualMapOpts(is_show=True)` 用颜色渐变表示数值大小 |
| 11 | 配置类从哪导入 | `set_global_opts方法.py` | `from pyecharts.options import TitleOpts, LegendOpts, ...`，别漏了 `options` 喵 |
| 12 | 更多全局配置 | `set_global_opts方法.py` | 还有 `DataZoomOpts`（区域缩放）、`TooltipOpts`（提示框）等，用到再查文档喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ 四步曲顺序不能乱喵：必须先 `add_xaxis()` 再加 `add_yaxis()`，反了会报错或画不出图！
2. ⚠️ `add_yaxis()` 每调用一次就是一条新线（系列），系列名要唯一，重复了图例会打架、颜色混乱喵！
3. ⚠️ `set_global_opts()` 的关键字参数名要带 `_opts` 后缀（如 `title_opts=`、`legend_opts=`），漏写会直接 `TypeError: unexpected keyword argument` 喵！
4. ⚠️ 配置类记得从 `pyecharts.options` 导入，只 `from pyecharts.charts import Line` 就拿 `TitleOpts` 来用会 `NameError` 喵！
5. ⚠️ 两个案例都调用不带文件名的 `render()`，生成的是同一个 `render.html`，后运行的会覆盖先运行的，想保留多份要 `render("别的名字.html")` 喵！
6. ⚠️ `render()` 默认生成到「当前工作目录」，从别的目录运行脚本时 `render.html` 会跑到别处，找不到就先检查运行目录对不对喵！

*本笔记由喵喵助手整理，图表越来越好看喵！🐾*

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
   [`14-json原始数据/README.md`](../16-折线图开发/README.md) 喵！

---

*本笔记由喵喵助手整理，图表越来越好看喵！🐾*

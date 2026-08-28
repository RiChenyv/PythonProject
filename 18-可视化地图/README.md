# 🗺️ 18-可视化地图 —— 中国地图可视化

> 用 **pyecharts 地图** 做中国疫情/数据可视化喵！
> 让数据在地图上「上色」喵！🐱

---

## 📁 目录

```
18-可视化地图
├── test.py                 # ⭐ 中国地图测试案例
├── render.html             # 生成的地图网页
├── 国内疫情地图的构建.py    # 🚧 未完成（空文件，等待主人编写）
└── README.md               # 本文件
```

---

## 🔍 内容说明

### 1. 中国地图（`test.py`）

```python
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 99),
    ("上海市", 91),
    ("河南省", 78),
    ("广东省", 499)
]
map.add("测试", data, "china")    # "china" 是中国地图
map.render()
```

- `Map()` 创建地图对象
- `map.add(系列名, 数据, "china")`：数据是「(地区名, 数值)」列表
- `"china"` 指定中国地图

### 2. 视觉映射分段配色（`VisualMapOpts`）

```python
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,     # 分段显示
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"},
        ]
    )
)
```

- `is_piecewise=True`：把数值**分段**上色
- `pieces` 列表：每段的范围、标签、颜色
- 数值落在哪个区间，地区就显示对应的颜色喵！

### 3. 生成结果（`render.html`）

浏览器打开即可看到带分段配色的中国地图喵！

### 4. 待完成（`国内疫情地图的构建.py`）

目前是 **0 字节空文件**，应该是主人准备写的「国内疫情地图」正式案例喵！
完成方向参考：读取疫情数据 → 按省份整理 → Map 绘图 + 分段配色喵～

---

## 🚀 如何运行

```powershell
# 需要 pyecharts（已安装在 .venv 里喵）
.\.venv\Scripts\python.exe .\18-可视化地图\test.py
# 生成后浏览器打开 18-可视化地图\render.html
```

---

## 🎓 本文件夹总结的知识点

1. 🗺️ `Map` + `add(系列名, [(地区, 数值)], "china")` 画中国地图
2. 🎨 `VisualMapOpts` 视觉映射：`is_piecewise` 分段 + `pieces` 配色
3. 📌 地图数据格式：「(地区名, 数值)」元组列表
4. 🚧 正式案例待完成（`国内疫情地图的构建.py`）

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | Map 地图类导入与创建 | `test.py` | `from pyecharts.charts import Map` 后 `Map()` 创建中国地图对象喵 |
| 2 | 地图数据格式 | `test.py` | 数据是「(地区名, 数值)」元组列表，地区名必须用官方全称喵 |
| 3 | `add()` 添加系列 | `test.py` | `map.add("测试", data, "china")`，第三参 `"china"` 指定中国地图 |
| 4 | `set_global_opts` 全局配置 | `test.py` | 视觉映射等全局选项都通过它设置喵 |
| 5 | `VisualMapOpts` 视觉映射 | `test.py` | `VisualMapOpts(is_show=True, ...)` 控制颜色条的显示与样式 |
| 6 | `is_piecewise` 分段 | `test.py` | `is_piecewise=True` 把连续数值变成分段上色喵 |
| 7 | `pieces` 分段定义 | `test.py` | 每段 `{"min", "max", "label", "color"}`，数值落在区间内就显示对应颜色 |
| 8 | 十六进制颜色 | `test.py` | 颜色用 `#CCFFFF` 这类十六进制色值喵 |
| 9 | `render()` 生成网页 | `test.py` | `map.render()` 输出 `render.html`，浏览器打开即可看 |
| 10 | 异常兜底 | `test.py` | test.py 用 try/except 打印报错，生成失败不会静默挂掉喵 |
| 11 | 待完成案例 | `国内疫情地图的构建.py` | 0 字节空文件，等主人写正式「国内疫情地图」案例喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ 地区名必须用官方全称（如 `"北京市"`、`"广东省"`），写成 `"北京"`/`"广东"` 会匹配不上，地图上那块不上色喵！
2. ⚠️ test.py 里变量名用了 `map`，会覆盖 Python 内置的 `map()` 函数，主人在后面想用 `map()` 时就会踩坑，建议改名 `my_map` 喵！
3. ⚠️ `pieces` 区间是闭区间且不能重叠：`min:1, max:9` 和 `min:10, max:99` 必须无缝衔接；数值超过最大 `max`（如 500+）时没有对应分段，颜色会缺失喵！
4. ⚠️ 忘记写 `map.set_global_opts(...)` 或漏掉 `is_piecewise=True`，就变成连续渐变色，而不是分段配色了喵！
5. ⚠️ `render.html` 依赖 CDN 的 `echarts.min.js` 和 `china.js`，离线或 CDN 挂了时地图会空白喵！
6. ⚠️ 中文标签对编码敏感：`.py` 文件要用 UTF-8 保存，否则地图上的中文标签会乱码喵（render.html 里中文都被转成 `\uXXXX` 转义了喵）！

---

*本笔记由喵喵助手整理，地图点亮喵！🐾*

# 🗺️ 可视化地图 —— 中国地图可视化

> 用 **pyecharts 地图** 做中国疫情/数据可视化喵！
> 让数据在地图上「上色」喵！🐱

---

## 📁 目录

```
可视化地图
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
.\.venv\Scripts\python.exe .\可视化地图\test.py
# 生成后浏览器打开 可视化地图\render.html
```

---

## 🎓 本文件夹总结的知识点

1. 🗺️ `Map` + `add(系列名, [(地区, 数值)], "china")` 画中国地图
2. 🎨 `VisualMapOpts` 视觉映射：`is_piecewise` 分段 + `pieces` 配色
3. 📌 地图数据格式：「(地区名, 数值)」元组列表
4. 🚧 正式案例待完成（`国内疫情地图的构建.py`）

---

*本笔记由喵喵助手整理，地图点亮喵！🐾*

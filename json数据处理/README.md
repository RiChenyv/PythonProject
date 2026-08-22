# 📊 json数据处理 —— 新冠数据折线图开发

> 把 **JSON 数据处理 + pyecharts 可视化** 结合起来的大实战喵～
> 读取美、日、印三国的新冠数据，画出漂亮的折线图喵！🐱

---

## 📁 目录

```
json数据处理
├── 折线图开发.py            # ⭐ 主程序：三国新冠数据折线图
├── render.html             # ⭐ 生成的图表网页（内含 6 张图，浏览器即开即看）
├── 原始数据/                # 原始 JSON 数据文件
│   ├── covid19_2022_美国.txt
│   ├── covid19_2022_日本.txt
│   ├── covid19_2022_印度.txt
│   └── totallynum.txt      # 三国汇总数据
└── README.md               # 本文件
```

---

## 🔍 内容说明

### 1. 原始数据（`原始数据/`）

每个国家的 txt 文件里存的是 **JSON 格式**的数据，结构大致如下：

```json
{
  "data": {
    "name": "日本",
    "日期": [...],
    "num": {
      "确诊": [...],
      "新增": [...],
      "死亡": [...]
    }
  }
}
```

> 💡 文件扩展名虽然是 `.txt`，但内容是一行行的 JSON，
> 用 `json.loads(f.read())` 就能读成 Python 字典喵！

### 2. 主程序（`折线图开发.py`）—— 数据流

```
读取 txt → json.loads 解析 → 取出日期/确诊/新增/死亡 → Line 绘图 → render 生成网页
```

**第一部分：各国独立折线图**
- 用一个字典存三国路径，`for` 循环**批量处理**
- 每个国家一张 `Line` 图：新增 / 确诊 / 死亡 三条线
- `set_global_opts` 设置标题、图例、工具箱

**第二部分：三国对比图**
- 读取 `totallynum.txt` 汇总数据
- 确诊 / 新增 / 死亡 各画一张三国对比图

**第三部分：Tab 按钮切换**
- 用 `Tab()` 把多张图装进一个页面，点按钮切换喵！

```python
from pyecharts.charts import Line, Tab
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts

line = Line()
line.add_xaxis(x_date)
line.add_yaxis("新增", y_data_add)
line.set_global_opts(title_opts=TitleOpts(title="..."), ...)
tab.add(line, "国家名")
tab.render()      # 生成 render.html
```

### 3. 生成结果（`render.html`）

当前版本的 `render.html` 共包含 **6 张图**，用浏览器打开即可交互查看喵：

| # | 图表标题 | 内容 |
|---|----------|------|
| 1 | 美国 2022年度新冠数据统计 | 美国「新增 / 确诊 / 死亡」三条线 |
| 2 | 日本 2022年度新冠数据统计 | 日本「新增 / 确诊 / 死亡」三条线 |
| 3 | 印度 2022年度新冠数据统计 | 印度「新增 / 确诊 / 死亡」三条线 |
| 4 | 美、日、印三国2022年度新冠确诊数据统计 | 三国**确诊**同图对比 |
| 5 | 美、日、印三国2022年度新冠新增数据统计 | 三国**新增**同图对比 |
| 6 | 美、日、印2022年度新冠死亡数据统计 | 三国**死亡**同图对比 |

页面支持 **Tab 按钮切换**、图表缩放、工具箱导出图片喵～

> ⚠️ **注意**：再次运行 `折线图开发.py` 会**重新生成并覆盖** `render.html`，
> 主人移入的版本会被新生成的替换掉喵！

---

## 🚀 如何运行

```powershell
# 需要 pyecharts（已安装在 .venv 里喵）
.\.venv\Scripts\python.exe .\json数据处理\折线图开发.py
# 生成后浏览器打开 json数据处理\render.html
```

---

## 📝 更新记录

- `2026-08-22`：移入新版本 `render.html`（6 张三国新冠折线图页面，含各国图与三国对比图）

---

## 🎓 本文件夹总结的知识点

1. 📄 `json.loads()` 解析 JSON 数据文件
2. 📈 pyecharts `Line` 折线图：`add_xaxis` / `add_yaxis`
3. ⚙️ `set_global_opts` 全局配置（标题、图例、工具箱）
4. 🔀 字典 + for 循环**批量处理**多个数据文件
5. 🗂️ `Tab` 把多张图放进一个网页切换

---

*本笔记由喵喵助手整理，数据可视化大师之路喵！🐾*

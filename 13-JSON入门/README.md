# 📄 13-JSON入门

> 记录 **JSON 数据格式** 的入门笔记喵～
> JSON 是 Python 和很多程序之间交换数据的「通用语言」喵！🐱

---

## 📁 目录

```
13-JSON入门
├── json数据格式.py      # json 与 python 互相转化演示
├── Learnjson           # 学习笔记（JSON 格式示例）
└── README.md           # 本文件
```

---

## 🔍 内容说明

### 1. JSON 是什么

- **JSON**（JavaScript Object Notation）是一种轻量级的数据交换格式
- 长得像 Python 的字典/列表，但**本质是一段字符串**！
- 例：

```json
{"name": "admin", "age": 18}
[{"name": "admin", "age": 18}, {"name": "admin", "age": 18}]
```

### 2. 与 Python 互相转化（`json数据格式.py`）

| 函数                | 作用                   | 方向      |
|-------------------|----------------------|---------|
| `json.dumps(数据)`  | Python 数据 → JSON 字符串 | 🔴 py 出 |
| `json.loads(字符串)` | JSON 字符串 → Python 数据 | 🔵 py 入 |

```python
import json

data = [{"name": "日辰羽", "age": 18}]
json_str = json.dumps(data, ensure_ascii=False)
# 注意 ensure_ascii=False 才能保留中文！
print(json_str)             # [{"name": "日辰羽", "age": 18}]
print(type(json_str))       # <class 'str'>  ← JSON 本质是字符串

new_data = json.loads(json_str)   # 转回 Python 列表
print(new_data)             # [{'name': '日辰羽', 'age': 18}]
```

> ⚠️ **`ensure_ascii=False`** 很关键：不加的话中文会变成
> `\u65e5\u8fb0\u7fbd` 这样的转义字符喵！

### 3. 学习笔记（`Learnjson`）

记录了 JSON 格式示例和转化口诀：

```
python与json转化：
首先要 import json
再调用 json.dumps()  json.loads()
```

---

## 🎓 本文件夹总结的知识点

1. 🔤 JSON 本质是**字符串**，用 `{}` 表示对象、`[]` 表示数组
2. 📤 `json.dumps()`：Python 数据 → JSON 字符串
3. 📥 `json.loads()`：JSON 字符串 → Python 数据
4. 🌏 `ensure_ascii=False` 保留中文
5. 🚀 进阶实战见 [`16-折线图开发/README.md`](../16-折线图开发/README.md)（用 json 数据画折线图）喵！

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | JSON 本质是字符串 | `Learnjson` | 长得像字典/列表，但本质是 `str`，`{}` 表示对象、`[]` 表示数组喵 |
| 2 | 先 `import json` | `Learnjson` | 用之前必须先导入 json 模块，笔记第一句就强调喵 |
| 3 | `json.dumps()` 序列化 | `json数据格式.py` | Python 数据 → JSON 字符串（py 出），列表、字典都能转喵 |
| 4 | `ensure_ascii=False` | `json数据格式.py` | 不加它中文会变成 `\u65e5\u8fb0\u7fbd` 转义字符喵 |
| 5 | `json.loads()` 反序列化 | `json数据格式.py` | JSON 字符串 → Python 数据（py 入），转回 list / dict 喵 |
| 6 | `type()` 验证类型 | `json数据格式.py` | dumps 后是 `<class 'str'>`，loads 后变回原来的类型喵 |
| 7 | 中文字符串示例 | `json数据格式.py` | 数据里有「日辰羽 / richenyv」，证明中文也能正常转换喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ **忘记 `import json`** 就直接调 `json.dumps()`：会直接报 `NameError` 喵！笔记里第一句就强调「首先要 import json」喵。
2. ⚠️ **忘记 `ensure_ascii=False`**：中文会变成 `\u65e5\u8fb0\u7fbd` 这样的转义序列，打印出来像乱码喵！
3. ⚠️ **搞混 `dumps` / `loads` 方向**：dumps 是 py 出（Python → JSON 字符串），loads 是 py 入（JSON 字符串 → Python），反了会报 `TypeError` 喵。
4. ⚠️ **`json.loads()` 只能吃字符串**：参数必须是 dumps 出来的字符串，直接传字典/列表进去会报错喵。
5. ⚠️ **中文编码问题**：JSON 文本文件读写记得用 UTF-8 编码，否则中文会乱码，`ensure_ascii=False` 也救不回来喵～

---

*本笔记由喵喵助手整理，JSON 认识 get 喵！🐾*

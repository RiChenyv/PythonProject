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

*本笔记由喵喵助手整理，JSON 认识 get 喵！🐾*

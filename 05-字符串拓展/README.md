# 🔤 05-字符串拓展

> 记录字符串的进阶玩法学习笔记喵～
> 字符串用得好，代码写得妙喵！🐾

---

## 📁 目录

```
05-字符串拓展
├── 01_字符串拼接与重复.py     # + 拼接、* 重复、+= 追加、切片
├── 02_字符串格式化.py         # %、format()、f-string
├── 03_字符串常用方法.py       # 大小写、strip、find、replace、split、join
├── 04_字符串判断方法.py       # isdigit、isalpha、isalnum 等
└── README.md                  # 本文件
```

---

## 1. 拼接与重复

```python
"hello" + " " + "world"   # 拼接 → 'hello world'
"哈" * 3                   # 重复 → '哈哈哈'
msg = "你好"; msg += "喵"   # 追加 → '你好喵'
```

> ⚠️ 字符串不能直接和数字 `+`，要先 `str(数字)` 转换喵！

## 2. 字符串格式化（三种方式）

| 方式 | 语法 | 例子 |
|------|------|------|
| `%` 格式化 | `"我是%s，今年%d岁" % (name, age)` | 老方法 |
| `format()` | `"我是{}，今年{}岁".format(name, age)` | 常用 |
| **f-string** | `f"我是{name}，今年{age}岁"` | ⭐ 最推荐 |

```python
# f-string 可以直接写表达式，还能控制小数位
print(f"明年我就{age + 1}岁了")
print(f"圆周率：{3.1415926:.2f}")   # 3.14
```

## 3. 常用方法速查表

| 方法 | 作用 | 例子 |
|------|------|------|
| `upper()` / `lower()` | 转大写 / 转小写 | `"abc".upper()` → `"ABC"` |
| `strip()` | 去左右空白 | `" hi ".strip()` → `"hi"` |
| `find()` / `rfind()` | 查找下标（从左 / 从右） | `"abc".find("b")` → `1` |
| `count()` | 统计出现次数 | `"aaa".count("a")` → `3` |
| `replace()` | 替换 | `"ab".replace("a","x")` → `"xb"` |
| `split()` | 分割成列表 | `"a,b".split(",")` → `['a','b']` |
| `join()` | 列表拼成字符串 | `"-".join(['a','b'])` → `"a-b"` |
| `startswith()` / `endswith()` | 判断开头 / 结尾 | `"abc".startswith("a")` → `True` |

## 4. 判断方法速查表

| 方法 | 判断内容 | 例子 |
|------|----------|------|
| `isdigit()` | 是否全是数字 | `"123".isdigit()` → `True` |
| `isalpha()` | 是否全是字母 | `"abc".isalpha()` → `True` |
| `isalnum()` | 是否全是字母或数字 | `"abc123".isalnum()` → `True` |
| `isspace()` | 是否全是空白 | `"  ".isspace()` → `True` |
| `isupper()` / `islower()` | 是否全大写 / 全小写 | `"ABC".isupper()` → `True` |

> 💡 判断方法常用来**验证用户输入**是否合法喵！

---

*本笔记由喵喵助手补全，字符串玩得溜喵！🐾*

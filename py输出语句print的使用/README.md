# 🖨️ py输出语句print的使用

> 记录 Python 第一个学习内容 —— `print()` 输出语句的笔记喵～
> 让程序学会「开口说话」喵！🐱

---

## 📁 目录

```
py输出语句print的使用
├── 01_print基础使用.py         # print 基础用法
├── 02_print的sep和end参数.py   # sep 分隔符 / end 结尾
├── 03_print格式化输出.py       # %、format()、f-string
├── 04_综合案例_打印图形.py     # 用 print 打印各种图形
└── README.md                   # 本文件
```

---

## 1. 基础语法

```python
print("hello world")        # 输出字符串
print(666)                  # 输出数字
print(name)                 # 输出变量
print("a", "b", "c")        # 输出多个内容，默认空格隔开
print(10 + 20)              # 输出表达式结果
```

> 💡 `print()` 输出完默认会**自动换行**喵！

## 2. 进阶参数：sep 和 end

| 参数 | 作用 | 默认值 |
|------|------|--------|
| `sep` | 多个内容之间的分隔符 | 空格 `" "` |
| `end` | 输出结尾的字符 | 换行 `"\n"` |

```python
print("a", "b", "c", sep="-")   # a-b-c
print("hello", end="")          # 不换行
print("world")                  # helloworld
```

## 3. 格式化输出（三种方式）

| 方式 | 语法 | 例子 |
|------|------|------|
| `%` 格式化 | `"我是%s，今年%d岁" % (name, age)` | 老方法 |
| `format()` | `"我是{}，今年{}岁".format(name, age)` | 常用 |
| **f-string** | `f"我是{name}，今年{age}岁"` | ⭐ 最推荐 |

```python
print(f"明年我就{age + 1}岁了")    # f-string 里可以写表达式
print(f"成绩：{95.5:.2f}")         # 控制小数位数 → 95.50
```

> 🐍 **占位符速记**：`%s` 字符串、`%d` 整数、`%f` 小数

## 4. 小贴士

1. 🖨️ `print()` 是 Python 里**最常用**的函数，调试代码靠它喵！
2. 📝 多个内容用逗号隔开，`sep` 和 `end` 可以一起用喵！
3. 🎨 用 `print` 的重复 `*` 和 `end` 可以画出各种图形喵！

---

*本笔记由喵喵助手补全，输出快乐喵！🐾*

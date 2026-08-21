# 🚀 py函数进阶 —— 函数进阶技巧

> 记录 **函数进阶玩法** 的学习笔记喵～
> 学会这些，函数就能玩出花来喵！🐱

---

## 📁 目录

```
py函数进阶
├── return.py                  # 多返回值
├── 传入参数的方式.py          # 位置/关键字/缺省/不定长参数
└── 匿名函数/
    ├── lambda关键字.py        # lambda 匿名函数
    └── 函数逻辑传递.py        # 函数作为参数传递
```

---

## 🔍 内容说明

### 1. 多返回值（`return.py`）

```python
def test_return():
    return 1, True, 'hello'

x, y, z = test_return()   # 用多个变量接收
print(x, y, z)            # 1 True hello
```

> 💡 返回值本质是**元组**，用多个变量一一对应接收喵！

### 2. 参数传递的多种方式（`传入参数的方式.py`）

| 方式 | 语法 | 特点 |
|------|------|------|
| 位置参数 | `user_info('richenyv', 19, "man")` | 按位置一一对应 |
| 关键字参数 | `user_info(name="richenyv", age=19)` | 按名字传参，可乱序 |
| 缺省参数 | `def user_info(name, age, gender='男')` | 不传就用默认值 |
| 位置不定长 | `def f(*args)` | 收成**元组** |
| 关键字不定长 | `def f(**kwargs)` | 收成**字典** |

```python
def without_length(*args):       # 位置不定长
    print(args)                  # ('TOM', 18, True)

def with_lengths(**kwargs):      # 关键字不定长
    print(kwargs)                # {'age': 18, 'gender': 'man'}
```

> ⚠️ 缺省参数必须放在**参数列表最后**喵！

### 3. 匿名函数 lambda（`匿名函数/lambda关键字.py`）

```python
# lambda 传入参数: 函数体（只能写一行）
def test_func(computer):
    result = computer(1, 2)
    print(result)

test_func(lambda x, y: x + y)    # 输出 3
```

### 4. 函数逻辑传递（`匿名函数/函数逻辑传递.py`）

函数也能当参数传！`test_func(computer)` 把 `computer` 函数
作为参数传进去，内部再调用它喵！

```python
def test_func(computer):
    result = computer(1, 2)   # 调用传进来的函数

def computer(a, b):
    return a + b

test_func(computer)           # 传函数，不传括号
```

> 💡 传函数时**不要加括号**（`computer` 而不是 `computer()`）喵！

---

## 🎓 本文件夹总结的知识点

1. 📦 `return 值1, 值2` 多返回值，用多变量接收
2. 🎛️ 参数五种姿势：位置 / 关键字 / 缺省 / `*args` / `**kwargs`
3. 🐑 `lambda 参数: 表达式` 匿名函数，一行搞定
4. 🔄 函数可以作为参数传递（高阶函数的雏形喵！）

---

*本笔记由喵喵助手整理，函数进阶毕业喵！🐾*

# 📦 pyMode —— 模块的导入

> 记录 **Python 模块（Module）导入方式** 的学习笔记喵～
> 模块就是一个 `.py` 文件，学会导入它，代码就能「拼积木」喵！🐱

---

## 📁 目录

```
pyMode
├── import模块.py           # import 各种形式实战
├── py模块.md               # 模块导入语法笔记
├── DiyPyMode/              # 自定义模块练习
│   ├── READMODE.py         # 自定义模块（含 __all__）
│   └── test.py             # 导入 READMODE 的测试
└── README.md               # 本文件
```

---

## 🔍 内容说明

### 1. 导入的四种核心形式（`import模块.py`）

| 形式 | 语法 | 使用方式 |
|------|------|----------|
| 导入模块 | `import time` | `time.sleep(1)` |
| 导入模块里的函数 | `from time import sleep` | `sleep(1)` |
| 导入全部 | `from time import *` | 直接用，不用对象调用 |
| 别名导入 | `from time import sleep as ZZZ` | `ZZZ(1)` |

```python
from time import *            # 导入全部功能
from time import sleep as richenyv   # 起别名
richenyv(1)                   # 等价于 sleep(1)
```

> ⚠️ `from 模块 import *` 会受模块里 `__all__` 的控制喵！

### 2. 自定义模块练习（`DiyPyMode/`）

**`READMODE.py`** —— 自己写的模块：

```python
__all__ = ["readMode"]        # 控制 * 导入只拿 readMode

def readMode(path):           # 打开文件返回文件对象
    temp = open(path, "r", encoding="utf-8")
    return temp

if __name__ == '__main__':    # 自我测试
    ...
```

**`test.py`** —— 导入并使用：

```python
from READMODE import *        # 用 * 导入
f = readMode("/test.txt")
print(f.readline())
```

> 💡 注意 `__all__` 里只列了 `readMode`，所以 `*` 导入时
> `CountMode` 函数不会被带进来喵！

### 3. 语法笔记（`py模块.md`）

模块导入的万能公式：

```
[from 模块名] import [模块|类|变量|函数|*][as 别名]
```

---

## 🎓 本文件夹总结的知识点

1. 📄 **模块** = 一个 `.py` 文件
2. 🔀 四种导入：`import` / `from import` / `from import *` / `as 别名`
3. 📋 `__all__` 控制 `import *` 的范围
4. 🧪 `if __name__ == '__main__'` 区分「直接运行」和「被导入」
5. 🔗 更深入的**包（Package）**知识见 [`PythonPackage/README.md`](../PythonPackage/README.md) 喵！

---

*本笔记由喵喵助手整理，导入快乐喵！🐾*

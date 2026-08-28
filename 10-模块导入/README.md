# 📦 10-模块导入 —— 模块的导入

> 记录 **Python 模块（Module）导入方式** 的学习笔记喵～
> 模块就是一个 `.py` 文件，学会导入它，代码就能「拼积木」喵！🐱

---

## 📁 目录

```
10-模块导入
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
5. 🔗 更深入的**包（Package）**知识见 [`11-包与导入/README.md`](../11-包与导入/README.md) 喵！

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | 模块的四种导入形式 | `py模块.md` | 万能公式 `[from 模块名] import [模块\|类\|变量\|函数\|*][as 别名]` |
| 2 | `import 模块名` 整模块导入 | `py模块.md` | 导入后要 `模块名.成员` 调用，如 `time.sleep(1)` |
| 3 | `from 模块 import 成员` | `py模块.md` | 只拿某个函数，之后直接 `sleep(1)` 就能用喵 |
| 4 | `from 模块 import *` 全量导入 | `import模块.py` | 不用对象直接调用，但导入范围受 `__all__` 管控喵 |
| 5 | `as` 起别名 | `import模块.py` | `sleep as richenyv` 之后 `richenyv(1)` 等价于 `sleep(1)` |
| 6 | `__all__` 控制 `*` 导入的范围 | `DiyPyMode/READMODE.py` | `__all__ = ["readMode"]`，`CountMode` 不会被 `*` 带进来喵 |
| 7 | 自定义模块 + 文件读取 | `DiyPyMode/READMODE.py` | `readMode()` 用 `encoding="utf-8"` 打开文件并返回文件对象 |
| 8 | `if __name__ == '__main__'` | `DiyPyMode/READMODE.py` | 直接运行才执行自我测试，被 import 时整段跳过喵 |
| 9 | 导入自定义模块并使用 | `DiyPyMode/test.py` | `from READMODE import *` 后直接 `readMode()` 读文件，用完 `f.close()` |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ `import模块.py` 只写了 `from time import *` 就直接 `time.sleep(5)` —— `*` 导入**不会**把模块名 `time` 绑进来，一运行就报 `NameError: name 'time' is not defined` 喵！要用 `time.xxx` 得先写 `import time` 喵！
2. ⚠️ 路径坑喵！`test.py` 里 `readMode("/test.txt")` 是**根目录绝对路径**（Windows 下就是 `C:\test.txt`），文件不在那儿就 `FileNotFoundError`；`READMODE.py` 里写死的 `"D:/PythonProject/test.txt"` 换个电脑也会失效喵——用真实存在的相对路径或 `os.path` 拼接才稳喵！
3. ⚠️ 打开文件用完记得 `f.close()`（示例里都关了，但自己写时一忘就泄漏文件句柄喵）——更省心的是 `with open(...) as f` 自动关闭喵～
4. ⚠️ `open()` 不写 `encoding="utf-8"` 时，Windows 默认按 gbk 解码，读 UTF-8 的中文文件会 `UnicodeDecodeError` 喵！`READMODE.py` 特意写 `encoding="utf-8"` 就是防这个坑喵。
5. ⚠️ `__all__` 没列出的名字，`from 模块 import *` 是导不进来的（`CountMode` 就是被挡掉的例子喵）——想让别人能全量导入，就把名字都写进 `__all__` 喵！
6. ⚠️ import 语句里**不能写文件夹路径**（比如 `test.py` 里被注释掉的 `from 09-异常处理.10-模块导入.DiyPyMode.READMODE import CountMode`）喵——要按「包.模块」的点分名导入，且目录还得是合法包结构才行喵！

*本笔记由喵喵助手整理，导入快乐喵！🐾*

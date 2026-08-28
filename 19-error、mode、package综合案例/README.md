# 🧩 error、mode、package 的综合案例

> 把 **异常处理（error）+ 模块导入（mode）+ 自定义包（package）** 三个知识点
> 串起来的综合练习喵～！🐱

---

## 📁 目录

```
19-综合案例
├── test.py                 # 综合调用测试入口
└── my_utils/               # 自建工具包
    ├── __init__.py         # 包的标志 + 预导入 + __all__
    ├── file_util.py        # 文件工具：打印/追加
    └── str_util.py         # 字符串工具：反转/截取
```

---

## 🔍 内容说明

### 1. 自建工具包 `my_utils`

**`file_util.py`（文件工具）**

| 函数 | 作用 |
|------|------|
| `print_file_info(file_name)` | 读取文件并打印内容，异常时提示错误 |
| `append_to_file(file_name, content)` | 向文件追加内容 |

> 🐍 亮点：内部使用 `try / except / finally` 保证**文件一定被关闭**，
> 还带 `if __name__ == "__main__"` 自我测试入口喵！

**`str_util.py`（字符串工具）**

| 函数 | 作用 |
|------|------|
| `str_reverse(s)` | 字符串反转（如 `"ikuY"` → `"Yuki"`） |
| `substr(s, x, y)` | 截取第 x 到第 y 位字符 |

> 💡 注释里还保留了切片写法 `s[::-1]`、`s[x-1:y-1]` 作为对比喵！

**`__init__.py`（包的关键）**

```python
from . import str_util, file_util   # 预导入子模块
__all__ = ['str_util', 'file_util'] # 控制 * 导入范围
```

> ⚠️ 这是之前踩坑后的正确写法：
> 只写 `__all__` 不够，必须配合 `from . import` 真正导入喵！

### 2. 综合调用 `test.py`

```python
import my_utils

my_utils.file_util.print_file_info(r"D:\...\bill.txt")
my_utils.file_util.append_to_file(r"D:\...\bill.txt", "\n日辰羽记录")
honey = my_utils.str_util.str_reverse("ikuY")   # Yuki
lover = my_utils.str_util.substr(honey, 1, 2)   # Yu
```

- ✅ 用 `import my_utils` 导入包，`包.模块.函数` 的方式调用
- ✅ 路径使用 `r"..."` 原始字符串，避免转义坑
- ✅ 一次案例同时用上了文件工具 + 字符串工具

---

## 🎓 本案例总结的知识点

1. 📦 **包** = 文件夹 + `__init__.py`
2. 🔄 `__init__.py` 里 `from . import 子模块` 是预导入的标准套路
3. 📋 `__all__` 只是名单，真正导入要靠 `from . import`
4. 🛡️ 文件操作用 `try/except/finally` 保证关闭
5. 🧪 `if __name__ == "__main__"` 让模块既能测试又能复用

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | 字符串反转 `str_reverse(s)` | `my_utils/str_util.py` | 用 while 从末尾往前拼接字符实现反转，注释里藏着切片 `s[::-1]` 的一行流写法喵 |
| 2 | 字符串截取 `substr(s, x, y)` | `my_utils/str_util.py` | 参数 x、y 从 1 开始数，内部转 0 基索引（`start=x-1`、`end=y-1`），等价切片 `s[x-1:y-1]` |
| 3 | 读取文件并打印 `print_file_info` | `my_utils/file_util.py` | open 后放进 try，except 打印友好报错，finally 里确保文件一定被 close |
| 4 | 追加内容 `append_to_file` | `my_utils/file_util.py` | 用 `"a"` 追加模式写文件，不会清空原内容，写失败也有异常兜底 |
| 5 | `if __name__ == "__main__"` 自测入口 | `my_utils/file_util.py` | 直接运行文件才执行测试代码，被 import 时自动跳过，实现「既能测试又能复用」 |
| 6 | 包 = 文件夹 + `__init__.py` | `my_utils/__init__.py` | 包必须带 `__init__.py` 才被 Python 认作包，里面用相对导入 `from . import` 预导入子模块 |
| 7 | `__all__` 控制 `import *` 名单 | `my_utils/__init__.py` | `__all__` 只是导出名单，真正让子模块可用还得靠 `from . import str_util, file_util` 喵 |
| 8 | 包.模块.函数 三级调用 | `test.py` | `import my_utils` 后一路点下去（如 `my_utils.str_util.substr(...)`），文件工具 + 字符串工具一次串起来 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ 只写 `__all__` 不写 `from . import` 是白给喵！`__all__` 只是名单，`import my_utils` 后 `my_utils.str_util` 依然不存在——预导入必须靠 `__init__.py` 里的 `from . import` 真正执行。
2. ⚠️ Windows 路径的反斜杠会触发转义（`\P`、`\t` 全变味），一定要用 `r"D:\PythonProject\..."` 原始字符串；或者像 `file_util.py` 自测那样直接写正斜杠 `"D:/..."` 也行喵。
3. ⚠️ open 过的文件不 close 会泄漏资源喵！手写文件操作容易漏，参照 `file_util.py` 把关闭动作放进 finally，文件不存在/打不开时走 except 也不会让 file 变量悬空。
4. ⚠️ `substr(s, x, y)` 的 x、y 是从 1 开始且**包含第 y 位**的（左闭右闭），跟习惯的切片前闭后开不一样：`substr("Yuki", 1, 2)` 得到 `"Yu"`，数位数时别按 0 基算喵！
5. ⚠️ `test.py` 里引用的 `bill.txt` 其实在 `12-文件操作` 文件夹里，跨文件夹用绝对路径时写错目录会走 except 打印「存在异常」——路径写对、文件真实存在才看得到内容喵。

---

*本笔记由喵喵助手整理，综合实力 up up 喵！🐾*

# 🧩 error、mode、package 的综合案例

> 把 **异常处理（error）+ 模块导入（mode）+ 自定义包（package）** 三个知识点
> 串起来的综合练习喵～！🐱

---

## 📁 目录

```
error,mode,package的综合案例
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

*本笔记由喵喵助手整理，综合实力 up up 喵！🐾*

# 基础语法

```python
try
    print("可能发生错误的代码")
except:
    print("出现异常执行的代码")
```

## 捕获指定异常

```python
try:
    print(name)
except NameError as e:
    print('变量名未定义')
```

## 捕获多个异常

```python
try:
    print(name)
    1 / 0
except (NameError, ZeroDivisionError) as e:
    print("变量未定义或除零异常")

```

## 捕获全部异常

```python
try:
    print(name)
    1 / 0
    fr = open("D:/PythonProject/666.txt", "r", encoding="utf-8")
except Exception as e:
    print("错误")
```

## finally

```python
try:
    print(name)
    1 / 0
    fr = open("D:/PythonProject/666.txt", "r", encoding="utf-8")
except Exception as e:
    print("错误")
finally:
    fr.close()
```

---

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | try/except 基础结构 | `TyrCatch.py` | try 里放可能出错的代码，except 里放出错后的兜底代码，程序不会崩溃喵 |
| 2 | 捕获指定异常 | `TyrCatch.py` | `except NameError as e` 只接住"变量未定义"这一种，`as e` 能拿到异常对象喵 |
| 3 | 捕获多个异常 | `TyrCatch.py` | `except (NameError, ZeroDivisionError)` 用元组一次接住多种异常喵 |
| 4 | 捕获全部异常 | `TyrCatch.py` | `except Exception as e` 兜底接住几乎所有异常，比裸 except 更规范喵 |
| 5 | 裸 except 的写法 | `TyrCatch.py` | `except:` 不写类型，什么异常都吞，但拿不到异常对象、还会误吞 KeyboardInterrupt 喵 |
| 6 | else 子句 | `TyrCatch.py` | 没发生异常时才走 else 分支，比如打印"开心呢，没有异常"喵 |
| 7 | finally 收尾 | `TyrCatch.py` | 无论有没有异常 finally 都执行，最适合放关文件等收尾动作喵 |
| 8 | 异常沿调用链传播 | `past.py` | 函数内抛出的异常会一层层往上抛，Traceback 完整记录了 main→funco2→funco1 的调用链喵 |
| 9 | 在外层捕获内层异常 | `dePastBug.py` | 在 main 用 try 包住 funco2()，就能接住 funco1 里 1/0 抛出的 ZeroDivisionError 喵 |
| 10 | Windows 路径写法 | `TyrCatch.py` | 路径统一写 `D:/PythonProject/...` 正斜杠，省掉反斜杠转义的麻烦喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ **finally 里别直接 close 可能不存在的文件**：README 末尾和 `TyrCatch.py` 都是 `finally: f.close()`，可如果前面的 `open()` 抛了异常，`f` 根本没定义，finally 里会再抛 `NameError` 把原异常盖掉喵！要先判断 `f` 是否存在（如 `if 'f' in locals()`）再关喵。
2. ⚠️ **别用裸 `except:`**：`TyrCatch.py` 第一段就是裸 except，它会连 `KeyboardInterrupt`、`SystemExit` 一起吞掉，还拿不到异常对象；想捕获全部请写 `except Exception as e` 喵。
3. ⚠️ **捕获多个异常要写成元组**：必须写 `except (NameError, ZeroDivisionError)`，漏掉括号写成 `except NameError, ZeroDivisionError` 是 Python 2 旧语法，直接语法报错喵。
4. ⚠️ **函数内部的异常要在外层调用处捕获**：`past.py` 里 `funco1` 的 `1 / 0` 不会自己消失，只会沿调用链一路往上抛直到程序崩溃；要像 `dePastBug.py` 那样在 `main` 的调用处用 try 包住喵。
5. ⚠️ **Windows 路径的转义坑**：代码里统一用正斜杠 `"D:/PythonProject/666.txt"`；要是手滑写成反斜杠 `"D:\PythonProject\666.txt"`，`\P`、`\6` 会被当成转义字符，路径就错了喵。
6. ⚠️ **else 和 finally 的分工别搞混**：只有没异常才走 else（成功后的操作），无论有没有异常都走 finally（必须的收尾）——顺序和用途反了，逻辑就乱了喵。

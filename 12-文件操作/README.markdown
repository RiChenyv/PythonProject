# 12-文件操作

## 1.文件编码:

### 编码技术即：翻译的规则，记录了如何将内容转化为二进制

计算机中有很多可用编码，如UTF-8 GBK Big5,其中，***UTF-8是目前全球通用的编码格式***

## 2.什么是文件：

### 文件的操作步骤

***打开、读写、关闭文件***

### open函数：

通过&nbsp;&nbsp; f=open(file,mode,encoding)&nbsp;&nbsp;来在py中打开文件

```python
f = open('D:/python.txt', 'r', encoding="UTF-8")
# f为open函数的文件对象，拥有属性和方法
```

mode常用的三种基础访问方式：

| 模式 | 描述                                                 |
|----|----------------------------------------------------|
| r  | 以只读的方式打开文件                                         |
| w  | 打开文件只用于写入，如果文件已经打开，则从头开始编译，原有内容会被删除，如果文件不存在，创建新的文件 |
| a  | 打开文件用于追加，若文件已经存在，新扽内容将会被写到已有内容中，若无文件，则创建文件         |

### read、readlines方法

文件对象.read(num):  
不输入num默认读取文件全部内容

```python
f = open('D:/python.txt', 'r', encoding="UTF-8")
print(f"输出10个字节：{f.read(10)}")
print(f"输出全部内容：{f.read()}")
# 
```

##

##

***f.read()为str类型***

##

##

文件对象.readlines()：  
按照行的方式一次性读取整个文件，并返回一个列表，其中每一行数据为一个元素

```python
f = open('D:/python.txt', 'r', encoding="UTF-8")
lines = f.readlines()
print(type(lines))
print(lines)
# line只读取一行数据
line = f.readline()
print(line)
```

### 文件关闭close:

```python
import time

f = open('D:/python.txt', 'r', encoding="UTF-8")
time.sleep(500000)
f.close()
```

### with open语法：

自动在程序操作完成后关闭文件

```python
with open('D:/python.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        print(line)
```

# 总结：

![总结](../images/文件读取操作总结_01.jpg)

## 🧠 知识点总结（复习速查）

> 两天后复习就看这块喵！每个知识点都标注了原码位置，点开对应文件就能回忆喵！

| # | 知识点 | 原码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | open() 三要素：路径 + mode + encoding | `read/文件读取.py` | r 只读 / w 覆盖写 / a 追加写，读中文文件记得带 encoding="UTF-8" 喵 |
| 2 | read / readlines / readline 读取三兄弟 | `read/文件读取.py` | read(num) 读 num 字节、read() 读全部、readlines() 按行返回列表、readline() 只读一行 |
| 3 | 文件指针会"接着读" | `read/文件读取.py` | read 完指针在文件末尾，再 readlines / readline 只能拿到空内容 |
| 4 | for 循环逐行读文件 | `read/01_countnum.py` | for line in f 每次拿一行，配合 strip() 去掉换行符再处理 |
| 5 | w 模式：覆盖写入 + 自动建文件 | `write/文件写入.py` | w 会清空原内容重写，文件不存在会自动新建；close() 内置了 flush |
| 6 | a 模式：末尾追加不覆盖 | `文件的追加/追加.py` | 追加写不删旧内容；write() 不会自动换行，要自己拼上 '\n' |
| 7 | with open 自动关闭文件 | `write/文件写入.py` | with 块结束自动 close，比手动 f.close() 更省心、不容易忘 |
| 8 | 词频统计：count + split 组合拳 | `read/01_countnum.py` | f.read().count("python") 直接数次数；split(" ") 切词后逐个 count 更准 |
| 9 | 账单综合案例：读写分流 | `综合案例.py` | 逐行 strip 去换行 → split(",") 取第 5 列判断"正式" → 分别写入 bill.txt.bak 和 bill_test.txt |
| 10 | 账单数据文件格式 | `bill.txt` | 每行逗号分隔 name,date,money,type,remarks 五列，第 5 列是"正式/测试"标记喵 |

---

## ⚠️ 注意事项（易踩的坑）

1. ⚠️ read 完再 readlines 会读到空：文件指针已经跑到末尾啦，`read/文件读取.py` 里就演示了这种"无输出"现象，想重新读必须重新 open 一次喵。
2. ⚠️ w 模式会清空原文件：用 w 打开已有文件等于从头覆盖，旧内容全没！`write/文件写入.py` 里第二次 with open w 就把第一次写的 hello world 覆盖成 byebye 了，想保留旧内容要用 a 追加模式喵。
3. ⚠️ write() 不自动换行：`文件的追加/追加.py` 里每次写入都手动拼了 '\n'，忘了加的话所有内容会全部挤在一行喵。
4. ⚠️ 忘记 close 文件：文件会一直占用资源，`read/文件读取.py` 用 time.sleep(500000) 演示了不关文件挂住的后果，能用 with open 就别手动开喵。
5. ⚠️ split 后按下标取值会越界：`综合案例.py` 用 line.split(",")[4] 取第 5 列，可 bill.txt 最后一行"日辰羽记录"没有逗号，split 出来列表太短，[4] 直接 IndexError 崩掉，处理数据前先想想数据规不规范喵。
6. ⚠️ 文件名末尾多打一个点：`综合案例.py` 里输出文件名写成了 "bill_test.txt."（末尾多个点），Windows 会默默忽略末尾的点所以侥幸能跑，但换到 Linux 上就会生成带点的新文件，回头找不到文件喵。
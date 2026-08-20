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

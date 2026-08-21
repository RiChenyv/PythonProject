# py模块

## 模块的导入

[from 模块名] import [模块|类|变量|函数|*][as 别名]

```python
import time
```

又如单独调用一个模块的一个方法

````python
from time import sleep
````

或者仅调用且调用全部方法本身

```python
from time import *

sleep(1)
```

加别名

```python
from time import sleep as ZZZ

ZZZ(1)
```
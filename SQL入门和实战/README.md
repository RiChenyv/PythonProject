# 🐬 SQL入门和实战 —— MySQL 学习笔记

> 记录 **MySQL 数据库** 的语法梳理与实战案例喵～
> 从建库建表到多表查询，再到事务与 Python 连接实战，一站式整理喵！🐱

---

## 📁 目录

```
SQL入门和实战
└── README.md     # 本文件（MySQL 语法梳理 + 实战案例）
```

> 📌 本文件夹原计划用于 MySQL 学习，已通过 MySQL 软件完成学习喵～
> 这里就是完整的学习笔记沉淀喵！🐾

---

## 🧭 一、MySQL 基础

### 1. 什么是 MySQL？

- **数据库（Database）**：存储数据的仓库，本质是文件系统上的文件集合
- **表（Table）**：数据库里存数据的二维结构（行 + 列）
- **SQL（Structured Query Language）**：操作数据库的标准化语言

### 2. 三大类 SQL 语言

| 分类 | 全称 | 作用 |
|------|------|------|
| **DDL** | Data Definition Language | 定义库、表结构（创建/修改/删除） |
| **DML** | Data Manipulation Language | 操作数据（增/删/改） |
| **DQL** | Data Query Language | 查询数据（查，最常用！） |

> 💡 另外还有 DCL（权限控制）、TCL（事务控制）喵！

### 3. 连接 MySQL

```bash
# 命令行连接
mysql -u root -p

# 图形化工具（本喵推荐）
# Navicat / MySQL Workbench / DataGrip 都可以喵！
```

---

## 🏗️ 二、DDL —— 库与表的定义

### 1. 数据库操作

```sql
-- 查看所有数据库
SHOW DATABASES;

-- 创建数据库（指定 utf8mb4 编码，支持中文和 emoji 喵！）
CREATE DATABASE IF NOT EXISTS school DEFAULT CHARSET utf8mb4;

-- 使用数据库
USE school;

-- 删除数据库
DROP DATABASE IF EXISTS school;
```

### 2. 表操作

```sql
-- 创建表
CREATE TABLE student (
    id       INT PRIMARY KEY AUTO_INCREMENT COMMENT '学号',
    name     VARCHAR(20) NOT NULL COMMENT '姓名',
    gender   CHAR(1) DEFAULT '男' COMMENT '性别',
    age      INT COMMENT '年龄',
    score    DECIMAL(5,2) COMMENT '成绩',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
);

-- 查看表结构
DESC student;

-- 修改表（增列 / 改列 / 删列）
ALTER TABLE student ADD COLUMN phone VARCHAR(11);
ALTER TABLE student MODIFY COLUMN age TINYINT;
ALTER TABLE student DROP COLUMN phone;

-- 重命名 / 删除表
RENAME TABLE student TO stu;
DROP TABLE IF EXISTS stu;
```

### 3. 常用数据类型速查

| 类型 | 说明 | 例子 |
|------|------|------|
| `INT` | 整数 | 年龄、数量 |
| `VARCHAR(n)` | 可变长字符串 | 姓名、地址 |
| `CHAR(n)` | 定长字符串 | 性别、状态码 |
| `DECIMAL(m,n)` | 定点小数（钱！） | `DECIMAL(10,2)` 金额 |
| `DATE` / `DATETIME` | 日期 / 日期时间 | 生日、下单时间 |
| `TEXT` | 长文本 | 备注、内容 |

> ⚠️ **金额不要用 FLOAT/DOUBLE**，精度会丢，要用 `DECIMAL` 喵！

---

## ✏️ 三、DML —— 数据的增删改

### 1. 插入 INSERT

```sql
-- 指定列插入
INSERT INTO student (name, gender, age, score) VALUES ('日辰羽', '男', 18, 95.5);

-- 批量插入
INSERT INTO student (name, gender, age, score) VALUES
('richenyv', '男', 19, 92.0),
('cunriyang', '女', 19, 88.5),
('yuki', '女', 18, 99.0);
```

### 2. 修改 UPDATE

```sql
-- 更新指定行（⚠️ 不写 WHERE 会更新全表！）
UPDATE student SET score = 100 WHERE name = 'yuki';

-- 多列更新
UPDATE student SET age = age + 1, score = score + 5 WHERE id = 1;
```

### 3. 删除 DELETE

```sql
-- 删除指定行（⚠️ 不写 WHERE 会清空全表！）
DELETE FROM student WHERE id = 4;

-- 清空整张表（自增从 1 重新开始）
TRUNCATE TABLE student;
```

> ⚠️ **UPDATE / DELETE 忘记 WHERE = 灾难**，一定要养成先 SELECT 看一眼的习惯喵！

---

## 🔍 四、DQL —— 数据查询（重点中的重点！）

### 1. 基础查询

```sql
-- 查所有列
SELECT * FROM student;

-- 查指定列 + 别名
SELECT name AS 姓名, score AS 成绩 FROM student;

-- 去重
SELECT DISTINCT gender FROM student;
```

### 2. 条件查询 WHERE

| 运算符 | 说明 |
|--------|------|
| `=` `!=` `>` `<` `>=` `<=` | 比较 |
| `AND` / `OR` / `NOT` | 逻辑 |
| `LIKE` | 模糊匹配（`%` 任意多个，`_` 一个） |
| `IN (...)` | 在集合内 |
| `BETWEEN a AND b` | 在区间内 |
| `IS NULL` / `IS NOT NULL` | 空值判断 |

```sql
-- 成绩大于等于 90 的男生
SELECT * FROM student WHERE score >= 90 AND gender = '男';

-- 姓名包含「羽」的同学（模糊查询）
SELECT * FROM student WHERE name LIKE '%羽%';

-- 成绩在 80~90 之间
SELECT * FROM student WHERE score BETWEEN 80 AND 90;

-- 年龄是 18 或 20 的
SELECT * FROM student WHERE age IN (18, 20);
```

### 3. 聚合函数

| 函数 | 作用 |
|------|------|
| `COUNT(*)` | 计数 |
| `SUM(列)` | 求和 |
| `AVG(列)` | 平均值 |
| `MAX(列)` / `MIN(列)` | 最大 / 最小 |

```sql
SELECT
    COUNT(*)       AS 总人数,
    AVG(score)     AS 平均分,
    MAX(score)     AS 最高分,
    MIN(score)     AS 最低分
FROM student;
```

### 4. 分组 GROUP BY + HAVING

```sql
-- 按性别统计平均分（WHERE 过滤原始行，HAVING 过滤分组结果）
SELECT gender AS 性别, COUNT(*) AS 人数, AVG(score) AS 平均分
FROM student
WHERE age >= 18
GROUP BY gender
HAVING AVG(score) > 85;
```

> 💡 **WHERE vs HAVING**：WHERE 在分组前过滤行，HAVING 在分组后过滤组喵！

### 5. 排序 ORDER BY + 分页 LIMIT

```sql
-- 按成绩降序（升序 ASC / 降序 DESC）
SELECT * FROM student ORDER BY score DESC;

-- 多字段排序：成绩降序，同分按年龄升序
SELECT * FROM student ORDER BY score DESC, age ASC;

-- 分页：第 2 页，每页 3 条（偏移量 = (页码-1) × 每页条数）
SELECT * FROM student ORDER BY score DESC LIMIT 3 OFFSET 3;
-- 或简写：LIMIT 偏移量, 条数
SELECT * FROM student ORDER BY score DESC LIMIT 3, 3;
```

### 6. DQL 完整执行顺序（背下来喵！）

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

> 🐱 记忆口诀：**从哪来（FROM）→ 过滤行（WHERE）→ 分组（GROUP BY）→ 过滤组（HAVING）→ 选出列（SELECT）→ 排序（ORDER BY）→ 分页（LIMIT）** 喵！

---

## 🔒 五、约束

| 约束 | 关键字 | 作用 |
|------|--------|------|
| 主键 | `PRIMARY KEY` | 唯一标识一行，非空且唯一 |
| 非空 | `NOT NULL` | 不能为空 |
| 唯一 | `UNIQUE` | 不能重复 |
| 默认值 | `DEFAULT` | 不填时用默认值 |
| 自增 | `AUTO_INCREMENT` | 自动 +1（常配合主键） |
| 外键 | `FOREIGN KEY` | 关联另一张表 |

```sql
CREATE TABLE class (
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE
);

-- 带外键的表（student 的 class_id 指向 class 的 id）
CREATE TABLE student (
    id       INT PRIMARY KEY AUTO_INCREMENT,
    name     VARCHAR(20) NOT NULL,
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES class(id)
);
```

---

## 🔗 六、多表查询

### 1. 连接查询

```sql
-- 内连接：只取两表匹配上的行
SELECT s.name, c.name AS 班级
FROM student s
INNER JOIN class c ON s.class_id = c.id;

-- 左连接：左表全保留，右表没匹配上就 NULL
SELECT s.name, c.name AS 班级
FROM student s
LEFT JOIN class c ON s.class_id = c.id;

-- 右连接：右表全保留
SELECT s.name, c.name AS 班级
FROM student s
RIGHT JOIN class c ON s.class_id = c.id;
```

| 连接 | 结果 |
|------|------|
| `INNER JOIN` | 只留交集 |
| `LEFT JOIN` | 左表全留 + 交集 |
| `RIGHT JOIN` | 右表全留 + 交集 |

### 2. 子查询

```sql
-- 查询成绩高于平均分的同学
SELECT * FROM student
WHERE score > (SELECT AVG(score) FROM student);

-- 查询有学生的班级（IN 子查询）
SELECT * FROM class
WHERE id IN (SELECT DISTINCT class_id FROM student WHERE class_id IS NOT NULL);
```

---

## 💼 七、事务

### 1. 四大特性 ACID

| 特性 | 含义 |
|------|------|
| **A**tomicity 原子性 | 要么全成功，要么全失败 |
| **C**onsistency 一致性 | 数据前后保持一致 |
| **I**solation 隔离性 | 事务之间互不干扰 |
| **D**urability 持久性 | 提交后永久保存 |

### 2. 事务操作

```sql
-- 开启事务
START TRANSACTION;

-- 转账案例：扣钱 + 加钱 必须同时成功！
UPDATE account SET money = money - 500 WHERE name = '日辰羽';
UPDATE account SET money = money + 500 WHERE name = 'yuki';

-- 成功就提交（永久生效）
COMMIT;

-- 出错就回滚（撤销全部操作）
ROLLBACK;
```

> 🐱 银行转账就是最经典的事务场景喵！

---

## 🏆 八、实战案例

### 🎓 案例 1：学生成绩管理

```sql
-- 1. 建库建表
CREATE DATABASE IF NOT EXISTS school DEFAULT CHARSET utf8mb4;
USE school;

CREATE TABLE student (
    id     INT PRIMARY KEY AUTO_INCREMENT,
    name   VARCHAR(20) NOT NULL,
    gender CHAR(1) DEFAULT '男',
    score  DECIMAL(5,2)
);

-- 2. 插入数据
INSERT INTO student (name, gender, score) VALUES
('日辰羽', '男', 95.5), ('richenyv', '男', 92.0),
('cunriyang', '女', 88.5), ('yuki', '女', 99.0), ('momo', '女', 76.0);

-- 3. 实战查询
-- ① 成绩排名（降序）
SELECT name, score FROM student ORDER BY score DESC;

-- ② 各性别平均分
SELECT gender, AVG(score) AS 平均分 FROM student GROUP BY gender;

-- ③ 及格率（条件聚合）
SELECT
    COUNT(*) AS 总人数,
    SUM(score >= 60) AS 及格人数,
    ROUND(SUM(score >= 60) / COUNT(*) * 100, 1) AS 及格率
FROM student;

-- ④ 前三名
SELECT name, score FROM student ORDER BY score DESC LIMIT 3;
```

### 🛒 案例 2：电商订单统计

```sql
USE shop;

-- 订单表
CREATE TABLE orders (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    user_name  VARCHAR(20),
    amount     DECIMAL(10,2),
    status     VARCHAR(10) DEFAULT '待支付',   -- 待支付/已支付/已取消
    order_time DATETIME
);

-- ① 每个用户消费总额（按用户分组）
SELECT user_name AS 用户, SUM(amount) AS 总消费
FROM orders
WHERE status = '已支付'
GROUP BY user_name
ORDER BY 总消费 DESC;

-- ② 每月销售额
SELECT DATE_FORMAT(order_time, '%Y-%m') AS 月份,
       SUM(amount) AS 销售额
FROM orders
WHERE status = '已支付'
GROUP BY 月份
ORDER BY 月份;

-- ③ 大额订单（超过平均订单金额的）
SELECT * FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders WHERE status = '已支付');
```

### 🐍 案例 3：Python + pymysql 连接实战

> 这是 Python 项目，当然要联动起来喵！

```python
# pip install pymysql

import pymysql

# 1. 连接数据库
conn = pymysql.connect(
    host="localhost", user="root", password="你的密码",
    database="school", charset="utf8mb4"
)

# 2. 创建游标
cursor = conn.cursor()

# 3. 执行 SQL（查询）
cursor.execute("SELECT name, score FROM student ORDER BY score DESC")
for row in cursor.fetchall():
    print(f"姓名: {row[0]}, 成绩: {row[1]}")

# 4. 执行 SQL（写入，需要提交事务）
cursor.execute(
    "INSERT INTO student (name, gender, score) VALUES (%s, %s, %s)",
    ("新同学", "女", 89.0)
)
conn.commit()   # 别忘了提交喵！

# 5. 关闭连接
cursor.close()
conn.close()
```

---

## 📋 九、常用命令速查表

| 场景 | 命令 |
|------|------|
| 建库 | `CREATE DATABASE 库名 DEFAULT CHARSET utf8mb4;` |
| 建表 | `CREATE TABLE 表名 (列 类型 约束, ...);` |
| 插入 | `INSERT INTO 表 (列...) VALUES (...);` |
| 更新 | `UPDATE 表 SET 列=值 WHERE 条件;` ⚠️ 带 WHERE |
| 删除 | `DELETE FROM 表 WHERE 条件;` ⚠️ 带 WHERE |
| 查询 | `SELECT 列 FROM 表 WHERE 条件 GROUP BY 列 HAVING 条件 ORDER BY 列 LIMIT n;` |
| 排序 | `ORDER BY 列 ASC/DESC` |
| 分页 | `LIMIT 偏移量, 条数` |
| 模糊 | `WHERE 列 LIKE '%关键字%'` |
| 连接 | `INNER/LEFT/RIGHT JOIN 表 ON 条件` |
| 事务 | `START TRANSACTION; ... COMMIT; / ROLLBACK;` |

---

## 💡 小贴士（踩坑记录）

1. ⚠️ `UPDATE` / `DELETE` 忘写 `WHERE` = 全表遭殃，动手前先 `SELECT` 喵！
2. 💰 金额用 `DECIMAL`，别用 `FLOAT`，精度会哭喵！
3. 🔤 建库建表统一 `utf8mb4` 编码，中文 emoji 都安全喵！
4. 📏 DQL 执行顺序：`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` 喵！
5. 🐍 Python 连 MySQL 用 `pymysql`，写操作记得 `commit()` 喵！
6. 🚧 备份好习惯：`mysqldump -u root -p 库名 > 备份.sql` 喵！

---

*本笔记由喵喵助手整理，SQL 大师毕业喵！🐾*

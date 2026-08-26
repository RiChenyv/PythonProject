# 🐬 SQL入门和实战 —— MySQL 学习笔记

> 记录 **MySQL 数据库** 的语法梳理与实战案例喵～
> 从建库建表到多表查询，再到事务与 Python 连接实战，一站式整理喵！🐱

---

## 📁 目录

```
21-SQL入门和实战
├── README.md          # 本文件（MySQL 语法梳理 + 实战案例）
├── pymysql入门.py     # 🐍 Python 连接 MySQL 基础操作（真实代码）
└── 综合案例/          # 📦 销售数据上传数据库综合案例
    ├── data_define.py # Record 数据封装类
    ├── File_define.py # 文件读取器（txt / JSON）
    └── 综合案例.py     # ⭐ 读取数据 → 上传 MySQL
```

> 📌 本文件夹原计划用于 MySQL 学习，已通过 MySQL 软件完成学习喵～
> 这里就是完整的学习笔记沉淀喵！🐾

---

## 🧭 一、MySQL 基础

### 1. 什么是 MySQL？

- **数据库（Database）**：存储数据的仓库，本质是文件系统上的文件集合
- **表（Table）**：数据库里存数据的二维结构（行 + 列）
- **SQL（Structured Query Language）**：操作数据库的标准化语言

### 2. 五大类 SQL 语言

| 分类 | 全称 | 作用 |
|------|------|------|
| **DDL** | Data Definition Language | 定义库、表结构（创建/修改/删除） |
| **DML** | Data Manipulation Language | 操作数据（增/删/改） |
| **DQL** | Data Query Language | 查询数据（查，最常用！） |
| **DCL** | Data Control Language | 用户与权限控制（授权/收权） |
| **TCL** | Transaction Control Language | 事务控制（提交/回滚） |

### 3. 连接 MySQL

```bash
# 命令行连接
mysql -u root -p

# 图形化工具（本喵推荐）
# Navicat / MySQL Workbench / DataGrip 都可以喵！
```

---

## 🏗️ 二、DDL —— 库与表的定义

> 📌 **SQL 语法符号说明**（语法文档通用惯例喵！）：
> - `[ ]` 方括号：**可选**部分，写不写都行喵！
> - `|` 竖线：**或**，多选一（如 `ASC | DESC`）
> - `...` 省略号：可**重复**（如多列 `列1, 列2, ...`）
> - 中文占位符（如 `库名`、`表名`）：使用时替换成真实名字喵！

### 1. 数据库操作

```sql
-- 📐 语法模板（[ ] 里的内容都可以省略喵！）
CREATE DATABASE [IF NOT EXISTS] 库名 [DEFAULT CHARSET 字符集];

-- ✅ 实际例子（三种写法从简到全）
CREATE DATABASE school;                                        -- 最简：只写库名
CREATE DATABASE IF NOT EXISTS school;                          -- 可选：已存在就不报错
CREATE DATABASE IF NOT EXISTS school DEFAULT CHARSET utf8mb4;  -- 完整：指定编码（推荐）

-- 查看所有数据库
SHOW DATABASES;

-- 使用数据库
USE school;

-- 删除数据库（[IF EXISTS] 也是可选的喵！）
DROP DATABASE [IF EXISTS] 库名;
DROP DATABASE IF EXISTS school;
```

### 2. 表操作

```sql
-- 📐 语法模板
CREATE TABLE [IF NOT EXISTS] 表名 (
    列名 数据类型 [约束] [COMMENT '说明'],
    ...
) [DEFAULT CHARSET 字符集];

-- ✅ 实际例子
CREATE TABLE student (
    id       INT PRIMARY KEY AUTO_INCREMENT COMMENT '学号',
    name     VARCHAR(20) NOT NULL COMMENT '姓名',
    gender   CHAR(1) DEFAULT '男' COMMENT '性别',
    age      INT COMMENT '年龄',
    score    DECIMAL(5,2) COMMENT '成绩',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) DEFAULT CHARSET utf8mb4;

-- 查看表结构
DESC student;

-- 修改表（增列 / 改列 / 删列）
ALTER TABLE student ADD COLUMN phone VARCHAR(11);
ALTER TABLE student MODIFY COLUMN age TINYINT;
ALTER TABLE student DROP COLUMN phone;

-- 重命名 / 删除表（[IF EXISTS] 可选喵！）
RENAME TABLE student TO stu;
DROP TABLE [IF EXISTS] 表名;
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
-- 📐 语法模板（列名列表可省略，省略就按所有列的顺序插喵！）
INSERT INTO 表名 [(列1, 列2, ...)] VALUES (值1, 值2, ...);

-- ✅ 指定列插入
INSERT INTO student (name, gender, age, score) VALUES ('日辰羽', '男', 18, 95.5);

-- 批量插入（多组 VALUES 用逗号隔开）
INSERT INTO student (name, gender, age, score) VALUES
('richenyv', '男', 19, 92.0),
('cunriyang', '女', 19, 88.5),
('yuki', '女', 18, 99.0);
```

### 2. 修改 UPDATE

```sql
-- 📐 语法模板（⚠️ WHERE 不是 [ ] 可选项，是必选项喵！）
UPDATE 表名 SET 列1 = 值1 [, 列2 = 值2, ...] [WHERE 条件];

-- ✅ 更新指定行（⚠️ 不写 WHERE 会更新全表！）
UPDATE student SET score = 100 WHERE name = 'yuki';

-- 多列更新
UPDATE student SET age = age + 1, score = score + 5 WHERE id = 1;
```

### 3. 删除 DELETE

```sql
-- 📐 语法模板（⚠️ WHERE 建议必写！）
DELETE FROM 表名 [WHERE 条件];

-- ✅ 删除指定行（⚠️ 不写 WHERE 会清空全表！）
DELETE FROM student WHERE id = 4;

-- 清空整张表（自增从 1 重新开始，不能带 WHERE）
TRUNCATE TABLE student;
```

> ⚠️ **UPDATE / DELETE 忘记 WHERE = 灾难**，一定要养成先 SELECT 看一眼的习惯喵！
> 💡 语法模板里 `[WHERE 条件]` 加了方括号，但实际使用中**强烈建议必写**喵！

---

## 🔍 四、DQL —— 数据查询（重点中的重点！）

### 1. 基础查询

```sql
-- 📐 语法模板（[] 全是可选项，最简就是 SELECT * FROM 表; 喵！）
SELECT [DISTINCT] 列1 [, 列2, ...] | *
FROM 表名
[WHERE 条件]
[GROUP BY 分组列]
[HAVING 分组后条件]
[ORDER BY 排序列 ASC | DESC]
[LIMIT 条数];

-- ✅ 查所有列
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

## 🛡️ 八、DCL —— 用户与权限控制

> 管理「谁能连数据库、能对哪些库表做什么」喵！只有 root 或超级管理员能执行喵！

### 1. 用户管理

```sql
-- 📐 语法模板
CREATE USER '用户名'@'主机' [IDENTIFIED BY '密码'];
ALTER USER '用户名'@'主机' [IDENTIFIED BY '新密码'];
DROP USER '用户名'@'主机';

-- ✅ 查看所有用户（用户信息存在 mysql 库的 user 表里）
USE mysql;
SELECT user, host FROM user;

-- 创建用户（'用户名'@'主机'，localhost 只允许本机，% 允许任意主机）
CREATE USER 'richenyv'@'localhost' IDENTIFIED BY '123456';
CREATE USER 'yuki'@'%' IDENTIFIED BY '123456';

-- 修改密码
ALTER USER 'richenyv'@'localhost' IDENTIFIED BY 'new_password';

-- 删除用户
DROP USER 'richenyv'@'localhost';
```

### 2. 权限控制

```sql
-- 📐 语法模板
GRANT 权限列表 ON 库名.表名 TO '用户名'@'主机';
REVOKE 权限列表 ON 库名.表名 FROM '用户名'@'主机';
SHOW GRANTS FOR '用户名'@'主机';

-- ✅ 授权：把 school 库所有表的 查询+插入 权限给用户
GRANT SELECT, INSERT ON school.* TO 'richenyv'@'localhost';

-- 授权：全部库全部权限（谨慎！相当于半个管理员）
GRANT ALL PRIVILEGES ON *.* TO 'yuki'@'%';

-- 授权后刷新权限（部分版本/场景需要）
FLUSH PRIVILEGES;

-- 查看用户的权限
SHOW GRANTS FOR 'richenyv'@'localhost';

-- 收回权限：把插入权限收回来
REVOKE INSERT ON school.* FROM 'richenyv'@'localhost';

-- 收回全部权限
REVOKE ALL PRIVILEGES ON *.* FROM 'yuki'@'%';
```

### 3. 常用权限清单

| 权限 | 作用 |
|------|------|
| `ALL PRIVILEGES` | 全部权限（最高） |
| `SELECT` / `INSERT` / `UPDATE` / `DELETE` | 增删改查（最常用） |
| `CREATE` / `DROP` / `ALTER` | 建删改表结构 |
| `GRANT OPTION` | 允许用户再给别人授权 |

> 💡 `ON 数据库.表` 的写法：
> `school.*` 表示 school 库的所有表，`*.*` 表示所有库所有表喵！

> 🐱 **最小权限原则**：给用户够用的最小权限就好，别动不动就 `ALL PRIVILEGES` 喵！

---

## 🏆 九、实战案例

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
> 📄 **真实代码已落地**：[`pymysql入门.py`](./pymysql入门.py)（连接测试、查询、插入一条龙喵！）

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

> 💡 `pymysql入门.py` 里的实际写法：
> - `from pymysql import Connect` 或 `from pymysql import connect` 都能连
> - `autocommit=True` 自动提交，写操作不用手动 `commit()` 喵！
> - `conn.get_server_info()` 测试连接是否成功
> - `conn.select_db("库名")` 选择数据库，`cursor.fetchall()` 取回查询结果喵！

### 🔐 案例 4：数据库账号与权限管理（DCL）

> 给团队成员创建账号，按职责分配最小权限喵！

```sql
-- 1. 创建两个账号：开发账号（本机）、只读分析账号（任意主机）
CREATE USER 'dev'@'localhost' IDENTIFIED BY 'dev123456';
CREATE USER 'analyst'@'%' IDENTIFIED BY 'read123456';

-- 2. 授权：开发账号对 school 库拥有增删改查
GRANT SELECT, INSERT, UPDATE, DELETE ON school.* TO 'dev'@'localhost';

-- 3. 授权：分析账号只能查，不能改！
GRANT SELECT ON school.* TO 'analyst'@'%';

-- 4. 刷新权限，让授权立即生效
FLUSH PRIVILEGES;

-- 5. 验证：查看每个账号的权限
SHOW GRANTS FOR 'dev'@'localhost';
SHOW GRANTS FOR 'analyst'@'%';

-- 6. 人员离职 / 岗位调整：收回权限或删除账号
REVOKE DELETE ON school.* FROM 'dev'@'localhost';
DROP USER 'analyst'@'%';
```

> 🐱 案例要点：**开发给写权限、分析只给读权限**，就是最小权限原则的实践喵！

### 📦 案例 5：销售数据上传 MySQL（综合案例/）

> 把 20 号文件夹的**面向对象** + 14 号文件夹的**销售数据** + **pymysql** 全部串起来喵！
> 📄 真实代码在 [`综合案例/`](./综合案例/) 里喵！

```
读取销售数据（txt + JSON）→ 封装成 Record 对象 → 连接 MySQL → 批量 INSERT → 验证上传
```

**三个文件的分工喵：**

| 文件 | 作用 |
|------|------|
| `data_define.py` | `Record` 类封装一条销售记录（日期/订单id/金额/省份） |
| `File_define.py` | `Filereader` 父类 + `textreader`（读 txt 文本）+ `filereader`（读 JSON）子类 |
| `综合案例.py` | 主程序：读取 → 上传 → 验证 |

```python
# 综合案例.py 的核心逻辑
conn = connect(host="localhost", user="root", passwd="...", autocommit=True)
cursor = conn.cursor()
conn.select_db("py_sql")   # 选择数据库

for record in all_data:
    SQL = f"insert into orders(order_data, order_id, money, province) " \
          f"values('{record.date}', {record.ID}, {record.money}, '{record.province}')"
    cursor.execute(SQL)    # 循环插入每一天的销售记录

cursor.execute("select * from orders")
if cursor.fetchall() != ():
    print("已完成数据库上传")
```

> 💡 案例亮点喵：
> - 面向对象读取两种格式的文件，代码复用率高喵！
> - `autocommit=True` 每条插入自动提交，不用手动 `commit()` 喵！
> - 插入后 `SELECT` 验证数据真的进了数据库喵！

> ⚠️ **安全提醒**：`pymysql入门.py` / `综合案例.py` 里是**明文密码**，
> 如果推送到 GitHub 会被看到喵！建议改用环境变量或配置文件读取密码喵！

---

## 📋 十、常用命令速查表

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
| 建用户 | `CREATE USER '用户名'@'主机' IDENTIFIED BY '密码';` |
| 授权 | `GRANT 权限 ON 库.表 TO '用户名'@'主机';` |
| 收权 | `REVOKE 权限 ON 库.表 FROM '用户名'@'主机';` |
| 查权限 | `SHOW GRANTS FOR '用户名'@'主机';` |
| 删用户 | `DROP USER '用户名'@'主机';` |

---

## 💡 小贴士（踩坑记录）

1. ⚠️ `UPDATE` / `DELETE` 忘写 `WHERE` = 全表遭殃，动手前先 `SELECT` 喵！
2. 💰 金额用 `DECIMAL`，别用 `FLOAT`，精度会哭喵！
3. 🔤 建库建表统一 `utf8mb4` 编码，中文 emoji 都安全喵！
4. 📏 DQL 执行顺序：`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` 喵！
5. 🐍 Python 连 MySQL 用 `pymysql`，写操作记得 `commit()`（或 `autocommit=True`）喵！
6. 🚧 备份好习惯：`mysqldump -u root -p 库名 > 备份.sql` 喵！
7. 🔐 DCL 遵循**最小权限原则**，别随手 `ALL PRIVILEGES`；用户授权后记得 `FLUSH PRIVILEGES` 喵！
8. 👤 `'用户'@'主机'` 是一对组合：`localhost` 只本机能连，`%` 任意主机能连喵！
9. 🔑 代码里的数据库密码别明文写死，用环境变量（`os.getenv`）或配置文件，防泄露喵！
10. 📦 大批量插入数据用循环 + `autocommit=True` 最省事，插入后记得 `SELECT` 验证喵！

---

*本笔记由喵喵助手整理，SQL 大师毕业喵！🐾*

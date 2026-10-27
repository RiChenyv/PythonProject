# 🐬 SQL入门和实战 —— MySQL 学习笔记

> 记录 **MySQL 数据库** 的语法梳理与实战案例喵～
> 从建库建表到多表查询，再到事务与 Python 连接实战，一站式整理喵！🐱

> **适用范围**：以 **MySQL 8.0.16+、InnoDB** 为练习基准；CTE、窗口函数需要 MySQL 8.0+，`CHECK` 从 8.0.16 起真正执行检查。这里的 `AUTO_INCREMENT`、`LIMIT`、`SHOW`、`IFNULL` 等有 MySQL 方言特征，不能直接当成所有数据库通用语法。
> **练习方式**：语法模板中的中文占位符和 `[可选项]` 需要替换；标为“独立示例”的代码单独练习。第二章创建的 `school.student` 用于第三至六章；删除库表的演示默认注释，避免复制后把后续练习表删掉。

## 🗺️ 内容导航

| 章节 | 学习内容 |
|------|----------|
| [一、MySQL 基础](#mysql-basics) | 连接、SQL 分类、标识符与字符集 |
| [二、DDL](#ddl) | 建库建表、改表、[数据类型与选型](#data-types) |
| [三、DML](#dml) | 插入、更新、删除及三种删除方式对比 |
| [四、DQL](#dql) | 条件、NULL、聚合、分组、分页、常用函数 |
| [五、约束](#constraints) | 主键、唯一、检查、外键和关系建模 |
| [六、多表查询](#multi-table) | JOIN、子查询、EXISTS、UNION、CTE、窗口函数 |
| [七、事务](#transactions) | ACID、提交回滚、保存点、隔离级别与锁 |
| [八、DCL](#dcl) | 用户、授权、权限生效机制 |
| [九、实战案例](#practice) | 成绩、电商、Python、销售数据导入导出 |
| [十、常用命令](#quick-reference) | 快速回顾基础命令 |
| [十一、索引与性能](#indexes) | 联合索引、EXPLAIN、分页与查询优化 |
| [十二、视图与数据库编程](#database-programming) | 视图、存储过程、触发器的用途 |
| [十三、备份与排错](#maintenance) | 备份恢复、错误定位、跨数据库差异 |
| [文末复习](#review) | 现有代码对照、练习题、官方参考资料 |

---

## 📁 目录

```
21-SQL入门和实战
├── README.md          # 本文件（MySQL 语法梳理 + 实战案例）
├── pymysql入门.py     # 🐍 Python 连接 MySQL 基础操作（真实代码）
└── 综合案例/          # 📦 销售数据上传数据库综合案例
    ├── data_define.py # Record 数据封装类
    ├── File_define.py # 文件读取器（txt / JSON）
    ├── 综合案例.py     # ⭐ 读取数据 → 上传 MySQL
    ├── 读取数据库.py   # ⭐ 从数据库读出 → 转 JSON 写入文件
    └── json数据.txt    # 读取数据库.py 生成的 JSON 输出文件
```

> 📌 本文件夹原计划用于 MySQL 学习，已通过 MySQL 软件完成学习喵～
> 这里就是完整的学习笔记沉淀喵！🐾

---

<a id="mysql-basics"></a>

## 🧭 一、MySQL 基础

### 1. 什么是 MySQL？

- **MySQL**：关系型数据库管理系统（DBMS），负责存储、查询、权限和并发控制
- **数据库（Database）**：表等对象的逻辑集合；在 MySQL 中 `SCHEMA` 通常与 `DATABASE` 同义
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

# 指定主机、端口、数据库（-p 后不直接写密码，等待提示输入）
mysql -h 127.0.0.1 -P 3306 -u root -p school

# 图形化工具（本喵推荐）
# Navicat / MySQL Workbench / DataGrip 都可以喵！
```

### 4. 写 SQL 前先认识这些规则

- 语句通常用 `;` 结束。关键字习惯大写，库名、表名、列名使用一致的命名方式。
- 字符串和日期用单引号：`'yuki'`、`'2026-01-01'`；标识符需要转义时用反引号，例如 `` `order` ``。双引号含义会受 `ANSI_QUOTES` 模式影响，不依赖它表示字符串。
- `-- 注释` 中第二个短横线后要有空白；多行注释写成 `/* 注释 */`。MySQL 也支持 `#` 单行注释。
- 库名、表名是否区分大小写与系统及 `lower_case_table_names` 设置有关，统一小写更省心。
- **字符集**决定能存哪些字符，**排序规则（collation）**决定怎样比较和排序。`utf8mb4` 支持完整 Unicode；`_ci` 通常表示比较时忽略大小写，`_ai` 表示忽略重音，选型时还要查看具体规则。
- 查询结果没有天然顺序，要稳定输出就写 `ORDER BY`；行本身也没有可依赖的“默认顺序”。

```sql
SELECT VERSION(), DATABASE(), CURRENT_USER();
SELECT @@sql_mode, @@autocommit, @@session.time_zone;
SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'collation%';
```

---

<a id="ddl"></a>

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
-- DROP DATABASE IF EXISTS school;  -- 破坏性演示，练习主线不要执行
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 查看表结构
DESC student;
SHOW CREATE TABLE student;  -- 查看完整建表语句、索引、约束、引擎等
SHOW TABLES;

-- 修改表（增列 / 改列 / 删列）
ALTER TABLE student ADD COLUMN phone VARCHAR(11);
ALTER TABLE student MODIFY COLUMN age TINYINT UNSIGNED COMMENT '年龄';
ALTER TABLE student DROP COLUMN phone;

-- 重命名 / 删除表（[IF EXISTS] 可选喵！）
-- RENAME TABLE student TO stu;  -- 演示，后续章节继续使用 student
DROP TABLE [IF EXISTS] 表名;
-- DROP TABLE IF EXISTS stu;
```

> `IF NOT EXISTS` 只避免“对象已存在”的错误，不会把旧表自动升级成你写的新结构。修改列类型前先检查旧数据；`MODIFY COLUMN` 应重写需要保留的 `NOT NULL`、`DEFAULT`、`COMMENT` 等属性，不能假定都会自动保留。

<a id="data-types"></a>

### 3. 数据类型：整数、精确小数与浮点数

整数默认有符号；加 `UNSIGNED` 后只能存非负数，但上界扩大。下表中的字节数是类型自身的数据宽度，不代表整行实际占用。

| 类型 | 字节 | 有符号范围 | 无符号范围 | 用途与示例 |
|------|------|------------|------------|------------|
| `TINYINT` | 1 | -128～127 | 0～255 | 小范围状态、年龄；`age TINYINT UNSIGNED` |
| `SMALLINT` | 2 | -32768～32767 | 0～65535 | 年份编号、小规模计数 |
| `MEDIUMINT` | 3 | -8388608～8388607 | 0～16777215 | 中等规模编号，MySQL 扩展 |
| `INT` / `INTEGER` | 4 | -2147483648～2147483647 | 0～4294967295 | 常规主键、数量 |
| `BIGINT` | 8 | -2^63～2^63-1 | 0～2^64-1 | 大规模 ID、累计计数 |

整数范围可查 [MySQL 整数类型文档](https://dev.mysql.com/doc/refman/8.0/en/integer-types.html)。

| 类型 | 精度和空间 | 作用 | 注意事项 |
|------|------------|------|----------|
| `DECIMAL(M,D)` / `NUMERIC(M,D)` | 精确十进制；空间随精度变化 | 金额、单价、税率等需要十进制精确表示的数据 | `M` 是总位数，`D` 是小数位数，整数部分最多 `M-D` 位 |
| `FLOAT` | 通常 4 字节，约 7 位十进制有效数字 | 可接受近似误差的测量值 | 二进制浮点，不能保证十进制小数精确表示 |
| `DOUBLE` | 通常 8 字节，约 15～16 位十进制有效数字 | 科学计算、较高精度测量值 | 仍是近似值，不适合直接存精确金额 |
| `BOOL` / `BOOLEAN` | MySQL 中是 `TINYINT(1)` 的别名 | 真/假开关 | 不会自动限制只能存 0、1；需要 `CHECK` |
| `BIT(M)` | 1～64 个二进制位 | 位标志、紧凑的位集合 | 字面量如 `b'101'`；客户端可能以字节形式返回 |

- `DECIMAL(10,2)` 能存 `-99999999.99`～`99999999.99`；`DECIMAL(5,2)` 能存 `-999.99`～`999.99`，适合百分制成绩但还应加成绩范围约束。
- MySQL 的 `DECIMAL` 最大总精度为 65 位、小数位最多 30 位，且 `D <= M`。小数位过多会按目标精度转换，应在业务层明确舍入规则；越界处理还受严格模式影响。
- `INT(11)` 的 `11` 是旧式显示宽度，不是 11 位数，也不改变 4 字节和取值范围；整数显示宽度已弃用。补零展示用 `LPAD()`，不要靠旧式 `ZEROFILL`。
- `TRUE`、`FALSE` 在 MySQL 中分别是 1、0；非零值在条件中一般按真处理，所以 `BOOLEAN` 本身不等于完整的业务校验。
- 电话、身份证、邮编、带前导零的订单号是**标识字符串**，不参与运算，应使用 `CHAR` / `VARCHAR`，例如 `'00123'`，避免丢失前导零。

精确小数说明见 [DECIMAL 文档](https://dev.mysql.com/doc/refman/8.0/en/fixed-point-types.html)，数值别名与属性见 [数值类型语法](https://dev.mysql.com/doc/refman/8.0/en/numeric-type-syntax.html)。

### 4. 数据类型：字符、文本与二进制

| 类型 | 长度或容量 | 适用场景 | 重要区别 |
|------|------------|----------|----------|
| `CHAR(n)` | `n` 为字符数，0～255 | 长度稳定的代码，如两位地区码 | 定长；尾随空格的存取和比较行为要结合规则判断，不适合精确保留原始尾空格 |
| `VARCHAR(n)` | `n` 为最大字符数 | 姓名、地址、手机号、URL | 按实际内容加长度信息存储；可用长度受字符集和整行字节限制影响 |
| `TINYTEXT` / `TEXT` | 最多 255 / 65535 字节 | 短备注、文章正文 | 存字符，有字符集与排序规则 |
| `MEDIUMTEXT` / `LONGTEXT` | 最多 16777215 / 4294967295 字节 | 大文本、较大日志内容 | 上限还受传输包大小、内存等约束，不代表推荐存满 |
| `BINARY(n)` | `n` 为字节数，定长 | 固定长度摘要、二进制标识 | 不足长度用 `0x00` 补齐，比较按字节 |
| `VARBINARY(n)` | `n` 为最大字节数，变长 | 需要按原始字节保存的数据 | 不使用字符集，不把内容当文本解释 |
| `TINYBLOB` / `BLOB` | 最多 255 / 65535 字节 | 较小二进制内容 | 对应 TEXT 家族的二进制版本 |
| `MEDIUMBLOB` / `LONGBLOB` | 最多 16777215 / 4294967295 字节 | 较大二进制内容 | 图片、视频等大文件通常更适合对象存储，数据库保存引用 |
| `ENUM('待支付','已支付','已取消')` | 从预定义值中选择一个 | 取值少且稳定的枚举 | 增加选项涉及改表；排序与内部序号有关，跨库迁移成本较高 |
| `SET('邮件','短信','站内信')` | 最多 64 个候选成员，可多选 | 小而固定的选项集合 | 与 SQL 的集合运算不是一回事；复杂多选关系优先用关联表 |

> `VARCHAR(100)` 表示最多 100 个字符，**不是 100 字节**。`utf8mb4` 中一个字符最多占 4 字节；`VARCHAR` 还受最大行大小 65535 字节及其他列影响，不能据此直接创建 `VARCHAR(65535)`。TEXT/BLOB 表中的容量按字节理解，中文能放多少字还取决于编码。参见 [字符串类型说明](https://dev.mysql.com/doc/refman/8.0/en/string-type-syntax.html)。

```sql
SELECT CHAR_LENGTH('中文') AS 字符数, LENGTH('中文') AS 字节数;
-- 在 utf8mb4 连接下，结果分别为 2 和 6
```

### 5. 数据类型：日期和时间

以下宽度以 MySQL 8.0 的现代存储格式、不带小数秒时为基准，不包括行管理开销。

| 类型 | 基础字节 | 范围 / 格式 | 用途与注意事项 |
|------|----------|-------------|----------------|
| `DATE` | 3 | `1000-01-01`～`9999-12-31` | 生日、账期日期，只有年月日 |
| `TIME(fsp)` | 3 | `-838:59:59`～`838:59:59`，可带小数秒 | 一天中的时刻，或此范围内的时长；长时长也可用整数秒 |
| `DATETIME(fsp)` | 5 | `1000-01-01 00:00:00`～`9999-12-31 23:59:59`，可带小数秒 | 业务日期时间；存字面日期时间，不自动做时区转换 |
| `TIMESTAMP(fsp)` | 4 | 不带小数秒时，UTC `1970-01-01 00:00:01`～`2038-01-19 03:14:07` | 按会话时区与 UTC 互转；有 2038 范围限制 |
| `YEAR` | 1 | 1901～2155，另有 0000 | 只保存年份；不使用旧式两位年份 |

- `fsp` 是小数秒位数，0～6，省略时为 0；1～2、3～4、5～6 位分别增加 1、2、3 字节。`DATETIME(3)` 可保存毫秒，`DATETIME(6)` 可保存微秒。
- `TIMESTAMP` 不保存原始时区名称或偏移；`DATETIME` 也不携带时区。跨时区系统应统一约定，例如在应用与连接中统一使用 UTC。
- `DATETIME` 和 `TIMESTAMP` 都能显式写 `DEFAULT CURRENT_TIMESTAMP`；加 `ON UPDATE CURRENT_TIMESTAMP` 可在行其他值实际改变时自动更新时间。不要误以为只有 `TIMESTAMP` 支持自动时间。
- 使用完整四位年份和标准格式；不要依赖 `0000-00-00` 等零日期，是否合法受 `sql_mode` 影响。

```sql
-- 独立示例：记录业务时间和更新时间
CREATE TABLE event_log (
    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    occurred_at DATETIME(3) NOT NULL,
    updated_at DATETIME(3) NOT NULL
        DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

日期范围和时区行为见 [日期时间类型](https://dev.mysql.com/doc/refman/8.0/en/datetime.html)；空间与小数秒开销见 [类型存储需求](https://dev.mysql.com/doc/refman/8.0/en/storage-requirements.html)。

### 6. 数据类型：JSON 与空间数据

| 类型 | 作用 | 示例与选型 |
|------|------|------------|
| `JSON` | 保存合法 JSON 对象、数组、标量，并支持路径查询 | 可变的产品属性；核心金额、关联 ID 等仍优先建普通列 |
| `GEOMETRY` | 通用空间对象 | GIS 数据；需要明确坐标参考系 |
| `POINT` / `LINESTRING` / `POLYGON` | 点 / 线 / 面 | 位置、路线、区域 |
| `MULTIPOINT` / `MULTILINESTRING` / `MULTIPOLYGON` / `GEOMETRYCOLLECTION` | 多个或混合空间对象 | 多区域边界等专业 GIS 场景 |

```sql
-- 独立示例：JSON 列会校验输入是否为合法 JSON
CREATE TABLE product_extra (
    product_id BIGINT UNSIGNED PRIMARY KEY,
    attrs JSON NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO product_extra VALUES
(1, JSON_OBJECT('color', '蓝色', 'tags', JSON_ARRAY('文具', '新品')));

SELECT product_id, attrs->>'$.color' AS color FROM product_extra;
-- -> 返回 JSON 值；->> 返回去掉 JSON 字符串引号后的文本
```

> JSON 文档中的 `null` 与 SQL 的 `NULL` 不相同；路径不存在也需要单独处理。JSON 列不能直接像普通标量列一样建普通索引，常用生成列或函数索引提取需要检索的属性。参见 [JSON 类型文档](https://dev.mysql.com/doc/refman/8.0/en/json.html)。空间类型见 [空间数据类型](https://dev.mysql.com/doc/refman/8.0/en/spatial-type-overview.html)。

### 7. 字段选型：从业务含义出发

| 业务字段 | 推荐起点 | 为什么 |
|----------|----------|--------|
| 自增行 ID | `INT UNSIGNED` 或 `BIGINT UNSIGNED` | 按预期规模选择；关联表的外键类型、符号保持一致 |
| 年龄 | `TINYINT UNSIGNED` + `CHECK` | 类型只规定存储范围，业务范围还需约束；更长期的资料可存生日 |
| 金额 | `DECIMAL(12,2)` | 精确十进制；币种和小数位规则应明确 |
| 开关 | `BOOLEAN NOT NULL` + `CHECK (列 IN (0,1))` | 同时表达存储形式、非空和合法值 |
| 电话、外部订单号 | `VARCHAR(n)` | 保留前导零、字母、加号等格式 |
| 状态 | `VARCHAR` + `CHECK`，或状态字典表 | 状态常变化时比固定 ENUM 更便于维护 |
| 生日 / 下单时间 | `DATE` / `DATETIME(3)` | 选择所需的时间精度和时区策略 |
| 文章 / 文件 | `TEXT` / 文件地址字符串 | 大文件优先放文件或对象存储 |

> 选择能满足范围和增长需求的类型；类型、`NOT NULL`、默认值、约束、索引各管不同问题，不能互相替代。不要把所有字段都设为 `VARCHAR(255)`，也不要为了“以后可能用到”全部设为最大类型喵！

---

<a id="dml"></a>

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
-- 📐 语法模板：WHERE 在语法上可选，更新部分行时必须写正确条件
UPDATE 表名 SET 列1 = 值1 [, 列2 = 值2, ...] [WHERE 条件];

-- ✅ 更新指定行（⚠️ 不写 WHERE 会更新全表！）
UPDATE student SET score = 100 WHERE name = 'yuki';

-- 多列更新
UPDATE student SET age = age + 1, score = LEAST(score + 5, 100) WHERE id = 1;
```

### 3. 删除 DELETE

```sql
-- 📐 语法模板（⚠️ WHERE 建议必写！）
DELETE FROM 表名 [WHERE 条件];

-- ✅ 删除指定行（⚠️ 不写 WHERE 会清空全表！）
DELETE FROM student WHERE id = 4;

-- 清空整张表（自增从 1 重新开始，不能带 WHERE）
-- TRUNCATE TABLE student;  -- 破坏性演示，后续练习不要执行
```

> ⚠️ **UPDATE / DELETE 忘记 WHERE = 灾难**，一定要养成先 SELECT 看一眼的习惯喵！
> 💡 语法模板里 `[WHERE 条件]` 加了方括号，但实际使用中**强烈建议必写**喵！

### 4. DELETE、TRUNCATE、DROP 有什么不同？

| 命令 | 删除内容 | 能带 WHERE | InnoDB 中能否事务回滚 | 自增计数 |
|------|----------|------------|----------------------|----------|
| `DELETE FROM 表 WHERE ...` | 满足条件的数据行，保留结构 | 能 | 未提交时可以；自动提交后不可以 | 通常不重置 |
| `TRUNCATE TABLE 表` | 全部数据，保留表定义 | 不能 | 不能当普通 DML 回滚，会隐式提交 | 重置为起始值 |
| `DROP TABLE 表` | 表定义和数据 | 不能 | 普通表的 DROP 会隐式提交 | 随表删除 |

`TRUNCATE` 属于 DDL，通常比逐行删除快，但外键引用等情况会限制执行。删除前确认库名、条件和备份；`CREATE`、`ALTER` 等 DDL 也通常会隐式提交，不能靠“包进事务里”防误操作。参见 [隐式提交语句](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html)。

```sql
-- 把查询结果写入另一张表：先建好 student_archive 表再执行
-- INSERT INTO student_archive (name, gender, age, score)
-- SELECT name, gender, age, score FROM student WHERE score >= 90;
```

---

<a id="dql"></a>

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
| `=` `<>`（或 `!=`）`>` `<` `>=` `<=` | 比较；SQL 标准不等号为 `<>` |
| `AND` / `OR` / `NOT` | 逻辑 |
| `LIKE` | 模糊匹配（`%` 任意多个，`_` 一个） |
| `IN (...)` | 在集合内 |
| `BETWEEN a AND b` | 闭区间，包含两端 |
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

**条件与 NULL 的关键规则：**

- `NULL` 表示未知或缺失，不是 0，也不是空字符串 `''`。`score = NULL`、`score <> NULL` 都不能正确筛选空值，应使用 `IS NULL` / `IS NOT NULL`。
- 普通比较遇到 `NULL` 通常得到 UNKNOWN；`WHERE` 只保留 TRUE。`NULL + 1` 仍为 `NULL`，可用 `COALESCE(score, 0)` 显式指定缺失值的替代值，但是否按 0 统计要由业务决定。
- `NOT IN` 的候选集合或子查询含 `NULL` 时容易得到 UNKNOWN，排除关联记录通常优先使用 `NOT EXISTS`。
- 逻辑优先级通常为 `NOT` → `AND` → `OR`，复杂条件加括号。例如 `(age = 18 OR age = 19) AND score >= 90`。
- `%` 匹配零个或多个字符，`_` 匹配一个字符；搜索字面通配符可指定转义符，例如 `LIKE '%!_%' ESCAPE '!'` 搜索下划线。
- MySQL 特有的 `<=>` 是 NULL 安全相等：`NULL <=> NULL` 为 1；普通 SQL 优先使用 `IS NULL` 明确表达。

```sql
SELECT * FROM student WHERE score IS NULL;
SELECT name, COALESCE(score, 0) AS 展示成绩 FROM student;
```

### 3. 聚合函数

| 函数 | 作用 |
|------|------|
| `COUNT(*)` | 统计结果行数，不因某列为 NULL 而漏计 |
| `COUNT(列)` / `COUNT(DISTINCT 列)` | 统计非 NULL 值数 / 不重复的非 NULL 值数 |
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

> `SUM`、`AVG`、`MAX`、`MIN` 忽略 NULL；空结果集上 `COUNT` 为 0，而这些聚合通常返回 NULL。`AVG(score)` 是有成绩者的平均值，`AVG(COALESCE(score,0))` 则把缺失成绩也当作 0，含义不同。

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

> 默认启用 `ONLY_FULL_GROUP_BY` 时，SELECT 中非聚合列应出现在 GROUP BY 中，或能由分组列函数依赖地确定。入门时遵循“非聚合列都写入 GROUP BY”更直观，不要随便关闭模式来掩盖含义不清的查询。

### 5. 排序 ORDER BY + 分页 LIMIT

```sql
-- 按成绩降序（升序 ASC / 降序 DESC）
SELECT * FROM student ORDER BY score DESC;

-- 多字段排序：成绩降序，同分按年龄升序
SELECT * FROM student ORDER BY score DESC, age ASC;

-- 分页：第 2 页，每页 3 条（偏移量 = (页码-1) × 每页条数）
SELECT * FROM student ORDER BY score DESC, id ASC LIMIT 3 OFFSET 3;
-- 或简写：LIMIT 偏移量, 条数
SELECT * FROM student ORDER BY score DESC, id ASC LIMIT 3, 3;
```

> 分页排序加唯一列（如 id）作为同分时的次级排序，否则同分记录的页内顺序可能变化；并发插入或删除仍可能让 OFFSET 分页产生重复或遗漏，大数据分页见第十一章。

### 6. DQL 逻辑处理顺序

```
FROM / JOIN / ON → WHERE → GROUP BY → HAVING → 窗口计算 → SELECT → DISTINCT → ORDER BY → LIMIT
```

> 🐱 记忆口诀：**从哪来（FROM）→ 过滤行（WHERE）→ 分组（GROUP BY）→ 过滤组（HAVING）→ 选出列（SELECT）→ 排序（ORDER BY）→ 分页（LIMIT）** 喵！

> 这是理解语义的逻辑顺序，优化器的实际物理执行计划可能不同。SELECT 中的别名通常不能用于同层 WHERE；MySQL 允许在 GROUP BY、HAVING、ORDER BY 中引用适用的 SELECT 别名。窗口计算的结果需放到外层查询中再筛选。

### 7. 常用函数与 CASE 表达式

| 类别 | 函数 / 表达式 | 作用和例子 |
|------|---------------|------------|
| 字符串 | `CONCAT`、`CONCAT_WS` | 拼接文本；后者使用分隔符并跳过 NULL 参数 |
| 字符串 | `CHAR_LENGTH`、`LENGTH` | 字符数 / 字节数 |
| 字符串 | `SUBSTRING`、`TRIM`、`REPLACE`、`UPPER`、`LOWER` | 截取、去首尾空格、替换、大小写转换 |
| 数值 | `ROUND(x,d)`、`ABS`、`CEIL`、`FLOOR` | 舍入、绝对值、向上 / 向下取整 |
| 空值 | `COALESCE(a,b,...)`、`IFNULL(a,b)` | 第一个非 NULL 值；IFNULL 是 MySQL 常用写法 |
| 防除零 | `NULLIF(a,b)` | 两值相等返回 NULL，否则返回 a；`x / NULLIF(y,0)` |
| 日期 | `CURRENT_DATE`、`NOW()` | 当前日期 / 当前日期时间，受会话时区影响 |
| 日期 | `DATE_FORMAT`、`DATE_ADD`、`DATEDIFF` | 日期格式化、日期加减、两日期相差天数 |
| 转换 | `CAST(expr AS DECIMAL(10,2))` | 显式转换类型，避免依赖隐式转换 |
| 条件 | `CASE WHEN ... THEN ... ELSE ... END` | 多分支分类，返回表达式值 |

```sql
SELECT name, score,
       CASE
           WHEN score IS NULL THEN '未录入'
           WHEN score >= 90 THEN '优秀'
           WHEN score >= 60 THEN '及格'
           ELSE '不及格'
       END AS 等级
FROM student;

SELECT DATE_ADD('2026-01-01', INTERVAL 7 DAY) AS 一周后;
```

> `CONCAT('成绩：', NULL)` 返回 NULL；需要时先 `COALESCE`。将字符串编号列与数字比较可能发生隐式转换，既改变语义又影响索引，例如不要用 `phone = 13800138000` 代替 `phone = '13800138000'`。

---

<a id="constraints"></a>

## 🔒 五、约束

| 约束 | 关键字 | 作用 |
|------|--------|------|
| 主键 | `PRIMARY KEY` | 唯一标识一行，非空且唯一 |
| 非空 | `NOT NULL` | 不能为空 |
| 唯一 | `UNIQUE` | 不能重复 |
| 检查 | `CHECK (条件)` | 限制成绩、金额、状态等合法值（MySQL 8.0.16+） |
| 默认值 | `DEFAULT` | 不填时用默认值 |
| 自增属性 | `AUTO_INCREMENT` | 自动生成整数值（常配合主键），不保证连续 |
| 外键 | `FOREIGN KEY` | 关联另一张表 |

```sql
USE school;
CREATE TABLE class (
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 给第二章已创建的 student 增加外键，避免重复建表
ALTER TABLE student
    ADD COLUMN class_id INT,
    ADD CONSTRAINT fk_student_class FOREIGN KEY (class_id)
        REFERENCES class(id) ON DELETE SET NULL ON UPDATE RESTRICT,
    ADD CONSTRAINT chk_student_score CHECK (score BETWEEN 0 AND 100),
    ADD CONSTRAINT chk_student_age CHECK (age BETWEEN 0 AND 150);

INSERT INTO class (name) VALUES ('一班'), ('二班'), ('三班');
UPDATE student SET class_id = (SELECT id FROM class WHERE name = '一班')
WHERE name IN ('日辰羽', 'richenyv');
UPDATE student SET class_id = (SELECT id FROM class WHERE name = '二班')
WHERE name = 'cunriyang';
```

**约束不是写上去就万事大吉：**

- 一张表只有一个主键，但主键可由多列组成。`UNIQUE` 可以有多个；MySQL 唯一索引允许多个 NULL，需要“必填且唯一”时同时使用 `NOT NULL UNIQUE`。
- `DEFAULT` 在省略该列或显式写 `DEFAULT` 时使用；显式插入 NULL 不会普遍自动换成默认值。
- `CHECK (score BETWEEN 0 AND 100)` 允许 NULL，因为检查结果 UNKNOWN 也通过；若成绩必填，再加 `NOT NULL`。旧版本可能解析 CHECK 却不执行，参见 [CHECK 约束文档](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html)。
- `AUTO_INCREMENT` 是列属性；删除、回滚或并发分配都可能产生编号空洞，不能用最大 ID 代表行数。
- 外键负责引用完整性：先插父表再插子表。整数外键与被引用列的类型和符号应匹配，字符串还要考虑字符集和排序规则；被引用列优先使用主键或唯一键。
- `RESTRICT` / InnoDB 中的 `NO ACTION` 拒绝破坏引用的修改；`CASCADE` 级联修改或删除；`SET NULL` 将外键置空，要求该列可空。级联删除会扩大影响范围，按业务选择。

### 关系建模：把数据放在哪张表？

| 关系 / 概念 | 建模方式 | 例子 |
|-------------|----------|------|
| 一对多 | 在“多”的一方放外键 | 一个班级有多个学生，student.class_id |
| 一对一 | 外键加 UNIQUE，或合理合表 | 用户与仅有一份的扩展资料 |
| 多对多 | 新建关联表，使用复合主键或唯一键 | 学生选多门课，课程也有多名学生 |
| 第一范式 | 每个字段存当前模型下不可再分的单值 | 不把多个课程 ID 拼成逗号字符串 |
| 第二范式 | 非键属性依赖整个候选键 | 选课表的成绩依赖“学生 + 课程” |
| 第三范式 | 消除非键属性之间的传递依赖 | 班级名称放 class 表，不在每个学生行反复维护 |

```sql
CREATE TABLE course (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE enrollment (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score DECIMAL(5,2),
    PRIMARY KEY (student_id, course_id),
    CONSTRAINT fk_enrollment_student FOREIGN KEY (student_id) REFERENCES student(id),
    CONSTRAINT fk_enrollment_course FOREIGN KEY (course_id) REFERENCES course(id),
    CONSTRAINT chk_enrollment_score CHECK (score BETWEEN 0 AND 100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

> 适度反范式化可用于报表或性能需求，但要有同步机制。例如订单保存下单时单价，是保留交易快照的业务要求，不能一概当成“冗余错误”。

---

<a id="multi-table"></a>

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
| `INNER JOIN` | 每个符合 ON 的行对；一对多时同一左表行可重复 |
| `LEFT JOIN` | 匹配行对 + 左表未匹配行（右侧补 NULL） |
| `RIGHT JOIN` | 匹配行对 + 右表未匹配行（左侧补 NULL） |

> JOIN 不是简单的集合交集：一对多关联会增加结果行数，不要随手 `DISTINCT` 来掩盖关系或统计错误。`CROSS JOIN` 产生笛卡尔积；自连接是同一张表使用不同别名连接；MySQL 8.0 不原生支持 `FULL OUTER JOIN`。

```sql
-- 统计每班的高分学生数，也保留没有高分学生的班级
SELECT c.id, c.name, COUNT(s.id) AS 高分人数
FROM class c
LEFT JOIN student s ON s.class_id = c.id AND s.score >= 90
GROUP BY c.id, c.name;
```

> 左连接右表的筛选条件放在 `ON` 中可以保留没有匹配的左表行；放在 `WHERE s.score >= 90` 中会过滤掉右侧补 NULL 的行。统计右表匹配数量用 `COUNT(s.id)`，不能用会把补空行也算进去的 `COUNT(*)`。

### 2. 子查询

```sql
-- 查询成绩高于平均分的同学
SELECT * FROM student
WHERE score > (SELECT AVG(score) FROM student);

-- 查询有学生的班级（IN 子查询）
SELECT * FROM class
WHERE id IN (SELECT DISTINCT class_id FROM student WHERE class_id IS NOT NULL);
```

| 子查询形式 | 返回内容 | 用法 |
|------------|----------|------|
| 标量子查询 | 一列且最多一行 | `score > (SELECT AVG(score) ...)`；多行会报错 |
| 列子查询 | 一列多行 | `IN (SELECT class_id ...)` |
| 派生表 | 多行多列 | `FROM (SELECT ...) AS t`，MySQL 要写别名 |
| 相关子查询 | 通过外层列关联 | `EXISTS` / `NOT EXISTS`，表达是否存在匹配行 |

```sql
-- 没有学生的班级：不受 student.class_id 中 NULL 的干扰
SELECT c.id, c.name
FROM class c
WHERE NOT EXISTS (
    SELECT 1 FROM student s WHERE s.class_id = c.id
);
```

### 3. 集合合并：UNION 与 UNION ALL

```sql
-- 两份结果按列纵向合并，UNION ALL 保留重复行
SELECT name, '高分' AS 来源 FROM student WHERE score >= 90
UNION ALL
SELECT name, '成年' AS 来源 FROM student WHERE age >= 18;
```

两侧列数必须相同，相应列的类型应兼容；输出列名通常取第一条 SELECT。`UNION` 对整行去重，有额外开销；确定需要保留重复行就用 `UNION ALL`。JOIN 是按关系横向组合列，UNION 是纵向合并结果行。MySQL 8.0.31+ 才支持 `INTERSECT` / `EXCEPT`，较早的 8.0 版本可用 EXISTS / NOT EXISTS 表达相应需求。

### 4. CTE：给中间结果起名字（MySQL 8.0+）

```sql
WITH class_avg AS (
    SELECT class_id, AVG(score) AS avg_score
    FROM student
    WHERE class_id IS NOT NULL
    GROUP BY class_id
)
SELECT s.name, s.score, a.avg_score
FROM student s
JOIN class_avg a ON s.class_id = a.class_id
WHERE s.score > a.avg_score;
```

CTE（公用表表达式）只在当前语句内有效，适合把复杂查询拆成清楚的步骤；它不等于新建持久表，也不保证性能更好。递归层级数据可用 `WITH RECURSIVE`，需要终止条件和深度控制。

### 5. 窗口函数：保留明细的排名与统计（MySQL 8.0+）

```sql
SELECT id, name, class_id, score,
       ROW_NUMBER() OVER (PARTITION BY class_id ORDER BY score DESC, id ASC) AS 序号,
       RANK() OVER (PARTITION BY class_id ORDER BY score DESC) AS 竞赛排名,
       DENSE_RANK() OVER (PARTITION BY class_id ORDER BY score DESC) AS 连续排名,
       AVG(score) OVER (PARTITION BY class_id) AS 班级平均分
FROM student
WHERE class_id IS NOT NULL AND score IS NOT NULL;
```

| 函数 | 分数 100、100、90 的结果 | 用途 |
|------|------------------------|------|
| `ROW_NUMBER()` | 1、2、3 | 每行唯一序号；想稳定结果就加唯一排序列 |
| `RANK()` | 1、1、3 | 并列后跳号的竞赛排名 |
| `DENSE_RANK()` | 1、1、2 | 并列后不跳号，取前 N 档分数 |
| `LAG(列)` / `LEAD(列)` | 取排序后的上一行 / 下一行 | 环比、前后记录比较 |
| `SUM(列) OVER (...)` | 每行仍保留，可计算分区合计或累计值 | 累计销售额等 |

`PARTITION BY` 划分计算窗口，不会像 GROUP BY 一样把明细压成一行。窗口内 ORDER BY 控制计算顺序，最终展示顺序仍由最外层 ORDER BY 决定。累计值应明确框架，例如 `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`，避免默认框架把同排序值的行一起计入。

```sql
-- 每班最多取两名：先排名，再在外层筛选
WITH ranked AS (
    SELECT id, name, class_id, score,
           ROW_NUMBER() OVER (PARTITION BY class_id ORDER BY score DESC, id ASC) AS rn
    FROM student
    WHERE class_id IS NOT NULL AND score IS NOT NULL
)
SELECT * FROM ranked WHERE rn <= 2 ORDER BY class_id, rn;
```

进一步阅读：[WITH / CTE](https://dev.mysql.com/doc/refman/8.0/en/with.html)、[窗口函数](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html)。

---

<a id="transactions"></a>

## 💼 七、事务

### 1. 四大特性 ACID

| 特性 | 含义 |
|------|------|
| **A**tomicity 原子性 | 要么全成功，要么全失败 |
| **C**onsistency 一致性 | 事务应把数据从一个合法状态带到另一个合法状态，依赖约束和正确业务逻辑 |
| **I**solation 隔离性 | 通过隔离级别控制并发事务之间可见性和相互影响 |
| **D**urability 持久性 | 成功提交的数据按持久化机制保存；实际保障也受日志刷盘配置和硬件影响 |

### 2. 事务操作

```sql
-- 独立练习表：先建表和准备数据，再开始事务
CREATE TABLE account (
    id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    money DECIMAL(12,2) NOT NULL,
    CONSTRAINT chk_account_money CHECK (money >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT INTO account VALUES (1, '日辰羽', 1000.00), (2, 'yuki', 500.00);

START TRANSACTION;
-- 按主键顺序锁住两行，检查双方存在和余额充足
SELECT id, money FROM account WHERE id IN (1, 2) ORDER BY id FOR UPDATE;
UPDATE account SET money = money - 500 WHERE id = 1 AND money >= 500;
SELECT ROW_COUNT() AS 扣款影响行数;  -- 必须为 1
UPDATE account SET money = money + 500 WHERE id = 2;
SELECT ROW_COUNT() AS 入账影响行数;  -- 必须为 1
-- 本例已知两行存在且余额充足，提交
COMMIT;
-- 实际程序任一步异常或影响行数不符，应走 ROLLBACK 分支，不执行 COMMIT
```

> SQL 客户端不会因为注释“必须为 1”就自动判断；实际程序必须检查结果并分支。普通语句报错也不意味着整个事务一定已回滚，应用应捕获异常并明确回滚。**COMMIT 后再 ROLLBACK 不能撤销已提交结果**；MySQL 不支持用嵌套 START TRANSACTION 实现嵌套事务。

### 3. 自动提交与保存点

```sql
SELECT @@autocommit;  -- MySQL 会话默认通常为 1；客户端可覆盖

-- 独立演示：回滚到保存点只撤销保存点之后的操作
START TRANSACTION;
UPDATE account SET money = money + 10 WHERE id = 1;
SAVEPOINT after_first_update;
UPDATE account SET money = money + 20 WHERE id = 2;
ROLLBACK TO SAVEPOINT after_first_update;
ROLLBACK;  -- 最后连第一步也撤销，示例不保留余额改动
```

显式 `START TRANSACTION` 可把多条语句组成一次事务，直到 COMMIT / ROLLBACK。`SET autocommit = 0` 影响当前会话，连接池归还连接前还需恢复状态；不要在事务中混入会隐式提交的普通 DDL。事务示例要求 InnoDB 等事务型引擎，MyISAM 不能提供同样的事务回滚能力。

### 4. 隔离级别与并发问题

| 问题 | 含义 |
|------|------|
| 脏读 | 读到了其他事务尚未提交的数据 |
| 不可重复读 | 同一事务重复读取同一行，值发生变化 |
| 幻读 | 重复按条件查询，满足条件的行集合发生变化 |

| 隔离级别 | InnoDB 中的典型行为 |
|----------|--------------------|
| `READ UNCOMMITTED` | 可能脏读，通常不作为业务默认 |
| `READ COMMITTED` | 不读未提交值；每次一致性读建立新的快照 |
| `REPEATABLE READ` | InnoDB 默认；同一事务的一致性读通常共享首次一致性读建立的快照 |
| `SERIALIZABLE` | 更强隔离，锁等待和并发开销通常更大 |

```sql
SELECT @@transaction_isolation;
-- 必须在事务开始前设置；只作用于下一次事务
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT * FROM account;
COMMIT;
```

> 隔离级别的教科书表格不能代替 InnoDB 的具体实现：普通 SELECT 的 MVCC 快照读，与 `SELECT ... FOR UPDATE`、UPDATE、DELETE 等锁定读或写入行为不同。可重复读下，一致性快照避免看到新增行，合适的范围锁定读还可通过 next-key lock 限制范围插入；不要概括成“任何查询都绝对不会幻读”。参见 [InnoDB 隔离级别](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html)。

### 5. 锁与并发写入的实用原则

- InnoDB 支持行锁，但锁作用于扫描的索引记录，范围扫描还可能涉及间隙；缺少合适索引时锁范围可能很大。
- 余额、库存等“先查再改”应使用事务内锁定读，或带条件的原子 UPDATE，并检查影响行数。例如 `UPDATE stock SET quantity = quantity - 1 WHERE id = 1 AND quantity > 0`。
- 乐观锁常用 `version` 列：更新条件带旧版本，成功后版本加 1；影响 0 行意味着需处理冲突或记录不存在。
- 死锁并不等于数据库损坏：保持事务短小、按统一顺序访问记录；遇到死锁应回滚后有界重试整个事务，不能无限重试。


---

<a id="dcl"></a>

## 🛡️ 八、DCL —— 用户与权限控制

> 管理「谁能连数据库、能对哪些库表做什么」喵！执行者需要相应的账号管理或授权权限，并不限于 root。

### 1. 用户管理

```sql
-- 📐 语法模板
CREATE USER '用户名'@'主机' [IDENTIFIED BY '密码'];
ALTER USER '用户名'@'主机' [IDENTIFIED BY '新密码'];
DROP USER '用户名'@'主机';

-- ✅ 查看所有用户（用户信息存在 mysql 库的 user 表里）
SELECT user, host FROM mysql.user;

-- 创建用户（账号名由 '用户名'@'来源主机' 共同组成）
CREATE USER 'richenyv'@'localhost' IDENTIFIED BY '替换为独立的强密码';
-- 跨主机示例使用明确来源地址；按实际网络修改
CREATE USER 'yuki'@'192.0.2.10' IDENTIFIED BY '替换为另一独立强密码';

-- 修改密码
ALTER USER 'richenyv'@'localhost' IDENTIFIED BY 'new_password';

-- 删除用户
-- DROP USER 'richenyv'@'localhost';  -- 管理演示，后续授权仍要用此账号
```

### 2. 权限控制

```sql
-- 📐 语法模板
GRANT 权限列表 ON 库名.表名 TO '用户名'@'主机';
REVOKE 权限列表 ON 库名.表名 FROM '用户名'@'主机';
SHOW GRANTS FOR '用户名'@'主机';

-- ✅ 授权：把 school 库所有表的 查询+插入 权限给用户
GRANT SELECT, INSERT ON school.* TO 'richenyv'@'localhost';

-- 授权另一个账号只读访问 school
GRANT SELECT ON school.* TO 'yuki'@'192.0.2.10';

-- CREATE USER / GRANT / REVOKE 会由服务器自动装载相应修改
-- 无需例行执行 FLUSH PRIVILEGES

-- 查看用户的权限
SHOW GRANTS FOR 'richenyv'@'localhost';

-- 收回权限：把插入权限收回来
REVOKE INSERT ON school.* FROM 'richenyv'@'localhost';

-- 收回全部权限
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'yuki'@'192.0.2.10';
```

### 3. 常用权限清单

| 权限 | 作用 |
|------|------|
| `ALL PRIVILEGES` | 指定授权层级可授予的权限；不自动包含 GRANT OPTION，并非所有管理能力的统称 |
| `SELECT` / `INSERT` / `UPDATE` / `DELETE` | 增删改查（最常用） |
| `CREATE` / `DROP` / `ALTER` | 建删改表结构 |
| `GRANT OPTION` | 允许用户再给别人授权 |

> 💡 `ON 数据库.表` 的写法：
> `school.*` 表示 school 库的所有表，`*.*` 表示所有库所有表喵！

> 🐱 **最小权限原则**：给用户够用的最小权限就好，别动不动就 `ALL PRIVILEGES` 喵！

> `'用户'@'主机'` 共同标识账号。`%` 表示广泛的来源主机匹配，但能否远程连接还取决于监听、网络、认证和 TLS 配置；MySQL 8.0.35 起账号主机通配符已弃用，新配置优先使用明确主机或合适网段。`192.0.2.10` 是文档示例地址，实际练习需替换。
> 标准账号管理语句不需要手动刷新授权表；已有连接何时看到权限变化与权限层级有关，验证时可重新连接。直接修改系统授权表不推荐，特殊情况下才涉及重新加载。参见 [权限修改生效机制](https://dev.mysql.com/doc/refman/8.0/en/privilege-changes.html)。

---

<a id="practice"></a>

## 🏆 九、实战案例

### 🎓 案例 1：学生成绩管理

> 独立案例放在 `school_practice` 库，避免和前文的 `school.student` 结构冲突。首次练习时建表并插入一次；重复插入会增加重复的业务记录。

```sql
-- 1. 建库建表
CREATE DATABASE IF NOT EXISTS school_practice DEFAULT CHARSET utf8mb4;
USE school_practice;

CREATE TABLE student (
    id     INT PRIMARY KEY AUTO_INCREMENT,
    name   VARCHAR(20) NOT NULL,
    gender CHAR(1) DEFAULT '男',
    score  DECIMAL(5,2),
    CONSTRAINT chk_practice_score CHECK (score BETWEEN 0 AND 100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. 插入数据
INSERT INTO student (name, gender, score) VALUES
('日辰羽', '男', 95.5), ('richenyv', '男', 92.0),
('cunriyang', '女', 88.5), ('yuki', '女', 99.0), ('momo', '女', 76.0);

-- 3. 实战查询
-- ① 成绩排名（降序）
SELECT name, score FROM student ORDER BY score DESC;

-- ② 各性别平均分
SELECT gender, AVG(score) AS 平均分 FROM student GROUP BY gender;

-- ③ 及格率（以已录入成绩人数为分母，避免空表除零）
SELECT
    COUNT(*) AS 总人数,
    COUNT(score) AS 已录入人数,
    SUM(CASE WHEN score >= 60 THEN 1 ELSE 0 END) AS 及格人数,
    ROUND(100.0 * SUM(CASE WHEN score >= 60 THEN 1 ELSE 0 END)
          / NULLIF(COUNT(score), 0), 1) AS 及格率
FROM student;

-- ④ 前三名
SELECT name, score FROM student ORDER BY score DESC, id ASC LIMIT 3;
```

这五条初始数据的平均分为 **90.2**，及格率为 **100.0%**，前三名为 yuki、日辰羽、richenyv。没有任何已录入成绩时及格率返回 NULL，表示没有可计算的分母。

### 🛒 案例 2：电商订单统计

```sql
CREATE DATABASE IF NOT EXISTS shop DEFAULT CHARSET utf8mb4;
USE shop;

-- 订单表
CREATE TABLE orders (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    user_name  VARCHAR(20) NOT NULL,
    amount     DECIMAL(10,2) NOT NULL,
    status     VARCHAR(10) NOT NULL DEFAULT '待支付',
    order_time DATETIME NOT NULL,
    CONSTRAINT chk_order_amount CHECK (amount >= 0),
    CONSTRAINT chk_order_status CHECK (status IN ('待支付', '已支付', '已取消'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO orders (user_name, amount, status, order_time) VALUES
('yuki', 120.00, '已支付', '2026-01-05 10:00:00'),
('日辰羽', 80.00, '已支付', '2026-01-20 12:30:00'),
('yuki', 200.00, '已支付', '2026-02-02 09:00:00'),
('momo', 500.00, '待支付', '2026-02-03 15:00:00');

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
WHERE status = '已支付'
  AND amount > (SELECT AVG(amount) FROM orders WHERE status = '已支付');

-- ④ 查询某月订单：用半开区间覆盖整月，不遗漏月末带小数秒的数据
SELECT * FROM orders
WHERE order_time >= '2026-01-01' AND order_time < '2026-02-01';
```

初始数据中：yuki 已支付总额 320.00，日辰羽 80.00；一月、二月销售额均为 200.00；已支付订单均额约 133.33，只有 200.00 的已支付订单满足③。待支付的 500.00 不应混进已支付大额订单结果。

### 🐍 案例 3：Python + pymysql 连接实战

> 这是 Python 项目，当然要联动起来喵！
> 📄 **现有学习代码**：[`pymysql入门.py`](./pymysql入门.py) 使用 `school_student.infernation_student`，不是前文的 `school.student`，需事先建好对应表；其中固定插入的 ID 重复运行可能触发主键冲突。下面是基于前文 `school.student` 的改进示例，不代表现有 `.py` 已同步修改。

```python
# pip install pymysql

import os
from decimal import Decimal
import pymysql

password = os.environ["MYSQL_PASSWD"]  # PowerShell 中先设置环境变量
conn = pymysql.connect(
    host=os.getenv("MYSQL_HOST", "127.0.0.1"),
    port=int(os.getenv("MYSQL_PORT", "3306")),
    user=os.getenv("MYSQL_USER", "dev"),
    password=password,
    database="school", charset="utf8mb4", autocommit=False,
)
try:
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO student (name, gender, score) VALUES (%s, %s, %s)",
            ("新同学", "女", Decimal("89.00")),
        )
        new_id = cursor.lastrowid  # 本次生成的自增主键
        cursor.execute("SELECT id, name, score FROM student WHERE id = %s", (new_id,))
        print(cursor.fetchone())
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```

> 💡 `pymysql入门.py` 里的实际写法：
> - `from pymysql import Connect` 或 `from pymysql import connect` 都能连
> - `autocommit=True` 自动提交，写操作不用手动 `commit()` 喵！
> - `conn.get_server_info()` 测试连接是否成功
> - `conn.select_db("库名")` 选择数据库，`cursor.fetchall()` 取回查询结果喵！

**Python 对接时还应知道：**

- PyMySQL 用 `%s` 绑定所有值类型，不给占位符再加引号，也不用 Python 的 `%` 运算、f-string、字符串相加拼入数据。单个参数要传 `(value,)`。
- 参数绑定适用于值，不能把表名、列名或 ASC/DESC 当作普通参数；动态标识符需从可信白名单选择。
- `fetchone()` 返回一行或 None，`fetchmany(n)` 分批取行，`fetchall()` 取剩余全部结果；默认游标一般返回元组，`DictCursor` 返回字典。
- 默认缓冲游标可能已把结果读入内存，大结果集可考虑 `SSCursor` 等流式游标，不能只换成 fetchmany 就认为没有内存压力。
- `cursor.rowcount` / `execute()` 返回值可检查写入影响行数；UPDATE 的“实际改变行数”与“匹配行数”还取决于连接选项，不能无条件把 0 当作 SQL 失败。
- 精确金额从源字符串开始使用 `Decimal('12.30')`，避免先变为 float 再转换；日期列可传 `datetime.date` / `datetime.datetime`，SQL NULL 对应 Python `None`。
- PyMySQL 默认 `autocommit=False`，与 MySQL 服务端新会话常见默认值不同；明确配置并处理提交、回滚和资源关闭。

连接和游标接口参见 [PyMySQL 官方示例](https://pymysql.readthedocs.io/en/latest/user/examples.html)。

### 🔐 案例 4：数据库账号与权限管理（DCL）

> 给团队成员创建账号，按职责分配最小权限喵！

```sql
-- 1. 创建两个账号：开发账号（本机）、只读分析账号（指定来源）
CREATE USER 'dev'@'localhost' IDENTIFIED BY '替换为开发账号强密码';
CREATE USER 'analyst'@'192.0.2.10' IDENTIFIED BY '替换为分析账号强密码';

-- 2. 授权：开发账号对 school 库拥有增删改查
GRANT SELECT, INSERT, UPDATE, DELETE ON school.* TO 'dev'@'localhost';

-- 3. 授权：分析账号只能查，不能改！
GRANT SELECT ON school.* TO 'analyst'@'192.0.2.10';

-- 4. GRANT 无需 FLUSH PRIVILEGES；用目标账号重新连接测试读写权限

-- 5. 验证：查看每个账号的权限
SHOW GRANTS FOR 'dev'@'localhost';
SHOW GRANTS FOR 'analyst'@'192.0.2.10';

-- 6. 人员离职 / 岗位调整：收回权限或删除账号
REVOKE DELETE ON school.* FROM 'dev'@'localhost';
-- DROP USER 'analyst'@'192.0.2.10';  -- 确认不再使用时执行
```

> 🐱 案例要点：**开发给写权限、分析只给读权限**，就是最小权限原则的实践喵！

### 📦 案例 5：销售数据上传 MySQL（综合案例/）

> 把 20 号文件夹的**面向对象** + 14 号文件夹的**销售数据** + **pymysql** 全部串起来喵！
> 📄 真实代码在 [`综合案例/`](./综合案例/) 里喵！

**运行前提**：先准备 `14-json原始数据/原始数据/` 中两份销售文件，核对脚本里的绝对路径，并设置 `MYSQL_PASSWD`。以下是供本案例使用的建表方案；`order_data` 保留现有代码的拼写（语义为订单日期），不同于电商案例的 `shop.orders`。

```sql
CREATE DATABASE IF NOT EXISTS py_sql DEFAULT CHARSET utf8mb4;
USE py_sql;
CREATE TABLE orders (
    order_data DATE NOT NULL,
    order_id VARCHAR(64) PRIMARY KEY,
    money DECIMAL(12,2) NOT NULL,
    province VARCHAR(50) NOT NULL,
    CONSTRAINT chk_sales_money CHECK (money >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

此表假设“一条销售记录对应一个唯一订单”。若一个订单有多条商品明细，应改为订单表 + 明细表，不能直接把订单号当明细行唯一键。

```
读取销售数据（txt + JSON）→ 封装成 Record 对象 → 连接 MySQL → 批量 INSERT → 验证上传
```

**文件分工喵：**

| 文件 | 作用 |
|------|------|
| `data_define.py` | `Record` 类封装一条销售记录（日期/订单id/金额/省份） |
| `File_define.py` | `Filereader` 父类 + `textreader`（读 txt 文本）+ `filereader`（读 JSON）子类 |
| `综合案例.py` | 主程序：读取 → 上传 → 验证 |
| `读取数据库.py` | 读取 orders，按行输出 JSON（JSON Lines） |

```python
# 改进版核心逻辑：all_data 来自文件读取器；连接异常处理见案例 3
# 现有 .py 仍为 f-string + 循环自动提交，下面展示推荐替换方式
import os
from decimal import Decimal
from pymysql import connect

conn = connect(
    host="localhost", user="dev", password=os.environ["MYSQL_PASSWD"],
    database="py_sql", charset="utf8mb4", autocommit=False,
)
try:
    rows = [
        (record.date, str(record.ID), Decimal(str(record.money)), record.province)
        for record in all_data
    ]
    with conn.cursor() as cursor:
        affected = cursor.executemany(
            "INSERT INTO orders (order_data, order_id, money, province) "
            "VALUES (%s, %s, %s, %s)",
            rows,
        )
        if affected != len(rows):
            raise RuntimeError("写入数量与输入数量不一致")
    conn.commit()
    print(f"本批次已提交 {affected} 条销售记录")
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```

> 💡 案例亮点喵：
> - 面向对象读取两种格式的文件，代码复用率高喵！
> - 现有代码 `autocommit=True` 每条提交，中途失败可能留下部分数据；上面的改进版统一提交或回滚，且使用参数化批量插入。
> - 改进版使用 `dev` 账号时，还需按第八章授权 `py_sql.orders` 的 SELECT、INSERT 权限。
> - `File_define.py` 目前先把金额转为 float；`Decimal(str(record.money))` 无法找回此前已丢失的精度。完整改进应在读取原始金额字符串时直接转 Decimal；JSON 可考虑 `json.loads(..., parse_float=Decimal)`。
> - 普通 INSERT 配合订单主键会在重复导入时冲突并回滚；需要重复导入时，先明确“跳过 / 覆盖 / 报错”的业务规则，不要用 `INSERT IGNORE` 掩盖所有错误。
> - `SELECT` 结果非空只说明表里有数据，不能证明本批次完整；提交前检查影响行数，必要时按本批次订单 ID 核对金额、数量。同步执行的 SQL 不需要 `sleep(2)` 才能完成。
> - 海量输入应分批处理以控制内存和事务长度；分批提交会改变“整份文件全部成功或失败”的语义，需要记录批次与恢复策略。

> 🔐 **安全提醒**：`pymysql入门.py` / `综合案例.py` / `读取数据库.py` 的数据库密码
> 当前从环境变量 `MYSQL_PASSWD` 读取（`os.getenv`），避免在这几份源码里直接写入密码。
> 运行前先设置：`$env:MYSQL_PASSWD='你的密码'` 喵！

### 📤 案例 6：数据库导出 JSON Lines

[`读取数据库.py`](./综合案例/读取数据库.py) 当前用 `SELECT *` 取所有行，以追加模式写出一行一个 JSON 对象。这是 **JSON Lines / NDJSON**，整份文件不是一个 JSON 数组：逐行可 `json.loads(line)`，不能直接对整份文件 `json.load()`。

- 导出时显式写列名并指定 ORDER BY，避免表结构或返回顺序变化影响 `r[0]`、`r[1]` 的对应关系。
- 快照导出通常用 `w` 覆盖模式；现有脚本用 `a`，重复运行会重复追加。需要追加时应设计去重或批次标识。
- `ensure_ascii=False` 让中文直接输出；`default=str` 会把 date、Decimal 等变成字符串，消费端应了解这一约定，不能把金额随意转 float。
- JSON 文件路径也需核对。大结果集采用流式读取和逐行写出，避免 `fetchall()` 占用过多内存。

```python
# 核心导出片段：conn 为已连接到 py_sql 的连接；连接关闭见案例 3
import json
from pathlib import Path

with conn.cursor() as cursor:
    cursor.execute(
        "SELECT order_data, order_id, money, province "
        "FROM orders ORDER BY order_data, order_id"
    )
    with Path("sales_export.jsonl").open("w", encoding="utf-8") as output:
        for order_date, order_id, money, province in cursor:
            item = {
                "date": order_date.isoformat(),
                "order_id": order_id,
                "money": str(money),
                "province": province,
            }
            output.write(json.dumps(item, ensure_ascii=False) + "\n")
```

---

<a id="quick-reference"></a>

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

<a id="indexes"></a>

## 🚀 十一、索引与查询性能

### 1. 索引解决什么问题？

索引相当于帮助定位数据的有序目录。InnoDB 常见索引基于 B+Tree，适合等值、范围查询和一定条件下的排序；代价是占用空间、增加写入和维护成本，所以索引不是越多越好。

| 索引 / 概念 | 作用与区别 |
|-------------|------------|
| 主键索引 | 唯一且非空；InnoDB 按聚簇主键组织行数据，主键宜短且稳定 |
| 普通索引 | 加速检索，不要求值唯一 |
| 唯一索引 | 同时约束唯一性和支持检索；MySQL 允许多个 NULL |
| 联合索引 | 多列组成一个索引，列顺序影响可用的检索前缀和排序 |
| 覆盖索引 | 某次查询所需列都能从索引取得，是查询与索引的关系，不是单独的 CREATE INDEX 类型 |
| 全文索引 | 文本词项检索；中文分词与检索语义需要专门配置 |
| 空间索引 | GIS 空间关系检索，不等同于普通 B+Tree 索引 |

```sql
USE shop;
CREATE INDEX idx_orders_status_time ON orders (status, order_time);
SHOW INDEX FROM orders;

EXPLAIN
SELECT id, order_time FROM orders
WHERE status = '已支付'
  AND order_time >= '2026-01-01' AND order_time < '2026-02-01'
ORDER BY order_time;

-- DROP INDEX idx_orders_status_time ON orders;  -- 删除索引的语法演示
```

### 2. 联合索引的最左前缀

对 `(status, order_time)`，按 status 查询，或按 status 等值再查 order_time 范围，通常容易利用索引的有序性；只按 order_time 查询不能简单视为拥有独立的 order_time 索引。优化器有时会选择 skip scan、索引全扫描等其他方式，最终以执行计划为准。

“范围条件后面的索引列完全没用”也过于绝对：后续列可能仍参与索引条件下推、覆盖或其他处理，只是未必继续缩小连续扫描区间。设计索引应结合过滤、连接、排序和返回列，而不是只背口诀。参见 [多列索引](https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html)。

### 3. 读懂 EXPLAIN

| 重点字段 | 看什么 |
|----------|--------|
| `type` | 常见访问方式有 const、eq_ref、ref、range、index、ALL；ALL 是全表扫描，index 通常是全索引扫描 |
| `possible_keys` / `key` | 可能使用 / 实际选择的索引 |
| `rows` / `filtered` | 预计扫描行数 / 过滤后比例，属于估计值 |
| `Extra` | `Using index` 常提示覆盖索引；`Using filesort` 表示额外排序，不一定写磁盘；`Using temporary` 提示临时表 |

MySQL 8.0.18+ 的 `EXPLAIN ANALYZE SELECT ...` 会**实际执行**查询并输出实际耗时和行数；不要把它当作零成本的静态分析。小表被优化器选中全表扫描常常合理，不能仅凭没有用索引就判定性能差。参见 [EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。

### 4. 常见优化做法

- 只取需要的列，避免无意义的 `SELECT *`、重复查询，以及在应用循环中对每行再查一次的 N+1 查询。
- 时间筛选优先写范围：`order_time >= '2026-01-01' AND order_time < '2026-02-01'`；对列直接套 `DATE_FORMAT()` 再比较，通常不利于直接利用该列普通索引。
- `LIKE 'abc%'` 在条件合适时可作索引范围检索；`LIKE '%abc%'` 通常无法直接使用普通 B+Tree 的前缀范围定位。全文检索与任意子串搜索也不是相同语义。
- 值类型和列类型一致，避免隐式转换；对列运算或函数调用可能影响普通索引使用，具体看计划，必要时评估生成列或函数索引。
- 低选择性列不代表“永远不能建索引”，应结合数据分布及联合条件。先 EXPLAIN，再用真实规模数据衡量，不要直接强制索引。
- 大偏移分页需要扫描和跳过大量记录。若业务允许只按 ID 顺序翻页，可改为 `WHERE id > 上一页末尾ID ORDER BY id LIMIT 20`；复合排序则需保存完整排序游标。
- 批量写入可用多行 INSERT、`executemany()`、合理大小的事务；索引、网络往返和日志刷盘都会影响速度。

---

<a id="database-programming"></a>

## 🪟 十二、视图与数据库编程

### 1. 视图 VIEW

视图保存查询定义，让调用者像查询表一样复用逻辑；普通视图一般不保存查询结果，也不自动带来性能提升。

```sql
USE school;
CREATE VIEW v_student_score AS
SELECT id, name, score FROM student WHERE score IS NOT NULL;

SELECT * FROM v_student_score WHERE score >= 90;
SHOW CREATE VIEW v_student_score;
-- DROP VIEW v_student_score;
```

包含聚合、分组等结构的视图通常不能直接更新。视图的执行权限还受 `SQL SECURITY DEFINER/INVOKER` 和授权控制影响，不能仅凭隐藏了某列就认为底表已被安全隔离。

### 2. 存储过程、函数、触发器和事件

| 对象 | 做什么 | 典型调用 / 注意点 |
|------|--------|--------------------|
| 存储过程 PROCEDURE | 封装多步数据库操作，支持参数 | `CALL 过程名(...)`；不自动保证事务原子性 |
| 存储函数 FUNCTION | 接收参数并返回单个值 | 在表达式中调用；有权限、复制等使用限制 |
| 触发器 TRIGGER | 某表 INSERT / UPDATE / DELETE 前后自动执行 | 行级触发；隐式副作用会增加调试成本，TRUNCATE 不触发 DELETE 触发器 |
| 事件 EVENT | 由数据库调度器定时执行任务 | 需要事件调度器启用和相应权限 |

```sql
-- 在 mysql 命令行中执行的完整存储过程示例
USE school;
DELIMITER $$
CREATE PROCEDURE list_students_by_min_score(IN p_min_score DECIMAL(5,2))
BEGIN
    SELECT id, name, score
    FROM student
    WHERE score >= p_min_score
    ORDER BY score DESC, id ASC;
END$$
DELIMITER ;

CALL list_students_by_min_score(90.00);
-- DROP PROCEDURE list_students_by_min_score;
```

> `DELIMITER` 是 mysql 客户端识别的命令，用于临时改变语句分隔符，**不是服务端 SQL**。从 PyMySQL 创建过程时不要把 DELIMITER 发送给 execute；应把完整 CREATE PROCEDURE 语句作为一次调用发送。初学优先掌握普通 SQL 与事务，再按需求引入数据库编程对象。

---

<a id="maintenance"></a>

## 🧰 十三、备份恢复、排错与方言差异

### 1. 逻辑备份与恢复

以下命令在终端执行，不是在 SQL 查询窗口执行。PowerShell 用 `--result-file` 避免旧版本重定向改变备份文件编码。

```powershell
# 备份 InnoDB 数据；将路径换成存在的备份目录
mysqldump -u root -p --default-character-set=utf8mb4 --single-transaction --routines --events --triggers --result-file="D:\backup\school.sql" school

# 恢复前先创建目标库，再进入 mysql 客户端
mysql -u root -p school_restore
```

```sql
-- 在 mysql 客户端中执行：source 是客户端命令，路径使用 / 更方便
SOURCE D:/backup/school.sql;
```

`--single-transaction` 主要为 InnoDB 提供一致性数据快照，不保证非事务表一致性；备份期间应避免相关 DDL。指定选项和对象可能需要额外权限。上述例子未备份 MySQL 账号授权；若需要时间点恢复，还需设计全量备份 + binlog 保留与恢复流程。备份只有在验证可恢复后才算可靠。参见 [mysqldump 文档](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)。

### 2. 常见错误怎么查？

| 现象 / 错误 | 优先检查 |
|-------------|----------|
| 无法连接服务器（如 2003） | 服务状态、主机、端口、监听、防火墙 |
| Access denied（1045） | 用户名、密码、账号 Host 匹配、认证方式 |
| No database selected（1046） | 是否 USE 了库，或连接参数指定 database |
| Unknown database / table（1049 / 1146） | 对象是否存在、当前库是否正确、大小写 |
| Duplicate entry（1062） | 主键 / 唯一键冲突，是否重复导入 |
| Data too long / Out of range（1406 / 1264） | 列长度、数值范围、源数据和严格模式 |
| 外键错误（如 1451 / 1452） | 父记录存在与否、删除顺序、关联列定义 |
| GROUP BY 错误（1055） | 非聚合列与分组语义是否正确 |
| 锁等待超时 / 死锁（1205 / 1213） | 长事务、访问顺序、索引、是否及时提交 |
| 中文乱码 / emoji 插入失败 | 文件、连接、库表列的编码是否一致为所需字符集 |

```sql
USE school;
SELECT DATABASE(), VERSION(), @@sql_mode;
SHOW CREATE TABLE student;
SHOW WARNINGS;  -- 紧接产生告警的语句查看
-- 管理员排锁时可按权限使用：SHOW PROCESSLIST; SHOW ENGINE INNODB STATUS;
```

### 3. 不同数据库的语法别混用

| 需求 | 本文 MySQL 写法 | 其他数据库常见写法 / 差异 |
|------|----------------|--------------------------------|
| 自动生成 ID | `AUTO_INCREMENT` | PostgreSQL 常用 identity，SQL Server 用 IDENTITY，SQLite 有自己的 INTEGER PRIMARY KEY 规则 |
| 分页 | `LIMIT n OFFSET m` | PostgreSQL / SQLite 也支持；SQL Server 常用 ORDER BY + OFFSET/FETCH |
| 标识符转义 | 反引号 | 标准 SQL 和 PostgreSQL 常用双引号；SQL Server 常见方括号 |
| 空值替代 | `COALESCE` / `IFNULL` | COALESCE 较通用，IFNULL 不通用 |
| 字符串拼接 | `CONCAT()` | 一些数据库使用 `\|\|`；MySQL 默认模式下 `\|\|` 通常表示逻辑 OR |
| 布尔类型 | `BOOLEAN` 是 TINYINT 别名 | PostgreSQL 有真正的 boolean，SQLite 类型体系不同 |
| 日期格式化 | `DATE_FORMAT()` | PostgreSQL 常用 to_char，SQL Server 函数不同 |
| 修改表 / DDL 事务 | MySQL 特有细节，普通 DDL 常隐式提交 | 各产品可用语法与事务语义不同，迁移时逐项核对 |

> MariaDB 与 MySQL 也不能视为完全相同的产品，版本、JSON 实现、优化器与特性支持都有差别。学概念时抓住通用 SQL，写代码时明确数据库产品和版本喵！

---

## 💡 小贴士（踩坑记录）

1. ⚠️ `UPDATE` / `DELETE` 忘写 `WHERE` = 全表遭殃，动手前先 `SELECT` 喵！
2. 💰 金额用 `DECIMAL`，别用 `FLOAT`，精度会哭喵！
3. 🔤 建库建表统一 `utf8mb4` 编码，中文 emoji 都安全喵！
4. 📏 DQL 的简化逻辑顺序：`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`，实际计划由优化器决定喵！
5. 🐍 Python 连 MySQL 用 `pymysql`，写操作记得 `commit()`（或 `autocommit=True`）喵！
6. 🚧 备份用 mysqldump，Windows PowerShell 优先 `--result-file`；还要实际验证恢复喵！
7. 🔐 DCL 遵循**最小权限原则**；使用标准授权语句后无需手动 `FLUSH PRIVILEGES` 喵！
8. 👤 `'用户'@'主机'` 是一对组合；优先限定来源主机，远程连接还受网络和监听配置限制喵！
9. 🔑 代码里的数据库密码别明文写死，用环境变量（`os.getenv`）或配置文件，防泄露喵！
10. 📦 批量写入优先参数化 `executemany()` + 合理事务；检查本批次数据，表非空不代表导入完整喵！

---

<a id="review"></a>

## 🧠 知识点总结（复习速查）

> 这张表按**现有源码**记录，便于对照；改进建议见第九章，不表示脚本已经完成重构。

| # | 知识点 | 源码引用 | 要点速记 |
|---|--------|----------|----------|
| 1 | pymysql 连接数据库 | `pymysql入门.py` | `Connect(host=, user=, passwd=, port=, autocommit=True)` 建连，`get_server_info()` 测试是否连通 |
| 2 | 游标执行 SQL 全流程 | `pymysql入门.py` | `cursor()` 拿游标 → `select_db()` 选库 → `execute()` 执行 → `fetchall()` 取回结果 → `close()` 断开 |
| 3 | 数据封装类 | `data_define.py` | `Record` 类用 `__init__` 封装日期/ID/金额/省份，`__str__` 魔术方法方便打印测试 |
| 4 | 面向对象文件读取 | `File_define.py` | `Filereader` 父类定义 `read_data()` 接口，子类 `textreader` / `filereader` 各自实现 |
| 5 | 读取 txt 文本数据 | `File_define.py` | `textreader` 用 count 跳过表头行，`strip()` + `split(',')` 拆列，金额转 `float` |
| 6 | 读取 JSON 数据 | `File_define.py` | `filereader` 用 `json.loads` 解析，按中文键 `日期/订单id/销售额/销售省份` 取值 |
| 7 | 数据合并 + 循环上传 | `综合案例.py` | 当前逐条拼接 INSERT；推荐改参数化 executemany + 事务 |
| 8 | 上传结果验证 | `综合案例.py` | 当前 sleep 后判断表非空，不能证明本批次完整；SQL 执行无需额外 sleep |
| 9 | 数据库读出转 JSON | `读取数据库.py` | 当前 fetchall 后逐行追加 JSON Lines；重复运行会追加重复数据 |
| 10 | 自动提交 autocommit | `pymysql入门.py` | 连接参数 `autocommit=True` 后写操作自动生效，不用手动 `commit()` |

---

## ⚠️ 注意事项（易踩的坑）

1. 🔐 **密码从环境变量读取**：三份数据库脚本用 `os.getenv("MYSQL_PASSWD")` 取密码。运行前设置 `$env:MYSQL_PASSWD='你的密码'`；不要把真实密码写进 README、日志、截图或提交记录喵！
2. ⚠️ **f-string 拼 SQL 有注入和转义风险**：现有导入脚本直接拼接值，含单引号的省份文本、带前导零或非数字的订单号都可能出错。学习练习也应采用 `%s` 参数化绑定，不靠手动加引号修补喵！
3. ⚠️ **读 txt 要跳表头**：`File_define.py` 里用 `count` 变量跳过第一行，忘了跳会把 `日期,订单id,...` 表头当数据插进库里喵！
4. ⚠️ **路径反斜杠转义**：`File_define.py`、`综合案例.py` 都用 `r"..."` 原始字符串写 Windows 路径，不用 `r` 前缀的话 `\t`、`\n` 会被当成转义符喵！
5. ⚠️ **文件编码与 JSON 类型约定**：读写文件显式带 `encoding='utf-8'`；`ensure_ascii=False` 影响可读性，不改变 JSON 的含义；日期、Decimal 需按约定显式转换，`default=str` 是一种简便策略喵！
6. ⚠️ **用完记得关连接**：操作完要 `conn.close()`，数据库连接不关会一直占着资源喵！

---

## 📝 自测练习与核对要点

1. 设计商品表，包含商品 ID、条码、价格、库存、上架开关、创建时间。说明条码为什么不用 INT、价格为什么用 DECIMAL，以及如何限制库存非负和开关为 0/1。
2. 在 `school` 中查找未录入成绩的学生，分别比较 `COUNT(*)`、`COUNT(score)` 和 `AVG(score)` 的含义。
3. 查询每个班级的学生数，包含空班级。核对 LEFT JOIN 的筛选位置与 COUNT(s.id)。
4. 查询每个班级前两档分数，允许并列。核对 DENSE_RANK 与 ROW_NUMBER 的差异，以及窗口结果为什么需要外层筛选。
5. 在 `shop` 中计算每月已支付销售额；原始数据应得到一月 200.00、二月 200.00，待支付的 500.00 不计入。
6. 在 account 事务中修改余额再回滚，检查值是否恢复；再演示提交后 ROLLBACK 无法撤销已提交修改。
7. 对 `shop.orders` 创建联合索引，比较带状态和时间范围、只有时间范围的 EXPLAIN。样本很小时优化器不选索引也可能合理。
8. 让销售文件中两行拥有相同订单 ID，思考逐条自动提交和整批事务各会留下什么数据；不要在真实库做破坏性实验。

## 📚 官方参考资料

本文是学习用整理；范围、默认行为和版本差异应结合实际服务器配置核对。

- [MySQL 8.0 数据类型总览](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)：按数值、日期时间、字符串、空间、JSON 继续查阅。
- [聚合函数](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)、[NULL 的处理](https://dev.mysql.com/doc/refman/8.0/en/working-with-null.html)：核对统计与三值逻辑。
- [外键约束](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html)、[CHECK](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html)：核对关联与业务范围约束。
- [事务控制](https://dev.mysql.com/doc/refman/8.0/en/commit.html)、[隔离级别](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html)：区分快照、锁与提交边界。
- [账号名称](https://dev.mysql.com/doc/refman/8.0/en/account-names.html)、[权限生效机制](https://dev.mysql.com/doc/refman/8.0/en/privilege-changes.html)：理解账号 Host 和授权。
- [PyMySQL 官方文档](https://pymysql.readthedocs.io/en/latest/)：连接、游标、参数绑定与事务接口。

*先理解数据含义，再选择类型、约束、查询和事务；把例子跑通，也要能解释结果为什么正确喵！🐾*

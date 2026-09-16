"""
演示pymysql的基础操作
"""
import os

from pymysql import Connect

# 密码从环境变量读取，避免明文写入代码（PowerShell 设置：$env:MYSQL_PASSWD='你的密码'）
MYSQL_PASSWD = os.getenv("MYSQL_PASSWD")
if not MYSQL_PASSWD:
    raise SystemExit("未设置环境变量 MYSQL_PASSWD，请先设置后再运行：$env:MYSQL_PASSWD='你的密码'")

conn = Connect(
    host="localhost",  # 主机名
    user="root",  # 用户名
    passwd=MYSQL_PASSWD,  # 密码（来自环境变量）
    port=3306,  # 端口
    autocommit=True,  # 自动提交
)
# 测试能否连接到MySQL
print(conn.get_server_info())
"""进行SQL查询"""
# 获得游标对象
cursor = conn.cursor()
# 获取(选择)数据库
conn.select_db("school_student")
# execute执行SQL
cursor.execute("select * from infernation_student")
# fetchall获取游标对象结果
result = cursor.fetchall()
for r in result:
    print(r)
print("————————————————————————————————————————————————")
"""进行SQL插入"""
cursor = conn.cursor()
conn.select_db("school_student")
cursor.execute("insert into infernation_student values(007,'Yuki有希',16)")
cursor.execute("select * from infernation_student")
# 确认更改
result = cursor.fetchall()
for r in result:
    print(r)
# 断开此次链接
conn.close()

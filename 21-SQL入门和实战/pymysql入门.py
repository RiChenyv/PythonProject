"""
演示pymysql的基础操作
"""
from pymysql import Connect

conn = Connect(
    host="localhost",  # 主机名
    user="root",  # 用户名
    passwd="REDACTED_PASSWORD",  # 密码
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

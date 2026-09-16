import json
import os

from pymysql import connect

# 密码从环境变量读取，避免明文写入代码（PowerShell 设置：$env:MYSQL_PASSWD='你的密码'）
MYSQL_PASSWD = os.getenv("MYSQL_PASSWD")
if not MYSQL_PASSWD:
    raise SystemExit("未设置环境变量 MYSQL_PASSWD，请先设置后再运行：$env:MYSQL_PASSWD='你的密码'")

conn = connect(
    port=3306,
    user='root',
    password=MYSQL_PASSWD,
    host='localhost',
    autocommit=True,
)

cursor = conn.cursor()

conn.select_db("py_sql")

cursor.execute("select * from orders")

result = cursor.fetchall()
with open(r"D:\PythonProject\21-SQL入门和实战\综合案例\json数据.txt", 'a', encoding='utf-8') as f:
    for r in result:
        json_data = json.dumps({"date": r[0], "order_id": r[1], "money": r[2], "province": r[3]}, ensure_ascii=False,
                               default=str)
        f.write(json_data + "\n")
        print(r)

conn.close()

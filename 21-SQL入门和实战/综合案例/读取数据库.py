import json

from pymysql import connect

conn = connect(
    port=3306,
    user='root',
    password='REDACTED_PASSWORD',
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

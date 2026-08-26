import time

from pymysql import connect

from File_define import *
from data_define import *

text = textreader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
file = filereader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")

data_01 = text.read_data()
data_02 = file.read_data()

all_data: list[Record] = data_01 + data_02

conn = connect(
    host="localhost",
    user="root",
    passwd="********",
    autocommit=True,
    port=3306,
)
cursor = conn.cursor()

conn.select_db("py_sql")

for record in all_data:
    SQL = f"insert into orders(order_data,order_id,money,province) " \
          f"values('{record.date}', {record.ID}, {record.money}, '{record.province}')"
    cursor.execute(SQL)
print("正在进行数据库上传...")
time.sleep(2)
cursor.execute("select * from orders")
result = cursor.fetchall()
if result != ():
    print("已完成数据库上传")
conn.close()

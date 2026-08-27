from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("test_PySpark")

sc = SparkContext(conf=conf)
# 写入内容
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
rdd1 = sc.parallelize({"key": 1, "key2": 2, "key3": 3, "key4": 4})
rdd2 = sc.parallelize("hello world")
# 输出
print(rdd.collect())
print(rdd1.collect())
print(rdd2.collect())
# 读取文件
redd4 = sc.textFile(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
# 输出，发现文本文件按行输出
print(redd4.collect())

sc.stop()

from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("test_PySpark")

sc = SparkContext(conf=conf)
# 写入内容
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])
rdd1 = sc.parallelize({"key": 1, "key2": 2, "key3": 3, "key4": 4})
# 输出
print(rdd.collect())
print(type(rdd.collect()))
print(rdd1.collect())
print(type(rdd1.collect()))

sc.stop()

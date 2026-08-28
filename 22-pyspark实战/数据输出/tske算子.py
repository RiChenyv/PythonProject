from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster("local[*]").setAppName("test_PySpark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8])

take_list = rdd.take(5)

print(take_list)

sc.stop()

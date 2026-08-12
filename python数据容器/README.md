# 数据容器的通用操作：

## 1.循环遍历操作：

尽管数据容器各有特点，但在遍历上，五类数据容器都支持使用for循环进行遍历,但是list/tuple/str支持  
while循环遍历，而set/dict不支持（无法进行下标索引操作）

## 2.统计功能：

len(容器)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;统计容器的元素个数  
max(容器)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;统计容器的最大元素  
min(容器)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同上，自行理解

![totally](images/微信图片_20260812174848_388_1.jpg)

## 3.容器的通用转换：

如图所示：

![change](images/微信图片_20260812175243_390_1.jpg)

特殊情况：  
字符串与字典转列表或元组或集合时，字符串被按单字符分开，字典仅保留key，丢弃value  
存在dict()函数，但无法将其他数据容器转换为字典

## 4.容器的通用排序功能：

sorted(容器,[reverse = Ture])&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从大到小进行排序  
sorted(容器,[reverse = False])&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从小到大进行排序  
注意：排序的结果会统统变成列表对象，reverse默认为False，即默认排序为正向排序（小到大）

# 总结：

![总结](images/totally.jpg)
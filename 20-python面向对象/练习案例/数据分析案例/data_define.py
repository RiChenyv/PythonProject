# 设计一个完成数据封装的类
class Record:
    # 构造方法
    def __init__(self, date, ID, money, province):
        self.date = date
        self.ID = ID
        self.money = money
        self.province = province

    # 实现对类输出的魔术方法
    def __str__(self):
        return f"{self.date},{self.ID},{self.money},{self.province}"

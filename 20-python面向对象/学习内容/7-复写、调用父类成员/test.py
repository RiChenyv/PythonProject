class Phone:
    IMEI = "菠萝手机"
    producer = "HUAWEI"

    def show_by_5g(self):
        print(f"IMEI: {self.IMEI}, producer: {self.producer}")


class MyPhone(Phone):
    # 复写
    IMEI = "水果手机"
    producer = "APPLE"

    # 复写
    def show_by_5g(self):
        # 子类调用父类方法的两种形式
        Phone.show_by_5g(self)
        super().show_by_5g()
        print("老板给我来碗忘情牛肉面喵~~~")
        print(f"父类的厂商是{Phone.producer},{super().producer}加油！！！！")
        print("不放眼泪不放盐，放忘情汤喵~~~")


phone = Phone()
phone.show_by_5g()
myPhone = MyPhone()
myPhone.show_by_5g()

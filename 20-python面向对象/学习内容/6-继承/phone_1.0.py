class Phone_1:
    IMEI = None
    prducer = None

    def __init__(self, IMEI, prducer):
        self.IMEI = IMEI
        self.prducer = prducer

    def call_by_4g(self):
        print("4g通话")


class NFC:
    NFC_type = "第五代"

    def __init__(self, NFC_type):
        self.NFC_type = NFC_type

    def read(self):
        print("读卡")


class Phone_2(Phone_1, NFC):
    face_id = "1001"

    def __init__(self, IMEI, prducer, NFC_type, face_id):
        Phone_1.__init__(self, IMEI, prducer)
        self.NFC_type = NFC_type
        self.face_id = face_id

    def call_by_5g(self):
        print("5g通话")

    def face_know(self):
        if self.face_id == "1001":
            print("面部解锁成功")


phone = Phone_2("mac", "huawei", "5.0", "1001")
phone.call_by_4g()
phone.read()
phone.call_by_5g()
phone.face_know()

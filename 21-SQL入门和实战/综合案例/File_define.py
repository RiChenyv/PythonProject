import json

from data_define import *


class Filereader:
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        pass


class textreader(Filereader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        count = 0
        record_list = []
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if count == 0:
                    count += 1
                    continue
                else:
                    line = line.strip()
                    data_list = line.split(',')
                    record = Record(data_list[0], data_list[1], float(data_list[2]), data_list[3])
                    record_list.append(record)
            return record_list


class filereader(Filereader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list = []
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            for line in data:
                record = Record(line["日期"], line["订单id"], line["销售额"], line["销售省份"])
                record_list.append(record)

        return record_list


"""————————————————————————测试——————————————————————————"""
if __name__ == '__main__':
    text_filereader = textreader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
    json_reader = filereader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")
    text_list: list[Record] = text_filereader.read_data()
    test_list = json_reader.read_data()
    for record in test_list:
        print(record)

    for record in text_list:
        print(record)

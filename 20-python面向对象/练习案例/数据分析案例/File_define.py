import json

from data_define import Record


# 设计一个抽象类，来做顶层设计，实现文件的读取相关功能
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，使每一条数据都转化为Record，再将它们封装到list"""
        pass


"""读取1月份txt文本的类"""


class TextReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list = []
        count: int = 0
        with open(self.path, 'r', encoding="utf-8") as f:
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


"""读取二月份JSON文本的类"""


class JsonReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list = []
        with open(self.path, 'r', encoding="utf-8") as f:
            data = json.loads(f.read())
            for line in data:
                data_dict = line
                record = Record(data_dict["日期"], data_dict["订单id"], float(data_dict["销售额"]),
                                data_dict["销售省份"])
                record_list.append(record)
        return record_list


if __name__ == '__main__':
    text_filereader = TextReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
    json_reader = JsonReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")
    text_list: list[Record] = text_filereader.read_data()
    test_list = json_reader.read_data()
    for record in test_list:
        print(record)

    for record in text_list:
        print(record)

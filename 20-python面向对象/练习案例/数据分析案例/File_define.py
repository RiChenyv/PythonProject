import json

from data_define import Record


# 设计一个抽象类，来做顶层设计，实现文件的读取相关功能
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，使每一条数据都转化为Record，再将它们封装到list"""
        pass


"""读取1月份txt文本的类"""


class TextReader(FileReader):
    # 构造方法方便数据文件路径写入
    def __init__(self, path):
        self.path = path

    # 复写接口的抽象方法
    def read_data(self) -> list[Record]:
        # 创建对象列表
        record_list = []
        # 设计计数器，去除原始数据的表头（第一行）
        count: int = 0
        with open(self.path, 'r', encoding="utf-8") as f:
            # 按行读取文件，将每行拆成一个列表，依次填入record对象
            for line in f.readlines():
                if count == 0:
                    count += 1
                    continue
                else:
                    # 数据处理
                    line = line.strip()
                    data_list = line.split(',')
                    # 创建对象（保证money是浮点数变量）
                    record = Record(data_list[0], data_list[1], float(data_list[2]), data_list[3])
                    # 并入对象列表
                    record_list.append(record)
        return record_list


"""读取二月份JSON文本的工具类"""


class JsonReader(FileReader):
    # 构造方法
    def __init__(self, path):
        self.path = path

    # 复写接口方法
    def read_data(self) -> list[Record]:
        # 制定return列表
        record_list = []
        with open(self.path, 'r', encoding="utf-8") as f:
            # 由于原始数据是个列表套字典的形式，直接全部读取转化为python数据，此时data为列表
            data = json.loads(f.read())
            # 按元素个数对data循环遍历
            for line in data:
                # 取出每个元素（字典）
                data_dict = line
                record = Record(data_dict["日期"], data_dict["订单id"], float(data_dict["销售额"]),
                                data_dict["销售省份"])
                record_list.append(record)
        return record_list


"""————————————————————————测试——————————————————————————"""
if __name__ == '__main__':
    text_filereader = TextReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年1月销售数据.txt")
    json_reader = JsonReader(r"D:\PythonProject\14-json原始数据\原始数据\2026年2月销售数据.txt")
    text_list: list[Record] = text_filereader.read_data()
    test_list = json_reader.read_data()
    for record in test_list:
        print(record)

    for record in text_list:
        print(record)

#
# 和文件相关的类定义
#
from data_define import Record
import json

class FileReader:

    # 读取文件的数据，读到的每一条数据都转换为 Record 对象，将它们封装在 list 中
    def read_data(self) -> list[Record]:
        pass


# 读取 txt 文件
class TextFileReader(FileReader):
    
    def __init__(self, path):
        self.path = path                        # 记录文件位置

    def read_data(self) -> list[Record]:
        record_list:list[Record] = []
        f = open(self.path, 'r', encoding = 'utf-8')
        for line in f.readlines():
            line = line.strip()                 # 删除所有回车
            data_lst = line.split(',')
            record = Record(data_lst[0], data_lst[1], int(data_lst[2]), data_lst[3])
            record_list.append(record)
        #record_list[1:]
        
        f.close
        return record_list


# 读取 Json 文件
class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list:list[Record] = []
        f = open(self.path, 'r', encoding = 'utf-8')
        for item in f.readlines():
            data_dic = json.loads(item)
            record = Record(data_dic['date'], data_dic['order_id'], int(data_dic['money']), data_dic['province'])
            record_list.append(record)
        
        f.close
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader('C:/Users/YiMon/Source/Repos/MyPythonLearning/MyPythonLearning2/package2/2011年1月销售数据.txt')
    json_file_reader = JsonFileReader('C:/Users/YiMon/Source/Repos/MyPythonLearning/MyPythonLearning2/package2/2011年2月销售数据JSON.txt')
    lst1 = text_file_reader.read_data()
    lst2 = json_file_reader.read_data()

    # 使用了 class Record 中的 __str__ 方法，以正确显示内容
    for i in lst1:
        print(i)
    print('<-------------------------------------->')
    for i in lst2:
        print(i)
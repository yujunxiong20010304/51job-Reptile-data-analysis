# sql转csv
import pymysql
from pprint import pprint
import pandas


class Test_myqsl(object):
    # 运行数据库和建立游标对象
    def __init__(self):
        self.list_city = {'北京': '010000', '上海': '020000', '广东': '030000', '深圳': '040000', '成都': '090200'}
        self.list_work = ['Web前端开发', 'Java开发工程师', 'Android开发工程师', '软件测试工程师', 'ios开发工程师', '数据分析师']
        self.file_list = []
        self.connect = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="yjx20010304",
                                       database="51job",
                                       charset="utf8", cursorclass=pymysql.cursors.DictCursor)
        # 返回一个cursor对象,也就是游标对象
        self.cursor = self.connect.cursor()

    # 关闭数据库和游标对象
    def __del__(self):  # 魔术方法在对象实例执行完后执行
        self.connect.close()
        self.cursor.close()

    def write(self):
        city_value = list(self.list_city.keys())
        for city in city_value:
            for work in self.list_work:
                city_work = city + work
                self.file_list.append(city_work)
        for mysql in self.file_list:
            # 将数据转化成DataFrame数据格式
            data = pandas.DataFrame(self.read(mysql))
            # 把id设置成行索引
            data_1 = data.set_index("company_name", drop=True)
            file_name = mysql+'.csv'
            # 写入数据
            pandas.DataFrame.to_csv(data_1, file_name, encoding="utf_8_sig")
            print(mysql+"写入成功")

    def read(self, mysql):
        sql = "select * from {}".format(mysql)
        # 读取数据库的所有数据
        data = self.cursor.execute(sql)
        field_2 = self.cursor.fetchall()
        return field_2


# 封装
def main():
    write = Test_myqsl()
    write.write()


if __name__ == '__main__':
    main()

import pymysql
class LevelThree:
    def __init__(self):
        self.list_city = {'北京': '010000', '上海': '020000', '广东': '030000', '深圳': '040000', '成都': '090200'}
        self.list_work = ['Web前端开发','Java开发工程师','Android开发工程师','软件测试工程师','ios开发工程师','数据分析师']
        # url所需参数
        self.threeLevelWebsite = []  # 三级网址列表
        self.url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2'
        self.table = "CREATE TABLE {} (company_name varchar(255)," \
                     "max_wages int," \
                     "min_wages int," \
                     "place varchar(255)," \
                     "place2 varchar(255)," \
                     "education varchar(255)," \
                     "treatment varchar(255)," \
                     "requirement text) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"

    def three_level_analysis(self):
        city_value = list(self.list_city.values())   # 获取参数的value值
        for city in city_value:
            for work in self.list_work:
                url = self.url.format(city,work)
                self.threeLevelWebsite.append(url)
        return self.threeLevelWebsite



    def test_example(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                               user='root', password='yjx20010304', db='51job')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8mb4;')
        try:
            city_value = list(self.list_city.keys())
            for city in city_value:
                for work in self.list_work:
                    city_work = city+work
                    h = cur.execute(self.table.format(city_work))
        except pymysql.err.InternalError as e:
            print('数据库已建立')
        cur.close()
        conn.close()








if __name__ == '__main__':
    implement = LevelThree()
    '''a = implement.three_level_analysis()
    print(a)'''
    implement.test_example()

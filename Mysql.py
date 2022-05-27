import pymysql
import asyncio


class Mysql:

    def __init__(self, kind_result, company_name, max_wages, min_wages, place2,
                 place, education, treatment, requirement):
        self.kind_result = kind_result
        self.company_name = pymysql.escape_string(company_name)
        self.max_wages = max_wages
        self.min_wages = min_wages
        self.place2 = pymysql.escape_string(place2)
        self.place = pymysql.escape_string(place)
        self.education = pymysql.escape_string(education)
        self.treatment = pymysql.escape_string(treatment)
        self.requirement = pymysql.escape_string(requirement)

    async def test_example(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                               user='root', password='yjx20010304', db='51job')
        cur = conn.cursor()
        sql = "insert into {} values('{}',{},{},'{}','{}','{}','{}','{}') ".format(self.kind_result, self.company_name,
                                                                                   self.max_wages, self.min_wages,
                                                                                   self.place, self.place2,
                                                                                   self.education, self.treatment,
                                                                                   self.requirement)
        cur.execute(sql)
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 关闭数据库


if __name__ == '__main__':
    tt = Mysql(1, 2, 3, 4, 5, 6, 7, 8, 9)
    tt.test_example()

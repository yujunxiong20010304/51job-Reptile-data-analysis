import asyncio
import aiohttp
import re
import Mysql
import Level2
from lxml import etree
import jieba


class LevelOne:
    def __init__(self, url, kind_result):
        self.url = url  # 一级网址
        self.kind_result = kind_result  # 爬取分类
        self.headers = Level2.LevelTwo().headers  # 请求头信息
        self.max_wages = None  # 最大工资
        self.min_wages = None  # 最少工资
        self.place = None  # 上班地点
        self.place2 = None  # 工作位置
        self.education = None  # 学历
        self.company_name = None  # 公司名称
        self.treatment = None  # 公司待遇
        self.requirement = None  # 职位信息

    async def analysis_level_one(self):
        sem = asyncio.Semaphore(200)
        with(await sem):
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with await session.get(self.url, timeout=650) as response:
                    response = await response.text(encoding='GBK', errors='ignore')  # 解析获取到的url
                    judge = etree.HTML(response)  # 判断网址是否为常规网址
                    self.company_name = judge.xpath('//div[@class="cn"]/h1/text()')  # 判断网址内容是否存在
                    if self.company_name:

                        # 公司名称
                        self.company_name = self.company_name[0]

                        # 工资
                        wages_tree = etree.HTML(response)  # 可能有可能没有 天，年，月
                        wages = wages_tree.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()')
                        try:
                            if wages:
                                wages = wages[0]
                                wages_list = jieba.lcut_for_search(wages)  # 把wages拆分为列表
                                if '天' in wages_list:
                                    self.max_wages = int(wages_list[0]) * 30
                                    self.min_wages = "NULL"
                                elif '月' in wages_list:
                                    if '万' in wages_list:
                                        self.min_wages = int(float(wages_list[0]) * 10000)
                                        self.max_wages = int(float(wages_list[2]) * 10000)
                                    if '千' in wages_list:
                                        self.min_wages = int(float(wages_list[0]) * 1000)
                                        self.max_wages = int(float(wages_list[2]) * 1000)
                                elif '年' in wages_list:
                                    self.max_wages = int(float(wages_list[0]) * 10000 / 12)
                                    self.min_wages = int(float(wages_list[2]) * 10000 / 12)
                                else:
                                    self.min_wages = "NULL"
                                    self.max_wages = "NULL"
                            else:
                                self.min_wages = "NULL"
                                self.max_wages = "NULL"
                        except ValueError as e:
                            self.min_wages = "NULL"
                            self.max_wages = "NULL"
                            print('工资特殊情况')

                        # 工作位置
                        place2 = re.compile(r'<p class="msg ltype" title="(.*?)&nbsp;', re.S)
                        place2_list = place2.findall(response)
                        if place2_list:
                            self.place2 = place2_list[0]
                        else:
                            self.place2 = '无'

                        # 上班地点
                        place_tree = etree.HTML(response)  # 详细的可能有可能没有
                        place_list = place_tree.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')
                        if place_list:
                            self.place = place_list[0]
                        else:
                            self.place = '无'

                        # 学历
                        eduction = re.compile(r'</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;<span>', re.S)
                        education_list = eduction.findall(response)
                        if len(education_list) > 2:
                            self.education = education_list[1]
                        else:
                            self.education = '无'

                        # 公司待遇
                        treatment = re.compile(r'<span class="sp4">(.*?)</span>', re.S)
                        treatment_judge = treatment.findall(response)
                        if treatment_judge:
                            self.treatment = ','.join(treatment_judge)
                        else:
                            self.treatment = '无'

                        # 职位信息
                        requirement_tree = etree.HTML(response)
                        requirement_rough = requirement_tree.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div//text()')
                        if requirement_rough:
                            requirement = []
                            for x in requirement_rough:
                                if x.strip():
                                    requirement.append(x.strip())
                            self.requirement = ''.join(requirement)
                        else:
                            self.requirement = '无'
                        print(self.kind_result, self.company_name, self.max_wages, self.min_wages, self.place2,
                              self.place, self.education, self.treatment, self.requirement, self.url)
                        # 数据导入数据库
                        t = Mysql.Mysql(self.kind_result, self.company_name, self.max_wages, self.min_wages, self.place2,
                                        self.place, self.education, self.treatment, self.requirement)
                        await t.test_example()

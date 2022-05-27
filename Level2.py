import asyncio
import aiohttp
import re
from Level3 import LevelThree
import Level1


class LevelTwo:
    def __init__(self):
        self.url = None
        self.headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                                                'AppleWebKit/537.36 (KHTML,like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    async def analysis(self, urls):
        sem = asyncio.Semaphore(200)  # 限制协程数为200
        with(await sem):
            i = 1  # 准备拼凑二级网址的页数
            while True:
                s = ',{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_' \
                    'field=0&dibiaoid=0&line=&welfare='.format(i)  # 拼凑二级网址最后的一部分
                url = urls + s  # 拼凑二级网址
                async with aiohttp.ClientSession(headers=self.headers) as session:
                    async with await session.get(url, timeout=650) as response:
                        reponse = await response.text(encoding='GBK', errors='ignore')  # 对网址进行解析
                        reguler = re.compile(r'"job_href":"(.*?)"', re.S)  # 正则表达式匹配一级网址
                        result = reguler.findall(reponse)
                        if result == []:  # 判断页数是否到达最后一页
                            break
                        else:
                            for ii in result:
                                start = urls.find('99,') + 3
                                end = urls.find(',2')
                                kind = urls[start:end]

                                start2 = urls.find('list/') + 5
                                end2 = urls.find(',000000')
                                kind2 = urls[start2:end2]
                                list_city = {'北京': '010000', '上海': '020000', '广东': '030000', '深圳': '040000',
                                             '成都': '090200'}
                                result = list(list_city.keys())[list(list_city.values()).index(kind2)]

                                kind_result = result+kind

                                class_a_url = ii.replace('\\', '', 10)
                                pp = Level1.LevelOne(class_a_url, kind_result)
                                await pp.analysis_level_one()  # 对爬取的url进行处理，并且把获取的url传递给level1
                            i += 1

    def main(self):
        implement = LevelThree()
        implement.test_example()
        self.url = implement.three_level_analysis()  # 获取level3中的url
        loop = asyncio.get_event_loop()  # 获取事件循环
        tasks = [self.analysis(urls) for urls in self.url]  # 把所有任务放到一个列表中 把url传递给上面的那个函数
        loop.run_until_complete(asyncio.wait(tasks))  # 激活协程


if __name__ == '__main__':
    pp = LevelTwo()
    pp.main()

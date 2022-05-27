# 画饼状图
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt


class analysis:
    def __init__(self):
        self.list_city = ['北京', '上海', '广东', '深圳', '成都']
        self.list_work = ['Web前端开发', 'Java开发工程师', 'Android开发工程师', '软件测试工程师', 'ios开发工程师', '数据分析师']
        self.file_address = []
        self.classification = [0, 3000, 6000, 9000, 12000, 15000, 500000]

    def merge(self):
        for i in self.list_city:
            for ii in self.list_work:
                file_name = '/Users/yujunxiong/Desktop/Python/Python end/存储/' + i + ii + '新' + '.csv'
                self.file_address.append(file_name)

    def analyse(self):
        for i in self.file_address:
            # 最大值
            data1 = list(chain.from_iterable(pd.read_csv(i, usecols=[1]).values.tolist()))
            cats1 = pd.cut(data1, self.classification)
            paragraph1 = list(pd.value_counts(cats1))
            # 最小值
            data2 = list(chain.from_iterable(pd.read_csv(i, usecols=[2]).values.tolist()))
            cats2 = pd.cut(data2, self.classification)
            paragraph2 = list(pd.value_counts(cats2))

            start = i.find('存储/') + 3
            end = i.find('新.csv')
            kind = i[start:end]

            labels = ['(15000,+∞)', '(12000,15000]', '(9000,12000]', '(6000,9000]', '(3000,6000]', '(0,3000]']
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
            explode = (0.1, 0, 0.1, 0, 0.1, 0)

            # 121 > 1行2列第1个
            fig1 = plt.subplot(121)
            plt.pie(paragraph1, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
            plt.title(kind+'最大工资')

            # 122 > 1行2列第2个
            fig2 = plt.subplot(122)
            plt.pie(paragraph2, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
            plt.title(kind+'最小工资')
            plt.show()


if __name__ == '__main__':
    tt = analysis()
    tt.merge()
    tt.analyse()

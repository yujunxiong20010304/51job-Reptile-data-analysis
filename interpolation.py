# 拉格朗日插值法
import pandas as pd
from scipy.interpolate import lagrange
import warnings

warnings.filterwarnings("ignore")  # 设置忽略警告信息


class handle:
    def __init__(self):
        self.list_city = ['北京', '上海', '广东', '深圳', '成都']
        self.list_work = ['Web前端开发', 'Java开发工程师', 'Android开发工程师', '软件测试工程师', 'ios开发工程师', '数据分析师']

    def file_name(self):
        for i in self.list_city:
            for ii in self.list_work:
                filename = i + ii + '.csv'
                new_filename = '/Users/yujunxiong/Desktop/Python/Python end/存储/' + i + ii + '新' + '.csv'
                self.giao(filename, new_filename)

    def giao(self, filename, new_filename):
        input_file = filename  # 文件进入路径
        output_file = new_filename  # 输出数据路径
        data = pd.read_csv(input_file, encoding='utf-8')  # 读入数据
        data = data.fillna(0)
        # 最大工资
        max_Q3 = data.describe().iat[6, 0]  # 上四分位
        max_Q1 = data.describe().iat[4, 0]  # 下四分位
        max_IQR = max_Q3 - max_Q1
        max_upper_edge = max_Q3 + 1.5 * max_IQR  # 求上边缘
        max_lower_edge = max_Q1 - 1.5 * max_IQR  # 求下边缘
        # 最小工资
        min_Q3 = data.describe().iat[6, 1]
        min_Q1 = data.describe().iat[4, 1]
        min_IQR = min_Q3 - min_Q1
        min_upper_edge = min_Q3 + 1.5 * min_IQR  # 求上边缘
        min_lower_edge = min_Q1 - 1.5 * min_IQR  # 求下边缘
        data[u'max_wages'][
            (data[u'max_wages'] > max_upper_edge) | (data[u'max_wages'] < max_lower_edge) | (
                    data[u'max_wages'] == 0)] = None  # 过滤异常值，将其变为空值
        data[u'min_wages'][
            (data[u'min_wages'] > min_upper_edge) | (data[u'min_wages'] < min_lower_edge) | (
                    data[u'min_wages'] == 0)] = None  # 过滤异常值，将其变为空值
        self.main(data, output_file)

    # s为列向量，n为被插值位置，k为取前后的数据个数
    def ployinter(self, s, n, k=1):
        y = s.reindex(list(range(n - k, n)) + list(range(n + 1, n + 1 + k)))  # 取数
        y = y[y.notnull()]
        return abs(lagrange(y.index, list(y))(n))

    def main(self, data, output_file):
        # 逐个元素判断是否需要插值
        for i in data.columns:
            for j in range(len(data)):
                # 如果遇到salary的值为空，就进行插值
                if (data[i].isnull())[j]:
                    data[i][j] = self.ployinter(data[i], j)
        data.to_csv(output_file,index=False)


if __name__ == '__main__':
    tt = handle()
    tt.file_name()

# 合并csv文件
import pandas as pd
from scipy.interpolate import lagrange
import warnings

warnings.filterwarnings("ignore")  # 设置忽略警告信息


class handle:
    def __init__(self):
        self.list_city = ['北京', '上海', '广东', '深圳', '成都']
        self.list_work = ['Web前端开发', 'Java开发工程师', 'Android开发工程师', '软件测试工程师', 'ios开发工程师', '数据分析师']

    def file_name(self):
        for i in range(len(self.list_work)):
            for ii in range(len(self.list_city)):
                filename = '/Users/yujunxiong/Desktop/Python/Python end/存储/' + self.list_city[ii] + self.list_work[i] + '新' + '.csv'
                self.giao(filename,ii)

    def giao(self, filename,ii):
        input_file = filename  # 文件进入路径
        if ii != 0:
            data = pd.read_csv(input_file, encoding='utf-8',header=1)
        else:
            data = pd.read_csv(input_file, encoding='utf-8')  # 读入数据
        start = filename.find('存储/') + 5
        kind = filename[start:len(filename)]
        output_file = '/Users/yujunxiong/Desktop/Python/Python end/存储1/' + kind
        self.main(data, output_file)

    def main(self, data, output_file):
        data.to_csv(output_file, index=False,mode='a')


if __name__ == '__main__':
    tt = handle()
    tt.file_name()

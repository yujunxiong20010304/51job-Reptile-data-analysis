# 画箱型图
import numpy as np
from itertools import chain
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # 设置忽略警告信息
from pylab import *

rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# ***********************上海**************************

# 上海Android开发工程师工资最大值
data1 = list(chain.from_iterable(pd.read_csv('上海Android开发工程师.csv', usecols=[1]).values.tolist()))
# 上海Android开发工程师工资最小值
data2 = list(chain.from_iterable(pd.read_csv('上海Android开发工程师.csv', usecols=[2]).values.tolist()))

data = {"上海Android开发工程师工资最大值": data1, "上海Android开发工程师工资最小值": data2}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata() # 异常值标签
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 上海ios开发工程师最大工资
data3 = list(chain.from_iterable(pd.read_csv('上海ios开发工程师.csv', usecols=[1]).values.tolist()))
# 上海ios开发工程师最小工资
data4 = list(chain.from_iterable(pd.read_csv('上海ios开发工程师.csv', usecols=[2]).values.tolist()))

data = {"上海ios开发工程师工资最大值": data3, "上海ios开发工程师工资最小值": data4}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 上海java开发工程师最大工资
data5 = list(chain.from_iterable(pd.read_csv('上海Java开发工程师.csv', usecols=[1]).values.tolist()))
# 上海java开发工程师最小工资
data6 = list(chain.from_iterable(pd.read_csv('上海Java开发工程师.csv', usecols=[2]).values.tolist()))

data = {"上海Java开发工程师工资最大值": data5, "上海Java开发工程师工资最小值": data6}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 上海Web前端开发最大工资
data7 = list(chain.from_iterable(pd.read_csv('上海Web前端开发.csv', usecols=[1]).values.tolist()))
# 上海Web前端开发最小工资
data8 = list(chain.from_iterable(pd.read_csv('上海Web前端开发.csv', usecols=[2]).values.tolist()))

data = {"上海Web前端开发工资最大值": data7, "上海Web前端开发工资最小值": data8}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 上海数据分析师最大工资
data9 = list(chain.from_iterable(pd.read_csv('上海数据分析师.csv', usecols=[1]).values.tolist()))
# 上海数据分析师最小工资
data10 = list(chain.from_iterable(pd.read_csv('上海数据分析师.csv', usecols=[2]).values.tolist()))

data = {"上海数据分析师工资最大值": data9, "上海数据分析师工资最小值": data10}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 上海软件测试工程师最大工资
data11 = list(chain.from_iterable(pd.read_csv('上海软件测试工程师.csv', usecols=[1]).values.tolist()))
# 上海软件测试工程师最小工资
data12 = list(chain.from_iterable(pd.read_csv('上海软件测试工程师.csv', usecols=[2]).values.tolist()))

data = {"上海软件测试工资最大值": data11, "上海软件测试工资最小值": data12}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# *********************北京**************************
# 北京Android开发工程师工资最大值
data13 = list(chain.from_iterable(pd.read_csv('北京Android开发工程师.csv', usecols=[1]).values.tolist()))
# 北京Android开发工程师工资最小值
data14 = list(chain.from_iterable(pd.read_csv('北京Android开发工程师.csv', usecols=[2]).values.tolist()))

data = {"北京Android开发工程师工资最大值": data13, "北京Android开发工程师工资最小值": data14}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 北京ios开发工程师最大工资
data15 = list(chain.from_iterable(pd.read_csv('北京ios开发工程师.csv', usecols=[1]).values.tolist()))
# 北京ios开发工程师最小工资
data16 = list(chain.from_iterable(pd.read_csv('北京ios开发工程师.csv', usecols=[2]).values.tolist()))

data = {"北京ios开发工程师最大工资": data15, "北京ios开发工程师最小工资": data16}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 北京java开发工程师最大工资
data17 = list(chain.from_iterable(pd.read_csv('北京Java开发工程师.csv', usecols=[1]).values.tolist()))
# 北京java开发工程师最小工资
data18 = list(chain.from_iterable(pd.read_csv('北京Java开发工程师.csv', usecols=[2]).values.tolist()))

data = {"北京java开发工程师最大工资": data17, "北京java开发工程师最小工资": data18}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 北京Web前端开发最大工资
data19 = list(chain.from_iterable(pd.read_csv('北京Web前端开发.csv', usecols=[1]).values.tolist()))
# 北京Web前端开发最小工资
data20 = list(chain.from_iterable(pd.read_csv('北京Web前端开发.csv', usecols=[2]).values.tolist()))

data = {"北京Web前端开发最大工资": data19, "北京Web前端开发最小工资": data20}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 北京数据分析师最大工资
data21 = list(chain.from_iterable(pd.read_csv('北京数据分析师.csv', usecols=[1]).values.tolist()))
# 北京数据分析师最小工资
data22 = list(chain.from_iterable(pd.read_csv('北京数据分析师.csv', usecols=[2]).values.tolist()))

data = {"北京数据分析师最大工资": data21, "北京数据分析师最小工资": data22}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 北京软件测试工程师最大工资
data23 = list(chain.from_iterable(pd.read_csv('北京软件测试工程师.csv', usecols=[1]).values.tolist()))
# 北京软件测试工程师最大工资
data24 = list(chain.from_iterable(pd.read_csv('北京软件测试工程师.csv', usecols=[2]).values.tolist()))

data = {"北京软件测试工程师最大工资": data23, "北京软件测试工程师最小工资": data24}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# ******************广东************************

# 广东Android开发工程师工资最大值
data25 = list(chain.from_iterable(pd.read_csv('广东Android开发工程师.csv', usecols=[1]).values.tolist()))
# 广东Android开发工程师工资最小值
data26 = list(chain.from_iterable(pd.read_csv('广东Android开发工程师.csv', usecols=[2]).values.tolist()))

data = {"广东Android开发工程师工资最大值": data25, "广东Android开发工程师工资最小值": data26}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 广东ios开发工程师最大工资
data27 = list(chain.from_iterable(pd.read_csv('广东ios开发工程师.csv', usecols=[1]).values.tolist()))
# 广东ios开发工程师最小工资
data28 = list(chain.from_iterable(pd.read_csv('广东ios开发工程师.csv', usecols=[2]).values.tolist()))

data = {"广东ios开发工程师最大工资": data27, "广东ios开发工程师最小工资": data28}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 广东java开发工程师最大工资
data29 = list(chain.from_iterable(pd.read_csv('广东Java开发工程师.csv', usecols=[1]).values.tolist()))
# 广东java开发工程师最小工资
data30 = list(chain.from_iterable(pd.read_csv('广东Java开发工程师.csv', usecols=[2]).values.tolist()))

data = {"广东java开发工程师最大工资": data29, "广东java开发工程师最小工资": data30}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 广东Web前端开发最大工资
data31 = list(chain.from_iterable(pd.read_csv('广东Web前端开发.csv', usecols=[1]).values.tolist()))
# 广东Web前端开发最小工资
data32 = list(chain.from_iterable(pd.read_csv('广东Web前端开发.csv', usecols=[2]).values.tolist()))

data = {"广东Web前端开发最大工资": data31, "广东Web前端开发最小工资": data32}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 广东数据分析师最大工资
data33 = list(chain.from_iterable(pd.read_csv('广东数据分析师.csv', usecols=[1]).values.tolist()))
# 广东数据分析师最小工资
data34 = list(chain.from_iterable(pd.read_csv('广东数据分析师.csv', usecols=[2]).values.tolist()))

data = {"广东数据分析师最大工资": data33, "广东数据分析师最小工资": data34}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 广东软件测试工程师最大工资
data35 = list(chain.from_iterable(pd.read_csv('广东软件测试工程师.csv', usecols=[1]).values.tolist()))
# 广东软件测试工程师最小工资
data36 = list(chain.from_iterable(pd.read_csv('广东软件测试工程师.csv', usecols=[2]).values.tolist()))

data = {"广东软件测试工程师最大工资": data35, "广东软件测试工程师最小工资": data36}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# ***************成都****************

# 成都Android开发工程师工资最大值
data37 = list(chain.from_iterable(pd.read_csv('成都Android开发工程师.csv', usecols=[1]).values.tolist()))
# 成都Android开发工程师工资最小值
data38 = list(chain.from_iterable(pd.read_csv('成都Android开发工程师.csv', usecols=[2]).values.tolist()))

data = {"成都Android开发工程师工资最大值": data37, "成都Android开发工程师工资最小值": data38}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 成都ios开发工程师最大工资
data39 = list(chain.from_iterable(pd.read_csv('成都ios开发工程师.csv', usecols=[1]).values.tolist()))
# 成都ios开发工程师最小工资
data40 = list(chain.from_iterable(pd.read_csv('成都ios开发工程师.csv', usecols=[2]).values.tolist()))

data = {"成都ios开发工程师最大工资": data39, "成都ios开发工程师最小工资": data40}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 成都java开发工程师最大工资
data41 = list(chain.from_iterable(pd.read_csv('成都Java开发工程师.csv', usecols=[1]).values.tolist()))
# 成都java开发工程师最小工资
data42 = list(chain.from_iterable(pd.read_csv('成都Java开发工程师.csv', usecols=[2]).values.tolist()))

data = {"成都java开发工程师最大工资": data41, "成都java开发工程师最小工资": data42}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 成都Web前端开发最大工资
data43 = list(chain.from_iterable(pd.read_csv('成都Web前端开发.csv', usecols=[1]).values.tolist()))
# 成都Web前端开发最小工资
data44 = list(chain.from_iterable(pd.read_csv('成都Web前端开发.csv', usecols=[2]).values.tolist()))

data = {"成都Web前端开发最大工资": data43, "成都Web前端开发最小工资": data44}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 成都数据分析师最大工资
data45 = list(chain.from_iterable(pd.read_csv('成都数据分析师.csv', usecols=[1]).values.tolist()))
# 成都数据分析师最小工资
data46 = list(chain.from_iterable(pd.read_csv('成都数据分析师.csv', usecols=[2]).values.tolist()))

data = {"成都数据分析师最大工资": data45, "成都数据分析师最小工资": data46}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 成都软件测试工程师最大工资
data47 = list(chain.from_iterable(pd.read_csv('成都软件测试工程师.csv', usecols=[1]).values.tolist()))
# 成都软件测试工程师最小工资
data48 = list(chain.from_iterable(pd.read_csv('成都软件测试工程师.csv', usecols=[2]).values.tolist()))

data = {"成都软件测试工程师最大工资": data47, "成都软件测试工程师最小工资": data48}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# ***************深圳**********************

# 深圳Android开发工程师工资最大值
data49 = list(chain.from_iterable(pd.read_csv('深圳Android开发工程师.csv', usecols=[1]).values.tolist()))
# 深圳Android开发工程师工资最小值
data50 = list(chain.from_iterable(pd.read_csv('深圳Android开发工程师.csv', usecols=[2]).values.tolist()))

data = {"深圳Android开发工程师工资最大值": data49, "深圳Android开发工程师工资最小值": data50}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 深圳ios开发工程师最大工资
data51 = list(chain.from_iterable(pd.read_csv('深圳ios开发工程师.csv', usecols=[1]).values.tolist()))
# 深圳ios开发工程师最小工资
data52 = list(chain.from_iterable(pd.read_csv('深圳ios开发工程师.csv', usecols=[2]).values.tolist()))

data = {"深圳ios开发工程师最大工资": data51, "深圳ios开发工程师最小工资": data52}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 深圳java开发工程师最大工资
data53 = list(chain.from_iterable(pd.read_csv('深圳Java开发工程师.csv', usecols=[1]).values.tolist()))
# 深圳java开发工程师最小工资
data54 = list(chain.from_iterable(pd.read_csv('深圳Java开发工程师.csv', usecols=[2]).values.tolist()))

data = {"深圳java开发工程师最大工资": data53, "深圳java开发工程师最小工资": data54}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 深圳Web前端开发最大工资
data55 = list(chain.from_iterable(pd.read_csv('深圳Web前端开发.csv', usecols=[1]).values.tolist()))
# 深圳Web前端开发最小工资
data56 = list(chain.from_iterable(pd.read_csv('深圳Web前端开发.csv', usecols=[2]).values.tolist()))

data = {"深圳Web前端开发最大工资": data55, "深圳Web前端开发最小工资": data56}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 深圳数据分析师最大工资
data57 = list(chain.from_iterable(pd.read_csv('深圳数据分析师.csv', usecols=[1]).values.tolist()))
# 深圳数据分析师最小工资
data58 = list(chain.from_iterable(pd.read_csv('深圳数据分析师.csv', usecols=[2]).values.tolist()))

data = {"深圳数据分析师最大工资": data57, "深圳数据分析师最小工资": data58}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

# 深圳软件测试工程师最大工资
data59 = list(chain.from_iterable(pd.read_csv('深圳软件测试工程师.csv', usecols=[1]).values.tolist()))
# 深圳软件测试工程师最小工资
data60 = list(chain.from_iterable(pd.read_csv('深圳软件测试工程师.csv', usecols=[2]).values.tolist()))

data = {"深圳软件测试工程师最大工资": data59, "深圳软件测试工程师最小工资": data60}
df = pd.DataFrame(data)
h = df.plot.box(return_type='dict')
plt.xlabel("地址职位", fontsize=16)
plt.ylabel('工资', fontsize=16)
plt.grid(linestyle="--", alpha=0.8)
print(df.describe())  # 显示中位数、上下四分位数、标准偏差等内容

x = h['fliers'][0].get_xdata()
y = h['fliers'][0].get_ydata()
x1 = h['fliers'][1].get_xdata()
y1 = h['fliers'][1].get_ydata()
# y的值由大到小的顺序进行排序
y.sort()
y1.sort()
# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

for i in range(len(x1)):
    if i > 0:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.05 - 0.8 / (y1[i] - y1[i - 1]), y1[i]))
    else:
        plt.annotate(y1[i], xy=(x1[i], y1[i]), xytext=(x1[i] + 0.08, y1[i]))

plt.show()

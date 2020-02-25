import numpy as np
import pandas as pd
import collections
from matplotlib import pyplot as plt

'''
数据集来源
https://github.com/BlankerL/DXY-COVID-19-Data/

通过本福特定律(Benford's Law)来验证大规模数据的真实性
https://zh.wikipedia.org/wiki/%E6%9C%AC%E7%A6%8F%E7%89%B9%E5%AE%9A%E5%BE%8B

此次新冠状病毒"基本传染数" R>1，以指数方式传播,
https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%9C%AC%E4%BC%A0%E6%9F%93%E6%95%B0


本福特定律适用范围
1. 数据跨度必须足够大，横跨几个数量级
2. 数据无人为规则，如手机号码，身份证号不符合要求
3. 数据不能经过认为修饰
'''


def benford(n):
    '''
    本福特定律概率函数
    '''
    p_n = np.log10( (n+1) / n )
    return p_n

def collect_first(num):
    '''
    收集首个数字
    '''
    return int (str(num)[0] )

def p(datas):
    '''
    统计首个数字的频率，返回一个dict
    '''

    # 获取首个数字
    first_nums = map(collect_first,datas)
    # 频次统计
    freq = collections.Counter(first_nums)
    
    # 计算频率
    prob = {}
    for  i in range(1,10):
        if i in freq:
            prob[i] = freq[i] / len(datas)
        else:
            prob[i] = 0
    return prob

# 读取CSV文件
df = pd.read_csv('DXYArea.csv')
# 获取其中某个市的数据
city_data = df[ df['cityName'] == '武汉' ]
confirmed =  city_data['city_confirmedCount']

# 计算实际和预期概率
real_prob = p(confirmed)

total = len(confirmed)
print('[*]共计{}记录'.format(total))
print('[*]实际分布:{}'.format(real_prob))


# 绘制图像
x = np.arange(1,10,1)
y = list(map(lambda x : real_prob[x], x))
# 红色代表本福特定律预期分布
plt.plot(x, benford(x), 'r--')
# 绿色代表实际分布
plt.plot(x, y ,'go')
plt.show()
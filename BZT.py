import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import gaussian_kde

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
data=pd.read_csv('Total.csv')
#data=data["ZF_RATIO"]


# data=data[data['SUM_XFJE']<=6000]
# data=data[data['ZF_RATIO']<=0.2]
de1 = data['CY_XFJE'].sum()
print(de1)
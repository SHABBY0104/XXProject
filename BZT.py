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
CY_XFJE = float(data['CY_XFJE'].sum())
GW_XFJE = float(data['GW_XFJE'].sum())
YS_XFJE = float(data['YS_XFJE'].sum())
JF_XFJE = float(data['JF_XFJE'].sum())
JT_XFJE = float(data['JT_XFJE'].sum())
JY_XFJE = float(data['JY_XFJE'].sum())
JS_XFJE = float(data['JS_XFJE'].sum())
XY_XFJE = float(data['XY_XFJE'].sum())
QT_XFJE = float(data['QT_XFJE'].sum())


print(type(GW_XFJE))
print(type(YS_XFJE))
print(type(JF_XFJE))
print(type(JT_XFJE))
print(type(JY_XFJE))
print(type(JS_XFJE))
print(type(XY_XFJE))
print(type(QT_XFJE))




# labels = 'A','B','C','D'
# sizes = [10,20,30,40]
# print(type(sizes))
# plt.pie(sizes,labels = labels)
# plt.title('饼状图初始')
# plt.show()


labelList = 'CY_XFJE','GW_XFJE','YS_XFJE','JF_XFJE','JT_XFJE','JY_XFJE','JS_XFJE','XY_XFJE','QT_XFJE'
# dataList = np.array([CY_XFJE,GW_XFJE,YS_XFJE,JF_XFJE,JT_XFJE,JY_XFJE, JS_XFJE, XY_XFJE,QT_XFJE])
# print(type(dataList))
# print(dataList)
dataList = list([CY_XFJE,GW_XFJE,YS_XFJE,JF_XFJE,JT_XFJE,JY_XFJE, JS_XFJE, XY_XFJE,QT_XFJE])
print(type(dataList))

plt.pie(dataList,labels=labelList,autopct="%1.2f%%")
plt.title('消费占比')
plt.savefig("XFJE_BZT.jpg")
plt.show()
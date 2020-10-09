
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
data=pd.read_csv('Total.csv')
#data=data["ZF_RATIO"]


data=data[data['CY_XFCS']<=400]
print(data)
#data=data.sort_values(by="COUNT(BUSINESSTYPE)" , ascending=True)
#data["ZF_RATIO"]=data["ZF_RATIO"].apply(lambda x:  x*10000)
#data["GW_XFJE"]=data["GW_XFJE"].apply(lambda x:  x*10000)
y = data['ZF_RATIO']
x = data['CY_XFCS']
print(x)
x_data = np.array(x)#np.ndarray()
x_list=x_data.tolist()#list
y_data = np.array(y)#np.ndarray()
y_list=y_data.tolist()#list

# "r" 表示红色，ms用来设置*的大小
#plt.plot(x_list, y_list, "y", marker='*', ms=0, label="a")
plt.scatter(x_list, y_list, label='a',s=5)
# plt.plot([1, 2, 3, 4], [20, 30, 80, 40], label="b")
plt.xticks(rotation=45)
plt.xlabel("餐饮消费金额")
plt.ylabel("成绩")
plt.title("成绩与餐饮消费金额散点图")
# upper left 将图例a显示到左上角
plt.legend(loc="upper left")
# 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
#for x1, y1 in zip(x, y):
   # plt.text(x1, y1 + 1, str(y1), ha='center', va='bottom', fontsize=20, rotation=0)
plt.savefig("CYXFJE.jpg")
plt.show()

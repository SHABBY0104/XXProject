import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.stats import gaussian_kde

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
data=pd.read_csv('Total.csv')
#data=data["ZF_RATIO"]


Y_Name = 'ZF_RATIO'
# X_Name = 'IN_COUNT'
# Threshold = 400

# X_Name = 'CY_XFCS'
# Threshold = 300

# X_Name = 'CY_XFJE'
# Threshold = 5000
#
# X_Name = 'SUM_XFCS'
# Threshold = 800
#
X_Name = 'SUM_XFJE'
Threshold = 5000


data = data[data[X_Name]<Threshold]

x = np.array(data[X_Name])
y = np.array(data[Y_Name])

xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)


fig, ax = plt.subplots()
ax.scatter(x, y, c = z, s = 7, edgecolor ='')


plt.xlabel(X_Name)
plt.ylabel(Y_Name)
plt.title(X_Name + " AND " + Y_Name + " < " + str(Threshold))
plt.savefig(X_Name + "_DEN.jpg")


plt.show()
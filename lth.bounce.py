import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# for p in range(0,10):
#     p = p/10
#     print(p)

x_data = np.linspace(0,10,10)
y_data1 = 1 - pow(0.1,x_data)
y_data2 = 1 - pow(0.2,x_data)
y_data3 = 1 - pow(0.3,x_data)
y_data4 = 1 - pow(0.4,x_data)
y_data5 = 1 - pow(0.5,x_data)
y_data6 = 1 - pow(0.6,x_data)
y_data7 = 1 - pow(0.7,x_data)
y_data8 = 1 - pow(0.8,x_data)
y_data9 = 1 - pow(0.9,x_data)


plt.figure()
plt.xlabel("Number of bounces")
plt.ylabel("relative power")
plt.xlim((0,10))
plt.ylim((0,1))

l1,= plt.plot(x_data,y_data1)
l2,= plt.plot(x_data,y_data2)
l3,= plt.plot(x_data,y_data3)
l4,= plt.plot(x_data,y_data4)
l5,= plt.plot(x_data,y_data5)
l6,= plt.plot(x_data,y_data6)
l7,= plt.plot(x_data,y_data7)
l8,= plt.plot(x_data,y_data8)
l9,= plt.plot(x_data,y_data9)
plt.legend(handles=[l1,l2,l3,l4,l5,l6,l7,l8,l9,],
           labels = ['p=0.1','p=0.2','p=0.3','p=0.4','p=0.5','p=0.6','p=0.7','p=0.8','p=0.9'],
           loc= "best")
# plt.savefig('test')
plt.show()

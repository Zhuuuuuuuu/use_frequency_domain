import numpy as np
import matplotlib.pyplot as plt
import math

#定义阶跃函数
def step_function(x):
    return np.array(x > 0, dtype=np.int)

#参数初始定义
p = 0.8
Arx = 0.0001 #m2
Arx_room = 5*5 #m2
V_room = 5*5*3 #m3
c = 3*pow(10,8) # m/s


#公式
f = np.linspace(0,80*10**6,1000) # mhz
n_diff = (Arx*p)/(Arx_room*(1-p))
t1 = -(1/np.log(p))*(4*V_room/(Arx_room*c))

#jn频域表达式
H_diff = (1 + np.pi*2*f*t1*1j)
H_diff2 = n_diff**2/(H_diff.real **2 + H_diff.imag **2)
H = 10 * np.log10(H_diff2)


# t = np.linspace(0,80,8)
# h_diff = (n_diff*np.exp(-t/t1)*step_function(t))/t1

print("时延是",t1)
print("n_diff 是",n_diff)
# print("H_diff的值为",H_diff)


plt.figure()
plt.xlabel("f[Mhz]")
plt.ylabel("|H(f)|^2  [db]")
# plt.xticks()
# plt.yticks()
# plt.xlim((0,80))
# plt.ylim((-140,-100))
# plt.plot(f,H_diff)
plt.plot(f,H)
# plt.savefig('Jn-diffuse')
plt.show()

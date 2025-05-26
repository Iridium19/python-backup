import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import curve_fit

prozent1, q0 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q0.txt",delimiter=",", unpack=True)
prozent2, q1 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q1.txt",delimiter=",", unpack=True)
prozent3, q2 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q2.txt",delimiter=",", unpack=True)
prozent4, q3 = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\q3.txt",delimiter=",", unpack=True)


prozent11=prozent1*10**(-2)
prozent22=prozent2*10**(-2)
prozent33=prozent3*10**(-2)
prozent44=prozent4*10**(-2)
q00=q0*10**(-2)
q11=q1*10**(-2)
q22=q2*10**(-2)
q33=q3*10**(-2)

plt.scatter(prozent11,q00,marker='x',label='q0')
plt.scatter(prozent22,q11,marker='x',label='q1')
plt.scatter(prozent33,q22,marker='x',label='q2')
plt.scatter(prozent44,q33,marker='x',label='q3')


f=np.linspace(0.64,0.75,100)
u=(3*f-2)/(1-f)
plt.plot(f,u,color='blue', label='Theorie für q0')


p=np.linspace(0.0,0.67,100)
fitq1=(-1 +2* p) / (1 -  p)
e=np.linspace(0.66,0.8,100)
fitq11=(3-4*e)/(1-e)
plt.plot(p,fitq1,color='orange',label='Theorie für q1')
plt.plot(e,fitq11,color='orange')


hdfs=1-((p)/(1-p))
plt.plot(p,hdfs,color='red',label='Theorie für q3')


j=np.linspace(0.0,0.5,100)
x=j/(1-j)
plt.plot(j,x,color='green',label='Theorie für q2')


n=np.linspace(0.5,0.67,100)
h=(2-3*n)/(1-n)
plt.plot(n,h,color='green')




plt.ylabel('$Na_2O$  ')
plt.xlim(0,0.73)
plt.ylim(0,1)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.optimize as opt
from scipy.optimize import curve_fit

dicke,c1,c2,c3,c4,c5 = np.loadtxt(r'C:\Users\Justus\Desktop\12\Konzentrationen.csv',skiprows=0,delimiter=',',unpack=True)

plt.scatter(dicke,c1, marker='x', label='Datenwerte 1 mmol/L')
plt.scatter(dicke,c2, marker='x', label='Datenwerte 2 mmol/L')
plt.scatter(dicke,c3, marker='x', label='Datenwerte 3 mmol/L')
plt.scatter(dicke,c4, marker='x', label='Datenwerte 4 mmol/L')
plt.scatter(dicke,c5, marker='x', label='Datenwerte 5 mmol/L')

def linear1(dicke, m1):
    return (m1*dicke)
popt1, pcov1 = curve_fit(linear1, dicke, c1, p0=1)

m1=popt1
qm1=pcov1
#print(qm1,'Fehler von 1mmol')
#print(m1,'m von 1mmol')
plt.plot(dicke, (m1*dicke), label='Lineare Regression 1 mmol/L')

e1=-m1/0.001
print('1mmol',e1)




def linear2(dicke, m2):
    return (m2*dicke)
popt2, pcov2 = curve_fit(linear2, dicke, c2, p0=1)

m2=popt2
qm2=pcov2
#print(qm2,'Fehler von 2mmol')
#print(m2,'m von 2mmol')
plt.plot(dicke, (m2*dicke), label='Lineare Regression 2 mmol/L')

e2=-m2/0.002
print('2mmol',e2)

def linear3(dicke, m3):
    return (m3*dicke)
popt3, pcov3 = curve_fit(linear3, dicke, c3, p0=1)

m3=popt3
qm3=pcov3
#print(qm3,'Fehler von 3mmol')
#print(m3,'m von 3mmol')
plt.plot(dicke, (m3*dicke), label='Lineare Regression 3 mmol/L')

e3=-m3/0.003
print('3mmol',e3)



def linear4(dicke, m4):
    return (m4*dicke)
popt4, pcov4 = curve_fit(linear4, dicke, c4, p0=1)

m4=popt4
qm4=pcov4
#print(qm4,'Fehler von 4mmol')
#print(m4,'m von 4mmol')
plt.plot(dicke, (m4*dicke), label='Lineare Regression 4 mmol/L')

e4=-m4/0.004
print('4mmol',e4)




def linear5(dicke, m5):
    return (m5*dicke)
popt5, pcov5 = curve_fit(linear5, dicke, c5, p0=1)

m5=popt5
qm5=pcov5
#print(qm5,'Fehler von 5mmol')
#print(m5,'m von 5mmol')
plt.plot(dicke, (m5*dicke), label='Lineare Regression 5 mmol/L')

e5=-m5/0.005
print('5mmol',e5)
print(m5)



plt.xlabel('Schichtdicke [m]')
plt.ylabel('Absorption $[-log(I/I_0$)]')
plt.legend(fontsize=8)
plt.show()


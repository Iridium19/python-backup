import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.optimize as opt
from scipy.optimize import curve_fit


nummer22,di2, Absorbtion2 = np.loadtxt(r'C:\Users\Justus\Desktop\12\2mm.csv',skiprows=1,delimiter=',',unpack=True)
nummer52,di5, Absorbtion5 = np.loadtxt(r'C:\Users\Justus\Desktop\12\5mm.csv',skiprows=1,delimiter=',',unpack=True)
nummer102,di10, Absorbtion10 = np.loadtxt(r'C:\Users\Justus\Desktop\12\10mm.csv',skiprows=1,delimiter=',',unpack=True)

nummer2=nummer22 *0.001
nummer5=nummer52 *0.001
nummer10=nummer102 *0.001


plt.scatter(nummer2,Absorbtion2, marker='x',label='Datenwerte 2mm')
plt.scatter(nummer5,Absorbtion5, marker='x',label='Datenwerte 5mm')
plt.scatter(nummer10,Absorbtion10, marker='x',label='Datenwerte 10mm')

def linear2(nummer2, m):
    return (m*nummer2)
popt, pcov = curve_fit(linear2, nummer2, Absorbtion2, p0=0.001)

m=popt
qm=pcov
#print(qm,'Fehler vonm 2mm')
#print(m,'m von 2mm')

plt.plot(nummer2, (m*nummer2), label='Lineare Regression 2mm')

e6=-m/0.002
print('2mm',e6)

def linear5(nummer5, m5):
    return (m5*nummer5)
popt1, pcov1 = curve_fit(linear5, nummer5, Absorbtion5, p0=1)

m5=popt1
qm5=pcov1
#print(qm5,'Fehler von 5mm')
#print(m5,'m von 5mm')
plt.plot(nummer5, (m5*nummer5), label='Lineare Regression 5mm')

e7=-m5/0.005
print('5mm',e7)



def linear10(nummer10, m10):
    return (m10*nummer10)
popt2, pcov2 = curve_fit(linear10, nummer10, Absorbtion10, p0=0.001)

m10=popt2
qm10=pcov2
#print(qm10,'Fehler von 10mm')
#print(qm10,'m von 10mm')
plt.plot(nummer10, (m10*nummer10), label='Lineare Regression 10mm')


e8=-m10/0.01
print('10mm',e8)






plt.ylabel('Absorption $[I/I_0$]')
plt.xlabel('Konzentration [mol/L]')

plt.legend(fontsize=8)
plt.show()
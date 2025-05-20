import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.optimize as opt
from scipy.optimize import curve_fit



nummer102,di10, Absorbtion10 = np.loadtxt(r'C:\Users\Justus\Desktop\12\10mm.csv',skiprows=1,delimiter=',',unpack=True)
nummer1 = np.loadtxt(r'C:\Users\Justus\Desktop\12\xa.csv',skiprows=0,delimiter=',',unpack=True)

nummer10=nummer102*0.001

results8=sp.stats.linregress(nummer10,Absorbtion10)
Abs4_regress= results8.slope*nummer1+results8.intercept

plt.plot(nummer1,Abs4_regress,color='green',label='Lineare Regression 10mm')

plt.vlines(x=0.00590877, ymin=0, ymax=0.1429, colors='red', ls='--', lw=1,)
plt.hlines(y=0.1429, xmin=0.001, xmax=0.00590878, colors='red', linestyles='--', lw=1, label='Graphische Ermittlung für Konzentration')

plt.xlim(0.001,0.0065)
plt.ylim(0.02,0.15)
plt.ticklabel_format(axis='x', scilimits=(-3,-3))
plt.xlabel('Konzentration [mol/L]')
plt.ylabel('Absorption [-log(I/$I_0)$]')
plt.legend(loc=8)
plt.show()

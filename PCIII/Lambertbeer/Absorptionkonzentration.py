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


plt.scatter(nummer2,Absorbtion2, marker='x',label='Datenwerte 2 mm')
plt.scatter(nummer5,Absorbtion5, marker='x',label='Datenwerte 5 mm')
plt.scatter(nummer10,Absorbtion10, marker='x',label='Datenwerte 10 mm')


results6=sp.stats.linregress(nummer2,Absorbtion2)
Abs2_regress= results6.slope*nummer2+results6.intercept

plt.plot(nummer2,Abs2_regress,label='Lineare Regression 2 mm')

#print('m von 2mm',results6.slope)
#print('fm2', results6.stderr)



e6= -results6.slope/0.002
print('e 2mm',e6)

qe6=np.sqrt(((1/0.002)**2)*((results6.stderr)**2))
print('error e6',qe6)



results7=sp.stats.linregress(nummer5,Absorbtion5)
Abs3_regress= results7.slope*nummer5+results7.intercept

plt.plot(nummer5,Abs3_regress,label='Lineare Regression 5 mm')

#print('m von 5mm',results7.slope)
#print('fm5', results7.stderr)


e7=- results7.slope/0.005
print('e 5mm',e7)

qe7=np.sqrt(((1/0.005)**2)*((results7.stderr)**2))
print('error e7',qe7)




results8=sp.stats.linregress(nummer10,Absorbtion10)
Abs4_regress= results8.slope*nummer10+results8.intercept

plt.plot(nummer10,Abs4_regress,label='Lineare Regression 10 mm')

#print('m von 10mm',results8.slope)
#print('fm10', results8.stderr)

e8= -results8.slope/0.01
print('e 10mm',e8)

qe8=np.sqrt(((1/0.01)**2)*((results8.stderr)**2))
print('error e8',qe8)


















plt.ticklabel_format(axis='x', scilimits=(-3,-3))
plt.ylabel('Absorption $[-log(I/I_0$)]')
plt.xlabel('Konzentration [mol/L]')

plt.legend(fontsize=8)
plt.show()
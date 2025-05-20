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


results6=sp.stats.linregress(nummer2,Absorbtion2)
Abs2_regress= results6.slope*nummer2+results6.intercept

plt.plot(nummer2,Abs2_regress)

#print('m von 2mm',results6.slope)

e6= -results6.slope/0.002
#print('e 2mm',e6)

qe6=np.sqrt(((1/0.002)**2)*((results6.stderr)**2))
#print('error e6',qe6)



results7=sp.stats.linregress(nummer5,Absorbtion5)
Abs3_regress= results7.slope*nummer5+results7.intercept

plt.plot(nummer5,Abs3_regress)

#print('m von 5mm',results7.slope)

e7=- results7.slope/0.005
#print('e 5mm',e7)

qe7=np.sqrt(((1/0.005)**2)*((results7.stderr)**2))
#print('error e7',qe7)




results8=sp.stats.linregress(nummer10,Absorbtion10)
Abs4_regress= results8.slope*nummer10+results8.intercept

plt.plot(nummer10,Abs4_regress)

#print('m von 10mm',results8.slope)


e8= -results8.slope/0.01
#print('e 10mm',e8)

qe8=np.sqrt(((1/0.01)**2)*((results8.stderr)**2))
#print('error e8',qe8)











dicke,c1,c2,c3,c4,c5 = np.loadtxt(r'C:\Users\Justus\Desktop\12\Konzentrationen.csv',skiprows=0,delimiter=',',unpack=True)

plt.scatter(dicke,c1, marker='x', label='Datenwerte 1mmol')
plt.scatter(dicke,c2, marker='x', label='Datenwerte 2mmol')
plt.scatter(dicke,c3, marker='x', label='Datenwerte 3mmol')
plt.scatter(dicke,c4, marker='x', label='Datenwerte 4mmol')
plt.scatter(dicke,c5, marker='x', label='Datenwerte 5mmol')


results=sp.stats.linregress(dicke,c1)
c1_regress= results.slope*dicke+results.intercept

plt.plot(dicke,c1_regress, label='Lineare Regression 1mmol')

#print('m von 1mmol',results.slope)

e1= -results.slope/0.001
#print('e 1mmol',e1)

qe1=np.sqrt(((1/0.002)**2)*((results.stderr)**2))
#print('Error e1',qe1)


results2=sp.stats.linregress(dicke,c2)
c2_regress= results2.slope*dicke+results2.intercept

plt.plot(dicke,c2_regress,label='Lineare Regression 2mmol')

#print('m von 2mmol',results2.slope)

e2=- results2.slope/0.002
#print('e 2mmol',e2)

qe2=np.sqrt(((1/0.002)**2)*((results2.stderr)**2))
#print('error e2',qe2)



results3=sp.stats.linregress(dicke,c3)
c3_regress= results3.slope*dicke+results3.intercept

plt.plot(dicke,c3_regress,label='Lineare Regression 3mmol')

#print('m von 3mmol',results3.slope)

e3=- results3.slope/0.003
#print('e 3mmol',e3)

qe3=np.sqrt(((1/0.002)**2)*((results3.stderr)**2))
#print('error e3',qe3)



results4=sp.stats.linregress(dicke,c4)
c4_regress= results4.slope*dicke+results4.intercept

plt.plot(dicke,c4_regress,label='Lineare Regression 4mmol')

#print('m von 4mmol',results4.slope)

e4= -results4.slope/0.004
#print('e 4mmol',e4)

qe4=np.sqrt(((1/0.002)**2)*((results4.stderr)**2))
#print('error e4',qe4)




results5=sp.stats.linregress(dicke,c5)
c5_regress= results5.slope*dicke+results5.intercept

plt.plot(dicke,c5_regress,label='Lineare Regression 5mmol')

#print('m von 5mmol',results5.slope)

e5= -results5.slope/0.005
#print('e 5mmol',e5)


qe5=np.sqrt(((1/0.002)**2)*((results5.stderr)**2))
#print('error e5',qe5)


ea=np.array([e1,e2,e3,e4,e5,e6,e7,e8])

ef=np.mean(ea)

print(ef,'ef')
e=((e1+e2+e3+e4+e5+e6+e7+e8)/8)


print(e,'e')

qe=np.std(ea)


qe2=np.sqrt(qe**2+(((1/8)**2)*(qe1**2))+(((1/8)**2)*(qe2**2))+(((1/8)**2)*(qe3**2))+(((1/8)**2)*(qe4**2))+(((1/8)**2)*(qe5**2))+(((1/8)**2)*(qe6**2))+(((1/8)**2)*(qe7**2))+(((1/8)**2)*(qe8**2)))

print('qe',qe)
print('qe2',qe2)



cges=0.1429/(-e*0.01)
print('Gesuchte Konzentration',cges)

qcges=np.sqrt(((((0.1429/(0.01*(-e**2))))**2))*(qe2**2))
print('qcges',qcges)




plt.legend(fontsize=8)
#plt.show()
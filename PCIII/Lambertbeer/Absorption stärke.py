import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.optimize as opt
from scipy.optimize import curve_fit

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
#print('Fehler von m1',results.stderr)
#print('y abschnitt', results.intercept)

e1= -results.slope/0.001
print('e 1mmol',e1)

qe1=np.sqrt(((1/0.002)**2)*((results.stderr)**2))
print('Error e1',qe1)


results2=sp.stats.linregress(dicke,c2)
c2_regress= results2.slope*dicke+results2.intercept

plt.plot(dicke,c2_regress,label='Lineare Regression 2mmol')

#print('m von 2mmol',results2.slope)
#print('fm',results2.stderr)


e2=- results2.slope/0.002
print('e 2mmol',e2)

qe2=np.sqrt(((1/0.002)**2)*((results2.stderr)**2))
print('error e2',qe2)



results3=sp.stats.linregress(dicke,c3)
c3_regress= results3.slope*dicke+results3.intercept

plt.plot(dicke,c3_regress,label='Lineare Regression 3mmol')

#print('m von 3mmol',results3.slope)
#print('fm',results3.stderr)



e3=- results3.slope/0.003
print('e 3mmol',e3)

qe3=np.sqrt(((1/0.002)**2)*((results3.stderr)**2))
print('error e3',qe3)



results4=sp.stats.linregress(dicke,c4)
c4_regress= results4.slope*dicke+results4.intercept

plt.plot(dicke,c4_regress,label='Lineare Regression 4mmol')

#print('m von 4mmol',results4.slope)
#print('fm',results4.stderr)




e4= -results4.slope/0.004
print('e 4mmol',e4)

qe4=np.sqrt(((1/0.002)**2)*((results4.stderr)**2))
print('error e4',qe4)




results5=sp.stats.linregress(dicke,c5)
c5_regress= results5.slope*dicke+results5.intercept

plt.plot(dicke,c5_regress,label='Lineare Regression 5mmol')

#print('m von 5mmol',results5.slope)
#print('fm',results5.stderr)



e5= -results5.slope/0.005
print('e 5mmol',e5)


qe5=np.sqrt(((1/0.002)**2)*((results5.stderr)**2))
print('error e5',qe5)










x=10^-3


plt.ticklabel_format(axis='x', scilimits=(-3,-3))
plt.xlabel('Schichtdicke [m]')
plt.ylabel('Absorption $[I/I_0$]')
plt.legend(fontsize=8)
plt.show()
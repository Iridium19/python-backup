import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Sauerstoff, Volumen = np.loadtxt(r"C:\Users\Justus\Desktop\Python\ACIII\Plots\supraleiter.txt",delimiter=',', unpack=True)


plt.scatter(Sauerstoff,Volumen,marker='x',color='red',label='Daten')

def lin (x,a,b):
    return a*x+b

parameter, fehler=curve_fit(lin,Sauerstoff,Volumen)
a,b=parameter
print(parameter,'parameter')
fehler1 = np.sqrt(np.diag(fehler))
print(fehler1,'fehler')


x=np.linspace(5.5,7.3,100)
g= a*x+b
plt.plot(x,g,label='Linear Fit')

plt.hlines(173.04,0,6.7832799902,color='black',label='Herrgestellter Supraleiter')
plt.vlines(6.7832799902,0,173.04,color='black')



plt.xlim(5.9,7.1)
plt.ylim(171.5,177)
plt.ylabel('Elementarzellenvolumen in $\AA^3$')
plt.xlabel('Sauerstoffanteil in der Verbindung $YBa_2Cu_3O_x$')
plt.legend()
plt.show()

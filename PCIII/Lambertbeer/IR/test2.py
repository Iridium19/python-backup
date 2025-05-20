import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import io
import sympy as sp
import scipy.constants as kon

wellenlängel05, Intensitätl05=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Luft_050.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängel05i, Intensitätl05i=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Luft_05_inter0.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängel80, Intensitätl80=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Luft_80.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängeM02bg, IntensitätM02bg0=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p02_bg0.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängeM02, IntensitätM02=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p02_probe0.dpt', skiprows=0, delimiter='\t', unpack=True)
wellenlängeM80, IntensitätM80=np.loadtxt(r'C:\Users\Justus\Desktop\IR\Gr_12_Methan_p080.dpt', skiprows=0, delimiter='\t', unpack=True)
rzweig, ir=np.loadtxt(r'C:\Users\Justus\Desktop\IR\rzweig.csv', delimiter='\t', skiprows=0,  unpack=True)
pzweig=np.loadtxt(r'C:\Users\Justus\Desktop\IR\p-zweig.csv',skiprows=0,  unpack=True)

ghf=IntensitätM02/IntensitätM02bg0

plt.plot(wellenlängeM80,IntensitätM80 ,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

print(min(ghf)) # bei 1306
plt.ylim(0.8,1.1)
plt.xlim(2550,2620)
plt.show()
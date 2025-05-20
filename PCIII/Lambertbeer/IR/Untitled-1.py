


# %% [markdown]
# Datenimport
# 

# %%
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




# %% [markdown]
# Spektren

# %%
plt.plot(wellenlängel05, Intensitätl05,label='Luft 0.5$cm^{-1}$',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Intensität')
plt.legend()
plt.show()

# %% [markdown]
# Wellenzahl 8
# 

# %%
plt.plot(wellenlängel80, Intensitätl80,label='Luft 8$cm^{-1}$',linewidth='0.3', color='black')


plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Intensität')
plt.legend()
plt.show()

# %% [markdown]
# CO2 2200-2400
# 

# %%
plt.plot(wellenlängel05, Intensitätl05,label='CO$_2$ 0.5$cm^{-1}$',linewidth='0.3', color='black')

plt.xlim(2200,2400)
plt.vlines(ymin=0,ymax=0.09,x=2348.96888,linewidth=1,label='$\sigma$')
plt.ylabel('Intensität')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylim(0,0.09)
plt.legend()
plt.show()

sigmaCO2=2348.96888
usigmaCO2=0.12055

omega= ((kon.c*sigmaCO2*10**2*kon.h)/ kon.hbar)
uomega= np.sqrt(((kon.c*kon.h/kon.hbar)*usigmaCO2*10**2)**2)

reduziertemasseco2= 7.2*10**(-27)
KCO2= omega**2*reduziertemasseco2

uKCO2=np.sqrt(2*omega*reduziertemasseco2*uomega)

print(KCO2,'$KCO_2$')
print(uKCO2,'$uKCO_2$')


print(omega,'$\omega$')
print(uomega,'$\sigma\omega$')

# %% [markdown]
# CO2 620-720

# %%
plt.plot(wellenlängel05, Intensitätl05,label='Co$_2$ 0.5$cm^{-1}$',linewidth='0.3', color='black')

plt.vlines(ymin=0,ymax=0.05,x=667.82755,linewidth=1,label='$\sigma$')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Intensität')
plt.ylim(0,0.05)
plt.xlim(620,720)

plt.legend()
plt.show()



sigmaCO2=667.82755
usigmaCO2=0.12055

omega= ((kon.c*sigmaCO2*10**2*kon.h)/ kon.hbar)
uomega= np.sqrt(((kon.c*kon.h/kon.hbar)*usigmaCO2*10**2)**2)

reduziertemasseco2= 3.622*10**(-27)
KCO2= omega**2*reduziertemasseco2

uKCO2=np.sqrt(2*omega*reduziertemasseco2*uomega)

print(KCO2,'$KCO_2$')
print(uKCO2,'$uKCO_2$')


print(omega,'$\omega$')
print(uomega,'$\sigma\omega$')

# %%
wellenlängel05i1=wellenlängel05i*3.164*10**(-5)


plt.plot(wellenlängel05i1, Intensitätl05i,label='Luft 0.5$cm^{-1}$',linewidth='0.3', color='black')
plt.xlabel("Spiegelweg")
plt.ylabel("Amplitude")


plt.show()

# %% [markdown]
# Formier Trnasformation
# 

# %%
import numpy as np
import matplotlib.pyplot as plt

# Beispiel für ein Interferogramm: Ein einfaches sinusförmiges Signal (Interferogramm)
# Ersetze diese Daten mit deinem eigenen Interferogramm
x_data = wellenlängel05i1  # Zeit oder Positionswerte
y_data = Intensitätl05i

# Durchführung der Fourier-Transformation
y_fft = np.fft.fft(y_data)

# Berechnung der Frequenzen
sampling_interval = x_data[1] - x_data[0]  # Abtastintervall
sampling_rate = 1 / sampling_interval  # Abtastrate
frequencies = np.fft.fftfreq(len(x_data), d=sampling_interval)  # Frequenzwerte

# Nur die positiven Frequenzen verwenden
positive_frequencies = frequencies[:len(frequencies)//2]
positive_y_fft = y_fft[:len(frequencies)//2]

# Plotten des Interferogramms und seines Frequenzspektrums
plt.figure(figsize=(12, 6))

# Originales Interferogramm
plt.subplot(1, 2, 1)
plt.plot(x_data, y_data,linewidth='0.3',color='black')
plt.title("Interferogramm")
plt.xlabel("Spiegelweg")
plt.ylabel("Amplitude")

# Fourier-Spektrum
plt.subplot(1, 2, 2)
plt.plot(positive_frequencies, np.abs(positive_y_fft), linewidth='0.3',color='black')
plt.title("Frequenzspektrum (Fourier-Transformation)")
plt.xlim(200,8000)
plt.xlabel("Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$")
plt.ylabel("Intensität")

plt.tight_layout()
plt.show()






# %% [markdown]
# Methan
# 

# %%
plt.plot(wellenlängeM02bg, IntensitätM02bg0,label='Refernzspektrum',linewidth='0.3', color='black')
plt.ylabel('Intensität')
plt.xlabel("Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$")


plt.legend()
plt.show()

# %% [markdown]
# Methan 0.2 PRobe
# 

# %%
plt.plot(wellenlängeM02, IntensitätM02,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Intensität')


plt.legend()
plt.show()

# %% [markdown]
# Methan 0.2 normiert

# %%
ghf=IntensitätM02/IntensitätM02bg0

plt.plot(wellenlängeM02, ghf,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

plt.show()


# %% [markdown]
# Methan02 1200 1400
# 

# %%
ghf=IntensitätM02/IntensitätM02bg0

plt.plot(wellenlängeM02, ghf,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

print(min(ghf)) # bei 1306

plt.xlim(1200,1400)
plt.show()

# %% [markdown]
# Methan 02 2550 2650

# %%
ghf=IntensitätM02/IntensitätM02bg0

plt.plot(wellenlängeM02, ghf,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

plt.ylim(0.95,1.02)
plt.xlim(2550,2650)
plt.show()

# %% [markdown]
# Methan 0.8 

# %%
plt.plot(wellenlängeM80, IntensitätM80,label='Methan 0.8 bar',linewidth='0.3', color='black')


plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

plt.ylim(0.8,1.01)
plt.xlim(2550,2650)
plt.show()

# %% [markdown]
# methan 0.2 2800 3300

# %%
ghf=IntensitätM02/IntensitätM02bg0

plt.plot(wellenlängeM02, ghf,label='Methan 0.2 bar',linewidth='0.3', color='black')

plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.ylabel('Transmission')

plt.xlim(2800,3300)
plt.show()

# %% [markdown]
# Minimas 2800 3300

# %%
import numpy as np
import scipy.signal
ghf=IntensitätM02/IntensitätM02bg0





def find_local_minima(x, y):
    """
    Findet alle lokalen Minima in einem gegebenen Datensatz (x, y), wobei eine Mindestdifferenz
    von 0.3 zum nächsten lokalen Maximum eingehalten wird.
    
    :param x: Liste oder numpy-Array mit den x-Werten
    :param y: Liste oder numpy-Array mit den y-Werten
    :return: Liste mit Tupeln (x_min, y_min) der gefundenen Minima
    """
    x = wellenlängeM02
    y = ghf
    
    minima_indices = scipy.signal.argrelextrema(y, np.less)[0]
    
    # Nur Minima unter y=0.7 behalten
    minima = [(x[i], y[i]) for i in minima_indices if y[i] < 0.7]
    
    # Minima filtern, sodass sie mindestens 7 x-Einheiten voneinander entfernt sind
    filtered_minima = []
    for x_min, y_min in minima:
        if not filtered_minima or abs(x_min - filtered_minima[-1][0]) >= 7:
            filtered_minima.append((x_min, y_min))
        else:
            # Falls zu nah, behalte nur das tiefere Minimum
            if y_min < filtered_minima[-1][1]:
                filtered_minima[-1] = (x_min, y_min)
    
    return filtered_minima

x = wellenlängeM02
y = ghf

# Lokale Minima finden
minima = find_local_minima(x, y)

# Plot erstellen

plt.plot(x, y, label='Daten',color='black',linewidth=0.3)


plt.xlabel('Wellenzahl ${[\\tilde{\\nu}]=\\frac{1}{cm}}$')
plt.vlines(x=rzweig, ymin=0,ymax=1, color='red', linestyles='-', label='R-Zweig',linewidth=0.5)
plt.vlines(x=pzweig, ymin=0,ymax=1, color='red', linestyles='-',label='Pzweig',linewidth=0.5)

plt.xlim(2800,3300)
plt.title('Lokale Minima')
plt.show()

# Ergebnisse ausgeben
for x_min, y_min in minima:
    print(f"Lokales Minimum bei x={x_min:.2f}, y={y_min:.2f}")



# %% [markdown]
# Berechnung B' B''

# %%
w11,w22,banz1=np.loadtxt(r'C:\Users\Justus\Desktop\IR\B1.csv', skiprows=0,  unpack=True)
w1,w2,Banz=np.loadtxt(r'C:\Users\Justus\Desktop\IR\B2.csv', skiprows=0,  unpack=True)

dif1=w11-w22
dif2=w1-w2
B1array=dif1/banz1
B2array=dif2/Banz    
print(dif2,'Differnz',Banz,'AnzahlBs',B2array,'B')
B1=np.mean(B1array)*10**2
B2=np.mean(B2array)*10**2
print(B2)
uB1=np.std(B1array)*10**2
uB2=np.std(B2array)*10**2

#b2grundzustand

# %% [markdown]
# Bindungslänge
# 

# %%


mr1=4.04756362*10**(-27)
mr=8/3*kon.u



r1=np.sqrt(kon.h/(8*kon.pi**2*kon.c*B1*mr))
r2=np.sqrt(kon.h/(8*kon.pi**2*kon.c*B2*mr))

print(r1,'r1')
print(r2,'r2')

ur1=np.sqrt((-kon.h/(2**(5/2)*kon.pi*kon.c*mr*np.sqrt(kon.h/(kon.c*mr*B1))*B1**2)*uB1)**2)
ur2=np.sqrt((-kon.h/(2**(5/2)*kon.pi*kon.c*mr*np.sqrt(kon.h/(kon.c*mr*B2))*B2**2)*uB2)**2)

print(ur1,'ur1')
print(ur2,'ur2')

# %%
from scipy.optimize import curve_fit

def linearfit(m,x,t):
    return(m*x+t)

x=[1,2]
y=[1300.4,1288.3]
parameter, fehler= curve_fit(linearfit,x,y,p0=(-7.5,1270))
m,t=parameter
fehler1=np.sqrt(np.diag(fehler))
m_err, t_err= fehler1

print(m,'m')
#print(m_err,'m_err')
print(t,'t')
#print(t_err,'t_err')


xe=-m/(2*t)
print(xe,'xe')

De=kon.h*kon.c*t*10**2/(4*xe)
print(De,'De')


D0=De-1/2*kon.h*kon.c*t*10**2

print(D0,'D0')

D0KJ=D0*kon.N_A/1000

print(D0KJ,'D0KJ')




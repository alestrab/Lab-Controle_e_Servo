import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


#Dados coletados do osciloscopio
data = np.loadtxt('data.txt',delimiter='\\t',dtype=str)
#Tempo
t=np.array([float(i) for i in data[:,3]])
#Dados canal 1 - Tensao na Fonte
x1=np.array([float(i) for i in data[:,4]])
#Dados canal 2 - Tensao VTaco
x2=np.array([float(i) for i in data[:,5]])

#Correcao do tempo para inicializacao
t = t-t[0]


#Corte dos dados
ti=0.64
tf=3.9
i = find_nearest(t,ti)
f = find_nearest(t,tf)
t=t[i:f]-t[i]
x1=x1[i:f]
x2=x2[i:f]

#Correcao do degrau das tensoes
x1 = x1 -x1[0]
x2 = x2 -x2[0]

#Modelagem da tensao da fonte
def f(x,a,b):
    return b*(1-np.exp(-a*x))
popt,pcov = curve_fit(f,t,x1,maxfev=10000,p0=[10,11.68])
a = popt[0]
b = popt[1]
x1_fit = f(t,a,b)
r2 = r2_score(x1,x1_fit)

plt.scatter(t,x1,color='r',label='Dados Osciloscópio')
plt.plot(t,x1_fit,color='b',label='Ajuste, R² = '+str(round(r2,4)),linewidth=4)
plt.plot(np.NaN, np.NaN, '-', color='none', label=f'$V(t)=b\cdot(1-exp(-a\,t))$')
plt.plot(np.NaN, np.NaN, '-', color='none', label='a = '+str(round(a,4))+', b = '+str(round(b,4)))
plt.grid(which='both')
plt.legend(fontsize=20)
plt.xlabel('Tempo [s]',fontsize=20)
plt.ylabel('Tensão [V]',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
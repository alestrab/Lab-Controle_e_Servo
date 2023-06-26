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

#Dados simulados pelo simulink
data_sim = np.loadtxt('vtaco_simulink.txt')
t_sim = data_sim[:,0]
x2_sim_1 = data_sim[:,1]
x2_sim_2 = data_sim[:,2]

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

plt.scatter(t,x2,color='r',label='Dados Osciloscópio')
plt.plot(t_sim,x2_sim_1,color='b',label='Simulink - Primeira Ordem',linewidth=4)
plt.plot(t_sim,x2_sim_2,color='g',label='Simulink - Segunda Ordem',linewidth=4)
plt.legend(fontsize=20)
plt.xlabel('Tempo [s]',fontsize=20)
plt.ylabel('VTaco [V]',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
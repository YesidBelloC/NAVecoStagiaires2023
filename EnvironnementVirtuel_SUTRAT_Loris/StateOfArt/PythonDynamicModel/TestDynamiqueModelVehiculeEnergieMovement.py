import numpy
import math
import matplotlib.pyplot as plt

# Input constants
# Parametros ctes Peugeot 208
Cr =0.01  #[N/rad] Coef long delantero asociado al relacion (slip rate) deslizamiento
Rw =0.61976/2 #[m] Radio Llantas Style vertion
M  =1500  #[kgr] % 208 110 308 1300 508 1500

#Parametros ctes entorno
g    =9.81   #[m/s2] gravedad.
rho  =1.25  #[Kg/m3] Masa volumetrica aire
SCx  =0.24   #Coef aerodinamique 208 0.61 308 0.63 508 0.58

T = 20
alpha = -0.08726646259971647 #5deg
Eff = 0.7
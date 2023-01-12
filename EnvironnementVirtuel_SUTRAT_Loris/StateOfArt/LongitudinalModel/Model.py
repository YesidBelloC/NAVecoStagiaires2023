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

T = 0
alpha = 0 #5deg

d0 = d = 0
v0 = v = 20
a0 = 0

ts = numpy.linspace(0, 200, 1000)
dt = ts[1]

ds = []
vs = []
accs = []
for t in ts:

    Fw   = M*g*math.sin(alpha)
    Faer = 0.5*rho*SCx*v**2

    if v>=0:
        Frr  = M*g*Cr*math.cos(alpha)
    else:
        Frr  = 0


    dddt = v
    dvdt = (T/Rw-Faer-Frr-Fw)/M

    v += dvdt*dt
    d += dddt*dt
    a = dvdt

    vs.append(v)
    ds.append(d)
    accs.append(a)


plt.subplot(3, 1, 1)
# plt.figure(figsize=(10,4))
plt.plot(ts, ds)
#plt.fill_between(DistCum,theta_vals_int,alpha=0.1)
plt.ylabel("Position (m)")
plt.xlabel("Temps (s)")
plt.grid()
# plt.show()
plt.subplot(3, 1, 2)
# plt.figure(figsize=(10,4))
plt.plot(ts, vs)
#plt.fill_between(DistCum,theta_vals_int,alpha=0.1)
plt.ylabel("Vitesse (m/s)")
plt.xlabel("Temps (s)")
plt.grid()
# plt.show()
plt.subplot(3, 1, 3)
# plt.figure(figsize=(10,4))
plt.plot(ts, accs)
#plt.fill_between(DistCum,theta_vals_int,alpha=0.1)
plt.ylabel("Accel (m/s2)")
plt.xlabel("Temps (s)")
plt.grid()
plt.show()
# Car race along a track
# ----------------------
# An optimal control problem (OCP),
# solved with direct multiple-shooting.
#
# For more information see: http://labs.casadi.org/OCP
from casadi import *
import numpy as np

N = 100 # number of control intervals

opti = Opti() # Optimization problem

# Parametres ctes
p = 0       # pente en %
Cr = 0.01  #[N/rad] Coefficient de roulement
Rw = 0.3099 #Rayon de la roue
M  = 1500  #[kgr] % 208 1100 308 1300 508 1500

#Parametros ctes entorno
g    =9.81      #[m/s2] gravité.
pair =1.25      #[Kg/m3] Masse volumique de l'air
SCx  =2.2*0.11  #Surface*Coefficient aérodynamique
rend = 0.8   ## rendement du moteur
# u = 200 ## en N/m couple moteur
CoupleAnt= 1
# ---- decision variables ---------
X = opti.variable(3,N+1) # state trajectory
pos     = X[0,:]
speed   = X[1,:]
energie = X[2,:]
U = opti.variable(2,N)   # control trajectory (throttle)
Couple     = U[0,:]
RoueLibre  = U[1,:]
T = opti.variable()      # final time

# ---- objective          ---------
# opti.minimize(T)
# opti.minimize((speed[-1]-20)**2)
opti.minimize((pos[-1]-700)**2)
# opti.minimize(0.0001*energie[-1]+T)

# ---- dynamic constraints --------
f = lambda x,u: vertcat(x[1],u[1]*u[0]/(Rw*M)-g*Cr*cos(p)-g*sin(p)-pair*SCx*(0.5/M)*x[1]**2+(1-u[1])*CoupleAnt, x[1]*u[0]) # dx/dt = f(x,u)

dt = T/N # length of a control interval
for k in range(N): # loop over control intervals
   # Runge-Kutta 4 integration
   k1 = f(X[:,k],         U[:,k])
   k2 = f(X[:,k]+dt/2*k1, U[:,k])
   k3 = f(X[:,k]+dt/2*k2, U[:,k])
   k4 = f(X[:,k]+dt*k3,   U[:,k])
   x_next = X[:,k] + dt/6*(k1+2*k2+2*k3+k4)
   opti.subject_to(X[:,k+1]==x_next) # close the gaps

# ---- path constraints -----------
# limit = lambda pos: 1-sin(2*pi*pos)/2
# opti.subject_to(speed<=limit(pos))   # track speed limit
opti.subject_to(speed<=23)   # track speed limit
opti.subject_to(speed>=0)   # track speed limit
opti.subject_to(opti.bounded([-1000,0],U,[1000,1])) # control is limited

# ---- boundary conditions --------
opti.subject_to(pos[0]==0)   # start at position 0 ...
opti.subject_to(speed[0]==0) # ... from stand-still
opti.subject_to(energie[0]==0) # ... from stand-still
# opti.subject_to(pos[-1]==1000)  # finish line at position

# ---- misc. constraints  ----------
opti.subject_to(T==80) # Time must be positive

# ---- initial values for solver ---
opti.set_initial(speed, 0)
# opti.set_initial(T, 55)

# ---- solve NLP              ------
opti.solver("ipopt") # set numerical backend
sol = opti.solve()   # actual solve

# ---- post-processing        ------
from pylab import step, figure, show, spy
import matplotlib.pyplot as plt

figure()
plt.plot(np.arange(0,sol.value(T),sol.value(T)/(N+1)),sol.value(speed))
plt.xlabel('Temps [s]')
plt.ylabel('Speed')
plt.title('Speed state [m/s]')
plt.grid()

figure()
plt.plot(np.arange(0,sol.value(T),sol.value(T)/(N+1)),sol.value(pos))
plt.xlabel('Temps [s]')
plt.ylabel('Position')
plt.title('Position state [m]')
plt.grid()

figure()
plt.plot(np.arange(0,sol.value(T),sol.value(T)/N),sol.value(Couple),'k')
plt.xlabel('Temps [s]')
plt.ylabel('Couple')
plt.title('Couple Input [Nm]')
plt.grid()

figure()
plt.plot(np.arange(0,sol.value(T),sol.value(T)/N),sol.value(RoueLibre),'k')
plt.xlabel('Temps [s]')
plt.ylabel('RoueLibre')
plt.title('RoueLibre Input [Nm]')
plt.grid()

# figure()
# spy(sol.value(jacobian(opti.g,opti.x)))
# figure()
# spy(sol.value(hessian(opti.f+dot(opti.lam_g,opti.g),opti.x)[0]))

show()

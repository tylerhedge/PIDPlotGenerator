import matplotlib.pyplot as plt
import numpy as np
from math import copysign

SP = 0 #setpoint
velo = 5 #starting velocity
accel = 0 #starting acceleration
kp = 0.05
kd = 0.02
ki = 0.0001
I = 0
IMax = 2
withIMax = True
withBlockage = True
kfriction = 0.003
grav = -0.01
withGrav = True
elast = SP - velo #means kd wont freak out on first loop 
times, dt = np.linspace(0, 100, 2500, retstep=True)
y = []


for time in times:
    e = SP - velo
    de = (e - elast)/dt
    elast = e
    accel += kp*e*dt + de*kd + ki*I -accel*kfriction
    
    I += e*dt
    if withIMax: I = copysign(min(abs(I), IMax), I)
    
    if withGrav: accel += grav*dt
    if withBlockage and time < 30: accel = 0
    velo+= accel*dt
    y.append(velo)


plt.plot(times, y, label='velocity', color='r')
plt.plot((times[0], times[-1]), (SP, SP), label='setpoint', color='b')
plt.xlabel('Time')
plt.ylabel("Velocity")
plt.title("PID controller reacting less violently with max I")
plt.legend()
plt.show()
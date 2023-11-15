import matplotlib.pyplot as plt
import numpy as np

SP = 0 #setpoint
velo = 5 #starting velocity
accel = 0 #starting acceleration
kp = 0.03
kd = 0.009
kfriction = 0.003
elast = SP - velo #means kd wont freak out on first loop 
times, dt = np.linspace(0, 100, 2500, retstep=True)
y = []


for time in times:
    e = SP - velo
    de = (e - elast)/dt
    elast = e
    accel += kp*e*dt + de*kd -accel*kfriction
    velo+= accel*dt
    y.append(velo)


plt.plot(times, y, label='velocity', color='r')
plt.plot((times[0], times[-1]), (SP, SP), label='setpoint', color='b')
plt.xlabel('Time')
plt.ylabel("Velocity")
plt.title("Tuned PD controller")
plt.legend()
plt.show()
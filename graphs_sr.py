import subfunctions
from define_rovers import *
import numpy as np
import matplotlib.pyplot as plt
rover, planet = define_rover_1()
gear=subfunctions.get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
om=[]
for i in range(381):
    x=round(3.8-(0.01*i),6)
    om.append(x)

omega = np.array(om)
MST=subfunctions.tau_dcmotor(omega,rover['wheel_assembly']['motor'])
MST=MST*gear
pow=[]
for i in range(omega.size):
    x=omega[i]*MST[i]
    pow.append(x)
power=np.array(pow)
fig, (ax1,ax2,ax3) = plt.subplots(3)
ax1.plot(MST,omega,color='blue')
ax2.plot(MST,power,color='blue')
ax3.plot(omega,power,color='blue')
ax1.set_title('Graphs for graphs_sr')
ax1.set_xlabel('Speed Reducer Torque [Nm]')
ax2.set_xlabel('Speed Reducer Torque [Nm]')
ax3.set_xlabel('Speed Reducer Speed [rad/s]')
ax1.set_ylabel('Speed Reducer Speed [rad/s]')
ax2.set_ylabel('Speed Reducer Power [W]')
ax3.set_ylabel('Speed Reducer Power [W]')
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.subplots_adjust(bottom=0.088, right=0.989, top=0.947,left=0.052,wspace=0.2,hspace=0.386)
plt.show(

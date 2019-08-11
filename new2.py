import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp

mlp.style.use('default')
#parameter
n = 2001# no of point
f = np.pi #no of lobes
r = 5 # scaling factor

#data
theta = np.linspace(0,20.0*np.pi,n)
curve1 = r*np.cos(f*theta)
curve2 = r*np.sin(f*theta)

#get an axis handle/Object
ax1 = plt.subplot(111,polar = True)

#plot the graph
ax1.plot(theta,curve1,color = 'xkcd:salmon')
ax1.plot(theta,curve2,color = 'xkcd:azure')

#radius limits
ax1.set_ylim(-6,6)

#radius ticks
ax1.set_yticks(np.linspace(-6,6,7))

#radius tick position in degrees
ax1.set_rlabel_position(135)
#angle ticks
ax1.set_xticks(np.linspace(0,2.0*np.pi,17)[:-1])


#additional tweaks
#plt.grid(True)
#plt.legend()
#plt.title("Rose pattern")
plt.show()
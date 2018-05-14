#Problem 3: Write a nite-volume advection solver similar to the one we saw in class. Make
#this one have a negative velocity, and give it periodic boundary conditions. Plot the solution as a
#function of time - how does it behave? How does the total mass behave with time? (10)
#simple_advect_finite_volume.py

import numpy
from matplotlib import pyplot as plt
import time

# from simple advect finite volume
#simple_advect_finite_volume.py

n=3
v=-1.0 #negative velocity
dx=1.0
dt=1.0

if True: #do a boxcar
    rho=numpy.zeros(n)

    rho[int(n/3):int((2*n/3))]=1
    x=numpy.arange(n)*dx
else:
    x=numpy.arange(n);x=x-0.5*n
    rho=numpy.exp(-0.5*(x/20)**2)




plt.ion()
plt.clf()
#plt.axis([0,n,0,1.1])
plt.plot(x,rho)
plt.draw()
plt.savefig('advect_initial_conditions.png')

for step in range(0,50):
    #time.sleep(0.2)
    plt.pause(0.05)
    #take the difference in densities
    drho=rho[1:]-rho[0:-1]
    #update density.  We haven't said what happens at
    #cell 0 (since cell -1 doesn't exist), ignore for now
    rho[1:]=rho[1:]-v*dt/dx*drho

    #periodic boundary conditions
    rho[0]=rho[-1] #for periodic 
    

    plt.clf()
    #plt.axis([0,n,0,1.1])
    #plotting as a function of time
    plt.plot(x,rho)

    plt.draw()


#how does it behave? How does the total mass behave with time? (10)

# There are stablitlies as the time steps increase, at large 
# timesteps the amplitudes increase and instabilities are greater, but does not explode
# the total mass overtime continues and moves from right to left and since its periodic, 
# starts again until the time has finished 

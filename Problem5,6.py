#Problem 5: Look at hydro1d.py. youll see an assert guaranteed to fail at the end of get bc,
#the boundary condition routine. Why did I do this? (5)

#Code from hydro1d.py

import numpy
from matplotlib import pyplot as plt

class Fluid:
    def __init__(self,npix=200,gamma=5.0/3.0,bc_type='periodic'):
        self.rho=numpy.zeros(npix)
        self.p=numpy.zeros(npix)
        self.v=numpy.zeros(npix)
        self.rhoE=numpy.zeros(npix)
        self.P=numpy.zeros(npix)
        self.gradrho=numpy.zeros(npix)
        self.gradp=numpy.zeros(npix)
        self.gradrhoE=numpy.zeros(npix)
        self.gamma=gamma
        self.bc_type=bc_type
        self.n=npix
        self.dx=1.0/npix

    def ic_bullet(self):
        self.rho[:]=1.0
        self.rhoE[:]=1.0
        self.p[:]=0
        self.p[self.n/2:3*self.n/5]=1.0

    def ic_shock_tube(self):
        #set up classic Sod shock tube problem.
        self.rho[0:self.n/2]=1.0
        self.P[0:self.n/2]=1.0

        self.rho[self.n/2:]=0.125
        self.P[self.n/2:]=0.1
        self.p[:]=0
        #we really need the energy, not the pressure
        self.rhoE=1.0/(self.gamma-1.0)*self.P

    def get_velocity(self):
        #get the velocity, if density is zero, set velocity to be zero
        self.v[:]=0
        ii=self.rho>0
        self.v[ii]=self.p[ii]/self.rho[ii]

    def get_bc(self):
        if self.bc_type=='periodic':
            self.rho[0]=self.rho[-2]
            self.rho[-1]=self.rho[1]
            self.p[0]=self.p[-2]
            self.p[-1]=self.p[1]
            self.rhoE[0]=self.rhoE[-2]
            self.rhoE[-1]=self.rhoE[1]
            return
        if self.bc_type=='smooth':
            self.rho[0]=self.rho[1]
            self.rho[-1]=self.rho[-2]
            self.p[0]=self.p[1]
            self.p[-1]=self.p[-2]
            self.rhoE[0]=self.rhoE[1]
            self.rhoE[-1]=self.rhoE[-2]
            return    
        assert(1==0)  #why did we do this?  Tutorial problem 1

# Problem 5
# A) Assertionn is used to test the code written to ensure that it does what we want it to do.
#    Assertions are usually done in the form of unit testing, where every small part of code 
#    (every method, class,definition, etc) is tested.
#    Assertion or Unit testing is done by defining an expected outcome and then 
#    using it to ensure what we go it correct. 
#    If the code and the assert have the same value then the assert will fail, 
#    hence there will be an error in the code. 



    def do_eos(self):
        #self.get_velocity() #let's assume velocity has already been calculated
        thermal=self.rhoE-self.rho*0.5*self.v**2
        self.P=(self.gamma-1.0)*thermal
#Problem 5:
# B)    The derivatives are calculated in the definition underneath called get_derivs ()

    def get_derivs(self):
        frho=self.p
        fp=self.p*self.v #+self.P, but we'll handle pressure slightly differently
        fE=self.v*self.rhoE+self.v*self.P
        
        drho=0*self.rho
        dp=0*self.p
        drhoE=0*self.rhoE
        for ii in range(1,self.n-1):            
            if self.v[ii]>0:
                drho[ii+1]+=frho[ii]
                drho[ii]-=frho[ii]
                dp[ii+1]+=fp[ii]
                dp[ii]-=fp[ii]
                drhoE[ii+1]+=fE[ii]
                drhoE[ii]-=fE[ii]
            if self.v[ii]<0:
                drho[ii-1]+=frho[ii]
                drho[ii]-=frho[ii]
                dp[ii-1]+=fp[ii]
                dp[ii]-=fp[ii]
                drhoE[ii-1]+=fE[ii]
                drhoE[ii]-=fE[ii]
       
       #Problem 6
        #Why is there a factor of 1/2 in the pressure gradient? Tutorial problem 2
        # The pressure gradient has a factor of 1/2 at it is trying to find the gradient of P between two points. 
        # The gradp is 1/2 *P (range starting at the 2 position) - P(starting at the -2 position)
        #Since P (at 2) and P(at-2) have some points overlapping, it is best to half it.

        gradP=0.5*(self.P[2:]-self.P[0:-2])
        dp[1:-1]-=gradP
        self.gradrho=drho
        self.gradp=dp
        self.gradrhoE=drhoE
    def get_timestep(self,dt=0.1):

        #tutorial problem 3 - what should this timestep actually be from CFL?

        
        return 0.5*dt  #*self.dx
    def take_step(self):
        #before we can do anything else, get the boundary gonditions
        self.get_bc()
        #then, get the velocities
        self.get_velocity()
        #now calculate the pressure
        self.do_eos()
        #now we can get the derivatives
        self.get_derivs()
        
        #find out our timestep
        dt=self.get_timestep()
        
        #and update quantities
        self.rho+=self.gradrho*dt
        self.p+=self.gradp*dt
        self.rhoE+=self.gradrhoE*dt

def pp(x):
    plt.clf()
    plt.plot(x)
    plt.show()
if __name__=='__main__':
    plt.ion()
    fluid=Fluid(npix=500,bc_type='smooth')

    #fluid.ic_bullet()
    plt.plot(fluid.p)

    fluid.ic_shock_tube()
    plt.plot(fluid.rho)
    plt.draw()
    fluid.take_step()


    plt.clf()
    h,=plt.plot(fluid.rho)
    plt.axis([0,len(fluid.rho),0,1.2])
    plt.pause(0.01)

    for i in range(0,3000):
        fluid.take_step()
        #plt.clf()
        #plt.plot(fluid.rho)
        #plt.axis([0,len(fluid.rho),0,1.2])
        h.set_ydata(fluid.rho)
        plt.pause(0.001)

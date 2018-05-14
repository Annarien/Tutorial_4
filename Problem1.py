#Problem 1: Write linear least-squares code to t sines and cosines to evenly sampled data.
#Pick the sines and cosines to have integer numbers of periods, so you pick 100 numbers, should
#have sin = cos(2n(0 : 50)=100). Compare your t parameters to the FFT of the data. Note - sin
#should go from 1 to 49 instead of 0 to 50. Why is this? (10)

import numpy
import matplotlib 
from matplotlib import pyplot as pyplot
#using SciPy to optimise and to do linear least squares. See link below:
# https://python4mpia.github.io/fitting_data/least-squares-fitting.html
import scipy.optimize as optimization

def __init__(self,n,t,cosn,sinn):
    self.n=n
    self.t=t
    self.cosn=cosn
    self.sinn=sinn

def getCosn(n,t):
    for i in t:
        cosn=numpy.zeros([t.siza,npoly])
        cosn[:,0]=numpy.cos(n)
    if npoly>1:
        cosn[n:,1]=t
    for i in range(1,npoly-1):
        cosn[:,i+1]=((2.0*i+1)*t*cosn[:,i]-i*cosn[:,i-1])/(i+1.0)
        cosn=numpy.matrix(cons)

    return cosn
    
def getSinn(n,t):
    for i in t:
        sinn=numpy.zeros([t.siza,npoly])
        sinn[:,0]=numpy.sin(n)
    if npoly>1:
        sinn[n:,1]=t
    for i in range(1,npoly-1):
        sinnn[:,i+1]=((2.0*i+1)*t*sinn[:,i]-i*csinn[:,i-1])/(i+1.0)
        sinn=numpy.matrix(sinn)

    return sinn

def getCosLeastSquare(cosn,t):
    cosls=optimization.leastsq(cosn,t)
    
    return cosls

def getSinLeastSquare(sinn,t):
    sinls=optimization.leastsq(sinn,t)
    
    return sinls


if __name__=='main':
    n=100
    start=0
    end=0
    t=numpy.linspace(start,stop,100)

    cosn=getCosn(n,t)
    sinn=getSinn(n,t)

    cosls1=getCosLeastSquare(cosn,t)
    print (str(cosls1)
    #sinls1=getSinLeastSquare(sinn,t)
    #print (str(sinls1))


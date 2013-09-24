import matplotlib.pyplot as plt
from numpy import ones, linspace
#from newtonPoly import *
import time

x=linspace(-1,1,100)
y=1.0/(1.0+25*(x**2))
for i in range(7,16,2):
    fig = plt.figure()
    xequal=linspace(-1,1,i)
    yequal=1.0/(1.0+25*(xequal**2))
    #a=coeffts(xequal,yequal)
    #pval=evalPoly(a,xequal,x)
    #plt.plot(x,y,x,pval,xequal,yequal,'*')
    plt.plot(x,y,'*')
    plt.show(block=False)
    time.sleep(3)

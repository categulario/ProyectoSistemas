from pylab import *
from numpy import ones
from newtonPoly import *

x=linspace(-1,1,100)
y=1.0/(1.0+25*(x**2))
for i in range(7,16,2):
    xequal=linspace(-1,1,i)
    yequal=1.0/(1.0+25*(xequal**2))
    a=coeffts(xequal,yequal)
    pval=evalPoly(a,xequal,yequal)
    plot(x,y,x,pval,xequal,yequal,'*')
    show()
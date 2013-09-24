'''% Script File: ShowPWL1
% Convergence of the piecewise linear interpolant to
% humps(x) on [0,3]
'''
from numpy import linspace
from pwLEval import*
from pylab import *
from pwL import *
def humps(x):
     y=(1.0/((x-.3)**2)+.01)+((1.0/(  ((x-.9)**2) +.04)))-6
     return y


z = linspace(0,3,200)
fvals = humps(z);
for n in [5, 10, 25, 50]:
   figure()
   x = linspace(0,3,n)
   y = humps(x);
   [a,b] = pwL(x,y);
   Lvals = pwLEval(a,b,x,z);
   plot(z,Lvals,z,fvals,'--',x,y,'o');
   title('Interpolation of humps(x) with pwL, n = %2.0f'%n)

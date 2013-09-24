# -*- coding:utf-8 -*-
from numpy import array

def diff (x):
     """
     If X is a vector of length N, `diff (X)' is the vector of first
     differences  X(2) - X(1), ..., X(n) - X(n-1).
     """
     return array([x[n]-x[n-1] for n in xrange(2, len(x))])


def pwL(x,y):
     '''
     % [a,b] = pwL(x,y)
     %
     % Generates the piecewise linear interpolant of the data specified by the
     % column n-vectors x and y. It is assumed that x(1) < x(2) < ... < x(n).
     %
     % a and b are column (n-1)-vectors with the property that for i=1:n-1, the
     % line L(z) = a(i) + b(i)z passes though the points (x(i),y(i)) and (x(i+1),y(i+1)).
     '''
     n = len(x)
     a = y[:n-2]
     b = diff(y) / diff(x)
     return a, b
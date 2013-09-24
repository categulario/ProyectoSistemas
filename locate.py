# -*- coding:utf-8 -*-
import math

def Locate(x,z, *args):
    '''
    % i = Locate(x,z,g)
    % Locates z in a partition x.
    %
    % x is column n-vector with x(1) < x(2) <...<x(n) and
    % z is a scalar with x(1) <= z <= x(n).
    % g (1<=g<=n-1) is an optional input parameter
    %
    % i is an integer such that x(i) <= z <= x(i+1). Before the general
    % search for i begins, the value i=g is tried.
    '''
    if len(args) == 1:
        g = args[0]
        # Try the initial guess.
        if (x[g]<=z) & (z<=x[g+1]):
            return g

    n = len(x)
    if z==x[n-1]:
        i = n-1
    else:
        # Binary Search
        Left = 1
        Right = n
        while Right > Left+1:
            # x(Left) <= z <= x(Right)
            mid = math.floor((Left+Right)/2)
            if z < x[mid]:
                Right = mid
            else:
                Left = mid
        i = Left
    return i
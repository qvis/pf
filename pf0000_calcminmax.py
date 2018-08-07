#!/usr/bin/env python

import netCDF4 as nc
import numpy as np
import os
import sys


def calc_minmax ( args1, args2 ):
    xx=np.array(args1.split(":"))
    x=xx.astype(np.float)

    yy=np.array(args2.split(":"))
    y=yy.astype(np.float)
    
    minval=np.amin(x)
    maxval=np.amax(y)
    print str(minval)+':'+str(maxval)
    return

def get_ncdata ( fnc, var ):
    data=nc.Dataset( fnc )
    d=np.array(data.variables[var][:], dtype=float)
    b=d.ravel()
    str=""
    for i in range(len(b)):
        str+=`b[i]`+":"
    str=str[:-1]

    print str


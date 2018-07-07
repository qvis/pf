#!/usr/bin/env python
'''
To call python functions from bash with input variable, add this to shell script:
[variable]=`python -c "import [python file]; [python file].[python function]( '""$[input var1]""','""$[input var2]""',...)"`

example:
x=`python -c "import pf0003_nccalc; pf0003_nccalc.nccalc_min( '""$fncout""','""$uvar""')"`
'''
import netCDF4 as nc
import numpy as np
import os 


def nccalc_min(fin,fvar):
    #todo: get min value
    data = nc.Dataset(fin)
    vardata = data.variables[fvar][:]
    
    masked_array = np.ma.array (vardata, mask=np.isnan(vardata))
    print np.amin(masked_array)
    return

def nccalc_max(fin,fvar):
    #todo: get max value
    
    data = nc.Dataset(fin)
    vardata = data.variables[fvar][:]
    
    masked_array = np.ma.array (vardata, mask=np.isnan(vardata))
    print np.amax(masked_array)
    return


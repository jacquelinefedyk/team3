from numpy import *
from math import *
import pandas as pd

def rd_file(filedir,filename,threshold):
    no_fl  = len(filename)
    path_f = filedir + filename[0]
    ptemp  = pd.read_csv(path_f, '\s+', header=None,skiprows=1)
    time   = ptemp[0].values
    expec  = zeros((no_fl,len(time)))
    for i in range(no_fl):
        name = filedir + filename[i]
        ptemp = pd.read_csv(name, '\s+', header=None,skiprows=7)
        expec[i] = ptemp[1].values

    useless=(filename < threshold).all(axis=1)

    for i in range(len(useless)):
        if useless[i]==True:
            filename=np.delete(filename,i)

    return  expec

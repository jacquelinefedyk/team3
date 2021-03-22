import array
import numpy as np
from scipy.fftpack import fft, fftshift
from numpy import *

def num_crl(filedir,filename,threshold):
    "Add explanation here"
    dat_nst=dat_nst.T

    t2_wf=len(dat_nst[:,0])
    t_wf=int(t2_wf/2)
    p_wf=len(dat_nst[0])

    comp_vc=zeros([t_wf,p_wf],dtype=np.complex_)
    for t in range(t_wf):
        comp_vc[t]=dat_nst[t*2] + dat_nst[1+t*2]*1j

    ac_fc1=zeros([p_wf,t_wf+1],dtype=np.complex_)
    for n in range(p_wf):
        ac_fc1[n]=np.sum(comp_vc[:,0]*np.conjugate(comp_vc[:,n]))
        
    return

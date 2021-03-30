from scipy.fftpack import fft, fftshift
from numpy import *

def num_crl(wf_n):
    """Function computes the autocorrelation function from given vectors
    and the Discrete Fourier transform

    Args:
        wf_n(numpy array, complex): Wave function over time

    Returns:
        numpy array, complex: The autocorrelataion function over time.
        numpy array, complex: The Discrete Fourier Transformation function over\
        frequency
    """
    dat_nst=dat_nst.T
    #setting up the time vector
    t2_wf=len(dat_nst[:,0])
    
    t_wf=int(t2_wf/2)
    p_wf=len(dat_nst[0])

    comp_vc=zeros([t_wf,p_wf],dtype=np.complex_)
    for t in range(t_wf):
        comp_vc[t]=dat_nst[t*2] + dat_nst[1+t*2]*1j

    ac_file=zeros([p_wf,t_wf+1],dtype=np.complex_)
    for n in range(p_wf):
        ac_file[n]=np.sum(comp_vc[:,0]*np.conjugate(comp_vc[:,n]))

    FT_file = fft.fft(ac_file)
    FT_t  = fft.fftfreq(len(ac_file))
    return ac_file , FT_file , FT_t

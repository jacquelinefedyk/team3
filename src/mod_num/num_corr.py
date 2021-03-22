import array
import numpy as np
from scipy.fftpack import fft, fftshift
from numpy import *

def euclidean_distance(list_ref, list_comp, vectors):
    """Calculates the Euclidean distance (L2 norm) between pairs of vectors.
    Args:
    list_ref (integer list): A list with the indices of the reference vectors.
    list_comp (integer list): A list with the indices of the vectors to\
    compare to.
    data (numpy array): The data object.
    Returns:
    numpy array: The Euclidean distance (L2 norm) for comparison vs. reference\
    vectors."""
    distances = np.zeros(len(list_ref))
    for i in range(len(list_ref)):
        distances[i] = np.linalg.norm(vectors[list_comp[i]] - vectors[list_ref[i]])
    return distances

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

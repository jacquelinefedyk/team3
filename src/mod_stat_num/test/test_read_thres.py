import numpy as np
import pandas as pd
from mymodules import read_thres as thrs

def test_thr():
    path_f1 ='/home/gomezj/PhD/2021_Art_SSD/team3/src/mod_stat_num/test/test_file.csv'
    pt1 = pd.read_csv(path_f1, r'\s+', header=None,skiprows=1)
    fl1 = pt1[0].values
    no_fl1 = len(fl1)

    cl1 = open(path_f1, "r").readlines()
    line1 = cl1[1].split()
    no_cl1 = len(line1)

    fl_try = np.zeros((no_cl1,no_fl1))
    data = np.zeros((no_cl1,no_fl1))

    for i in range(no_cl1):
        pt2 = pd.read_csv(path_f1, r'\s+', header=None,skiprows=1)
        fl_try[i] = pt2[i].values

    filen = 'test_file.csv'
    filed = '/home/gomezj/PhD/2021_Art_SSD/team3/src/mod_stat_num/test/'
    thrs= '1.0E-4'
    data = thrs.ths_def(fl_try, thrs ,filed,filen)
    dat_nw = fl_try.drop(columns=["norm", "<x>", "<y>"])
    assert data.equals(dat_nw)

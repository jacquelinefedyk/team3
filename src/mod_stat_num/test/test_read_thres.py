import numpy as np
import pandas as pd
import read_thres as thrs

def test_thr():
    path_f1 ='./test/test_file.csv'
    pt1 = pd.read_csv(path_f1, r'\s+', header=None,skiprows=1)
    fl1 = pt1[0].values
    no_fl1 = len(fl1)

    cl1 = open(path_f1, "r").readlines()
    line1 = cl1[1].split()
    no_cl1 = len(line1)

    fl_try = np.zeros((no_cl1,no_fl1))
    for i in range(no_cl1):
        pt2 = pd.read_csv(path_f1, r'\s+', header=None,skiprows=1)
        fl_try[i] = pt2[i].values

    data, x = thrs.ths_def(fl_try, threshd=1.E-4)
    dat_nw = fl_try.drop(columns=["norm", "<x>", "<y>"])
    x_nw = dat_nw.columns.values
    assert len(x) == len(x_nw)
    assert np.array_equal(x, x_nw)
    assert data.equals(dat_nw)

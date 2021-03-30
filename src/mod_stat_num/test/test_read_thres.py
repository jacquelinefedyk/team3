import numpy as np
import pandas as pd
import read_thres as thrs


def check_thr():
    file1 = pd.read_csv(name_p, r'\s+', header=None,skiprows=1)
    fl_try = file1[0].values
    return fl_try


def test_thr(check_thr):
    data, x = thrs.ths_def(check_thr, threshd=1.E-4)
    dat_nw = check_thr.drop(columns=["norm", "<x>", "<y>"])
    x_nw = dat_nw.columns.values
    assert len(x) == len(x_nw)
    assert np.array_equal(x, x_nw)
    assert data.equals(dat_nw)

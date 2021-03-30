import numpy as np
import panda as pd
import read_thres as thrs


def check_thr(name_p='./test/test_file.csv'):
    file1 = pd.read_csv(name_p, r'\s+', header=None,skiprows=1)
    fl_try = file1[0].values
    return fl_try


def test_thr(fl_try):
    data, x = thrs.ths_def(fl_try, threshd=1.E-4)
    dat_nw = check_thr.drop(columns=["norm", "<x>", "<y>"])
    x_nw = dat_nw.columns.values
    assert len(x) == len(x_nw)
    assert np.array_equal(x, x_nw)
    assert data.equals(dat_nw)

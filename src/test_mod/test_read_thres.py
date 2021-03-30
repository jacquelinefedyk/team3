import pytest
import numpy as np
import read_thres as thrs

def test_thr(check_thr):
    data, x = thrs.ths_def(check_thr, threshd=1.E-5)
    dat_nw = check_thr.drop(columns=["norm", "<x>", "<y>"])
    x_nw = dat_nw.columns.values
    assert len(x) == len(x_ew)
    assert np.array_equal(x, x_nw)
    assert data.equals(dat_nw)

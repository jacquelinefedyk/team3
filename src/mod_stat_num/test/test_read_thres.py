import numpy as np
import read_thres as thrs


def chech_thr():
    fil = build_df('./test/test_file.csv')
    infmt = fil.read_df()
    return infmt


def test_thr(check_thr):
    data, x = thrs.ths_def(check_thr, threshd=1.E-4)
    dat_nw = check_thr.drop(columns=["norm", "<x>", "<y>"])
    x_nw = dat_nw.columns.values
    assert len(x) == len(x_nw)
    assert np.array_equal(x, x_nw)
    assert data.equals(dat_nw)

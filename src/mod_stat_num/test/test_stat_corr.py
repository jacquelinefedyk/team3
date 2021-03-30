import pytest
import pandas as pd
import numpy as np
import stat_corr as sc


class build_df:
    def __init__(self, name):
        self.dfnamepath = name

    def read_df(self):
        self.data = pd.read_csv(self.dfnamepath, r'\s+')
        return self.data


@pytest.fixture(scope='module')
def get_df():
    obj = build_df('./test/test_df.csv')
    data = obj.read_df()
    return data




def test_corr_matrix(get_df, xval_col_name):
    corrmat = sc.corr_matrix(get_df, xval_col_name)
    corrmat = corrmat.dropna().round(decimals=6)
    d = [0.832628, 0.228204, 0.136257]
    ind = pd.MultiIndex.from_tuples([
                                   ('norm', '<H>'),
                                   ('<z>', '<H>'),
                                   ('norm', '<z>')])
    ser_new = pd.Series(data=d, index=ind)
    assert corrmat.equals(ser_new)

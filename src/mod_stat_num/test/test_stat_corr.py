import pytest
import pandas as pd
import numpy as np
from mymodules import stat_corr as sc


class build_df:
    def __init__(self, name):
        self.dfnamepath = name

    def read_df(self):
        self.data = pd.read_table(self.dfnamepath,
                                  header=None,delim_whitespace=True,skiprows=2,
                                  names=['time','MO1','MO2','MO3',
                                         'MO4','MO5','MO6','MO7',
                                         'MO8','MO9','MO10','MO11',
                                         'MO12','MO13','MO14','MO15',
                                         'MO16','MO17','MO18','MO19',
                                         'MO20','MO21','MO22','MO23',
                                         'MO24','MO25','MO26','MO27',
                                         'MO28','MO29','MO30','MO31',
                                         'MO32','MO33','MO34','MO35',
                                         'MO36','MO37','MO38'])

        # discard all columns with variance below a set threshold
        threshold = 0.005
        index = np.linspace(1,38,38)
        tsteps = len(self.data['time'])
        for i in range(len(index)):
            npop_string = self.data[['MO'+str(int(index[i]))]].to_numpy()
            npop = npop_string.astype(float) #array of floats
            for t in range(tsteps):
                if npop[t] < threshold:
                   self.data = self.data.drop(columns='MO'+str(int(index[i])))
                   break
                else:
                   continue
        return self.data


@pytest.fixture(scope='module')
def get_df():
    obj = build_df('/tmpa/jacqueline/team3/data/npop.t')
    data = obj.read_df()
    return data




def test_corr_matrix(get_df):
    corrmat = sc.corr_matrix(get_df, 'time')
    d = [-0.962895, -0.951326, 0.923856, -0.920366, 0.914762, -0.911385,
         0.906915, -0.904690, -0.816567, -0.812710, -0.775375, 0.769862,
         0.759848, 0.713498, 0.689998, -0.619925, -0.619088, 0.618369,
         0.555122, -0.544947, -0.410215]
    ser_new = pd.Series(data=d)
    assert corrmat.equals(ser_new)

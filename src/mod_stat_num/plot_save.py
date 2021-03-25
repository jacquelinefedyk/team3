import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_save(xval_col_name,dataframe,path):
    plot = sns.pairplot(dataframe,x_vars=xval_col_name,height = 5)
    save = plt.savefig(os.path.join(path,str(dataframe)+'.png'))
    return plot, save

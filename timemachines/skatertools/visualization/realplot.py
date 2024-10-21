
from timemachines.skatertools.data.real import hospital_with_exog
from timemachines.skatertools.visualization.priorplot import prior_plot_exogenous
import numpy as np


def hospital_prior_plot_exogenous(f, k=None, x0=np.nan, n=150, n_plot=25):
    # Won't plot if matplotlib is not installed
    y, a = hospital_with_exog(k=k, n=450, offset=True)
    err = prior_plot_exogenous(f=f,k=k,y=y,a=a, n=450, n_plot=50)






import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st

def glResidual(_model):
    reg=smf.ols(_model.eval(),_model.getDataFrameModel())
    resul=reg.fit()
    glresiduales=resul.df_model
    return glresiduales


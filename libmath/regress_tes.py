import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st

def fit(_model):
    reg=smf.ols(_model.eval(),_model.getDataFrameModel())
    resul=reg.fit()
    return resul

def glResidual(_model):
    resul=fit(_model)
    glresiduales=resul.df_model
    return glresiduales

def glModel(_model):
    resul=fit(_model) 
    glmodelo=resul.df_resid
    return glmodelo

def aic(_model):
    resul=fit(_model)
    aic=round((resul.aic),4)
    return aic

def bic(_model):
    resul=fit(_model)
    bic=round((resul.bic),4)
    return bic

def logLikeliHead(_model):
    resul=fit(_model)
    like=round((resul.llf),4)
    return like

def RCuad(_model):
    resul=fit(_model)
    rcua=round((resul.rsquared),4)
    return rcua

def RCuadAdjust(_model):
    resul=fit(_model)
    rcuadj=round((resul.rsquared_adj),4)
    return rcuadj
    
def FStadistic(_model):
    resul=fit(_model)
    ffr=round((resul.fvalue),4)
    return ffr

def PValue(_model):
    resul=fit(_model)
    pvfisher=round((resul.f_pvalue),4)
    return pvfisher

def MSEModel(_model):
    resul=fit(_model)
    msemodelo=round((resul.mse_model),4)
    return msemodelo

def MSEResidual(_model):
    resul=fit(_model)
    mseresid=round((resul.mse_resid),4)
    return mseresid
    
def MSETotal(_model):
    resul=fit(_model)
    msetotal=round((resul.mse_total),4)
    return msetotal

def RMSEModel(_model):
    msetotal = MSETotal(_model)
    rmse=round(np.sqrt(msetotal),4)
    return rmse

def coefficientVariablesModel(_model):
    resul=fit(_model)
    coeff=list(resul.params)
    return coeff

def sterrVariablesModel(_model):
    resul=fit(_model)
    sterr=list(resul.bse)
    return sterr

def tcVariablesModel(_model):
    resul=fit(_model)
    tc=list(resul.tvalues)
    return tc

def pvCoefficientVariablesModel(_model):
    resul=fit(_model)
    pvcoeff=list(resul.pvalues)
    return pvcoeff 
    
    
    
    
    


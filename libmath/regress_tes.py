import os

import pandas as pd

import numpy as np

from scipy import stats as st
from scipy.stats import chisquare, kurtosis, skew, shapiro, kstest, stats, anderson, normaltest

from statsmodels.stats.diagnostic import lilliefors, het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import durbin_watson

import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.diagnostic as dg
import statsmodels.stats.api as sms

# --- Inicio de metodos comunes y utilizados en otros ---

def fitModel(_model):
    reg=smf.ols(_model.eval(),_model.getDataFrameModel())
    resul=reg.fit()
    return resul

def residualModel(_model):
    resul=fitModel(_model)
    residual=(resul.resid)
    return residual

def residualSTModel(_model):
    resul = fitModel(_model)
    rst=resul.outlier_test()
    residualesST=rst.student_resid
    return residualesST

# --- Fin de metodos comunes y utilizados en otros ---

def glResidual(_model):
    resul=fitModel(_model)
    glresiduales=resul.df_model
    return glresiduales

def glModel(_model):
    resul=fitModel(_model) 
    glmodelo=resul.df_resid
    return glmodelo

def aic(_model):
    resul=fitModel(_model)
    aic=round((resul.aic),4)
    return aic

def bic(_model):
    resul=fitModel(_model)
    bic=round((resul.bic),4)
    return bic

def logLikeliHead(_model):
    resul=fitModel(_model)
    like=round((resul.llf),4)
    return like

def RCuad(_model):
    resul=fitModel(_model)
    rcua=round((resul.rsquared),4)
    return rcua

def RCuadAdjust(_model):
    resul=fitModel(_model)
    rcuadj=round((resul.rsquared_adj),4)
    return rcuadj
    
def FStadistic(_model):
    resul=fitModel(_model)
    ffr=round((resul.fvalue),4)
    return ffr

def PValue(_model):
    resul=fitModel(_model)
    pvfisher=round((resul.f_pvalue),4)
    return pvfisher

def MSEModel(_model):
    resul=fitModel(_model)
    msemodelo=round((resul.mse_model),4)
    return msemodelo

def MSEResidual(_model):
    resul=fitModel(_model)
    mseresid=round((resul.mse_resid),4)
    return mseresid
    
def MSETotal(_model):
    resul=fitModel(_model)
    msetotal=round((resul.mse_total),4)
    return msetotal

def RMSEModel(_model):
    msetotal = MSETotal(_model)
    rmse=round(np.sqrt(msetotal),4)
    return rmse

def coefficientVariablesModel(_model):
    resul=fitModel(_model)
    coeff=list(resul.params)
    return coeff

def sterrVariablesModel(_model):
    resul=fitModel(_model)
    sterr=list(resul.bse)
    return sterr

def tcVariablesModel(_model):
    resul=fitModel(_model)
    tc=list(resul.tvalues)
    return tc

def pvCoefficientVariablesModel(_model):
    resul=fitModel(_model)
    pvcoeff=list(resul.pvalues)
    return pvcoeff

def lowerLimitVariablesModel(_model):
    resul=fitModel(_model)
    interconf=resul.conf_int(_model.getIntervalConfidence(),)
    lowerLimit=list(interconf[0]) 
    return lowerLimit
    
def upperLimitVariablesModel(_model):
    resul=fitModel(_model)
    interconf=resul.conf_int(_model.getIntervalConfidence(),)
    upperLimit=list(interconf[1])
    return upperLimit 

# ---- Inicio  pruebas  a los residuales sin escalamientos RWS----

def coefficientCurtosisRWS(_model):
    residuales=residualModel(_model)
    ku=round(kurtosis(residuales),4)
    return ku

def coefficientAsymetryRWS(_model):
    residuales=residualModel(_model)
    sk=round(skew(residuales),4)
    return sk

def testLillieforsRWS(_model):
    residuales=residualModel(_model)
    Li=lilliefors(residuales)
    D=round(Li[0],4)
    return D

def testLillieforsPValueRWS(_model):
    residuales=residualModel(_model)
    Li=lilliefors(residuales)
    PvalorLi=round(Li[1],4)
    return PvalorLi

def testShapiroWilkRWS(_model):
    residuales=residualModel(_model)
    shap = shapiro(residuales)
    W = round(shap[0],4)
    return W
    
def testShapiroWilkPValueRWS(_model):
    residuales=residualModel(_model)
    shap = shapiro(residuales)
    PvalorW=round(shap[1],4)
    return PvalorW

#TODO Duda paramaetro norm
def testKolmogorovSmirnovRWS(_model):
    residuales=residualModel(_model)
    ks=kstest(residuales,cdf="norm")
    KS=round(ks[0],4)
    return KS

def testKolmogorovSmirnovPValueRWS(_model):
    residuales=residualModel(_model)
    ks=kstest(residuales,cdf="norm")
    Pvalorks=round(ks[1],4)
    return Pvalorks

def testJarqueBeraRWS(_model):
    residuales=residualModel(_model)
    jarbera=stats.jarque_bera(residuales)
    JB=round(jarbera[0],4)
    return JB

def testJarqueBeraPValueRWS(_model):
    residuales=residualModel(_model)
    jarbera=stats.jarque_bera(residuales)
    PvalorJB=round(jarbera[1],4)
    return PvalorJB

def testAndersonDarlingRWS(_model):
    residuales=residualModel(_model)
    ander=anderson(residuales)
    AN=round(ander[0],4)
    return AN

def testAndersonDarlingPValueRWS(_model):
    residuales=residualModel(_model)
    ander=anderson(residuales)
    vc=(ander[1])
    VCand=round(vc[2],4)
    return VCand

def testKCuadDAngostinoRWS(_model):
    residuales=residualModel(_model)
    dan=stat, p = normaltest(residuales)
    DA=round(dan[0],4)
    return DA

def testKCuadDAngostinoPValueRWS(_model):
    residuales=residualModel(_model)
    dan=stat, p = normaltest(residuales)
    PvalorDA=round(dan[1],4)
    return PvalorDA

def testChiSquareRWS(_model):
    residuales=residualModel(_model)
    chi=chisquare(residuales)
    CHI=round(chi[0],4)
    return CHI

def testChiSquarePValueRWS(_model):
    residuales=residualModel(_model)
    chi=chisquare(residuales)
    PvalorCHI=round(chi[1],4)
    return PvalorCHI
    
# ---- Fin  pruebas  a los residuales sin escalamientos  RWS----


# ---- Inicio  pruebas  a los residuales estudentizados RE ----

def coefficientCurtosisRE(_model):
    residualesST=residualSTModel(_model) 
    kuST=round(kurtosis(residualesST),4)
    return kuST

def coefficientAsymetryRE(_model):
    residualesST=residualSTModel(_model)
    skST=round(skew(residualesST),4)
    return skST

def testLillieforsRE(_model):
    residualesST=residualSTModel(_model)
    LiST=lilliefors(residualesST)
    DST=round(LiST[0],4)
    return DST

def testLillieforsPValueRE(_model):
    residualesST=residualSTModel(_model)
    LiST=lilliefors(residualesST)
    PvalorLiST=round(LiST[1],4)
    return PvalorLiST

def testShapiroWilkRE(_model):
    residualesST=residualSTModel(_model)
    shapST= shapiro(residualesST)
    WST=round(shapST[0],4)
    return WST
    
def testShapiroWilkPValueRE(_model):
    residualesST=residualSTModel(_model)
    shapST= shapiro(residualesST)
    PvalorWST=round(shapST[1],4)
    return PvalorWST

def testKolmogorovSmirnovRE(_model):
    residualesST=residualSTModel(_model)
    ksST=stats.kstest(residualesST,cdf="norm")
    KSST=round(ksST[0],4)
    return KSST

def testKolmogorovSmirnovPValueRE(_model):
    residualesST=residualSTModel(_model)
    ksST=stats.kstest(residualesST,cdf="norm")
    PvalorksST=round(ksST[1],4)
    return PvalorksST

def testJarqueBeraRE(_model):
    residualesST=residualSTModel(_model)
    jarberaST=stats.jarque_bera(residualesST)
    JBST=round(jarberaST[0],4)
    return JBST

def testJarqueBeraPValueRE(_model):
    residualesST=residualSTModel(_model)
    jarberaST=stats.jarque_bera(residualesST)
    PvalorJBST=round(jarberaST[1],4)
    return PvalorJBST

def testAndersonDarlingRE(_model):
    residualesST=residualSTModel(_model)
    anderST=anderson(residualesST)
    ANST=round(anderST[0],4)
    return ANST

def testAndersonDarlingPValueRE(_model):
    residualesST=residualSTModel(_model)
    anderST=anderson(residualesST)
    vcST=(anderST[1])
    VCandST=round(vcST[2],4)
    return VCandST

#TODO aqui segun el informe en hoja es el mismo proceder que AndersonDarling
def testKCuadDAngostinoRE(_model):
    residualesST=residualSTModel(_model)
    danST=stat, p = normaltest(residualesST)
    DAST=round(danST[0],4)
    return DAST

def testKCuadDAngostinoPValueRE(_model):
    residualesST=residualSTModel(_model)
    danST=stat, p = normaltest(residualesST)
    PvalorDAST=round(danST[1],4)
    return PvalorDAST

def testChiSquareRE(_model):
    residualesST=residualSTModel(_model)
    chiST=stats.chisquare(residualesST)
    CHIST=round(chiST[0],4)
    return CHIST

def testChiSquarePValueRE(_model):
    residualesST=residualSTModel(_model)
    chiST=stats.chisquare(residualesST)
    PvalorCHIST=round(chiST[1],4)
    return PvalorCHIST
      
# ---- Fin  pruebas  a los residuales estudentizados RE ----
    
# ---- Inicio  pruebas  de homecedasticidad de los residuales ---- 

def testBreushPagan(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    breushp = sms.het_breuschpagan(residuales, resul.model.exog)
    BP=round(breushp [0],4)
    return BP

def testBreushPaganPValue(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    breushp = sms.het_breuschpagan(residuales, resul.model.exog)
    PvalorBP=round(breushp [1],4)
    return PvalorBP

def testGoldfeldQuandt(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    golqua = sms.het_goldfeldquandt(residuales,resul.model.exog)
    GQ=round(golqua[0],4)
    return GQ
    
def testGoldfeldQuandtPValue(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    golqua = sms.het_goldfeldquandt(residuales,resul.model.exog)
    PvalorGQ=round(golqua[1],4)
    return PvalorGQ

def testWhiteLH(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    white=het_white(residuales,resul.model.exog)
    LMw=round(white[0],4)
    return LMw

def testWhiteLHPValue(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    white=het_white(residuales,resul.model.exog)
    PvalorLMw=round(white[1],4)
    return PvalorLMw

def testWhiteFW(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    white=het_white(residuales,resul.model.exog)
    Fw=round(white[2],4)
    return Fw

def testWhiteFWPValue(_model):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    white=het_white(residuales,resul.model.exog)
    PvalorFw=round(white[3],4)
    return PvalorFw


# ---- Fin  pruebas  de homecedasticidad de los residuales  ---- 

# ---- Inicio  pruebas  de indepencias de residuales ---- 

def testDurbinWatson(_model):
    residuales = residualModel(_model)
    durbinwat=durbin_watson(residuales)
    DW=round(durbinwat,4)
    return DW


def testBreushGGodfrey(_model):
    resul = fitModel(_model)
    bregod=dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
    BG=round(bregod[0],4)
    return BG 

def testBreushGGodfreyPValue(_model):
    resul = fitModel(_model)
    bregod=dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
    PvalorBG=round(bregod[1],4)
    return PvalorBG 

# ---- Fin  pruebas  de independencias de residuales ----   
    
# ---- Inicio analisis de multicolinialidad ----


def analysisMultiColinialidad(_model):
    X_constant=sm.add_constant(_model.getDataFrameModel())
    vif = [variance_inflation_factor(X_constant.values, i) for i in range(X_constant.shape[1])]
    return vif
      

# ---- Fin analisis de multicolinialidad ---- 

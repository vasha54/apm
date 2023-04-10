import os

import pandas as pd

import numpy as np


from scipy import stats as st
from scipy.stats import chisquare, kurtosis, skew, shapiro, kstest, stats, anderson, normaltest, norm

import scipy.stats

from statsmodels.stats.diagnostic import lilliefors, het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import durbin_watson
from statsmodels.nonparametric.smoothers_lowess import lowess

import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.diagnostic as dg
import statsmodels.stats.api as sms



from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.model_selection import cross_val_score, cross_val_predict

from exceptions.exceptions import NotFoundParameterExtraException, EstadigrafoFisherCalFOException, RelationFOFTException, SumsNeighborsException, VariableNotFoundDataFrame

# --- Inicio de metodos comunes y utilizados en otros ---

cvar = lambda x: np. std (x, ddof = 1 ) / np. mean (x) * 100

def generateBars(_list):
    bars = {}
    _list.sort()
    intervalRange = (max(_list)-min(_list)) / 7
    
    minInterval = min(_list)
    maxInterval = minInterval + intervalRange
    
    for index in range(1,8):
        bars[index] = {}
        bars[index]['minInterval']=minInterval
        bars[index]['maxInterval']=maxInterval
        minInterval = maxInterval
        maxInterval = minInterval + intervalRange
        count = 0
        
        for v in _list:
            if float(minInterval)<= float(v) and float(v) <= float(maxInterval):
                count = count + 1
        bars[index]['frequency'] = count
     
    return bars

def fitModel(_model,**kwargs):
    reg=smf.ols(_model.eval(),_model.getDataFrameModel())
    resul=reg.fit()
    return resul

def residualModel(_model,**kwargs):
    resul=fitModel(_model)
    residual=(resul.resid)
    return residual

def residualSTModel(_model,**kwargs):
    resul = fitModel(_model)
    rst=resul.outlier_test()
    residualesST=rst.student_resid
    return residualesST

def residualCuaModel(_model,**kwargs):
    residuales = residualModel(_model,**kwargs)
    residcua=pow(residuales, 2)
    return residcua

def sslofModel(_model,**kwargs):
    residcua=residualCuaModel(_model,**kwargs)
    sumaVecinos = sumsNeighbors(_model,**kwargs)
    sumresidcua=sum(residcua) 
    SSlof=sumresidcua-sumaVecinos
    return SSlof

def scoreModel(_model,**kwargs):
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        X = _model.getDataFrameVI()
        y = _model.getDataFrameVD()
        clf = LinearRegression()
        model=clf.fit(X, y)
        scores = cross_validate(model, X, y, cv=k,scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
        return scores
    else:
        raise NotFoundParameterExtraException('k','scoreModel')

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

def testWhiteFWPValue(_model,**kwargs):
    resul = fitModel(_model)
    residuales = residualModel(_model)
    white=het_white(residuales,resul.model.exog)
    PvalorFw=round(white[3],4)
    return PvalorFw


# ---- Fin  pruebas  de homecedasticidad de los residuales  ---- 

# ---- Inicio  pruebas  de indepencias de residuales ---- 

def testDurbinWatson(_model,**kwargs):
    residuales = residualModel(_model)
    durbinwat=durbin_watson(residuales)
    DW=round(durbinwat,4)
    return DW


def testBreushGGodfrey(_model,**kwargs):
    resul = fitModel(_model)
    bregod=dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
    BG=round(bregod[0],4)
    return BG 

def testBreushGGodfreyPValue(_model,**kwargs):
    resul = fitModel(_model)
    bregod=dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
    PvalorBG=round(bregod[1],4)
    return PvalorBG 

# ---- Fin  pruebas  de independencias de residuales ----   
    
# ---- Inicio analisis de multicolinialidad ----


def analysisMultiColinialidad(_model,**kwargs):
    X_constant=sm.add_constant(_model.getDataFrameModel())
    vif = [variance_inflation_factor(X_constant.values, i) for i in range(X_constant.shape[1])]
    vif = vif[1:]
    return vif
      

# ---- Fin analisis de multicolinialidad ---- 

def sumsNeighbors(_model,**kwargs):
    sums = 0
    residcua = residualCuaModel(_model)
    namesVarInd= _model.getNamesVariableI()
    dataFrameVI = _model.getDataFrameVI()
    k= dataFrameVI[namesVarInd[0]]
    nameColumn = namesVarInd[0]
    
    for i in range(1,len(namesVarInd)):
        k = k - dataFrameVI[namesVarInd[i]]
        nameColumn = 'Unnamed 0'
    
    
    datos14=pd.DataFrame([k,_model.getDataFrameVD()[_model.getNameVariableD()]])
    datos15 = datos14.transpose()
    listaColA=list(k)
    cCount = len(listaColA)
    storage = []
    for i in range(0,cCount):
        if listaColA.count(listaColA[i]) > 1:
            storage.append(listaColA[i])
    
    if  len(storage) > 0: 
        storageDF = pd.DataFrame(storage)
        valueUnique = storageDF[0].unique()
        uniqueDataFrame = pd.DataFrame(valueUnique)
        
        r =  len(uniqueDataFrame)
        
        sumatoria = []
        
        for i in range(0,r):
            clasS = uniqueDataFrame[0][i]
            
            filter = datos15.loc[datos15[nameColumn] == clasS]
            dFFilter = pd.DataFrame(filter)
            observer = dFFilter.iloc[:,1]
            media = np.mean(observer)
            nobs = len(observer)
            for k in range(0,nobs):
                er = pow(observer-media,2)
                sumaER = sum(er)
            sumatoria.append(sumaER)
        return sum(sumatoria)
    else:
        raise SumsNeighborsException()

def relationRangeValuesAndErrorSTDMean(_model,**kwargs):
    resul = fitModel(_model)
    predicted_value=resul.fittedvalues
    rang=max(predicted_value)-min(predicted_value)
    p=len(_model.getNamesVariableI()) 
    sumaVecinos = sumsNeighbors(_model,**kwargs)
    n = _model.numberMeasurement()
    espg=np.sqrt(p*sumaVecinos/n)
    espgr=round(espg,4)
    rel=rang/espg
    relr=round(rel,4)
    return relr

def ssfa(_model,**kwargs):
    SSlof=sslofModel(_model)
    SSLAF=round(SSlof,4)
    return SSLAF
    
def sspe(_model,**kwargs):
    sumaVecinos = sumsNeighbors(_model,**kwargs)
    SSPE=round(sumaVecinos,4)
    return SSPE
    
def countLevelVarInd(_model,**kwargs):
    dfVI = _model.getDataFrameVI()
    u=dfVI.drop_duplicates()  
    m=len(u)
    return m
    
def estadigrafoFisherCalFO(_model,**kwargs):
    m = countLevelVarInd(_model,**kwargs)
    n = _model.numberMeasurement()
    sumaVecinos = sumsNeighbors(_model,**kwargs)
    SSlof = sslofModel(_model,**kwargs)
    if m-2 > 0 and sumaVecinos != 0 and n != m : 
        Fo=(SSlof/(m-2))/(sumaVecinos/(n-m))
        Forr=round(Fo,4)
        return Forr
    else:
        raise  EstadigrafoFisherCalFOException()
    
def estadigrafoFisherTabFT(_model,**kwargs):
    
    if 'alpha' in kwargs.keys():
        alpha = float(kwargs['alpha'])
        m = countLevelVarInd(_model,**kwargs)
        n = _model.numberMeasurement()
        a1=m-2
        a2=n-m
        Ft=scipy.stats.f.ppf(q=1-alpha,dfn=a1,dfd=a2)
        Ftr=round(Ft,4)
        return Ftr
    else :
        raise NotFoundParameterExtraException('alpha','estadigrafoFisherTabFT')
    
def relationFOFT(_model,**kwargs):
    if 'alpha' in kwargs.keys():
        alpha = float(kwargs['alpha'])
        m = countLevelVarInd(_model,**kwargs)
        n = _model.numberMeasurement()
        SSlof = sslofModel(_model,**kwargs)
        sumaVecinos = sumsNeighbors(_model)
        if m-2 > 0 and sumaVecinos != 0 and n != m :
            Fo=(SSlof/(m-2))/(sumaVecinos/(n-m))
            a1=m-2
            a2=n-m
            Ft=scipy.stats.f.ppf(q=1-alpha,dfn=a1,dfd=a2)
            relafisher=Ft/Fo
            Relar=round(relafisher,4)
            return Relar
        else:
            raise RelationFOFTException()
    else :
        raise NotFoundParameterExtraException('alpha','relationFOFT') 

def mediaNegRMSETVKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    a = score['test_neg_mean_squared_error']
    amenan=np.mean(a) 
    return amenan
    
def cvNegRMSETVKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    a = score['test_neg_mean_squared_error']
    acv=cvar(a) 
    return acv

def mediaNegRMSETEKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    b=score['train_neg_mean_squared_error']
    bmenan=np.mean(b)
    return bmenan

    
def cvNegRMSETEKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    b=score['train_neg_mean_squared_error']
    bcv=cvar(b)
    return bcv
    
def mediaRSquareTVKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    c=score['test_r2']
    cmenan=np.mean(c)
    return cmenan
    
def cvRSquareTVKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    c=score['test_r2']
    ccv=cvar(c)
    return ccv
    
def mediaRSquareTEKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    d=score['train_r2']
    dmenan=np.mean(d)
    return dmenan
    
def cvRSquareTEKFOLD(_model,**kwargs):
    score = scoreModel(_model,**kwargs)
    d=score['train_r2']
    dcv=cvar(d)
    return dcv

def mediaRSEMBootStropping(_model,**kwargs):
    boot_RMSE = []
    RMSEbtmean = None
    if 'boots' in kwargs.keys():
        boots = int(kwargs['boots'])
        k= _model.numberMeasurement()
        for _ in range(boots):
            data_df = _model.getDataFrameModel().copy(deep=True)
            sample_df = data_df.sample(n=k, replace=True)
            regbst=smf.ols(_model.eval(),sample_df)
            resulbst=regbst.fit() 
            RMSEbst=np.sqrt(resulbst.mse_total)
            boot_RMSE.append(RMSEbst)
        RMSEbtmean=np.mean(boot_RMSE)
    else :
        raise NotFoundParameterExtraException('boots','mediaRSEMBootStropping')  
    return RMSEbtmean
    
def cvRSEMBootStropping(_model,**kwargs):
    boot_RMSE = []
    RMSEcv = None
    if 'boots' in kwargs.keys():
        boots = int(kwargs['boots'])
        k= _model.numberMeasurement()
        for _ in range(boots):
            data_df = _model.getDataFrameModel().copy(deep=True)
            sample_df = data_df.sample(n=k, replace=True)
            regbst=smf.ols(_model.eval(),sample_df)
            resulbst=regbst.fit() 
            RMSEbst=np.sqrt(resulbst.mse_total)
            boot_RMSE.append(RMSEbst)
        RMSEcv=cvar(boot_RMSE)
    else :
        raise NotFoundParameterExtraException('boots','cvRSEMBootStropping') 
    return RMSEcv
    
def mediaRSquareBootStropping(_model,**kwargs):
    boot_rcuadj = []
    Rcuadjbtmean =None
    if 'boots' in kwargs.keys():
        boots = int(kwargs['boots'])
        k= _model.numberMeasurement()
        for _ in range(boots):
            data_df = _model.getDataFrameModel().copy(deep=True)
            sample_df = data_df.sample(n=k, replace=True)
            regbst=smf.ols(_model.eval(),sample_df)
            resulbst=regbst.fit()
            rcuadjbst=resulbst.rsquared_adj 
            boot_rcuadj.append(rcuadjbst)
        Rcuadjbtmean=np.mean(boot_rcuadj)
    else :
        raise NotFoundParameterExtraException('boots','mediaRSquareBootStropping') 
    return Rcuadjbtmean
    
def cvRSquareBootStropping(_model,**kwargs):
    boot_rcuadj = []
    Rcuacv = None
    if 'boots' in kwargs.keys():
        boots = int(kwargs['boots'])
        k= _model.numberMeasurement()
        for _ in range(boots):
            data_df = _model.getDataFrameModel().copy(deep=True)
            sample_df = data_df.sample(n=k, replace=True)
            regbst=smf.ols(_model.eval(),sample_df)
            resulbst=regbst.fit()
            rcuadjbst=resulbst.rsquared_adj 
            boot_rcuadj.append(rcuadjbst)
        Rcuacv=cvar(boot_rcuadj)
    else :
        raise NotFoundParameterExtraException('boots','cvRSquareBootStropping')
    return Rcuacv

def chartFrequencyCoefficientBootStropping(_model,**kwargs):
    data = {}
    if 'boots' in kwargs.keys():
       boots = int(kwargs['boots'])
       names = _model.getNamesVariableI().copy()
       k= _model.numberMeasurement()
       boot_coeff = []
       for _ in range(boots):
           data_df = _model.getDataFrameModel().copy(deep=True)
           sample_df = data_df.sample(n=k, replace=True)
           regbst=smf.ols(_model.eval(),sample_df)
           resulbst=regbst.fit()
           coeffbst=resulbst.params 
           boot_coeff.append(coeffbst)
       
       
       names.append('Intercept')
       
       for n in names:
           data[n] ={'name':n,'coeff':[]}
           for coeff in boot_coeff:
               data[n]['coeff'].append(coeff.at[n])
        
       for n in names:
           data[n]['coeff'].sort()
           nValues = len(data[n]['coeff'])
           
           if nValues % 2 == 1:
               data[n]['median'] = data[n]['coeff'][int(nValues/2)]
           else:
               data[n]['median'] = (data[n]['coeff'][int(nValues/2)]+ data[n]['coeff'][int(nValues/2)-1])/2
           mean = sum(data[n]['coeff'])/len(data[n]['coeff'])
           data[n]['mean'] =mean
           variance = sum([((x - mean) ** 2) for x in data[n]['coeff']]) / len(data[n]['coeff'])
           res = variance ** 0.5
           data[n]['std'] = res
           data[n]['cv'] = (res/mean)*100
           
           data[n]['bars'] = generateBars(data[n]['coeff'])
           
       return data 
    else:
       raise NotFoundParameterExtraException('boots','chartFrequencyCoefficientBootStropping') 
    return data
    
    
def testRMSETestKFOLD(_model,**kwargs):
    e = None
    
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        y = _model.getDataFrameVD()
        X = _model.getDataFrameVI()
        clf = LinearRegression()
        predictions=cross_val_predict(clf,X,y,cv=k)
        e = metrics.mean_squared_error(y,predictions)
        e= np.sqrt(e)
    else:
        raise NotFoundParameterExtraException('k','testRMSETestKFOLD')
    return e

def testSquareTwoTestKFOLD(_model,**kwargs):
    g = None
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        y = _model.getDataFrameVD()
        X = _model.getDataFrameVI()
        clf = LinearRegression()
        predictions=cross_val_predict(clf,X,y,cv=k)
        g= metrics.r2_score(y,predictions) 
    else:
        raise NotFoundParameterExtraException('k','testSquareTwoTestKFOLD')
    return g

def chartNegRMSEKFold(_model, **kwargs):
    data = None
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        
        y = _model.getDataFrameVD()
        X = _model.getDataFrameVI() 
    
        clf = LinearRegression()
        model=clf.fit(X, y) 
        
        scores = cross_validate(model, X, y, cv=k,scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
        a=scores['test_neg_mean_squared_error']
        b=scores['train_neg_mean_squared_error']
        data = {'test_neg_mean':a,'train_neg_mean':b}
        return data
    else:
        raise NotFoundParameterExtraException('k','chartNegRMSEKFold')
    
def chartRSquareKFold(_model, **kwargs):
    data = None
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        
        y = _model.getDataFrameVD()
        X = _model.getDataFrameVI() 
    
        clf = LinearRegression()
        model=clf.fit(X, y) 
        
        scores = cross_validate(model, X, y, cv=k,scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
        a=scores['test_r2']
        b=scores['train_r2']
        data = {'test_r2':a,'train_r2':b}
        return data
    else:
        raise NotFoundParameterExtraException('k','chartRSquareKFold')
    
def chartValuesPredictedKFold(_model, **kwargs):
    data = None
    if 'k' in kwargs.keys():
        k = int(kwargs['k'])
        
        clf = LinearRegression()
        
        y = _model.getDataFrameVD()
        X = _model.getDataFrameVI()
        
        
        resul = fitModel(_model,**kwargs)
        
        data = {}
        
        answer = cross_val_predict(clf,X,y,cv=k)
        data['value-y'] =np.ravel(answer)
        data['value-x'] = resul.fittedvalues
        
        return data
    else:
        raise NotFoundParameterExtraException('k','chartValuesPredictedKFold')

def analysisExtrapolationHide(_model,**kwargs):
    # result 0 si es desconocido, -1 si no hay evidencias , 1 si hay evidencia de extrapolacion
    answer = {'result':0,'msg':'','points':None}
    
    if 'esp' in kwargs.keys():
        esp = int(kwargs['esp'])
        
        namesVarI = _model.getNamesVariableI()
        lowerLimitVarI = _model.getLowerLimitAllVarIExtrapolationHide()
        upperLimitVarI = _model.getUpperLimitAllVarIExtrapolationHide()
        dataFrameVARI = _model.getDataFrameVI()
        y=_model.getDataFrameVD()
        
        dicLinSpace = {}
        dicMeshGrid = {}
        dicRavel = {}
        listLinSpace = []
        pointsMatrixD ={}
        matrixPointsL =[]
        
        B=dataFrameVARI 
        B_constant=sm.add_constant(B)   #Seria X en la formula de Montgomery
        B_constantTrans=B_constant.transpose()  #Seria X' en la formula de Montgomery

        A=B_constantTrans  
        BC=B_constant
        
        D = np.matmul(A,BC)
        Dinv=np.linalg.inv(D)
        
        
        linreg=sm.OLS(y,B_constant).fit()
        influence = linreg.get_influence()
        hatdiag = influence.hat_matrix_diag
        hmxm=max(hatdiag)
        
        for name in namesVarI:
            t = np.linspace(lowerLimitVarI[name],upperLimitVarI[name],esp)
            dicLinSpace[name] = t
            listLinSpace.append(t)
            pointsMatrixD[name]=[]
            
        P=np.meshgrid(*(v for _,v in dicLinSpace.items()))
        
        X=np.meshgrid(*(v for _,v in dicLinSpace.items()))
        
        # Hasta aqui todo OK
        
        index =0 
        for name in namesVarI:
            dicMeshGrid[name] = X[index]
            index = index + 1
        
        
        for name in namesVarI:
            dicRavel[name]= np.ravel(dicMeshGrid[name])
            
        n=len(namesVarI) #cantidad de variables barajadas en P (O sea cantidad de variables independientes)
        dim=np.size(P)
        dimf=dim/n
        dimfor=dimf
        end=int(dimfor) #convertir de float a int
        
        ho=list()
        
        
        for i in range(0,end):
            listDataFrame=[1]
            
            for name in namesVarI:
                listDataFrame.append(dicRavel[name][i])
            
            xi=pd.DataFrame(listDataFrame) #Vendria siendo xi' por el dataframe
            xit=xi.transpose()
            hy=np.matmul(xit,Dinv)
            hooi=np.matmul(hy,xi)
            hooc= hooi[0][0]
            
            if hooc > hmxm:
                ho.append(hooi)
                for name in namesVarI:
                    pointsMatrixD[name].append(dicRavel[name][i])
                
        for name in namesVarI:
            matrixPointsL.append(pointsMatrixD[name])    
        
        jk=len(ho)
        if jk == 0:
            answer['msg']='No hay evidencias de extrapolación oculta'
            answer['result'] = -1
        else:
            answer['msg']='Hay evidencias de extrapolación oculta'
            answer['result'] = 1
            pto=pd.DataFrame(matrixPointsL)
            ptos=pto.transpose()
            answer['points'] = ptos
    else:
        raise NotFoundParameterExtraException('esp','analysisExtrapolationHide')
    return answer


def serieChartQQTestNormalResidualNotScale(_model,**kwargs):
    residuales = residualModel(_model,**kwargs)
    [xs,ys]=st.probplot(residuales, sparams=(), dist='norm', fit=False, plot=None, rvalue=False)
    [u3,u4]=st.probplot(residuales, sparams=(), dist='norm', fit=True, plot=None, rvalue=False)
    m=u4[0]
    n=u4[1]
    maxX = max(xs)+0.1
    minX = min(xs)-0.1
    maxY = m*maxX +n
    minY = m*minX + n
    return [xs,ys,[minX,maxX],[minY,maxY]]

def serieChartQQTestNormalResidualStudentized(_model,**kwargs):
    residualesST = residualSTModel(_model, **kwargs)
    [xs,ys]=st.probplot(residualesST, sparams=(), dist='norm', fit=False, plot=None, rvalue=False)
    [u7,u8]=st.probplot(residualesST, sparams=(), dist='norm', fit=True, plot=None, rvalue=False)
    m=u8[0]
    n=u8[1]
    maxX = max(xs)+0.1
    minX = min(xs)-0.1
    maxY = m*maxX + n
    minY = m*minX + n
    return [xs,ys,[minX,maxX],[minY,maxY]]

def serieChartDistributionResidualNotScale(_model,**kwargs):
    residuales = residualModel(_model,**kwargs)
    xH3=residuales
    kde = sm.nonparametric.KDEUnivariate(xH3)
    kde.fit() 
    xKDE=kde.support  
    yKDE=kde.density
    
    g=len(xKDE)
    mu, std = norm.fit(residuales) 
    
    XH3min=min(xH3)
    XH3max=max(xH3)
    xNormal = np.linspace(XH3min, XH3max, g)
    yNormal = norm.pdf(xNormal, mu, std)
    
    return [xKDE,yKDE,xNormal,yNormal]

def serieChartDistributionResidualStudentized(_model, **kwargs):
    residualesST = residualSTModel(_model, **kwargs)
    xH4=residualesST
    kde = sm.nonparametric.KDEUnivariate(xH4)
    kde.fit() 
    xKDE=kde.support 
    yKDE=kde.density
    
    g=len(xKDE)
    mu1, std1 = norm.fit(residualesST) 
    
    XH4min=min(xH4)
    XH4max=max(xH4)
    xNormal = np.linspace(XH4min, XH4max, g)
    yNormal = norm.pdf(xNormal, mu1, std1)
    
    return [xKDE,yKDE,xNormal,yNormal] 
    
def meanResidualNotScaled(_model, **kwargs):
    residuals =residualModel(_model,**kwargs)
    return np.mean(residuals)

def meanResidualStudentized(_model, **kwargs):
    residuals = residualSTModel(_model,**kwargs)
    return np.mean(residuals)

def testSpecificationWhiteWE(_model, **kwargs):
    resul = fitModel(_model)
    residuales = residualModel(_model,**kwargs)
    whitespec=dg.spec_white(residuales, resul.model.exog)
    WE=whitespec[0]
    return WE

def testSpecificationWhitePValue(_model, **kwargs):
    resul = fitModel(_model)
    residuales = residualModel(_model,**kwargs)
    whitespec=dg.spec_white(residuales, resul.model.exog)
    PvWE=whitespec[1]
    return PvWE

def testRainbowLinearityF(_model, **kwargs):
    resul = fitModel(_model)
    rainbow=dg.linear_rainbow(resul, frac=0.5, order_by=None, use_distance=False,center=None)
    F=rainbow[0]
    return F

def testRainbowLinearityPValue(_model, **kwargs):
    resul = fitModel(_model)
    rainbow=dg.linear_rainbow(resul, frac=0.5, order_by=None, use_distance=False,center=None)
    pValue=rainbow[1]
    return pValue

def testHarveyCollierLinearityHC(_model, **kwargs):
    resul = fitModel(_model)
    harvey=dg.linear_harvey_collier(resul, order_by=None, skip=None)
    hc=harvey[0]
    return hc

def testHarveyCollierLinearityPValue(_model, **kwargs):
    resul = fitModel(_model)
    harvey=dg.linear_harvey_collier(resul, order_by=None, skip=None)
    pValue=harvey[1]
    return pValue

def testMultiplierLagrangeLinearityF(_model, **kwargs):
    resul = fitModel(_model,**kwargs)
    residuales = residualModel(_model,**kwargs)
    lagrange=dg.linear_lm(residuales, resul.model.exog, func=None)
    fValue = "NA"
    if hasattr(lagrange[2],'fvalue'):
        fValue = lagrange[2].fvalue
    else:
        raise NotFoundParameterExtraException('fvalue','dg.linear_lm')
    return fValue


def testMultiplierLagrangeLinearityPValue(_model, **kwargs):
    resul = fitModel(_model,**kwargs)
    residuales = residualModel(_model,**kwargs)
    lagrange=dg.linear_lm(residuales, resul.model.exog, func=None)
    pValue = "NA"
    if hasattr(lagrange[2],'pvalue'):
        pValue = lagrange[2].pvalue
    else:
        raise NotFoundParameterExtraException('pvalue','dg.linear_lm')
    return pValue


def testRamseyF(_model, **kwargs):
    fValue = None
    if 'power' in kwargs.keys():
        power = kwargs['power']
        resul = fitModel(_model, **kwargs)
        ramsey=dg.linear_reset(resul,power,test_type='fitted', use_f=True) 
        if hasattr(ramsey,'fvalue'):
            fValue = ramsey.fvalue
        else:
            raise NotFoundParameterExtraException('fvalue','dg.linear_reset')
    else:
        raise NotFoundParameterExtraException('power','testRamsey')
    return fValue

def testRamseyPValue(_model, **kwargs):
    fValue = None
    if 'power' in kwargs.keys():
        power = kwargs['power']
        resul = fitModel(_model, **kwargs)
        ramsey=dg.linear_reset(resul,power,test_type='fitted', use_f=True) 
        if hasattr(ramsey,'pvalue'):
            fValue = ramsey.pvalue
        else:
            raise NotFoundParameterExtraException('pvalue','dg.linear_reset')
    else:
        raise NotFoundParameterExtraException('power','testRamsey')
    return fValue

def chartValueObserverValueAdjust(_model, **kwargs):
    resul = fitModel(_model, **kwargs)
    x = resul.fittedvalues
    y = _model.getDataFrameVD()[_model.getNameVariableD()]
    data = {'x':x, 'y':y}
    return data

def chartResidualValueAdjust(_model, **kwargs):
    resul = fitModel(_model, **kwargs)
    xScatter = resul.fittedvalues
    yScatter =resul.resid
    
    grid, yhat=lowess(yScatter, xScatter).T
    
    xCurve=grid   
    yCurve=yhat
    
    data ={'xScatter':xScatter,
           'yScatter':yScatter,
           'xCurve':xCurve,
           'yCurve':yCurve
           }
    
    return data

def chartCoeffModel(_model, **kwargs):
    dictBetasCoeff = {}
    namesVariables = _model.getNamesVariableI().copy()
    data_dfvi = _model.getDataFrameVI().copy(deep=True)
    namesVariables.insert(0,'Intercepto')
    B = data_dfvi
    B_constant = sm.add_constant(B)
    y = _model.getDataFrameVD().copy(deep=True)
    lin_reg = sm.OLS(y,B_constant).fit()
    influence = lin_reg.get_influence()
    dfbetas = influence.dfbetas
    g=len(data_dfvi[namesVariables[1]])
    
    for j in range(0,len(namesVariables)):
        name = namesVariables[j]
        dictBetasCoeff[name] = {'name':name,'coef':list(),'title_X':'Observación','title_Y':'DfBeta'}
        for i in range(g):
            dictBetasCoeff[name]['coef'].append(dfbetas[i][j])
    
    return dictBetasCoeff

def distanceCooks(_model, **kwargs):
    data_dfvi = _model.getDataFrameVI().copy(deep=True)
    B = data_dfvi
    B_constant=sm.add_constant(B)
    y = _model.getDataFrameVD().copy(deep=True)
    lin_reg = sm.OLS(y,B_constant).fit()
    influence = lin_reg.get_influence()
    cooks = influence.cooks_distance
    return cooks[0]
    
def leverage(_model, **kwargs):
    data_dfvi = _model.getDataFrameVI().copy(deep=True)
    B = data_dfvi
    B_constant=sm.add_constant(B)
    y = _model.getDataFrameVD().copy(deep=True)
    lin_reg=sm.OLS(y,B_constant).fit()
    influence = lin_reg.get_influence()
    leverage = influence.hat_matrix_diag
    return leverage 

def covarianceRatio(_model, **kwargs):
    data_dfvi = _model.getDataFrameVI().copy(deep=True)
    B = data_dfvi
    B_constant=sm.add_constant(B)
    y = _model.getDataFrameVD().copy(deep=True)
    lin_reg=sm.OLS(y,B_constant).fit()
    influence = lin_reg.get_influence()
    cov_ratio=influence.cov_ratio
    return cov_ratio  

def dffits(_model, **kwargs):
    data_dfvi = _model.getDataFrameVI().copy(deep=True)
    B = data_dfvi
    B_constant=sm.add_constant(B)
    y = _model.getDataFrameVD().copy(deep=True)
    lin_reg = sm.OLS(y,B_constant).fit()
    influence = lin_reg.get_influence()
    dffits = influence.dffits[0] 
    return dffits
#-----------------------------------------------------------------------

def mean(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        a=np.mean(listValue)
        return a
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def maxVar(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        b=max(listValue)
        return b
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def minVar(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        b=min(listValue)
        return b
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def countMeas(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        b=len(listValue)
        return b
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def cv(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        b = cvar(listValue)
        return b
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def varianza(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        e=np.var(listValue)
        return e
    else:
        raise VariableNotFoundDataFrame(nameVar)
    
def std(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        e=np.std(listValue)
        return e
    else:
        raise VariableNotFoundDataFrame(nameVar)

def median(nameVar, dataFrame):
    if nameVar in dataFrame:
        listValue = dataFrame[nameVar].tolist()
        e=np.median(listValue)
        return e
    else:
        raise VariableNotFoundDataFrame(nameVar)
    

def getValuesThisVariable(nameVar, dataFrame):
    values = []
    if nameVar in dataFrame:
        values = dataFrame[nameVar]
    else:
        raise VariableNotFoundDataFrame(nameVar) 
    return values



    

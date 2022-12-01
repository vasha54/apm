import pandas as pd

from libmath import regress_tes as RGSST
class ModelLMR:

    
    def __init__(self,_idModel,_nameModel,_nameVariableD,_namesVariablesI, _intervalConfidence=0.05, _dataFrameVI=pd.DataFrame(), _dataFrameVD=pd.DataFrame(),_dataFrameModel=pd.DataFrame(),_isSelect=False, *args, **kwargs):
        super(ModelLMR, self).__init__(*args, **kwargs)
        self.idModel = _idModel
        self.nameModel= _nameModel
        self.nameVariableD = _nameVariableD
        self.namesVariableI = []
        self.namesAllVariables = []
        self.namesAllVariables.append(_nameVariableD)
        
        for name in _namesVariablesI:
            self.namesVariableI.append(name)
            self.namesAllVariables.append(name)
        
        self.dataFrameVI = _dataFrameVI
        self.dataFrameVD = _dataFrameVD
        self.dataFrameModel = _dataFrameModel
        self.isSelectModel = _isSelect
        self.intervalConfidence = _intervalConfidence
        
    def __str__(self):
        modelStr = self.nameModel+"("+self.nameVariableD+"~"
        union="+"
        union=union.join(self.namesVariableI)
        modelStr=modelStr+union+";"
        modelStr=modelStr+"intervalo confianza->"+str(self.intervalConfidence)+")";
        return modelStr
    
    def __eq__(self, _otherModel):
        isEqual = True
        
        if self.nameVariableD != _otherModel.getNameVariableD():
            isEqual = False
            
        if len(self.namesVariableI) != len(_otherModel.getNamesVariableI()):
            isEqual =False
        else:
            otherVI =[]
            selfVI = []
            cCount = len(self.namesVariableI)
            
            for i in range(0,cCount):
                otherVI.append(_otherModel.getNamesVariableI()[i])
                selfVI.append(self.namesVariableI[i])
                
            otherVI.sort()
            selfVI.sort()
            
            for i in range (0,cCount):
                if otherVI[i] != selfVI[i]:
                    isEqual = False
                     
        return isEqual
    
    def eval(self):
        eval = self.nameVariableD+"~"
        union="+"
        union=union.join(self.namesVariableI)
        eval = eval + union
        return eval
    
    NAME = 'getNameModel'    
    def getNameModel(self):
        return self.nameModel
    
    def getIDModel(self):
        return self.idModel
    
    NAME_VD = 'getNameVariableD'
    def getNameVariableD(self):
        return self.nameVariableD
    
    ALL_NAME_VARI = 'getNamesVariableI'
    def getNamesVariableI(self):
        return self.namesVariableI
    
    def getDataFrameVI(self):
        return self.dataFrameVI
    
    def getDataFrameVD(self):
        return self.dataFrameVD
    
    def getDataFrameModel(self):
        return self.dataFrameModel
    
    def isSelect(self):
        return self.isSelectModel
    
    def getIntervalConfidence(self):
        return self.intervalConfidence
    
    ALL_NAME_VAR= 'getNamesAllVariables'
    def getNamesAllVariables(self):
        return self.namesAllVariables
    
    def setNameModel(self, _nameModel):
        self.nameModel = _nameModel
    
    def setIDModel(self, _idModel):
        self.idModel = _idModel
    
    def setNameVariableD(self, _nameVariableD):
        #TODO Falta actualizar el listado con todos nombres de las variables del modelo
        self.nameVariableD = _nameVariableD
    
    def setNamesVariableI(self,_namesVariableI):
        #TODO Falta actualizar el listado con todos nombres de las variables del modelo 
        self.namesVariableI = _namesVariableI
    
    def setDataFrameVD(self,_dataFrameVD):
        self.dataFrameVD = _dataFrameVD
        
    def setDataFrameVI(self,_dataFrameVI):
        self.dataFrameVI = _dataFrameVI
        
    def setDataFrameModel(self, _dataFrameModel):
        self.dataFrameModel= _dataFrameModel
    
    NUMBER_MEAS = 'numberMeasurement' 
    def numberMeasurement(self):
        return len(self.dataFrameVD[self.nameVariableD])
    
    def setIsSelect(self, _select):
        self.isSelectModel = _select    
        
    def setIntervalConfidence(self,_intervalConfidence):
        self.intervalConfidence=_intervalConfidence    
        
    def detailsModelForMessageBox(self):
        detailsStr="<p><b>Nombre:</b>"+str(self.nameModel)+"</p>"
        detailsStr=detailsStr +"<p><b>ID:</b>"+str(self.idModel)+"</p>"
        detailsStr=detailsStr +"<p><b>Variable Dependiente:</b>"+str(self.nameVariableD)+"</p>"
        
        strNamesVariableI="["
        for c in range(0,len(self.namesVariableI)):
            if c == 0:
                strNamesVariableI = strNamesVariableI+str(self.namesVariableI[c])
            else:
                strNamesVariableI = strNamesVariableI+","+str(self.namesVariableI[c])
        strNamesVariableI=strNamesVariableI+"]"
        
        detailsStr=detailsStr +"<p><b>Variable Independientes:</b>"+strNamesVariableI+"</p>"
        return detailsStr
    
    GL_RESIDUAL = 'glResidual'
    def glResidual(self,**kwargs):
        return RGSST.glResidual(self,**kwargs)
    
    GL_MODEL ='glModel'
    def glModel(self,**kwargs):
        return RGSST.glResidual(self,**kwargs)
    
    AIC = 'aic'
    def aic(self,**kwargs):
        return RGSST.aic(self,**kwargs)
    
    BIC = 'bic'
    def bic(self,**kwargs):
        return RGSST.bic(self,**kwargs)
    
    LOG_LIKELI_HEAD = 'logLikeliHead'
    def logLikeliHead(self,**kwargs):
        return RGSST.logLikeliHead(self,**kwargs)
    
    RCUAD = 'RCuad'
    def RCuad(self,**kwargs):
        return RGSST.RCuad(self,**kwargs)
    
    RCUAD_ADJUST = 'RCuadAdjust'
    def RCuadAdjust(self,**kwargs):
        return RGSST.RCuadAdjust(self,**kwargs)
    
    FSTADISTIC = 'FStadistic'
    def FStadistic(self,**kwargs):
        return RGSST.FStadistic(self,**kwargs)
    
    PVALUE = 'PValue'
    def PValue(self,**kwargs):
        return RGSST.PValue(self,**kwargs)
    
    MSE_MODEL = 'MSEModel'
    def MSEModel(self,**kwargs):
        return RGSST.MSEModel(self,**kwargs)
    
    MSE_RESIDUAL = 'MSEResidual'
    def MSEResidual(self,**kwargs):
        return RGSST.MSEResidual(self,**kwargs)
    
    MSE_TOTAL = 'MSETotal'
    def MSETotal(self,**kwargs):
        return RGSST.MSETotal(self,**kwargs)
    
    RMSE_MODEL = 'RMSEModel'
    def RMSEModel(self,**kwargs):
        return RGSST.RMSEModel(self,**kwargs)
    
    NUMBER_VAR = 'numberVariablesModel'
    def numberVariablesModel(self,**kwargs):
        return 1 + len(self.namesVariableI,**kwargs) 
    
    COEFF_VAR = 'coefficientVariablesModel'
    def coefficientVariablesModel(self,**kwargs):
        return RGSST.coefficientVariablesModel(self,**kwargs)
    
    STD_ERR ='sterrVariablesModel'
    def sterrVariablesModel(self,**kwargs):
        return RGSST.sterrVariablesModel(self,**kwargs)
    
    TC = 'tcVariablesModel'
    def tcVariablesModel(self,**kwargs):
        return RGSST.tcVariablesModel(self,**kwargs)
    
    PV_COEFF = 'pvCoefficientVariablesModel'
    def pvCoefficientVariablesModel(self,**kwargs):
        return RGSST.pvCoefficientVariablesModel(self,**kwargs)
    
    LOWER_LIMIT_VAR = 'lowerLimitVariablesModel'
    def lowerLimitVariablesModel(self,**kwargs):
        return RGSST.lowerLimitVariablesModel(self,**kwargs)
    
    UPPER_LIMIT_VAR = 'upperLimitVariablesModel' 
    def upperLimitVariablesModel(self,**kwargs):
        return RGSST.upperLimitVariablesModel(self,**kwargs)
    
    COEFF_CURTOSIS_RWS = 'coefficientCurtosisRWS'
    def coefficientCurtosisRWS(self,**kwargs):
        return RGSST.coefficientCurtosisRWS(self,**kwargs)
    
    COEFF_ASYMETRY_RWS = 'coefficientAsymetryRWS'
    def coefficientAsymetryRWS(self,**kwargs):
        return RGSST.coefficientAsymetryRWS(self,**kwargs)
    
    LILLIEFORS_RWS = 'testLillieforsRWS'
    def testLillieforsRWS(self,**kwargs):
        return RGSST.testLillieforsRWS(self,**kwargs)
    
    LILLIEFORS_PVALUE_RWS = 'testLillieforsPValueRWS'
    def testLillieforsPValueRWS(self,**kwargs):
        return RGSST.testLillieforsPValueRWS(self,**kwargs)
    
    SHAPIRO_WILK_RWS = 'testShapiroWilkRWS'
    def testShapiroWilkRWS(self,**kwargs):
        return RGSST.testShapiroWilkRWS(self,**kwargs)
    
    SHAPIRO_WILK_PVALUE_RWS = 'testShapiroWilkPValueRWS'
    def testShapiroWilkPValueRWS(self,**kwargs):
        return RGSST.testShapiroWilkPValueRWS(self,**kwargs)
    
    KOLMOGOROV_SMIRNOV_RWS = 'testKolmogorovSmirnovRWS'
    def testKolmogorovSmirnovRWS(self,**kwargs):
        return RGSST.testKolmogorovSmirnovRWS(self,**kwargs)
    
    KOLMOGOROV_SMIRNOV_PVALUE_RWS = 'testKolmogorovSmirnovPValueRWS'
    def testKolmogorovSmirnovPValueRWS(self,**kwargs):
        return RGSST.testKolmogorovSmirnovPValueRWS(self,**kwargs)
    
    JARQUE_BERA_RWS = 'testJarqueBeraRWS'
    def testJarqueBeraRWS(self,**kwargs):
        return RGSST.testJarqueBeraRWS(self,**kwargs)
    
    JARQUE_BERA_PVALUE_RWS = 'testJarqueBeraPValueRWS'
    def testJarqueBeraPValueRWS(self,**kwargs):
        return RGSST.testJarqueBeraPValueRWS(self,**kwargs)
    
    ANDERSON_DARLING_RWS = 'testAndersonDarlingRWS'
    def testAndersonDarlingRWS(self,**kwargs):
        return RGSST.testAndersonDarlingRWS(self,**kwargs)
    
    ANDERSON_DARLING_PVALUE_RWS = 'testAndersonDarlingPValueRWS'
    def testAndersonDarlingPValueRWS(self,**kwargs):
        return RGSST.testAndersonDarlingPValueRWS(self,**kwargs)
    
    K_CUAD_DANGOSTINO_RWS = 'testKCuadDAngostinoRWS'
    def testKCuadDAngostinoRWS(self,**kwargs):
        return RGSST.testKCuadDAngostinoRWS(self,**kwargs)
    
    K_CUAD_DANGOSTINO_PVALUE_RWS = 'testKCuadDAngostinoPValueRWS'
    def testKCuadDAngostinoPValueRWS(self,**kwargs):
        return RGSST.testKCuadDAngostinoPValueRWS(self,**kwargs)
    
    CHI_SQUARE_RWS = 'testChiSquareRWS'
    def testChiSquareRWS(self,**kwargs):
        return RGSST.testChiSquareRWS(self,**kwargs)
    
    CHI_SQUARE_PVALUE_RWS = 'testChiSquarePValueRWS'
    def testChiSquarePValueRWS(self,**kwargs):
        return RGSST.testChiSquarePValueRWS(self,**kwargs)
    
    COEFF_CURTOSIS_RE = 'coefficientCurtosisRE'
    def coefficientCurtosisRE(self,**kwargs):
        return RGSST.coefficientCurtosisRE(self,**kwargs)
    
    COEFF_ASYMETRY_RE = 'coefficientAsymetryRE'
    def coefficientAsymetryRE(self,**kwargs):
        return RGSST.coefficientAsymetryRE(self,**kwargs)
    
    LILLIEFORS_RE = 'testLillieforsRE'
    def testLillieforsRE(self,**kwargs):
        return RGSST.testLillieforsRE(self,**kwargs)
    
    LILLIEFORS_PVALUE_RE = 'testLillieforsPValueRE'
    def testLillieforsPValueRE(self,**kwargs):
        return RGSST.testLillieforsPValueRE(self,**kwargs)
    
    SHAPIRO_WILK_RE = 'testShapiroWilkRE'
    def testShapiroWilkRE(self,**kwargs):
        return RGSST.testShapiroWilkRE(self,**kwargs)
    
    SHAPIRO_WILK_PVALUE_RE = 'testShapiroWilkPValueRE'
    def testShapiroWilkPValueRE(self,**kwargs):
        return RGSST.testShapiroWilkPValueRE(self,**kwargs)
    
    KOLMOGOROV_SMIRNOV_RE = 'testKolmogorovSmirnovRE'
    def testKolmogorovSmirnovRE(self,**kwargs):
        return RGSST.testKolmogorovSmirnovRE(self,**kwargs)
    
    KOLMOGOROV_SMIRNOV_PVALUE_RE = 'testKolmogorovSmirnovPValueRE'
    def testKolmogorovSmirnovPValueRE(self,**kwargs):
        return RGSST.testKolmogorovSmirnovPValueRE(self,**kwargs)
    
    JARQUE_BERA_RE = 'testJarqueBeraRE'
    def testJarqueBeraRE(self,**kwargs):
        return RGSST.testJarqueBeraRE(self,**kwargs)
    
    JARQUE_BERA_PVALUE_RE = 'testJarqueBeraPValueRE'
    def testJarqueBeraPValueRE(self,**kwargs):
        return RGSST.testJarqueBeraPValueRE(self,**kwargs)
    
    ANDERSON_DARLING_RE = 'testAndersonDarlingRE'
    def testAndersonDarlingRE(self,**kwargs):
        return RGSST.testAndersonDarlingRE(self,**kwargs)
    
    ANDERSON_DARLING_PVALUE_RE = 'testAndersonDarlingPValueRE'
    def testAndersonDarlingPValueRE(self,**kwargs):
        return RGSST.testAndersonDarlingPValueRE(self,**kwargs)
    
    K_CUAD_DANGOSTINO_RE = 'testKCuadDAngostinoRE'
    def testKCuadDAngostinoRE(self,**kwargs):
        return RGSST.testKCuadDAngostinoRE(self,**kwargs)
    
    K_CUAD_DANGOSTINO_PVALUE_RE = 'testKCuadDAngostinoPValueRE'
    def testKCuadDAngostinoPValueRE(self,**kwargs):
        return RGSST.testKCuadDAngostinoPValueRE(self,**kwargs)
    
    CHI_SQUARE_RE = 'testChiSquareRE'
    def testChiSquareRE(self,**kwargs):
        return RGSST.testChiSquareRE(self,**kwargs)
    
    CHI_SQUARE_PVALUE_RE = 'testChiSquarePValueRE'
    def testChiSquarePValueRE(self,**kwargs):
        return RGSST.testChiSquarePValueRE(self,**kwargs)
    
    BREUSH_PAGAN = 'testBreushPagan'
    def testBreushPagan(self,**kwargs):
        return RGSST.testBreushPagan(self,**kwargs)
    
    BREUSH_PAGAN_PVALUE = 'testBreushPaganPValue'
    def testBreushPaganPValue(self,**kwargs):
        return RGSST.testBreushPaganPValue(self,**kwargs)
    
    GOLDFELD_QUANDT = 'testGoldfeldQuandt'
    def testGoldfeldQuandt(self,**kwargs):
        return RGSST.testGoldfeldQuandt(self,**kwargs)
    
    GOLDFELD_QUANDT_PVALUE = 'testGoldfeldQuandtPValue'
    def testGoldfeldQuandtPValue(self,**kwargs):
        return RGSST.testGoldfeldQuandtPValue(self,**kwargs)
    
    WHITE_LH = 'testWhiteLH'
    def testWhiteLH(self,**kwargs):
        return RGSST.testWhiteLH(self,**kwargs)
    
    WHITE_LH_PVALUE = 'testWhiteLHPValue'
    def testWhiteLHPValue(self,**kwargs):
        return RGSST.testWhiteLHPValue(self,**kwargs)
    
    WHITE_FW = 'testWhiteFW'
    def testWhiteFW(self,**kwargs):
        return RGSST.testWhiteFW(self,**kwargs)
    
    WHITE_FW_PVALUE = 'testWhiteFWPValue'
    def testWhiteFWPValue(self,**kwargs):
        return RGSST.testWhiteFWPValue(self,**kwargs)
    
    DURBIN_WATSON = 'testDurbinWatson'
    def testDurbinWatson(self,**kwargs):
        return RGSST.testDurbinWatson(self,**kwargs)
    
    BREUSH_GGODFREY = 'testBreushGGodfrey'
    def testBreushGGodfrey(self,**kwargs):
        return RGSST.testBreushGGodfrey(self,**kwargs)
    
    BREUSH_GGODFREY_PVALUE = 'testBreushGGodfreyPValue'
    def testBreushGGodfreyPValue(self,**kwargs):
        return RGSST.testBreushGGodfreyPValue(self,**kwargs)
    
    ANALYSIS_MULTICOLINIALIDAD = 'analysisMultiColinialidad'
    def analysisMultiColinialidad(self,**kwargs):
        return RGSST.analysisMultiColinialidad(self,**kwargs)
    
    RELATION_RANGE_VALUES_AND_ERROR_STD_MEAN = 'relationRangeValuesAndErrorSTDMean'
    def relationRangeValuesAndErrorSTDMean(self,**kwargs):
        return RGSST.relationRangeValuesAndErrorSTDMean(self)
    
    SUMS_NEIGHBORS = 'sumsNeighbors'
    def sumsNeighbors(_model,**kwargs):
        return RGSST.sumsNeighbors(_model)
    
    SSfa = 'ssfa'
    def ssfa(self,**kwargs):
        pass
    
    SSpe = 'sspe'
    def sspe(self,**kwargs):
        pass
    
    COUNT_LEVEL_VAR_IND = 'countLevelVarInd'
    def countLevelVarInd(self,**kwargs):
        pass
    
    ESTADIGRAFO_FISHER_CAL_FO = 'estadigrafoFisherCalFO'
    def estadigrafoFisherCalFO(self,**kwargs):
        pass
    
    ESTADIGRAFO_FISHER_TAB_FT = 'estadigrafoFisherTabFT'
    def estadigrafoFisherTabFT(self,**kwargs):
        pass
    
    def relationFOFT(self,**kwargs):
        pass
    
    def mediaNegRMSETVKFOLD(self,**kwargs):
        pass
    
    def cvNegRMSETVKFOLD(self,**kwargs):
        pass
    
    def mediaNegRMSETEKFOLD(self,**kwargs):
        pass
    
    def cvNegRMSETEKFOLD(self,**kwargs):
        pass
    
    def mediaRSquareTVKFOLD(self,**kwargs):
        pass
    
    def cvRSquareTVKFOLD(self,**kwargs):
        pass
    
    def mediaRSquareTEKFOLD(self,**kwargs):
        pass
    
    def cvRSquareTEKFOLD(self,**kwargs):
        pass
    
    def mediaRSEMBootStropping(self,**kwargs):
        pass
    
    def cvRSEMBootStropping(self,**kwargs):
        pass
    
    def mediaRSquareBootStropping(self,**kwargs):
        pass
    
    def cvRSquareBootStropping(self,**kwargs):
        pass
    
    def testRMSETestKFOLD(self,**kwargs):
        pass
    
    def testSquareTwoTestKFOLD(self,**kwargs):
        pass
    
    
        
        
    
    
        
    
     
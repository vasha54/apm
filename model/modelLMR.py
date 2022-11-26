import pandas as pd

from libmath import regress_tes as RGSST
class ModelLMR:
    
    NAME = 'nameModel'
    NAME_VD = 'nameVD'
    ALL_NAME_VARI = 'allnameVI'
    NUMBER_MEAS = 'number_meas'
    GL_RESIDUAL = 'glresidual'
    GL_MODEL ='glmodel'
    AIC = 'aic'
    BIC = 'bic'
    LOG_LIKELI_HEAD = 'loglilkelihead'
    RCUAD = 'rcuad'
    RCUAD_ADJUST = 'rcuadadjust'
    FSTADISTIC = 'fstadistic'
    PVALUE = 'pvalue'
    MSE_MODEL = 'msemodel'
    MSE_RESIDUAL = 'mseresidual'
    MSE_TOTAL = 'msetotal'
    RMSE_MODEL = 'rmsemodel'
    NUMBER_VAR = 'number_var'
    ALL_NAME_VAR= 'all_name_var'
    COEFF_VAR = 'coeffvar'
    STD_ERR ='stderr'
    TC = 'tc'
    PV_COEFF = 'pvcoeff'
    LOWER_LIMIT_VAR = 'lowerlimitvar'
    UPPER_LIMIT_VAR = 'upperlimitvar' 
    COEFF_CURTOSIS_RWS = 'coeffcurtosisrws'
    COEFF_ASYMETRY_RWS = 'coeffasymetryrws'
    LILLIEFORS_RWS = 'lillieforsrws'
    LILLIEFORS_PVALUE_RWS = 'lillieforspvaluerws'
    SHAPIRO_WILK_RWS = 'shapirowilkrws'
    SHAPIRO_WILK_PVALUE_RWS = 'shapirowilkpvaluerws'
    KOLMOGOROV_SMIRNOV_RWS = 'kolmogorovsmirnovrws'
    KOLMOGOROV_SMIRNOV_PVALUE_RWS = 'kolmogorovsmirnovpvaluerws'
    JARQUE_BERA_RWS = 'jarqueberarws'
    JARQUE_BERA_PVALUE_RWS = 'jarqueberapvaluerws'
    ANDERSON_DARLING_RWS = 'andersondarlingrws'
    ANDERSON_DARLING_PVALUE_RWS = 'andersondarlingpvaluerws'
    K_CUAD_DANGOSTINO_RWS = 'kcuaddangostinorws'
    K_CUAD_DANGOSTINO_PVALUE_RWS = 'kcuaddangostinopvaluerws'
    CHI_SQUARE_RWS = 'chisquarerws'
    CHI_SQUARE_PVALUE_RWS = 'chisquarepvaluerws'
    COEFF_CURTOSIS_RE = 'coeffcurtosisre'
    COEFF_ASYMETRY_RE = 'coeffasymetryre'
    LILLIEFORS_RE = 'lillieforsre'
    LILLIEFORS_PVALUE_RE = 'lillieforspvaluere'
    SHAPIRO_WILK_RE = 'shapirowilkre'
    SHAPIRO_WILK_PVALUE_RE = 'shapirowilkpvaluere'
    KOLMOGOROV_SMIRNOV_RE = 'kolmogorovsmirnovre'
    KOLMOGOROV_SMIRNOV_PVALUE_RE = 'kolmogorovsmirnovpvaluere'
    JARQUE_BERA_RE = 'jarqueberare'
    JARQUE_BERA_PVALUE_RE = 'jarqueberapvaluere'
    ANDERSON_DARLING_RE = 'andersondarlingre'
    ANDERSON_DARLING_PVALUE_RE = 'andersondarlingpvaluere'
    K_CUAD_DANGOSTINO_RE = 'kcuaddangostinore'
    K_CUAD_DANGOSTINO_PVALUE_RE = 'kcuaddangostinopvaluere'
    CHI_SQUARE_RE = 'chisquarere'
    CHI_SQUARE_PVALUE_RE = 'chisquarepvaluere'
    BREUSH_PAGAN = 'breushpagan'
    BREUSH_PAGAN_PVALUE = 'breushpaganpvalue'
    GOLDFELD_QUANDT = 'goldfeldquandt'
    GOLDFELD_QUANDT_PVALUE = 'goldfeldquandtpvalue'
    WHITE_LH = 'whitelh'
    WHITE_LH_PVALUE = 'whitelhpvalue'
    WHITE_FW = 'whitefh'
    WHITE_FW_PVALUE = 'whitefwpvalue'
    DURBIN_WATSON = 'durbinwatson'
    BREUSH_GGODFREY = 'breushggodfrey'
    BREUSH_GGODFREY_PVALUE = 'breushggodfreypvalue'
    ANALYSIS_MULTICOLINIALIDAD = 'analysismulticolinialidad'
    
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
            otherVI = _otherModel.getNamesVariableI()
            cCount = len(self.namesVariableI)
            for i in range(0, cCount):
                if self.namesVariableI[i] != otherVI[i]:
                    isEqual = False        
        return isEqual
    
    def eval(self):
        eval = self.nameVariableD+"~"
        union="+"
        union=union.join(self.namesVariableI)
        eval = eval + union
        return eval
        
    def getNameModel(self):
        return self.nameModel
    
    def getIDModel(self):
        return self.idModel
    
    def getNameVariableD(self):
        return self.nameVariableD
    
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
    
    def glResidual(self):
        return RGSST.glResidual(self)
    
    def glModel(self):
        return RGSST.glResidual(self)
    
    def aic(self):
        return RGSST.aic(self)
    
    def bic(self):
        return RGSST.bic(self)
    
    def logLikeliHead(self):
        return RGSST.logLikeliHead(self)
    
    def RCuad(self):
        return RGSST.RCuad(self)
    
    def RCuadAdjust(self):
        return RGSST.RCuadAdjust(self)
    
    def FStadistic(self):
        return RGSST.FStadistic(self)
    
    def PValue(self):
        return RGSST.PValue(self)
    
    def MSEModel(self):
        return RGSST.MSEModel(self)
    
    def MSEResidual(self):
        return RGSST.MSEResidual(self)
    
    def MSETotal(self):
        return RGSST.MSETotal(self)
    
    def RMSEModel(self):
        return RGSST.RMSEModel(self)
    
    def numberVariablesModel(self):
        return 1 + len(self.namesVariableI) 
    
    def coefficientVariablesModel(self):
        return RGSST.coefficientVariablesModel(self)
    
    def sterrVariablesModel(self):
        return RGSST.sterrVariablesModel(self)
    
    def tcVariablesModel(self):
        return RGSST.tcVariablesModel(self)
    
    def pvCoefficientVariablesModel(self):
        return RGSST.pvCoefficientVariablesModel(self)
    
    def lowerLimitVariablesModel(self):
        return RGSST.lowerLimitVariablesModel(self)
    
    def upperLimitVariablesModel(self):
        return RGSST.upperLimitVariablesModel(self)
    
    def coefficientCurtosisRWS(self):
        return RGSST.coefficientCurtosisRWS(self)
    
    def coefficientAsymetryRWS(self):
        return RGSST.coefficientAsymetryRWS(self)
    
    def testLillieforsRWS(self):
        return RGSST.testLillieforsRWS(self)
    
    def testLillieforsPValueRWS(self):
        return RGSST.testLillieforsPValueRWS(self)
    
    def testShapiroWilkRWS(self):
        return RGSST.testShapiroWilkRWS(self)
    
    def testShapiroWilkPValueRWS(self):
        return RGSST.testShapiroWilkPValueRWS(self)
    
    def testKolmogorovSmirnovRWS(self):
        return RGSST.testKolmogorovSmirnovRWS(self)
    
    def testKolmogorovSmirnovPValueRWS(self):
        return RGSST.testKolmogorovSmirnovPValueRWS(self)
    
    def testJarqueBeraRWS(self):
        return RGSST.testJarqueBeraRWS(self)
    
    def testJarqueBeraPValueRWS(self):
        return RGSST.testJarqueBeraPValueRWS(self)
    
    def testAndersonDarlingRWS(self):
        return RGSST.testAndersonDarlingRWS(self)
    
    def testAndersonDarlingPValueRWS(self):
        return RGSST.testAndersonDarlingPValueRWS(self)
    
    def testKCuadDAngostinoRWS(self):
        return RGSST.testKCuadDAngostinoRWS(self)
    
    def testKCuadDAngostinoPValueRWS(self):
        return RGSST.testKCuadDAngostinoPValueRWS(self)
    
    def testChiSquareRWS(self):
        return RGSST.testChiSquareRWS(self)
    
    def testChiSquarePValueRWS(self):
        return RGSST.testChiSquarePValueRWS(self)
    
    def coefficientCurtosisRE(self):
        return RGSST.coefficientCurtosisRE(self)
    
    def coefficientAsymetryRE(self):
        return RGSST.coefficientAsymetryRE(self)
    
    def testLillieforsRE(self):
        return RGSST.testLillieforsRE(self)
    
    def testLillieforsPValueRE(self):
        return RGSST.testLillieforsPValueRE(self)
    
    def testShapiroWilkRE(self):
        return RGSST.testShapiroWilkRE(self)
    
    def testShapiroWilkPValueRE(self):
        return RGSST.testShapiroWilkPValueRE(self)
    
    def testKolmogorovSmirnovRE(self):
        return RGSST.testKolmogorovSmirnovRE(self)
    
    def testKolmogorovSmirnovPValueRE(self):
        return RGSST.testKolmogorovSmirnovPValueRE(self)
    
    def testJarqueBeraRE(self):
        return RGSST.testJarqueBeraRE(self)
    
    def testJarqueBeraPValueRE(self):
        return RGSST.testJarqueBeraPValueRE(self)
    
    def testAndersonDarlingRE(self):
        return RGSST.testAndersonDarlingRE(self)
    
    def testAndersonDarlingPValueRE(self):
        return RGSST.testAndersonDarlingPValueRE(self)
    
    def testKCuadDAngostinoRE(self):
        return RGSST.testKCuadDAngostinoRE(self)
    
    def testKCuadDAngostinoPValueRE(self):
        return RGSST.testKCuadDAngostinoPValueRE(self)
    
    def testChiSquareRE(self):
        return RGSST.testChiSquareRE(self)
    
    def testChiSquarePValueRE(self):
        return RGSST.testChiSquarePValueRE(self)
    
    def testBreushPagan(self):
        return RGSST.testBreushPagan(self)
    
    def testBreushPaganPValue(self):
        return RGSST.testBreushPaganPValue(self)
    
    def testGoldfeldQuandt(self):
        return RGSST.testGoldfeldQuandt(self)
    
    def testGoldfeldQuandtPValue(self):
        return RGSST.testGoldfeldQuandtPValue(self)
    
    def testWhiteLH(self):
        return RGSST.testWhiteLH(self)
    
    def testWhiteLHPValue(self):
        return RGSST.testWhiteLHPValue(self)
    
    def testWhiteFW(self):
        return RGSST.testWhiteFW(self)
    
    def testWhiteFWPValue(self):
        return RGSST.testWhiteFWPValue(self)
    
    def testDurbinWatson(self):
        return RGSST.testDurbinWatson(self)
    
    def testBreushGGodfrey(self):
        return RGSST.testBreushGGodfrey(self)
    
    def testBreushGGodfreyPValue(self):
        return RGSST.testBreushGGodfreyPValue(self)
    
    def analysisMultiColinialidad(self):
        return RGSST.analysisMultiColinialidad(self)
    
    
        
        
    
    
        
    
     
import pandas as pd

from libmath import regress_tes
class ModelLMR:
    
    NAME = 'nameModel'
    NAME_VD = 'nameVD'
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
    
    def __init__(self,_idModel,_nameModel,_nameVariableD,_namesVariablesI, _intervalConfidence=0.05, _dataFrameVI=pd.DataFrame(), _dataFrameVD=pd.DataFrame(),_dataFrameModel=pd.DataFrame(),_isSelect=False, *args, **kwargs):
        super(ModelLMR, self).__init__(*args, **kwargs)
        self.idModel = _idModel
        self.nameModel= _nameModel
        self.nameVariableD = _nameVariableD
        self.namesVariableI = []
        
        for name in _namesVariablesI:
            self.namesVariableI.append(name)
        
        self.dataFrameVI = _dataFrameVI
        self.dataFrameVD = _dataFrameVD
        self.dataFrameModel = _dataFrameModel
        self.isSelectModel = _isSelect
        self.intervalConfidence = _intervalConfidence
        
    def __str__(self):
        modelStr = self.nameModel+"("+self.nameVariableD+"~"
        union="+"
        union=union.join(self.namesVariableI)
        modelStr=modelStr+union+")"
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
    
    def setNameModel(self, _nameModel):
        self.nameModel = _nameModel
        
    def isSelect(self):
        return self.isSelectModel
    
    def getIntervalConfidence(self):
        return self.intervalConfidence
    
    def setIDModel(self, _idModel):
        self.idModel = _idModel
    
    def setNameVariableD(self, _nameVariableD):
        self.nameVariableD = _nameVariableD
    
    def setNamesVariableI(self,_namesVariableI):
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
        return regress_tes.glResidual(self)
    
    def glModel(self):
        return regress_tes.glResidual(self)
    
    def aic(self):
        return regress_tes.aic(self)
    
    def bic(self):
        return regress_tes.bic(self)
    
    def logLikeliHead(self):
        return regress_tes.logLikeliHead(self)
    
    def RCuad(self):
        return regress_tes.RCuad(self)
    
    def RCuadAdjust(self):
        return regress_tes.RCuadAdjust(self)
    
    def FStadistic(self):
        return regress_tes.FStadistic(self)
    
    def PValue(self):
        return regress_tes.PValue(self)
    
    def MSEModel(self):
        return regress_tes.MSEModel(self)
    
    def MSEResidual(self):
        return regress_tes.MSEResidual(self)
    
    def MSETotal(self):
        return regress_tes.MSETotal(self)
    
    def RMSEModel(self):
        return regress_tes.RMSEModel(self)
    
        
    
    
        
    
     
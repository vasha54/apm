from model.modelLMR import ModelLMR

class ManagerModel:
    def __init__(self):
        self.dictModel={}
        
    def addModel(self,_model):
        if self.canAddThisModel(_model):
            self.dictModel[_model.getIDModel()]=_model
    
    def removeModel(self,_key):
        if _key in self.dictModel.keys():
            self.dictModel.pop(_key)
        
    def isValidSetModelStatic(self,_models):
        isValid = True
        cCount =len(_models)
        for i in range(0,cCount):
            for j in range(i+1,cCount):
                if _models[i] == _models[j]:
                    isValid = True
        return isValid
    
    def canAddThisModel(self,_model):
        can = True
        for k,v in self.dictModel.items():
            if v == _model:
                can = False
        return can 
    
    def countModels(self):
        return len(self.dictModel.keys())
    
    def getKeysModels(self):
        return self.dictModel.keys()
    
    def getDataModel(self,_keyModel, _attr):
        data = ''
        if _keyModel in self.dictModel.keys():
            if _attr == ModelLMR.NAME:
                data = self.dictModel[_keyModel].getNameModel()
            elif _attr == ModelLMR.NAME_VD:
                data = self.dictModel[_keyModel].getNameVariableD()
            elif _attr == ModelLMR.NUMBER_MEAS:
                data = self.dictModel[_keyModel].numberMeasurement()
            elif _attr == ModelLMR.GL_RESIDUAL:
                data = self.dictModel[_keyModel].glResidual()
            elif _attr == ModelLMR.GL_MODEL:
                data = self.dictModel[_keyModel].glModel()
            elif _attr == ModelLMR.AIC:
                data = self.dictModel[_keyModel].aic()
            elif _attr == ModelLMR.BIC:
                data = self.dictModel[_keyModel].bic()
            elif _attr == ModelLMR.LOG_LIKELI_HEAD:
                data = self.dictModel[_keyModel].logLikeliHead()
            elif _attr == ModelLMR.RCUAD:
                data = self.dictModel[_keyModel].RCuad()
            elif _attr == ModelLMR.RCUAD_ADJUST:
                data = self.dictModel[_keyModel].RCuadAdjust()
            elif _attr == ModelLMR.FSTADISTIC:
                data = self.dictModel[_keyModel].FStadistic()
            elif _attr == ModelLMR.PVALUE:
                data = self.dictModel[_keyModel].PValue()
            elif _attr == ModelLMR.MSE_MODEL:
                data = self.dictModel[_keyModel].MSEModel()
            elif _attr == ModelLMR.MSE_RESIDUAL:
                data = self.dictModel[_keyModel].MSEResidual()
            elif _attr == ModelLMR.MSE_TOTAL:
                data = self.dictModel[_keyModel].MSETotal()
            elif _attr == ModelLMR.RMSE_MODEL:
                data = self.dictModel[_keyModel].RMSEModel()   
        return data
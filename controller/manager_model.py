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
            print(_attr,'line40')
            if _attr == ModelLMR.NAME:
                data = self.dictModel[_keyModel].getNameModel()
            elif _attr == ModelLMR.NAME_VD:
                data = self.dictModel[_keyModel].getNameVariableD()
            elif _attr == ModelLMR.NUMBER_MEAS:
                data = self.dictModel[_keyModel].numberMeasurement()
            elif _attr == ModelLMR.GL_RESIDUAL:
                data = self.dictModel[_keyModel].glResidual()    
        return data
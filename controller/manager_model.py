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
    
    def setSelectModel(self,_key):
        for key in self.dictModel.keys():
            if key != _key:
                self.dictModel[key].setIsSelect(False)
            else:
                self.dictModel[key].setIsSelect(True)
                
    def getKeyModelSelect(self):
        key =''
        for k in self.dictModel.keys():
            if self.dictModel[k].isSelect() == True:
                key = k
        return key
    
    def getDataModel(self,_keyModel, _method,**kwargs):
        data = ''
        if _keyModel in self.dictModel.keys():
            data = getattr(self.dictModel[_keyModel],_method)(**kwargs)
        return data
    
    def getThisModel(self,_key):
        model = None
        if _key in self.dictModel.keys():
            model = self.dictModel[_key]
        return model
       

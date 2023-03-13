from pattern.singleton import SingletonMeta

from controller.manager_model import ManagerModel
from controller.manager_variable import ManagerVariable

from model.modelLMR import ModelLMR

from util.read_excel import ReadExcel
import pandas as pd


class AnalysisData(metaclass=SingletonMeta):
    
    def __init__(self):
        self.handlerExcel = ReadExcel()
        self.variablesSelect = []
        self.correlactions = []
        self.managerModels = ManagerModel()
        self.managerVariable = ManagerVariable()
    
    def readFileExcel(self, _filename):
        self.handlerExcel.readData(_filename)
        self.handlerExcel.filterData()
        dataFrameClean = self.handlerExcel.getDataFrameFilter()
        self.managerVariable.setDataFrameVariable(dataFrameClean)
        
    def getNamesVariables(self):
        return self.managerVariable.getNamesVariables()
    
    def getDataFrame(self):
        return self.managerVariable.getDataFrame()
    
    def getVariablesSelect(self):
        return self.variablesSelect
     
    def addVariablesSelect(self,_variable):
        if _variable not in self.variablesSelect:
            self.variablesSelect.append(_variable)
    
    def removeVariablesSelect(self,_variable):
        if _variable in self.variablesSelect:
            self.variablesSelect.remove(_variable)
    
    def hasVariablesSelect(self):
        if len(self.variablesSelect) >= 2 :
            return True
        return False
    
    def getThisCorrelation(self,_pos):
        if len(self.correlactions) > _pos and _pos >=0:
            return self.correlactions[_pos]
        else:
            return None
    
    def getCorrelationVariablesSelect(self):
        self.correlactions = []
        for i in range(0,len(self.variablesSelect)):
            for j in range(i+1,len(self.variablesSelect)):
                correlactionIJ = {
                    'label-x':self.variablesSelect[i],
                    'label-y':self.variablesSelect[j],
                    'data-x':self.managerVariable.getDataVariable(self.variablesSelect[i],ManagerVariable.VALUES_VAR),
                    'data-y':self.managerVariable.getDataVariable(self.variablesSelect[j],ManagerVariable.VALUES_VAR),
                }
                
                # correlactionJI = {
                #     'label-x':self.variablesSelect[j],
                #     'label-y':self.variablesSelect[i],
                #     'data-x':self.dataFrameClean[self.variablesSelect[j]],
                #     'data-y':self.dataFrameClean[self.variablesSelect[i]],
                # }
                
                self.correlactions.append(correlactionIJ)
                # self.correlactions.append(correlactionJI)
        
        return self.correlactions
    
    def addModel(self,_model):
        nameVD = _model.getNameVariableD() 
        namesVI = _model.getNamesVariableI()
        
        valueD ={ nameVD : self.getDataVariable(nameVD,ManagerVariable.VALUES_VAR)}
        valueI = {}
        valueM = {}
        valueM[nameVD] = self.getDataVariable(nameVD,ManagerVariable.VALUES_VAR)
        
        for nVI in namesVI:
            valueI[nVI] = self.getDataVariable(nVI, ManagerVariable.VALUES_VAR)
            valueM[nVI] = self.getDataVariable(nVI, ManagerVariable.VALUES_VAR)
        
        dataFrameVD = pd.DataFrame(valueD)
        dataFrameVI = pd.DataFrame(valueI)
        dataFrameM  = pd.DataFrame(valueM)
        
        _model.setDataFrameVD(dataFrameVD)
        _model.setDataFrameVI(dataFrameVI)
        _model.setDataFrameModel(dataFrameM)
        
        self.managerModels.addModel(_model)
    
    def removeModel(self,_key):
        self.managerModels.removeModel(_key)
    
    def isValidSetModelStatic(self,_models):
        return self.managerModels.isValidSetModelStatic(_models)
    
    def countModels(self):
        return self.managerModels.countModels()
    
    def getKeysModels(self):
        return self.managerModels.getKeysModels()
    
    def getDataModel(self, _keyModel, _method, **kwargs):
        return self.managerModels.getDataModel( _keyModel, _method, **kwargs)
    
    def setSelectModel(self,_key):
        self.managerModels.setSelectModel(_key)
        
    def getKeyModelSelect(self):
        return self.managerModels.getKeyModelSelect()
    
    def canAddThisModel(self,model):
        return self.managerModels.canAddThisModel(model)
    
    def getThisModel(self,_key):
        return self.managerModels.getThisModel(_key)
    
    def getDataVariable(self,_nameVar, _method, **kwargs):
        return self.managerVariable.getDataVariable(_nameVar,_method,**kwargs)
    
    def tableCorrelations(self):
        return self.managerVariable.tableCorrelations(self.variablesSelect)
    
    def addKeyModelCompare(self,_keyModel):
        self.managerModels.addKeyModelCompare(_keyModel)
        
    def removeKeyModelCompare(self,_keyModel):
        self.managerModels.removeKeyModelCompare(_keyModel)
        
    def getKeyModelCompare(self):
        return self.managerModels.getKeyModelCompare()
    
    def getKeyNameModels(self):
        return self.managerModels.getKeyNameModels()
    
    def getDataFrameComparativeModel(self):
        data={'models':[],
              'R-Cuadrado':[],
              'AIC':[],
              'Log-likehead':[],
              'R-cuadrado adjustado':[],
              'RSME':[],
              'BIC':[]}
        
        keyModelsCompare = self.managerModels.getKeyModelCompare()
        
        for key in keyModelsCompare:
            data['models'].append(self.managerModels.getDataModel(key,ModelLMR.NAME))
            data['R-Cuadrado'].append(self.managerModels.getDataModel(key,ModelLMR.RCUAD))
            data['AIC'].append(self.managerModels.getDataModel(key, ModelLMR.AIC))
            data['Log-likehead'].append(self.managerModels.getDataModel(key,ModelLMR.LOG_LIKELI_HEAD))
            data['R-cuadrado adjustado'].append(self.managerModels.getDataModel(key,ModelLMR.RCUAD_ADJUST))
            data['RSME'].append(self.managerModels.getDataModel(key,ModelLMR.RMSE_MODEL))
            data['BIC'].append(self.managerModels.getDataModel(key,ModelLMR.BIC))
        
        data['AIC']=self.sortIndicators(data['AIC'],False)
        data['RSME']=self.sortIndicators(data['RSME'],False)
        data['BIC']=self.sortIndicators(data['BIC'],False)
        data['R-Cuadrado']=self.sortIndicators(data['R-Cuadrado'],False)
        data['R-cuadrado adjustado']=self.sortIndicators(data['R-cuadrado adjustado'],False)
        data['Log-likehead']=self.sortIndicators(data['Log-likehead'],False)
        
        df = pd.DataFrame(data)
        return df
    
    def sortIndicators(self,listIndicators,orderCre=True):
        listOrder = []
        
        if orderCre == True:
            for x in listIndicators:
                listOrder.append(sum(i < x for i in listIndicators)+1)
        else:
            for x in listIndicators:
                listOrder.append(sum(i > x for i in listIndicators)+1)
        
        print(listIndicators)
        print(listOrder)
        
        listIndicators = listOrder
        return listIndicators
#         df = pd.DataFrame({
# 'models': ['Model 1', 'Modelo 2','Modelo 3', 'Modelo 4', 'Modelo 5', 'Modelo 6'],
# 'R-Cuadrado': [3, 1, 0, 4, 3, 4],
# 'AIC': [2, 1, 6, 3, 2, 2],
# 'Log-likehead': [0, 3, 2, 4, 4, 4],
# 'R-cuadrado adjustado': [2, 1, 3, 4, 2,1],
# 'RSME': [2, 5, 3, 4, 3, 1],
# 'BIC': [2, 2, 3, 4, 3, 2]
# })
        
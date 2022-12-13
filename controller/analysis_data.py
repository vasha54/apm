from pattern.singleton_meta import SingletonMeta

from controller.manager_model import ManagerModel
from controller.manager_variable import ManagerVariable

from util.read_excel import ReadExcel
import pandas as pd


class AnalysisData(metaclass=SingletonMeta):
    
    def __init__(self):
        self.handlerExcel = ReadExcel()
        self.dataFrameClean = pd.DataFrame()
        self.variablesSelect = []
        self.correlactions = []
        self.managerModels = ManagerModel()
        self.managerVariable = ManagerVariable()
    
    def readFileExcel(self, _filename):
        self.handlerExcel.readData(_filename)
        self.handlerExcel.filterData()
        self.dataFrameClean = self.handlerExcel.getDataFrameFilter()
        self.managerVariable.setDataFrameVariable(self.dataFrameClean)
        
    def getNamesVariables(self):
        return list(self.dataFrameClean.columns.values)
    
    def getDataFrame(self):
        return self.dataFrameClean
    
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
                    'data-x':self.dataFrameClean[self.variablesSelect[i]],
                    'data-y':self.dataFrameClean[self.variablesSelect[j]],
                }
                
                correlactionJI = {
                    'label-x':self.variablesSelect[j],
                    'label-y':self.variablesSelect[i],
                    'data-x':self.dataFrameClean[self.variablesSelect[j]],
                    'data-y':self.dataFrameClean[self.variablesSelect[i]],
                }
                
                self.correlactions.append(correlactionIJ)
                self.correlactions.append(correlactionJI)
        
        return self.correlactions
    
    def addModel(self,_model):
        nameVD = _model.getNameVariableD() 
        namesVI = _model.getNamesVariableI()
        
        valueD ={ nameVD : self.dataFrameClean[nameVD]}
        valueI = {}
        valueM = {}
        valueM[nameVD] = self.dataFrameClean[nameVD]
        
        for nVI in namesVI:
            valueI[nVI] = self.dataFrameClean[nVI]
            valueM[nVI] = self.dataFrameClean[nVI]
        
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
            
        
from pattern.singleton_meta import SingletonMeta

from util.read_excel import ReadExcel
import pandas as pd


class AnalysisData(metaclass=SingletonMeta):
    
    def __init__(self):
        self.handlerExcel = ReadExcel()
        self.dataFrameClean = pd.DataFrame()
        self.variablesSelect = []
        self.correlactions = []
    
    def readFileExcel(self, _filename):
        self.handlerExcel.readData(_filename)
        self.handlerExcel.filterData()
        self.dataFrameClean = self.handlerExcel.getDataFrameFilter()
        
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
     
            
        
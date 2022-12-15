
import pandas as pd
import numpy as np

from libmath import regress_tes

class ManagerVariable:
    
    MEAN = 'mean'
    MIN = 'minVar'
    MAX = 'maxVar'
    COUNT_MEAS = 'countMeas'
    CV = 'cv'
    STD = 'std'
    VARIANZA ='varianza'
    MEDIAN = 'median'
    VALUES_VAR = 'getValuesThisVariable'
    
    def __init__(self):
        self.dataFrameVariable=pd.DataFrame()
        
    def setDataFrameVariable(self,_dataFrameVariable):
        self.dataFrameVariable =_dataFrameVariable
        
    def getDataVariable(self,_nameVar, _method, **kwargs):
        data = ''
        if _nameVar in self.dataFrameVariable:
            data = getattr(regress_tes,_method)(nameVar=_nameVar,dataFrame=self.dataFrameVariable)
        return data
    
    def getNamesVariables(self):
        return list(self.dataFrameVariable.columns.values)
    
    def getDataFrame(self):
        return self.dataFrameVariable
    
    def getDataFrameThisVar(self,_listNameVar):
        dictVAR = {}
        for var in _listNameVar:
            if var in self.dataFrameVariable:
                dictVAR[var]=self.dataFrameVariable[var] 
        dataFrame = pd.DataFrame(dictVAR)
        return dataFrame
    
    def tableCorrelations(self,_listNameVar):
        dataFrame = self.getDataFrameThisVar(_listNameVar)
        table = np.corrcoef(dataFrame)
        return table
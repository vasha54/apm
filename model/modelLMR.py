import pandas as pd

class ModelLMR:
    
 
    def __init__(self,_idModel,_nameModel,_nameVariableD,_namesVariablesI, _dataFrameVI=pd.DataFrame(), _dataFrameVD=pd.DataFrame(), *args, **kwargs):
        super(ModelLMR, self).__init__(*args, **kwargs)
        self.idModel = _idModel
        self.nameModel= _nameModel
        self.nameVariableD = _nameVariableD
        self.namesVariableI = []
        for name in _namesVariablesI:
            self.namesVariableI.append(name)
        self.dataFrameVI = _dataFrameVI
        self.dataFrameVD = _dataFrameVD
        self.modelStr = self.nameModel+"("+self.nameVariableD+"~"
        for c in range(0,len(self.namesVariableI)):
            if c == 0:
                self.modelStr = self.modelStr+str(self.namesVariableI[c])
            else:
                self.modelStr = self.modelStr+"+"+str(self.namesVariableI[c])
        self.modelStr=self.modelStr+")"
        
    def __str__(self):
        modelStr = self.nameModel+"("+self.nameVariableD+"~"
        union="+"
        union=union.join(self.namesVariableI)
        modelStr=modelStr+union+")"
        return modelStr
        
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
    
    def setNameModel(self, _nameModel):
        self.nameModel = _nameModel
    
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
        
    
    
        
    
     
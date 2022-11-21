import pandas as pd

class ReadExcel:
    def __init__(self):
        self.dataFrame = None
        self.dataFrameFilter = None
        
    def getDataFrameFilter(self):
        return self.dataFrameFilter
    
    def readData(self, _filename):
        self.dataFrame = pd.read_excel(_filename)

    def filterData(self):
        columnsName=list(self.dataFrame.columns.values)
        
        maxRow=-1
        
        for column in columnsName:
            valuesNoNull = self.dataFrame[column].notnull()
            countValuesValid = sum(valuesNoNull)
            if maxRow == -1:
                maxRow = countValuesValid
            maxRow = min(maxRow,countValuesValid)
            
        dataFilter ={}
            
        for column in columnsName:
            values = self.dataFrame[column]
            valuesNoNull = self.dataFrame[column].notnull()
            valuesFilter = []
            
            for i in range(0,len(values)):
                if valuesNoNull[i] == True and len(valuesFilter) < maxRow:
                    valuesFilter.append(values[i])
                    
            dataFilter[column]=valuesFilter
            
        self.dataFrameFilter = pd.DataFrame(dataFilter)
            
from PyQt5.QtCore import(
    QAbstractTableModel, QVariant, QAbstractItemModel, 
)

from PyQt5 import QtCore ,Qt

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class LimitVariableInpendentModel(QAbstractTableModel):
    def __init__(self,_keyModel, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.headersName=['Variables', 'Límite inferior', 'Limite superior']
        self.keyModel = _keyModel
        self.namesVarI = AnalysisData().getDataModel(self.keyModel,ModelLMR.ALL_NAME_VARI)
        

    def rowCount(self, parent=None):
        return len(self.namesVarI)

    def columnCount(self, parent=None):
        return 3

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
                varI = self.namesVarI[index.row()]
                if index.column() == 0:
                    return QVariant(varI)
                elif index.column() == 1:
                    limitLower = AnalysisData().getDataModel(self.keyModel,ModelLMR.LOWER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI)
                    return QVariant(limitLower)
                elif index.column() ==2:
                    limitUpper = AnalysisData().getDataModel(self.keyModel,ModelLMR.UPPER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI)
                    return QVariant(limitUpper)
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        return QVariant()
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.headersName[section])
        
    def flags(self,index):
        if index.isValid() == False or index.column()==0:
            return super().flags(index)
        else:
            return (super().flags(index) | QtCore.Qt.ItemIsEditable)
        
    
    def setData(self,_index,_value,_role):
        if _index.isValid():
            if _role == QtCore.Qt.EditRole:
                if isinstance(_value, (int)):
                    value = float(_value)
                    varI = self.namesVarI[_index.row()]
                    if _index.column() == 1:
                        AnalysisData().getDataModel(self.keyModel,ModelLMR.SET_LOWER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI,newValue=value)
                    elif _index.column() == 2:
                        AnalysisData().getDataModel(self.keyModel,ModelLMR.SET_UPPER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI,newValue=value)
                return True
        return False
       
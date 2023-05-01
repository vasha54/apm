from PyQt5.QtCore import(
  QVariant,QAbstractTableModel
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui, Qt

from controller.analysis_data import AnalysisData 

from model.modelLMR import ModelLMR

from view.preferences.preferences import PreferenceGUI

class ModelIntervalCoeffRegressModel(QAbstractTableModel):
    
    def __init__(self,_keyModel, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.keyModel=_keyModel
        self.namesSectionHeader=['Término','Límite inferior','Límite superior']
        self.terms =['Intercepto']
        self.terms = self.terms+AnalysisData().getDataModel(self.keyModel,ModelLMR.ALL_NAME_VARI)
        self.lowerLimit = AnalysisData().getDataModel(self.keyModel,ModelLMR.LOWER_LIMIT_VAR)
        self.upperLimit = AnalysisData().getDataModel(self.keyModel,ModelLMR.UPPER_LIMIT_VAR)
        self.decimalPlaces = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        self.formatStr = '.'+str(self.decimalPlaces)+'f'
        
    def rowCount(self, parent=None):
        return  len(self.terms)

    def columnCount(self, parent=None):
        return 3
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.namesSectionHeader[section])
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole :
                if index.column() == 0:
                    return QVariant(str(self.terms[index.row()]))
                elif index.column() == 1 :
                    return QVariant(str(format(self.lowerLimit[index.row()],self.formatStr)))
                elif index.column() == 2 :
                    return QVariant(str(format(self.upperLimit[index.row()],self.formatStr)))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        return QVariant()
    
    
    
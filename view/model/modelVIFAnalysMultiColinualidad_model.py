from PyQt5.QtCore import(
  QVariant,QAbstractTableModel
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui, Qt

from controller.analysis_data import AnalysisData 

from model.modelLMR import ModelLMR
from controller.analysis_data import AnalysisData

from view.preferences.preferences import PreferenceGUI


class ModelVIFAnalysMultiColinualidadModel(QAbstractTableModel):
    
    def __init__(self,_keyModel, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.keyModel=_keyModel
        self.namesSectionHeaderV = AnalysisData().getDataModel(self.keyModel,ModelLMR.ALL_NAME_VAR)
        self.valuesVIF =  AnalysisData().getDataModel(self.keyModel,ModelLMR.ANALYSIS_MULTICOLINIALIDAD)
        self.decimalPlaces = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        self.formatStr = '.'+str(self.decimalPlaces)+'f'     

        
        
    def rowCount(self, parent=None):
        return  1

    def columnCount(self, parent=None):
        if self.namesSectionHeaderV != None:
            return len(self.namesSectionHeaderV)
        return 0
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction == QtCore.Qt.Horizontal and section < len(self.namesSectionHeaderV):
            return QtCore.QVariant(self.namesSectionHeaderV[section])
        elif direction == QtCore.Qt.Vertical:
            return QtCore.QVariant("VIF")
        
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole :
                return QVariant(str(format(self.valuesVIF[index.column()],self.formatStr)))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        return QVariant()
    
    
    
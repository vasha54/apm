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

class ModelResultRegressModel(QAbstractTableModel):
    
    def __init__(self,_keyModel, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.keyModel=_keyModel
        self.namesSectionHeader=['Termino','Coeficiente','std error','t','P-valor']
        self.terms =['Intercepto']
        self.terms = self.terms+AnalysisData().getDataModel(self.keyModel,ModelLMR.ALL_NAME_VARI)
        self.coeff = AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_VAR)
        self.stderr = AnalysisData().getDataModel(self.keyModel,ModelLMR.STD_ERR)
        self.tc = AnalysisData().getDataModel(self.keyModel,ModelLMR.TC)
        self.pvalor =AnalysisData().getDataModel(self.keyModel,ModelLMR.PV_COEFF)
        self.decimalPlaces = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        self.formatStr = '.'+str(self.decimalPlaces)+'f'

    def rowCount(self, parent=None):
        return len(self.terms)

    def columnCount(self, parent=None):
        return 5
    
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
                    return QVariant(str(format(self.coeff[index.row()],self.formatStr)))
                elif index.column() == 2 :
                    return QVariant(str(format(self.stderr[index.row()],self.formatStr)))
                elif index.column() == 3 :
                    return QVariant(str(format(self.tc[index.row()],self.formatStr)))
                elif index.column() == 4 :
                    return QVariant(str(format(self.pvalor[index.row()],self.formatStr)))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        return QVariant()
    
    
    
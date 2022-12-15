from PyQt5.QtCore import(
  QVariant,QAbstractTableModel
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui, Qt

from controller.analysis_data import AnalysisData 

from model.modelLMR import ModelLMR


class TableCorrelationModel(QAbstractTableModel):
    
    def __init__(self,_headersVar,_data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.headersVar = _headersVar
        self.data =_data 

    def rowCount(self, parent=None):
        return len(self.headersVar)

    def columnCount(self, parent=None):
        return len(self.headersVar)
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal or direction == QtCore.Qt.Vertical:
            return QtCore.QVariant(self.headersVar[section])
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole :
                return QVariant(str( round(self.data[index.row()][index.column()],3) ))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        return QVariant()
    
    
    
from PyQt5.QtCore import(
    QAbstractTableModel, QVariant, QAbstractItemModel, 
)

from PyQt5 import QtCore ,Qt

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class PointsExtrapolationModel(QAbstractTableModel):
    
    def __init__(self,_keyModel,_matrizPoints, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.keyModel = _keyModel
        self.headersName = AnalysisData().getDataModel(self.keyModel,ModelLMR.ALL_NAME_VARI)
        self._data = _matrizPoints
        
    def rowCount(self, parent=None):
        return len(self.headersName)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QVariant(str(
                    self._data.iloc[index.row()][index.column()]))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        return QVariant()
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.headersName[section])
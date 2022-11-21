from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox
)

from PyQt5.QtCore import(
    QAbstractTableModel, QVariant
)

from PyQt5 import QtCore 

class DataFrameModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QVariant(str(
                    self._data.iloc[index.row()][index.column()]))
        return QVariant()
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal:
            return QtCore.QVariant(list(self._data.columns.values)[section])
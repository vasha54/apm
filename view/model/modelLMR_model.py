from PyQt5.QtCore import(
  QVariant
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui 

class ModelLMRModel(QStandardItemModel):
    def __init__(self, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.data = {}

    def rowCount(self, parent=None):
        return len(self.data.keys())

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole and len(self.data.keys()) > index.row():
                key = list(self.data.keys())[index.row()]
                model = self.data[key]
                return QVariant(str(model))
        return QVariant()
    
    def addElement(self,_model):
        self.data[_model.getIDModel()]=_model
        item = QtGui.QStandardItem(str(_model))
        self.appendRow(item)
        
    def revomeElement(self,_index):
        if 0 <=_index.row() and _index.row() <len(self.data.keys()):
            key = list(self.data.keys())[_index.row()]
            self.removeRow(_index.row())
            self.data.pop(key)
        
    def getElements(self):
        return self.data
    
    def getThisModel(self,_index):
        if 0 <= _index.row() and _index.row() < len(self.data.keys()):
           key = list(self.data.keys())[_index.row()]
           return self.data[key]
        return None
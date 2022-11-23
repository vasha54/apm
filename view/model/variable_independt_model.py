from PyQt5.QtCore import(
  QVariant
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui 

class VariableIndependtModel(QStandardItemModel):
    def __init__(self, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.data = []

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            
            if role == QtCore.Qt.DisplayRole and len(self.data) > index.row():
                return QVariant(self.data[index.row()])
        return QVariant()
    
    def addElement(self,_element):
        self.data.append(_element)
        item = QtGui.QStandardItem(_element)
        self.appendRow(item)
        
    def revomeElement(self,_element):
        index = self.data.index(_element)
        self.removeRow(index)
        self.data.remove(_element)
        
    def getElements(self):
        return self.data
    
    def clear(self):
        self.data.clear()
        super().clear()
        
    
from PyQt5.QtCore import(
  QVariant
)

from PyQt5.QtGui import (
    QStandardItemModel
)

from PyQt5 import QtCore, QtGui 

from controller.analysis_data import AnalysisData

class ModelLMRModel(QStandardItemModel):
    
    KEY = 'key'
    NAME = 'name'
    
    def __init__(self, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.analysData = AnalysisData()

    def rowCount(self, parent=None):
        return len(self.analysData.getKeysModels())

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole and len(self.analysData.getKeysModels()) > index.row():
                key = list(self.analysData.getKeysModels())[index.row()]
                model = self.analysData.getThisModel(key)
                return QVariant(str(model))
        return QVariant()
    
    def addElement(self,_model):
        if self.analysData.canAddThisModel(_model) == True:
            self.analysData.addModel(_model)
            item = QtGui.QStandardItem(str(_model))
            self.appendRow(item)
        
        
    def clearElements(self):
        pass
        
    def revomeElement(self,_index):
        if 0 <=_index.row() and _index.row() <len(self.analysData.getKeysModels()):
            key = list(self.analysData.getKeysModels())[_index.row()]
            self.removeRow(_index.row())
            self.analysData.removeModel(key)
        
    def getElements(self):
        return self.analysData.getKeysModels()
    
    def getThisModel(self,_index):
        if 0 <= _index.row() and _index.row() < len(self.analysData.getKeysModels()):
           key = list(self.analysData.getKeysModels())[_index.row()]
           return self.analysData.getThisModel(key)
        return None
    
    def canAddThisModel(self,_model):
        return self.analysData.canAddThisModel(_model)
    
    
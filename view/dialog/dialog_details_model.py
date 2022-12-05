from PyQt5.QtWidgets import (
    QAbstractItemView, QGridLayout,QHBoxLayout, QVBoxLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem, QDoubleSpinBox, QListView,
    QPushButton,QDialog
)

from PyQt5.QtGui import (
    QFont, 
)

from PyQt5.QtCore import(
    QSize
)

from PyQt5 import QtCore, QtGui, QtWidgets

from view.ui.dialog_details_model_ui import Ui_DialogDetailsModel

from view.model.data_frame_model import DataFrameModel

class DialogDetailsModel(QDialog,Ui_DialogDetailsModel):
    
    def __init__(self,_model,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.model = _model
        self.createWorkSpace()
        
    def createWorkSpace(self):
        self.lONameModel.setText(self.model.getNameModel())
        self.lONameVarD.setText(self.model.getNameVariableD())
        self.lOIntervalConfidence.setText(str(self.model.getIntervalConfidence()))
        self.modelVI = QtGui.QStandardItemModel(self.listViewVI)
        variablesI = self.model.getNamesVariableI()
        for line in variablesI:
            itemVI = QtGui.QStandardItem(line)
            self.modelVI.appendRow(itemVI)

        self.listViewVI.setModel(self.modelVI)
        
        self.modelDataFrame = DataFrameModel(self.model.getDataFrameModel(),self.tableViewMeasVariables)
        self.tableViewMeasVariables.setModel(self.modelDataFrame)
        self.tableViewMeasVariables.verticalHeader().hide()
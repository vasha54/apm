from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore, QtGui, QtWidgets

from view.ui.tab_data_filter_ui import Ui_WidgetDataFilter
from view.delegate.delegate import ListView
from controller.analysis_data import AnalysisData

from view.model.data_frame_model import DataFrameModel
from view.view.widget_tab import WidgetTab

class WidgetDataFilter(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createWorkspace()
        
    def setupUi(self, WidgetDataFilter):
        WidgetDataFilter.setObjectName("WidgetDataFilter")
        WidgetDataFilter.resize(696, 471)
        self.gridLayout = QtWidgets.QGridLayout(WidgetDataFilter)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableViewDataFrame = QtWidgets.QTableView(WidgetDataFilter)
        self.tableViewDataFrame.setMinimumSize(QtCore.QSize(600, 0))
        self.tableViewDataFrame.setObjectName("tableViewDataFrame")
        self.verticalLayout.addWidget(self.tableViewDataFrame)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listViewVariable = ListView(WidgetDataFilter)
        self.listViewVariable.setMaximumWidth(260)
        self.label_2.setMaximumWidth(260)
        self.listViewVariable.setObjectName("listViewVariable")
        self.verticalLayout_2.addWidget(self.listViewVariable)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonNext = QtWidgets.QPushButton(WidgetDataFilter)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.label.setText( "Datos Iniciales")
        self.label_2.setText( "Selecciones las variables del modelaje")
        self.pushButtonNext.setText( "Siguiente paso")
        self.pushButtonNext.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(WidgetDataFilter)
        
    def createWorkspace(self):
        
        self.model = QtGui.QStandardItemModel(self.listViewVariable)
        namesVariable = AnalysisData().getNamesVariables()
        for line in namesVariable:
            self.item = QtGui.QStandardItem(line)
            self.item.setCheckable(True)
            self.item.setCheckState(QtCore.Qt.Unchecked)
            self.model.appendRow(self.item)

        self.listViewVariable.setModel(self.model)
        modelData =DataFrameModel(AnalysisData().getDataFrame(),self.tableViewDataFrame)
        self.tableViewDataFrame.setModel(modelData)
        self.createConnect()
        
        
    
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def onChecked(self, index):
        item = self.model.itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            AnalysisData().addVariablesSelect(item.text())
        else:
            AnalysisData().removeVariablesSelect(item.text())    
        self.pushButtonNext.setEnabled(AnalysisData().hasVariablesSelect())
        
    
    def createConnect(self):
        self.listViewVariable.checked.connect(self.onChecked)
        self.pushButtonNext.clicked.connect(self.clickNextStage)
    
    def update(self):
        pass
from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore, QtGui, QtWidgets

from view.components.list_view import ListViewCheckBox
from controller.analysis_data import AnalysisData

from view.model.data_frame_model import DataFrameModel
from view.view.widget_tab.widget_tab import WidgetTab

class WidgetDataFilter(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        
    def createUI(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetCentral)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableViewDataFrame = QtWidgets.QTableView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewDataFrame.sizePolicy().hasHeightForWidth())
        self.tableViewDataFrame.setSizePolicy(sizePolicy)
        self.tableViewDataFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewDataFrame.setObjectName("tableViewDataFrame")
        self.verticalLayout.addWidget(self.tableViewDataFrame)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listViewVariable = ListViewCheckBox(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewVariable.sizePolicy().hasHeightForWidth())
        self.listViewVariable.setSizePolicy(sizePolicy)
        self.listViewVariable.setMinimumSize(QtCore.QSize(250, 0))
        self.listViewVariable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listViewVariable.setObjectName("listViewVariable")
        self.verticalLayout_2.addWidget(self.listViewVariable)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label.setText("Datos Iniciales")
        self.label_2.setText("Selecciones las variables del modelo")
        self.tableViewDataFrame.verticalHeader().hide()
        
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
        self.tableViewDataFrame.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewDataFrame.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.pushButtonNext.setEnabled(False)
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
        super().createConnect()
        self.listViewVariable.checked.connect(self.onChecked)
        
    
    def updateTab(self):
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
        self.pushButtonNext.setEnabled(False)
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QVBoxLayout, QLayout, QLabel, QSizePolicy, QTableView,
    QSpacerItem, QGroupBox, QHBoxLayout
)

from PyQt5.QtGui import (
    QFont
)

from PyQt5.QtCore import (
    QSize
)

from PyQt5 import QtCore, QtGui, QtWidgets

from view.components.list_view import ListViewCheckBox
from controller.analysis_data import AnalysisData, ManagerVariable

from view.model.data_frame_model import DataFrameModel
from view.view.widget_tab.widget_tab import WidgetTab

class WidgetDataFilter(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        
    def createUI(self):
        self.horizontalLayout = QHBoxLayout(self.widgetCentral)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.widgetCentral)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.tableViewDataFrame = QTableView(self.widgetCentral)
        self.tableViewDataFrame.setObjectName(u"tableViewDataFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableViewDataFrame.sizePolicy().hasHeightForWidth())
        self.tableViewDataFrame.setSizePolicy(sizePolicy1)
        self.tableViewDataFrame.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.tableViewDataFrame)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_5 = QSpacerItem(426, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widgetCentral)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.listViewVariable = ListViewCheckBox(self.widgetCentral)
        self.listViewVariable.setObjectName(u"listViewVariable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listViewVariable.sizePolicy().hasHeightForWidth())
        self.listViewVariable.setSizePolicy(sizePolicy3)
        self.listViewVariable.setMinimumSize(QSize(250, 0))
        self.listViewVariable.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.listViewVariable)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.gBVariable = QGroupBox(self.widgetCentral)
        self.gBVariable.setObjectName(u"gBVariable")
        sizePolicy3.setHeightForWidth(self.gBVariable.sizePolicy().hasHeightForWidth())
        self.gBVariable.setSizePolicy(sizePolicy3)
        self.gBVariable.setFont(font)
        self.gridLayout = QGridLayout(self.gBVariable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lOMin = QLabel(self.gBVariable)
        self.lOMin.setObjectName(u"lOMin")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.lOMin.setFont(font1)

        self.gridLayout.addWidget(self.lOMin, 2, 4, 1, 1)

        self.label_10 = QLabel(self.gBVariable)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.lOVarianza = QLabel(self.gBVariable)
        self.lOVarianza.setObjectName(u"lOVarianza")
        self.lOVarianza.setFont(font1)

        self.gridLayout.addWidget(self.lOVarianza, 2, 1, 1, 1)

        self.lOCV = QLabel(self.gBVariable)
        self.lOCV.setObjectName(u"lOCV")
        self.lOCV.setFont(font1)

        self.gridLayout.addWidget(self.lOCV, 1, 1, 1, 1)

        self.lOMedian = QLabel(self.gBVariable)
        self.lOMedian.setObjectName(u"lOMedian")
        self.lOMedian.setFont(font1)

        self.gridLayout.addWidget(self.lOMedian, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(71, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.label_5 = QLabel(self.gBVariable)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gBVariable)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(71, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.label_9 = QLabel(self.gBVariable)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_7 = QLabel(self.gBVariable)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.lOMedia = QLabel(self.gBVariable)
        self.lOMedia.setObjectName(u"lOMedia")
        self.lOMedia.setFont(font1)

        self.gridLayout.addWidget(self.lOMedia, 0, 1, 1, 1)

        self.lONumberMeas = QLabel(self.gBVariable)
        self.lONumberMeas.setObjectName(u"lONumberMeas")
        self.lONumberMeas.setFont(font1)

        self.gridLayout.addWidget(self.lONumberMeas, 3, 4, 1, 1)

        self.label_8 = QLabel(self.gBVariable)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_6 = QLabel(self.gBVariable)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(71, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.lOMax = QLabel(self.gBVariable)
        self.lOMax.setObjectName(u"lOMax")
        self.lOMax.setFont(font1)

        self.gridLayout.addWidget(self.lOMax, 1, 4, 1, 1)

        self.label_3 = QLabel(self.gBVariable)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(71, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lOSTD = QLabel(self.gBVariable)
        self.lOSTD.setObjectName(u"lOSTD")
        self.lOSTD.setFont(font1)

        self.gridLayout.addWidget(self.lOSTD, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gBVariable, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)
        
        self.tableViewDataFrame.verticalHeader().hide()
        self.label.setText(u"Datos Iniciales")
        self.label_2.setText(u"Selecciones las variables del gr\u00e1fico de correlacion")
        self.gBVariable.setTitle(u"Detalles de la variable")
        self.lOMin.setText(u"NA")
        self.label_10.setText(u"Cant. Obser.")
        self.lOVarianza.setText(u"NA")
        self.lOCV.setText(u"NA")
        self.lOMedian.setText(u"NA")
        self.label_5.setText(u"Varianza")
        self.label_4.setText(u"CV")
        self.label_9.setText(u"M\u00ednimo")
        self.label_7.setText(u"Mediana")
        self.lOMedia.setText(u"NA")
        self.lONumberMeas.setText(u"NA")
        self.label_8.setText(u"M\u00e1ximo")
        self.label_6.setText(u"Desviaci\u00f3n Estandar")
        self.lOMax.setText(u"NA")
        self.label_3.setText(u"Media")
        self.lOSTD.setText(u"NA")
        
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
        self.gBVariable.setVisible(False)
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
        self.listViewVariable.clicked.connect(self.showDetailsVariableSelect)
        
    def showDetailsVariableSelect(self, _index):
        nameVar=_index.data()
        self.lOCV.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.CV)))
        self.lOMax.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.MAX)))
        self.lOMin.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.MIN)))
        self.lOMedia.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.MEAN)))
        self.lOMedian.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.MEDIAN)))
        self.lONumberMeas.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.COUNT_MEAS)))
        self.lOVarianza.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.VARIANZA)))
        self.lOSTD.setText(str(AnalysisData().getDataVariable(nameVar,ManagerVariable.STD)))
        self.gBVariable.setVisible(True)
        
    
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
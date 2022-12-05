from PyQt5.QtWidgets import (
    QWidget,QHeaderView
)

from view.view.widget_tab.widget_tab import WidgetTab
from PyQt5 import QtCore, QtGui, QtWidgets

from model.modelLMR import ModelLMR

from controller.analysis_data import AnalysisData

from view.model.limit_variable_inpendent_model import LimitVariableInpendentModel

class WidgetInformationExtrapolacion(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetCentral)
        self.gridLayout = QtWidgets.QGridLayout()
        self.label = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.tableViewVarIND = QtWidgets.QTableView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewVarIND.sizePolicy().hasHeightForWidth())
        self.tableViewVarIND.setSizePolicy(sizePolicy)
        self.tableViewVarIND.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableViewVarIND.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        # self.tableViewVarIND.setColumnCount(0)
        # self.tableViewVarIND.setRowCount(0)
        self.tableViewVarIND.horizontalHeader().setStretchLastSection(True)
        self.tableViewVarIND.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableViewVarIND, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spBCountLevelN = QtWidgets.QSpinBox(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spBCountLevelN.sizePolicy().hasHeightForWidth())
        self.spBCountLevelN.setSizePolicy(sizePolicy)
        self.spBCountLevelN.setMinimum(2)
        self.spBCountLevelN.setMaximum(10)
        self.spBCountLevelN.setProperty("value", 3)
        self.horizontalLayout_2.addWidget(self.spBCountLevelN)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.pBAnalize = QtWidgets.QPushButton(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBAnalize.sizePolicy().hasHeightForWidth())
        self.pBAnalize.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.pBAnalize)
        spacerItem1 = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.lOMessage = QtWidgets.QLabel(self.widgetCentral)
        self.lOMessage.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lOMessage.setFont(font)
        self.lOMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.lOMessage, 0, 1, 1, 1)
        self.tableViewPointsExtrapolation = QtWidgets.QTableView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewPointsExtrapolation.sizePolicy().hasHeightForWidth())
        self.tableViewPointsExtrapolation.setSizePolicy(sizePolicy)
        self.gridLayout_2.addWidget(self.tableViewPointsExtrapolation, 1, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 311, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.label.setText("Establecer límite de análisis para las variables\n"
"independientes")
        self.label_2.setText("Cantidad de niveles por variable:")
        self.pBAnalize.setText("Analizar")
        self.lOMessage.setText("No se detecta extrapolación oculta")
    
    def createWorkspace(self):
        self.modelLimitVARI = LimitVariableInpendentModel(self.keyModel,self.tableViewVarIND)
        self.tableViewVarIND.setModel(self.modelLimitVARI)
        self.tableViewVarIND.verticalHeader().hide()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewVarIND.sizePolicy().hasHeightForWidth())
        self.tableViewVarIND.setSizePolicy(sizePolicy)
        self.tableViewVarIND.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewVarIND.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hideShowComponentsResult(False)
    
    def createConnect(self):
        self.pBAnalize.clicked.connect(self.analize)
        super().createConnect()
        
    def updateTab(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkspace()
        
    def hideShowComponentsResult(self,_visible):
        self.lOMessage.setVisible(_visible)
        self.tableViewPointsExtrapolation.setVisible(_visible)
        
    def analize(self):
        self.hideShowComponentsResult(False)
        countLevelVar = self.spBCountLevelN.value()
        answer = AnalysisData().getDataModel(self.keyModel,ModelLMR.ANALYSIS_EXTRAPOLATION_HIDE,res=int(countLevelVar))
        self.hideShowComponentsResult(True)
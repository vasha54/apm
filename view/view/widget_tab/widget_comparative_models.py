from view.view.widget_tab.widget_tab import WidgetTab

from controller.analysis_data import AnalysisData

from view.components.widget_validation_boot_stropping import  WidgetValidationBootStropping
from view.components.widget_validation_kold import WidgetValidationKold
from view.preferences.preferences import PreferenceGUI

from PyQt5 import QtCore, QtGui, QtWidgets
class WidgetComparativeModel(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect() 
        self.pushButtonNext.setVisible(False)   
    
    def createUI(self):
        self.gridLayout = QtWidgets.QGridLayout(self.widgetCentral)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)
        self.listViewModel = QtWidgets.QListView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewModel.sizePolicy().hasHeightForWidth())
        self.listViewModel.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.listViewModel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pBCompare = QtWidgets.QPushButton(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBCompare.sizePolicy().hasHeightForWidth())
        self.pBCompare.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.pBCompare)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(488, 5, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.widgetChartComparative = QtWidgets.QWidget(self.widgetCentral)
        self.widgetChartComparative.setStyleSheet("")
        self.vLayoutChartComparative = QtWidgets.QVBoxLayout(self.widgetChartComparative)
        self.gridLayout.addWidget(self.widgetChartComparative, 1, 1, 1, 1)
        self.tableViewModelCom = QtWidgets.QTableView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewModelCom.sizePolicy().hasHeightForWidth())
        self.tableViewModelCom.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.tableViewModelCom, 2, 0, 1, 2)
        self.label.setText("Modelos :")
        self.pBCompare.setText("Comparar")
        
    
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        pass
        
    def updateTab(self):
        pass
    
   
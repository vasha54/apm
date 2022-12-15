
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QVBoxLayout, QLayout, QLabel, QSizePolicy, QTableView,
    QSpacerItem, QGroupBox, QHBoxLayout, QPushButton, QTableWidget, QFrame, QAbstractItemView
)

from PyQt5.QtGui import (
    QFont, QPen
)

from PyQt5.QtCore import (
    QSize
)


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
from view.view.widget_tab.widget_tab import WidgetTab
from view.components.widget_chart_item import WidgetChartItem
from view.view.dialog_details_correlation import DialogDetailsCorrelation
from view.model.tableCorrelationModel import TableCorrelationModel
from controller.analysis_data import AnalysisData

class WidgetChartVariables(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()
        
    def createUI(self):
        self.gridLayout = QGridLayout(self.widgetCentral)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidgetChart = QTableWidget(self.widgetCentral)
        if (self.tableWidgetChart.columnCount() < 3):
            self.tableWidgetChart.setColumnCount(3)
        self.tableWidgetChart.setObjectName(u"tableWidgetChart")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetChart.sizePolicy().hasHeightForWidth())
        self.tableWidgetChart.setSizePolicy(sizePolicy)
        self.tableWidgetChart.setFrameShape(QFrame.NoFrame)
        self.tableWidgetChart.setFrameShadow(QFrame.Plain)
        self.tableWidgetChart.setLineWidth(0)
        self.tableWidgetChart.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidgetChart.setShowGrid(False)
        self.tableWidgetChart.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidgetChart.setColumnCount(3)
        self.tableWidgetChart.horizontalHeader().setVisible(False)
        self.tableWidgetChart.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidgetChart, 0, 0, 4, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.widgetCentral)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.tVCorrelations = QTableView(self.widgetCentral)
        self.tVCorrelations.setObjectName(u"tVCorrelations")
        sizePolicy1.setHeightForWidth(self.tVCorrelations.sizePolicy().hasHeightForWidth())
        self.tVCorrelations.setSizePolicy(sizePolicy1)
        self.tVCorrelations.setMinimumSize(QSize(350, 350))
        self.tVCorrelations.setMaximumSize(QSize(350, 350))

        self.gridLayout.addWidget(self.tVCorrelations, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)
        self.label.setText(u"Tabla de correlacion de las variables")
        
        
        
    def createWorkspace(self):
        self.tableWidgetChart.clear()
        self.tableWidgetChart.setColumnCount(3)
        header = self.tableWidgetChart.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        nameVarSelect = AnalysisData().getVariablesSelect()
        dataCorrelations = AnalysisData().tableCorrelations()
        self.modelCorrelation = TableCorrelationModel(nameVarSelect,dataCorrelations)
        self.tVCorrelations.setModel(self.modelCorrelation)
        
        correlations=AnalysisData().getCorrelationVariablesSelect()   
        
        rows = len(correlations)//3
        
        if len(correlations)% 3 !=0 :
            rows=rows+1
            
        self.tableWidgetChart.setRowCount(rows)
        
        for j in range(0,rows):
            self.tableWidgetChart.setRowHeight(j,250)
        
        for i in range(0,len(correlations)):
            item = WidgetChartItem(correlations[i])
            self.tableWidgetChart.setCellWidget(i//3,i%3,item)
                
      
        
    def createConnect(self):
        super().createConnect()
        self.tableWidgetChart.doubleClicked.connect(self.showCorrelations)
        
    def updateTab(self):
        self.createWorkspace()
        
    def showCorrelations(self,_index):
        pos = _index.row()*3+_index.column()
        correlation = AnalysisData().getThisCorrelation(pos)
        if correlation!= None:
            dialog = DialogDetailsCorrelation(correlation)
            dialog.setMinimumHeight(600)
            dialog.setMinimumWidth(600)
            dialog.exec()
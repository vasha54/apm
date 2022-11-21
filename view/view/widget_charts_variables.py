from PyQt5.QtWidgets import (
    QWidget, QPushButton
)

from PyQt5 import QtCore, QtGui, QtWidgets
from view.view.widget_tab import WidgetTab
from view.view.widget_chart_item import WidgetChartItem
from view.view.dialog_details_correlation import DialogDetailsCorrelation
from controller.analysis_data import AnalysisData

class WidgetChartVariables(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createWorkspace()
        self.createConnect()
        
    def setupUi(self, WidgetChartsVariables):
        WidgetChartsVariables.setObjectName("WidgetChartsVariables")
        WidgetChartsVariables.resize(861, 471)
        self.gridLayout = QtWidgets.QGridLayout(WidgetChartsVariables)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetChart = QtWidgets.QTableWidget(WidgetChartsVariables)
        self.tableWidgetChart.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidgetChart.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidgetChart.setLineWidth(0)
        self.tableWidgetChart.setStyleSheet('selection-background-color:white;')
        self.tableWidgetChart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidgetChart.setShowGrid(False)
        self.tableWidgetChart.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidgetChart.setColumnCount(3)
        self.tableWidgetChart.setObjectName("tableWidgetChart")
        self.tableWidgetChart.setRowCount(0)
        self.tableWidgetChart.horizontalHeader().setVisible(False)
        self.tableWidgetChart.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidgetChart, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(749, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButtonNext = QtWidgets.QPushButton(WidgetChartsVariables)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.gridLayout.addWidget(self.pushButtonNext, 1, 1, 1, 1)
        self.pushButtonNext.setText("Siguiente paso")
        
    def createWorkspace(self):
        self.tableWidgetChart.clear()
        self.tableWidgetChart.setColumnCount(3)
        header = self.tableWidgetChart.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        correlations=AnalysisData().getCorrelationVariablesSelect()   
        
        rows = len(correlations)//3
        
        if len(correlations)% 3 !=0 :
            rows=rows+1
            
        self.tableWidgetChart.setRowCount(rows)
        
        for j in range(0,rows):
            self.tableWidgetChart.setRowHeight(j,250)
        
        for i in range(0,len(correlations)):
            item = WidgetChartItem(correlations[i])
            self.tableWidgetChart.setCellWidget(i/3,i%3,item)
                
      
        
    def createConnect(self):
        self.pushButtonNext.clicked.connect(self.clickNextStage)
        self.tableWidgetChart.doubleClicked.connect(self.showCorrelations)
        
    def update(self):
        self.createWorkspace()
        
    def showCorrelations(self,_index):
        pos = _index.row()*3+_index.column()
        correlation = AnalysisData().getThisCorrelation(pos)
        if correlation!= None:
            dialog = DialogDetailsCorrelation(correlation)
            dialog.setMinimumHeight(600)
            dialog.setMinimumWidth(600)
            dialog.exec()
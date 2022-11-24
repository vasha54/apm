from PyQt5.QtWidgets import (
    QVBoxLayout, QTabWidget
)

from PyQt5 import QtCore, QtGui, QtWidgets,Qt

from view.view.widget_tab.widget_tab import WidgetTab
from view.components.widget_details_model_select import WidgetDetailsModelSelect

class WidgetDetailsModelSelect(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        self.gridLayout = QtWidgets.QGridLayout(self.widgetCentral)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidgetDetailsModelSelect = QtWidgets.QTabWidget(self.widgetCentral)
        self.tabWidgetDetailsModelSelect.setObjectName("tabWidgetDetailsModelSelect")
        self.tabTestNormalResidual = QtWidgets.QWidget()
        self.tabTestNormalResidual.setObjectName("tabTestNormalResidual")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidual, "")
        self.tabTestNormalResidualNot = QtWidgets.QWidget()
        self.tabTestNormalResidualNot.setObjectName("tabTestNormalResidualNot")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualNot, "")
        self.tabChartNormalResidualNot = QtWidgets.QWidget()
        self.tabChartNormalResidualNot.setObjectName("tabChartNormalResidualNot")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidualNot, "")
        self.tabChartNormalResidual = QtWidgets.QWidget()
        self.tabChartNormalResidual.setObjectName("tabChartNormalResidual")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidual, "")
        self.gridLayout.addWidget(self.tabWidgetDetailsModelSelect, 0, 0, 1, 1)
        
        self.tabWidgetDetailsModelSelect.setTabText(self.tabWidgetDetailsModelSelect.indexOf(self.tabTestNormalResidual),  "Prueba de normalidad (Residuales no escalados)")
        self.tabWidgetDetailsModelSelect.setTabText(self.tabWidgetDetailsModelSelect.indexOf(self.tabTestNormalResidualNot), "Pruebas de normalidad (Residuales estudertizados")
        self.tabWidgetDetailsModelSelect.setTabText(self.tabWidgetDetailsModelSelect.indexOf(self.tabChartNormalResidualNot), "Gráficos de normalidad residuales no escalados")
        self.tabWidgetDetailsModelSelect.setTabText(self.tabWidgetDetailsModelSelect.indexOf(self.tabChartNormalResidual), "Graficos de normalidad residuales estudertizados")
        
    
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        pass
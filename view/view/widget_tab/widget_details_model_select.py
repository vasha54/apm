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
        self.tabWidgetDetailsModelSelect = QtWidgets.QTabWidget(self.widgetCentral)
        
        self.tabTestNormalResidual = QtWidgets.QWidget()
        self.tabTestNormalResidualNotScale = QtWidgets.QWidget()
        self.tabChartNormalResidualNotScale = QtWidgets.QWidget()
        self.tabChartNormalResidual = QtWidgets.QWidget()
        self.tabTestHomecedasticidadResidual = QtWidgets.QWidget()
        self.tabChartHomecedasticidadResidual = QtWidgets.QWidget()
        self.tabAnalysMultiColinualidad = QtWidgets.QWidget()
        self.tabTestIndependenceResidual = QtWidgets.QWidget()
        self.tabChartIndependenceResidual = QtWidgets.QWidget()
        
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidual,"Analisis de normalidad (Residuales no escalados)")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualNotScale,"Analisis de normalidad (Residuales estudertizados")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidualNotScale,"Gráficos de normalidad residuales no escalados")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidual,"Graficos de normalidad residuales estudertizados")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestHomecedasticidadResidual,"Pruebas de homecedasticidad de los residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartHomecedasticidadResidual,"Graficos de homecedasticidad de los residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabAnalysMultiColinualidad,"Analisis de multicolinualidad")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestIndependenceResidual,"Pruebas de indepencia de residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartIndependenceResidual,"Graficos de indepencia de residuales")
        
        
        self.gridLayout.addWidget(self.tabWidgetDetailsModelSelect, 0, 0, 1, 1)

    
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        pass
from PyQt5.QtWidgets import (
    QVBoxLayout, QTabWidget
)

from PyQt5 import QtCore, QtGui, QtWidgets,Qt

from controller.analysis_data import AnalysisData

from view.view.widget_tab.widget_tab import WidgetTab
from view.components.widget_details_model_select import WidgetDetailsModelSelect

from view.widget.widget_test_normal_residual_not_scale import WidgetTestNormalResidualNotScale
from view.widget.widget_test_normal_residual_studentized import WidgetTestNormalResidualStudentized
from view.widget.widget_analys_multi_colinualidad import WidgetAnalysMultiColinualidad
from view.widget.widget_test_homecedasticidad_residual import WidgetTestHomecedasticidadResidual
from view.widget.widget_test_independence_residual import WidgetTestIndependenceResidual

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
        self.gridLayout.addWidget(self.tabWidgetDetailsModelSelect, 0, 0, 1, 1)

    
    def createWorkspace(self):
        keyModelSelect = AnalysisData().getKeyModelSelect()
        self.tabTestNormalResidualNotScale = WidgetTestNormalResidualNotScale(keyModelSelect)
        self.tabTestNormalResidualStudentized = WidgetTestNormalResidualStudentized(keyModelSelect)
        self.tabTestHomecedasticidadResidual = WidgetTestHomecedasticidadResidual(keyModelSelect)
        self.tabAnalysMultiColinualidad = WidgetAnalysMultiColinualidad(keyModelSelect)
        self.tabTestIndependenceResidual = WidgetTestIndependenceResidual(keyModelSelect)
        self.tabChartNormalResidualNotScale = QtWidgets.QWidget()
        self.tabChartNormalResidual = QtWidgets.QWidget()
        self.tabChartHomecedasticidadResidual = QtWidgets.QWidget()
        self.tabChartIndependenceResidual = QtWidgets.QWidget()
        
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualNotScale,"Analisis de normalidad (Residuales no escalados)")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualStudentized,"Analisis de normalidad (Residuales estudertizados)")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidualNotScale,"Gráficos de normalidad residuales no escalados")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartNormalResidual,"Graficos de normalidad residuales estudertizados")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestHomecedasticidadResidual,"Pruebas de homecedasticidad de los residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartHomecedasticidadResidual,"Graficos de homecedasticidad de los residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabAnalysMultiColinualidad,"Analisis de multicolinualidad")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestIndependenceResidual,"Pruebas de indepencia de residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartIndependenceResidual,"Graficos de indepencia de residuales")
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        self.tabTestIndependenceResidual.update()
        self.tabTestHomecedasticidadResidual.update()
        self.tabTestNormalResidualNotScale.update()
        self.tabTestNormalResidualStudentized.update()
        self.tabAnalysMultiColinualidad.update()
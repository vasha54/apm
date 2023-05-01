from PyQt5.QtWidgets import (
    QVBoxLayout, QTabWidget, QWidget
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
from view.widget.widget_charts_coeff_model_select import WidgetChartsCoeffModelSelect
from view.widget.widget_others_charts_model_select import WidgetOthersChartsModelSelect

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
        self.tabChartsCoeffModelSelect = WidgetChartsCoeffModelSelect(keyModelSelect)
        self.tabOthersChartsModelSelect = WidgetOthersChartsModelSelect(keyModelSelect)
        
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualNotScale,"Análisis de normalidad (Residuales no escalados)")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestNormalResidualStudentized,"Análisis de normalidad (Residuales estudertizados)")
        self.tabWidgetDetailsModelSelect.addTab(self.tabTestHomecedasticidadResidual,"Homocedasticidad e independencia de los residuales")
        self.tabWidgetDetailsModelSelect.addTab(self.tabAnalysMultiColinualidad,"VIF, linealidad y especificación")
        self.tabWidgetDetailsModelSelect.addTab(self.tabChartsCoeffModelSelect,"DFBTAS")
        self.tabWidgetDetailsModelSelect.addTab(self.tabOthersChartsModelSelect,"Otros gráficos")
        
        
    def createConnect(self):
        super().createConnect()
        
    def updateTab(self):
        self.tabTestIndependenceResidual.update()
        self.tabTestHomecedasticidadResidual.update()
        self.tabTestNormalResidualNotScale.update()
        self.tabTestNormalResidualStudentized.update()
        self.tabAnalysMultiColinualidad.update()
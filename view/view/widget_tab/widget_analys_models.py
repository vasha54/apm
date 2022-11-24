from PyQt5.QtWidgets import (
    QVBoxLayout, QTabWidget, QToolBox
)

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from view.view.widget_tab.widget_tab import WidgetTab
from view.components.widget_regress_model_result import WidgetRegressModelResult

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class WidgetAnalysModels(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        self.verticalLayout = QVBoxLayout(self.widgetCentral)
        self.toolBoxModel = QToolBox(self.widgetCentral)
        self.verticalLayout.addWidget(self.toolBoxModel)

        
    
    def createWorkspace(self):
        allKeysModels = AnalysisData().getKeysModels()
        for key in allKeysModels:
            widget = WidgetRegressModelResult(key,self)
            self.toolBoxModel.addItem(widget,AnalysisData().getDataModel(key,ModelLMR.NAME))
            
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        while self.toolBoxModel.count() >0:
            self.toolBoxModel.removeItem(0)
            
        allKeysModels = AnalysisData().getKeysModels()
        for key in allKeysModels:
            widget = WidgetRegressModelResult(key,self)
            self.toolBoxModel.addItem(widget,AnalysisData().getDataModel(key,ModelLMR.NAME))
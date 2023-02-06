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
        self.relationsPosWidgetKeyModel={}
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
        self.relationsPosWidgetKeyModel = {}
        pos =0
        isFirst = True
        for key in allKeysModels:
            if isFirst == True:
                isFirst = False
                AnalysisData().setSelectModel(key)
            widget = WidgetRegressModelResult(key,self)
            self.relationsPosWidgetKeyModel[pos]=key
            self.toolBoxModel.addItem(widget,AnalysisData().getDataModel(key,ModelLMR.NAME))
            pos = pos + 1
            
    
    def createConnect(self):
        self.toolBoxModel.currentChanged.connect(self.changeTab)
        super().createConnect()
        
    def updateTab(self):
        self.clearLayout(self.verticalLayout)
        self.toolBoxModel = QToolBox(self.widgetCentral)
        self.verticalLayout.addWidget(self.toolBoxModel)
        
        self.createWorkspace() 
        
    def changeTab(self,index):
        AnalysisData().setSelectModel(self.relationsPosWidgetKeyModel[index])
        
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
            
        
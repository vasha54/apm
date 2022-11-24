from PyQt5.QtWidgets import (
    QVBoxLayout, QTabWidget
)

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from view.view.widget_tab.widget_tab import WidgetTab

class WidgetAnalysModels(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        self.verticalLayout = QVBoxLayout(self.widgetCentral)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidgetModel = QTabWidget(self.widgetCentral)
        self.tabWidgetModel.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidgetModel.setUsesScrollButtons(True)
        self.tabWidgetModel.setDocumentMode(False)
        self.tabWidgetModel.setTabsClosable(False)
        self.tabWidgetModel.setMovable(True)
        self.verticalLayout.addWidget(self.tabWidgetModel)

        
    
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        pass
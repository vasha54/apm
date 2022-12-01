from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore
from view.ui.tab_widget_ui import Ui_WidgetTab
from abc import ABCMeta, abstractmethod


class WidgetTab(QWidget, Ui_WidgetTab):
    
    __metaclass__ = ABCMeta
    
    next = QtCore.pyqtSignal()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def clickNextStage(self):
        self.next.emit()
        
    def createConnect(self):
        self.pushButtonNext.clicked.connect(self.clickNextStage)
    
    @abstractmethod    
    def updateTab(self):
        pass
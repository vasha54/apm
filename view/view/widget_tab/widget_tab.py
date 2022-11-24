from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore
from view.ui.tab_widget_ui import Ui_WidgetTab


class WidgetTab(QWidget, Ui_WidgetTab):
    
    next = QtCore.pyqtSignal()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def clickNextStage(self):
        self.next.emit()
        
    def createConnect(self):
        self.pushButtonNext.clicked.connect(self.clickNextStage)
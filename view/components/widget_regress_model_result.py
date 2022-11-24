from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_regress_model_result_ui import Ui_WidgetRegressModelResult

class WidgetRegressModelResult(QWidget,Ui_WidgetRegressModelResult):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.createWorkSpace()
        
    def createWorkSpace(self):
        pass
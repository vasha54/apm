from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_details_model_select_ui import Ui_WidgetDetailsModelSelect

class WidgetDetailsModelSelect(QWidget,Ui_WidgetDetailsModelSelect):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.createWorkSpace()
        
    def createWorkSpace(self):
        pass
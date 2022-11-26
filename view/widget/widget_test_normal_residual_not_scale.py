from view.ui.widget_test_normal_residual_not_scale_ui import Ui_WidgetTestNormalResidualNotScale

from PyQt5.QtWidgets import (
    QWidget
)

class WidgetTestNormalResidualNotScale(QWidget,Ui_WidgetTestNormalResidualNotScale):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
    def createWorkSpace(self):
        pass
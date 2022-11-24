from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_regress_model_result_ui import Ui_WidgetRegressModelResult

class WidgetRegressModelResult(QWidget,Ui_WidgetRegressModelResult):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
        
    def createWorkSpace(self):
        self.lOVariableDependent.setText(AnalysisData().getDataModel(self.keyModel,ModelLMR.NAME_VD))
        self.lONumberObservations.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)))
        self.lOGLResidual.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.GL_RESIDUAL)) )
        
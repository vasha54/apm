from view.ui.widget_test_independence_residual_ui import Ui_WidgetTestIndependenceResidual

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class WidgetTestIndependenceResidual(QWidget,Ui_WidgetTestIndependenceResidual):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
    def createWorkSpace(self):
        self.lOBREUSH_GGODFREY.setText( str(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY )) )
        self.lOBREUSH_GGODFREY_PVALUE.setText( str(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY_PVALUE )) )
        self.lODURBIN_WATSON.setText( str(AnalysisData().getDataModel( self.keyModel, ModelLMR.DURBIN_WATSON )) )
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
from view.ui.widget_test_homecedasticidad_residual_ui import Ui_WidgetTestHomecedasticidadResidual

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class WidgetTestHomecedasticidadResidual(QWidget,Ui_WidgetTestHomecedasticidadResidual):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
    def createWorkSpace(self):
        self.lOBREUSH_PAGAN.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.BREUSH_PAGAN)))
        self.lOBREUSH_PAGAN_PVALUE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.BREUSH_PAGAN_PVALUE)))
        self.lOGOLDFELD_QUANDT.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.GOLDFELD_QUANDT)))
        self.lOGOLDFELD_QUANDT_PVALUE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.GOLDFELD_QUANDT_PVALUE)))
        self.lOWHITE_FW.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_FW)))
        self.lOWHITE_FW_PVALUE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_FW_PVALUE)))
        self.lOWHITE_LM.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_LH)))
        self.lOWHITE_LM_PVALUE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_LH_PVALUE)))
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
from view.ui.widget_test_homecedasticidad_residual_ui import Ui_WidgetTestHomecedasticidadResidual

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI

class WidgetTestHomecedasticidadResidual(QWidget,Ui_WidgetTestHomecedasticidadResidual):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        self.preference = PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOBREUSH_PAGAN.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.BREUSH_PAGAN),formatStr)))
        self.lOBREUSH_PAGAN_PVALUE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.BREUSH_PAGAN_PVALUE),formatStr)))
        self.lOGOLDFELD_QUANDT.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.GOLDFELD_QUANDT),formatStr)))
        self.lOGOLDFELD_QUANDT_PVALUE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.GOLDFELD_QUANDT_PVALUE),formatStr)))
        self.lOWHITE_FW.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_FW),formatStr)))
        self.lOWHITE_FW_PVALUE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_FW_PVALUE),formatStr)))
        self.lOWHITE_LM.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_LH),formatStr)))
        self.lOWHITE_LM_PVALUE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.WHITE_LH_PVALUE),formatStr)))
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
    
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.update()
from view.ui.widget_test_independence_residual_ui import Ui_WidgetTestIndependenceResidual

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI

class WidgetTestIndependenceResidual(QWidget,Ui_WidgetTestIndependenceResidual):
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
        self.lOBREUSH_GGODFREY.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY),formatStr)) )
        self.lOBREUSH_GGODFREY_PVALUE.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY_PVALUE),formatStr)) )
        self.lODURBIN_WATSON.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.DURBIN_WATSON),formatStr)) )
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.update()
        
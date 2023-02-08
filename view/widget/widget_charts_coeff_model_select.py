from view.ui.widget_charts_coeff_model_select_ui import Ui_WidgetChartsCoeffModelSelect

from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

import PyQt5.QtCore 

from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from controller.analysis_data import AnalysisData

class WidgetChartsCoeffModelSelect(QWidget,Ui_WidgetChartsCoeffModelSelect):
    
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.tWidgetChart.clear()
        data = AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_COEFF_MODEL)
        
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
    
    def changePreference(self,_listChange):
        if PreferenceGUI.COLOR_AXES_CHART in _listChange or PreferenceGUI.COLOR_BACKGROUND_CHART in _listChange  or PreferenceGUI.COLOR_TEXT_CHART in _listChange:
            self.update()
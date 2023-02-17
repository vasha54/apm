from view.ui.widget_charts_coeff_model_select_ui import Ui_WidgetChartsCoeffModelSelect

from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)
 

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from controller.analysis_data import AnalysisData
from view.components.widget_chart_histogram_coeff import WidgetChartHistogramCoeff

class WidgetChartsCoeffModelSelect(QWidget,Ui_WidgetChartsCoeffModelSelect):
    
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.tWidgetChart.clear()
        self.tWidgetChart.setColumnCount(3)
        header = self.tWidgetChart.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        datas = AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_COEFF_MODEL)
        
        rows = len(datas)//3
        
        if len(datas)% 3 !=0 :
            rows=rows+1
            
        self.tWidgetChart.setRowCount(rows)
        
        i=0
        
        for k,data in datas.items():
            self.tWidgetChart.setRowHeight(i//3,250)
            widget = WidgetChartHistogramCoeff(data)
            self.tWidgetChart.setCellWidget(i//3,i%3,widget)
            i=i+1
            
        
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
    
    def changePreference(self,_listChange):
        if PreferenceGUI.COLOR_AXES_CHART in _listChange or PreferenceGUI.COLOR_BACKGROUND_CHART in _listChange  or PreferenceGUI.COLOR_TEXT_CHART in _listChange:
            self.update()
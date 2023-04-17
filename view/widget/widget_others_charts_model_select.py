from view.ui.widget_others_charts_model_select_ui import Ui_WidgetOthersChartsModelSelect

from PyQt5.QtWidgets import (
    QWidget, QFrame
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

import PyQt5.QtCore 

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from controller.analysis_data import AnalysisData
from view.components.charts.chart_histogram import ChartHistogram 
from view.components.charts.chart_scatter import ChartScatter

class WidgetOthersChartsModelSelect(QWidget,Ui_WidgetOthersChartsModelSelect):
    
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.chartHistogram = list()
        self.createWorkSpace()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.tWidgetCharts.clear()
        self.tWidgetCharts.setColumnCount(3)
        self.tWidgetCharts.setRowCount(3)
        self.tWidgetCharts.setRowHeight(0,250)
        self.tWidgetCharts.setRowHeight(1,250)
        self.tWidgetCharts.setRowHeight(2,250)
        header = self.tWidgetCharts.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tWidgetCharts.setFrameShape(QFrame.NoFrame)
        self.tWidgetCharts.setFrameShadow(QFrame.Plain)
        self.chartHistogram.clear()
        self.createChartsHistograms()
        self.createChartsDistanceCooksLeverage()
        
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
        
    def changePreference(self,_listChange):
        if PreferenceGUI.COLOR_AXES_CHART in _listChange or PreferenceGUI.COLOR_BACKGROUND_CHART in _listChange  or PreferenceGUI.COLOR_TEXT_CHART in _listChange:
            colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
            colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
            colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
            
            for chart in self.chartHistogram:
                chart.setColorText(colorText)
                chart.setColorAxes(colorAxes)
                chart.setColorBackground(colorBackground)
                
            self.chartScatter.setColorAxes(colorAxes)
            self.chartScatter.setColorBackground(colorBackground)
            self.chartScatter.setColorText(colorText)
        
    
    def createChartsHistograms(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        COLUMNS = 3
        
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        dataCharts = [{'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.RESIDUAL_MODEL),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'Residuales'},
                      {'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.RESIDUAL_ST_MODEL),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'Residuales estudentizados'},
                      {'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.DISTANCE_COOKS),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'Distancia de Cooks'},
                      {'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.LEVERAGE),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'Leverage'},
                      {'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.COVARIANCE_RATIO),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'Ratio se la covarianza'},
                      {'heights':AnalysisData().getDataModel(self.keyModel,ModelLMR.DFFITS),
                       'bars':dataX,
                       'title_X':'Observación',
                       'title_Y':'DfFit'}]
        
        i = 0
        
        for d in dataCharts:
            
            widgetChart = ChartHistogram(self)
            widgetChart.makeChart(d)
            widgetChart.setColorText(colorText)
            widgetChart.setColorAxes(colorAxes)
            widgetChart.setColorBackground(colorBackground)
            self.chartHistogram.append(widgetChart)
            
            layout = QtWidgets.QVBoxLayout(self)
            layout.setSpacing(0)
            layout.addWidget(widgetChart)
            widget = QWidget(self)
            widget.setLayout(layout)
            self.tWidgetCharts.setCellWidget(i//COLUMNS,i%COLUMNS,widget)
            
            i=i+1
        
    
    def createChartsDistanceCooksLeverage(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataChart ={'valuesX':AnalysisData().getDataModel(self.keyModel,ModelLMR.LEVERAGE),
                    'valuesY':AnalysisData().getDataModel(self.keyModel,ModelLMR.DISTANCE_COOKS),
                    'title_Y':'Distancia de Cooks',
                    'title_X':'Leverage',
                    'sizePoints':5}
        
        self.chartScatter = ChartScatter(self)
        self.chartScatter.makeChart(dataChart)
        self.chartScatter.setColorAxes(colorAxes)
        self.chartScatter.setColorBackground(colorBackground)
        self.chartScatter.setColorText(colorText)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.chartScatter)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(2,0,widget)
        
    
        
from view.ui.widget_others_charts_model_select_ui import Ui_WidgetOthersChartsModelSelect

from PyQt5.QtWidgets import (
    QWidget, QFrame
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

import PyQt5.QtCore 

from PyQt5 import QtCore, QtGui, QtWidgets, Qt

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from controller.analysis_data import AnalysisData

class WidgetOthersChartsModelSelect(QWidget,Ui_WidgetOthersChartsModelSelect):
    
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.keyModel = _keyModel
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
        self.createChartsResidualObservation()
        self.createChartsResidualStudentizedObservation()
        self.createChartsDistanceCooksObservation()
        self.createChartsDistanceCooksLeverage()
        self.createChartsLeverageObservation()
        self.createChartsRatioCovarianzeObservation()
        self.createChartsDffitsObservation()
        
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
        
    def changePreference(self,_listChange):
        if PreferenceGUI.COLOR_AXES_CHART in _listChange or PreferenceGUI.COLOR_BACKGROUND_CHART in _listChange  or PreferenceGUI.COLOR_TEXT_CHART in _listChange:
            self.update()
        
            
    def createChartsResidualObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.RESIDUAL_MODEL)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetResidualObservation = pg.PlotWidget()
        self.graphWidgetResidualObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetResidualObservation.setLabel('left', 'Residuales', **styles)
        self.graphWidgetResidualObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetResidualObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetResidualObservation.addItem(bargraph)
        self.graphWidgetResidualObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetResidualObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(0,0,widget)
        
    
    def createChartsResidualStudentizedObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.RESIDUAL_ST_MODEL)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetResidualStudentizedObservation = pg.PlotWidget()
        self.graphWidgetResidualStudentizedObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetResidualStudentizedObservation.setLabel('left', 'Residuales estudentizados', **styles)
        self.graphWidgetResidualStudentizedObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetResidualStudentizedObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetResidualStudentizedObservation.addItem(bargraph)
        self.graphWidgetResidualStudentizedObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetResidualStudentizedObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(0,1,widget)
        
    
    def createChartsDistanceCooksObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.DISTANCE_COOKS)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
         
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetDistanceCooksObservation = pg.PlotWidget()
        self.graphWidgetDistanceCooksObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetDistanceCooksObservation.setLabel('left', 'Distancia de Cooks', **styles)
        self.graphWidgetDistanceCooksObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetDistanceCooksObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetDistanceCooksObservation.addItem(bargraph)
        self.graphWidgetDistanceCooksObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetDistanceCooksObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(0,2,widget)
        
    
    def createChartsDistanceCooksLeverage(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.DISTANCE_COOKS)
        dataX = AnalysisData().getDataModel(self.keyModel,ModelLMR.LEVERAGE)
        
        brushScatter = QBrush(QColor(0, 0, 255, 225))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetDistanceCooksLeverage = pg.PlotWidget()
        self.graphWidgetDistanceCooksLeverage.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetDistanceCooksLeverage.setLabel('left', 'Distancia de Cooks', **styles)
        self.graphWidgetDistanceCooksLeverage.setLabel('bottom','Leverage', **styles)
        self.graphWidgetDistanceCooksLeverage.setBackground(colorBackground)
        self.graphWidgetDistanceCooksLeverage.plot(dataX, dataY, pen=None,symbol='o', symbolSize=5, symbolBrush=brushScatter)
        self.graphWidgetDistanceCooksLeverage.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        self.graphWidgetDistanceCooksLeverage.setXRange(min(dataX)-0.001,max(dataX)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetDistanceCooksLeverage)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(1,0,widget)
        
    
    def createChartsLeverageObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.LEVERAGE)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetLeverageObservation = pg.PlotWidget()
        self.graphWidgetLeverageObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetLeverageObservation.setLabel('left', 'Leverage', **styles)
        self.graphWidgetLeverageObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetLeverageObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetLeverageObservation.addItem(bargraph)
        self.graphWidgetLeverageObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetLeverageObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(1,1,widget)
        
    
    def createChartsRatioCovarianzeObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.COVARIANCE_RATIO)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetRatioCovarianzeObservation = pg.PlotWidget()
        self.graphWidgetRatioCovarianzeObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetRatioCovarianzeObservation.setLabel('left', 'Ratio se la covarianza', **styles)
        self.graphWidgetRatioCovarianzeObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetRatioCovarianzeObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetRatioCovarianzeObservation.addItem(bargraph)
        self.graphWidgetRatioCovarianzeObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetRatioCovarianzeObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(1,2,widget)
        
    
    def createChartsDffitsObservation(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataY = AnalysisData().getDataModel(self.keyModel,ModelLMR.DFFITS)
        numberMeas = AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)
        dataX = list(range(1, numberMeas+1))
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidgetDffitsObservation = pg.PlotWidget()
        self.graphWidgetDffitsObservation.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidgetDffitsObservation.setLabel('left', 'DfFit', **styles)
        self.graphWidgetDffitsObservation.setLabel('bottom','Observación', **styles)
        self.graphWidgetDffitsObservation.setBackground(colorBackground)
        
        bargraph = pg.BarGraphItem(x = dataX, height = dataY, width = 0.5, brush ='g',pen=None)
        
        self.graphWidgetDffitsObservation.addItem(bargraph)
        self.graphWidgetDffitsObservation.setYRange(min(dataY)-0.001,max(dataY)+0.001)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.graphWidgetDffitsObservation)
        widget = QWidget(self)
        widget.setLayout(layout)
        
        self.tWidgetCharts.setCellWidget(2,0,widget)
        
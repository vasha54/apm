from view.ui.widget_test_homecedasticidad_residual_ui import Ui_WidgetTestHomecedasticidadResidual

from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

import PyQt5.QtCore 

from math import floor, ceil

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from view.components.charts.chart_multiple import ChartMultiple

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
        self.lOBREUSH_GGODFREY.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY),formatStr)) )
        self.lOBREUSH_GGODFREY_PVALUE.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.BREUSH_GGODFREY_PVALUE),formatStr)) )
        self.lODURBIN_WATSON.setText( str(format(AnalysisData().getDataModel( self.keyModel, ModelLMR.DURBIN_WATSON),formatStr)) )
        self.createChartValueObserverValueAdjust()
        self.createChartResidualValueAdjust()
    
    
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
    
    def changePreference(self,_listChange):
        self.update()
    
    def createChartValueObserverValueAdjust(self):
        
        data = AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_VALUE_OBSERVER_VALUE_ADJUST)
        
        ys = [min(data['y'])-0.05,max(data['y'])+0.05]
        xs = [min(data['x'])-0.05,max(data['x'])+0.05]
        
        limitsAxes = [floor(min(ys[0],xs[0])),ceil(max(ys[1],xs[1]))]
        
        ticks = {}
        
        for i in range(limitsAxes[0],limitsAxes[1]+1):
            ticks[i]=i
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        self.chartVOVA = ChartMultiple(self)
        
        self.chartVOVA.addPlot(xs,ys,color='#FF0000')
        self.chartVOVA.addScatter(data['x'], data['y'],c='#0000FF')
        
        self.chartVOVA.setTitleX('Valores ajustados')
        self.chartVOVA.setTitleY('Valores observados')
        self.chartVOVA.setColorText(colorText)
        self.chartVOVA.setColorAxes(colorAxes)
        self.chartVOVA.setColorBackground(colorBackground)
        self.chartVOVA.setLimitsAxisX(limitsAxes)
        self.chartVOVA.setLimitsAxisY(limitsAxes)
        self.chartVOVA.setXTicks(ticks)
        self.chartVOVA.setYTicks(ticks)
        
        self.clearLayout(self.vLChartValueObserverValueAdjust)
        self.vLChartValueObserverValueAdjust.addWidget(self.chartVOVA)
        

    def createChartResidualValueAdjust(self):
        
        data =AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_RESIDUAL_VALUE_ADJUST)
        
        xLine = [min(min(data['xCurve']),min(data['xScatter']))-0.05,max(max(data['xCurve']),max(data['xScatter']))+0.05]
        yLine = [0,0]
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        self.chartRVA = ChartMultiple(self)
        
        self.chartRVA.addPlot(xLine,yLine,color='#000000',linestyle='dashed')
        self.chartRVA.addPlot(data['xCurve'],data['yCurve'],color='#FF0000')
        self.chartRVA.addScatter(data['xScatter'], data['yScatter'],c='#0000FF')
        
        self.chartRVA.setTitleX('Valores ajustados')
        self.chartRVA.setTitleY('Residuales')
        self.chartRVA.setColorAxes(colorAxes)
        self.chartRVA.setColorBackground(colorBackground)
        self.chartRVA.setColorText(colorText)
        
        self.clearLayout(self.vLChartResidualValueAdjust)
        self.vLChartResidualValueAdjust.addWidget(self.chartRVA)
        
    
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
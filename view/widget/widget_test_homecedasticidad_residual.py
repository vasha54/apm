from view.ui.widget_test_homecedasticidad_residual_ui import Ui_WidgetTestHomecedasticidadResidual

from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

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
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'Valores observados', **styles)
        self.graphWidget.setLabel('bottom', 'Valores ajustados', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brushScatter = QBrush(QColor(0, 0, 255, 225))
        penLine = pg.mkPen(color=(255, 0, 0), width=2)
        
        self.graphWidget.addLegend()
        self.graphWidget.plot( xs, ys, pen=penLine,symbol=None, symbolSize=5, symbolBrush=None)
        self.graphWidget.plot(data['x'], data['y'], pen=None,symbol='o', symbolSize=5, symbolBrush=brushScatter)
        
        self.clearLayout(self.vLChartValueObserverValueAdjust)
        
        self.vLChartValueObserverValueAdjust.addWidget(self.graphWidget)
        
        
    
    def createChartResidualValueAdjust(self):
        
        data =AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_RESIDUAL_VALUE_ADJUST)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'Valores observados', **styles)
        self.graphWidget.setLabel('bottom', 'Valores ajustados', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brushScatter = QBrush(QColor(0, 0, 255, 225))
        penRed = pg.mkPen(color=(255, 0, 0), width=2)
        penBlack = pg.mkPen(color=(0, 0, 0), width=2)
        
        self.graphWidget.addLegend()
        self.graphWidget.plot(data['xCurve'], data['yCurve'], pen=penRed,symbol=None, symbolSize=5, symbolBrush=None)
        self.graphWidget.plot(data['xScatter'], data['yScatter'], pen=None, symbol='o', symbolSize=5, symbolBrush=brushScatter)
        
        
        self.clearLayout(self.vLChartResidualValueAdjust)
        
        self.vLChartResidualValueAdjust.addWidget(self.graphWidget)
        
        
    
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
from view.ui.widget_test_normal_residual_not_scale_ui import Ui_WidgetTestNormalResidualNotScale

from PyQt5.QtWidgets import (
    QWidget,QVBoxLayout
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

from view.preferences.preferences import PreferenceGUI

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.preferences.preferences import PreferenceGUI

class WidgetTestNormalResidualNotScale(QWidget,Ui_WidgetTestNormalResidualNotScale):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOANDERSON_DARLING_PVALUE_RWS.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_PVALUE_RWS),formatStr)))
        self.lOANDERSON_DARLING_RWS.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_RWS),formatStr)) )
        self.lOCHI_SQUARE_PVALUE_RWS.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_PVALUE_RWS),formatStr)))
        self.lOCHI_SQUARE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_RWS),formatStr)))
        self.lOCOEFF_ASYMETRY_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_ASYMETRY_RWS),formatStr)))
        self.lOCOEFF_CURTOSIS_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_CURTOSIS_RWS),formatStr)))
        self.lOJARQUE_BERA_PVALUE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_PVALUE_RWS),formatStr)))
        self.lOJARQUE_BERA_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_RWS),formatStr)))
        self.lOK_CUAD_DANGOSTINO_PVALUE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_PVALUE_RWS),formatStr)))
        self.lOK_CUAD_DANGOSTINO_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_RWS),formatStr)))
        self.lOKOLMOGOROV_SMIRNOV_PVALUE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_PVALUE_RWS),formatStr)))
        self.lOKOLMOGOROV_SMIRNOV_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_RWS),formatStr)))
        self.lOLILLIEFORS_PVALUE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_PVALUE_RWS),formatStr)))
        self.lOLILLIEFORS_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_RWS),formatStr)))
        self.lOSHAPIRO_WILK_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_RWS),formatStr)))
        self.lOSHAPIRO_WILK_PVALUE_RWS.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_PVALUE_RWS),formatStr)))
        
        self.clearLayout(self.widgetGraphOne.layout())
        self.clearLayout(self.widgetGraphTwo.layout())
        
        self.createChartQQTestNormalResidualNotScale()
        self.createChartDistributionResidualNotScale()
        
    def changePreference(self,_listChange):
        self.update()
         
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
                
    def createChartDistributionResidualNotScale(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        styles = {'color':colorText, 'font-size':'10px'}
        
        self.graphWidget.setLabel('left', 'Densidad', **styles)
        self.graphWidget.setLabel('bottom', 'Residuales', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        series = AnalysisData().getDataModel(self.keyModel,ModelLMR.SERIE_CHART_DISTRIBUTION_RESIDUAL_NOT_SCALE)
        
        xKDE = []
        yKDE = []
        xNormal = []
        yNormal = [] 
        
        if series != None:
            xKDE = series[0]
            yKDE = series[1]
            xNormal = series[2]
            yNormal = series[3]
            
        penLineNormal = pg.mkPen(color=(255, 0, 0), width=2)
        brushLineNormal = QBrush(QColor(255,0,0,255))
        
        penLineKDE = pg.mkPen(color=(0, 0, 0), width=2)
        self.graphWidget.addLegend()
        self.graphWidget.plot(xNormal, yNormal, name = "Distribución normal", pen=penLineNormal , symbol=None, symbolSize=5, symbolBrush=brushLineNormal)
        self.graphWidget.plot(xKDE,    yKDE   , name = "KDE", pen=penLineKDE    , symbol=None, symbolSize=None, symbolBrush=None)
        
        self.widgetGraphTwo.layout().addWidget(self.graphWidget)
        
        self.labelTitleDistributionResidual.setStyleSheet(" color:"+colorText+"; background-color:"+colorBackground+"; ")
        
        
                
    def createChartQQTestNormalResidualNotScale(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        styles = {'color':colorText, 'font-size':'10px'}
        
        serie = AnalysisData().getDataModel(self.keyModel,ModelLMR.SERIE_CHART_QQ_TEST_NORMAL_RESIDUAL_NOT_SCALE)
        xs = []
        ys = []
        xLine = []
        yLine = []
        
        if serie !=None :
            xs = serie[0]
            ys = serie[1]
            xLine = serie[2]
            yLine = serie[3]
        
        
        self.graphWidget.setLabel('left', 'Cuartiles de los residuales', **styles)
        self.graphWidget.setLabel('bottom', 'Cuartiles teoricos', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brush = QBrush(QColor(0,0,0,255))
        brushLine = QBrush(QColor(255,0,0,255))
        
        penLine = pg.mkPen(color=(255, 0, 0), width=2)
        
        self.graphWidget.plot(xLine, yLine,pen=penLine ,symbol=None, symbolSize=5, symbolBrush=brushLine)
        self.graphWidget.plot(xs, ys,pen=None,symbol='o', symbolSize=5, symbolBrush=brush)
        
        self.widgetGraphOne.layout().addWidget(self.graphWidget)
        
        self.labelTitleChartQQ.setStyleSheet("color:"+colorText+"; background-color:"+colorBackground+";")
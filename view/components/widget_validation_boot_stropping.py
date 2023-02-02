from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_boot_stropping_ui import Ui_WidgetValidationBootStropping

from view.preferences.preferences import PreferenceGUI

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class WidgetValidationBootStropping(QWidget,Ui_WidgetValidationBootStropping):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        self.createConnects()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.gBResult.setVisible(False)
        
    def setKeyModel(self, _keyModel):
        self.keyModel = _keyModel
    
    def createConnects(self):
        self.pBAnalizar.clicked.connect(self.calculate)
        #self.sBCountBoot.valueChanged.connect(self.changeValueBoost)
    
    def calculate(self):
        bootsValue = int(self.sBCountBoot.value())
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOCVRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOCVRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        
        self.gBResult.setVisible(True)
        self.createChart()
        
    def createChart(self):
        
        self.clearLayout(self.gLayoutChart)
        bootsValue = int(self.sBCountBoot.value())
        
        data = AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_FREQUENCY_COEFFICIENT_BOOT_STROPPING,boots=bootsValue)
        
        
        
        # colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        # colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        # colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        # pg.setConfigOption('foreground', colorAxes)
        # pg.setConfigOptions(antialias=True)
        # self.graphWidget = pg.PlotWidget()
        # self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        # styles = {'color':colorText, 'font-size':'10px'}
        # self.graphWidget.setLabel('left', 'Frecuencia', **styles)
        # self.graphWidget.setLabel('bottom', 'Coeficiente', **styles)
        # self.graphWidget.setBackground(colorBackground)
        
        # self.vLayoutChart.addWidget(self.graphWidget)
        
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
        
    def changeValueBoost(self,_value):
        bootsValue = int(_value)
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOCVRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOCVRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            bootsValue = int(self.sBCountBoot.value())
            placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
            formatStr = '.'+str(placeDecimal)+'f'
            self.lOCVRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
            self.lOCVRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
            self.lOMediaRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
            self.lOMediaRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
            
        
        
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QVBoxLayout, QLayout, QLabel, QSizePolicy, QTableView,
    QSpacerItem, QGroupBox, QHBoxLayout, QPushButton, QTableWidget, QFrame, QAbstractItemView
)

from PyQt5.QtGui import (
    QFont, QPen
)

from PyQt5.QtCore import (
    QSize
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_boot_stropping_ui import Ui_WidgetValidationBootStropping
from view.components.widget_chart_histogram import WidgetChartHistogram

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
        self.tWCharts.setVisible(False)
        self.tWCharts.setFrameShape(QFrame.NoFrame)
        self.tWCharts.setFrameShadow(QFrame.Plain)
        self.tWCharts.setLineWidth(0)
        self.tWCharts.setSelectionMode(QAbstractItemView.NoSelection)
        self.tWCharts.setShowGrid(False)
        self.tWCharts.setGridStyle(QtCore.Qt.NoPen)
        self.tWCharts.setColumnCount(3)
        self.tWCharts.horizontalHeader().setVisible(False)
        self.tWCharts.verticalHeader().setVisible(False)
        
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
        self.tWCharts.setVisible(True)
        self.createChart()
        
    def createChart(self):
        
        self.tWCharts.clear()
        self.tWCharts.setColumnCount(3)
        header = self.tWCharts.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        bootsValue = int(self.sBCountBoot.value())
        
        datas = AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_FREQUENCY_COEFFICIENT_BOOT_STROPPING,boots=bootsValue)
        
        index = 0
        
        rows = len(datas)//3
        
        if len(datas)% 3 !=0 :
            rows=rows+1
            
        self.tWCharts.setRowCount(rows)
        
        for j in range(0,rows):
            self.tWCharts.setRowHeight(j,250)
        
        for k,v in datas.items():
            item = WidgetChartHistogram(v)
            self.tWCharts.setCellWidget(index//3,index%3,item)
            index = index +1 
        
        
        
    
        
    def changeValueBoost(self,_value):
        bootsValue = int(_value)
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOCVRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOCVRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        
    def changePreference(self,_listChange):
        bootsValue = int(self.sBCountBoot.value())
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.lOCVRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOCVRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSME.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.lOMediaRSQUARE.setText( str(format(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue),formatStr)) )
        self.createChart();
            
        
        
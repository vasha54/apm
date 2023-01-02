from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_boot_stropping_ui import Ui_WidgetValidationBootStropping

from view.preferences.preferences import PreferenceGUI

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
            
        
        
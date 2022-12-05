from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_boot_stropping_ui import Ui_WidgetValidationBootStropping


class WidgetValidationBootStropping(QWidget,Ui_WidgetValidationBootStropping):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        self.createConnects()
        
    def createWorkSpace(self):
        self.gBResult.setVisible(False)
        
    def setKeyModel(self, _keyModel):
        self.keyModel = _keyModel
    
    def createConnects(self):
        self.pBAnalizar.clicked.connect(self.calculate)
        #self.sBCountBoot.valueChanged.connect(self.changeValueBoost)
    
    def calculate(self):
        bootsValue = int(self.sBCountBoot.value())
        
        
        self.lOCVRSME.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue)) )
        self.lOCVRSQUARE.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue)) )
        self.lOMediaRSME.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue)) )
        self.lOMediaRSQUARE.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue)) )
        
        self.gBResult.setVisible(True)
        
    def changeValueBoost(self,_value):
        bootsValue = int(_value)
        self.lOCVRSME.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSEM_BOOT_STROPPING, boots=bootsValue)) )
        self.lOCVRSQUARE.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.CV_RSQUARE_BOOT_STROPPING, boots=bootsValue)) )
        self.lOMediaRSME.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSEM_BOOT_STROPPING, boots=bootsValue)) )
        self.lOMediaRSQUARE.setText( str(AnalysisData().getDataModel(self.keyModel, ModelLMR.MEDIA_RSQUARE_BOOT_STROPPING, boots=bootsValue)) )
        
        
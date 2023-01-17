from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_kold_ui import Ui_WidgetValidationKold

from view.preferences.preferences import PreferenceGUI

class WidgetValidationKold(QWidget,Ui_WidgetValidationKold):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        self.createConnects()
        PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.frameResult.setVisible(False)
        
    def setKeyModel(self, _keyModel):
        self.keyModel = _keyModel
    
    def createConnects(self):
        self.pBAnalizar.clicked.connect(self.calculate)
        #self.sBK.valueChanged.connect(self.changeValueK)
    
    def calculate(self):
        kValue = int(self.sBK.value())
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        self.lOCVNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOCVNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOCVRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOCVRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOMediaNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOMediaNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOMediaRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOMediaRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
        self.lORMSETest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RMSE_TEST_KFOLD,k = kValue),formatStr)) )
        self.lORSquareTest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SQUARE_TWO_TEST_KFOLD,k = kValue),formatStr)) )
        
        self.frameResult.setVisible(True)
    
    def changeValueK(self,_value):
        kValue = int(_value)
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        self.lOCVNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOCVNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOCVRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOCVRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOMediaNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOMediaNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
        self.lOMediaRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
        self.lOMediaRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
        self.lORMSETest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RMSE_TEST_KFOLD,k = kValue),formatStr)) )
        self.lORSquareTest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SQUARE_TWO_TEST_KFOLD,k = kValue),formatStr)) )
        
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            kValue = int(self.sBK.value())
            placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
            formatStr = '.'+str(placeDecimal)+'f'
            
            self.lOCVNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
            self.lOCVNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
            self.lOCVRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
            self.lOCVRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
            self.lOMediaNegRSMETE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TE_KFOLD,k = kValue),formatStr)) )
            self.lOMediaNegRSMETV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TV_KFOLD,k = kValue),formatStr)) )
            self.lOMediaRSquareTE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TE_KFOLD,k = kValue),formatStr)) )
            self.lOMediaRSquareTV.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TV_KFOLD,k = kValue),formatStr)) )
            self.lORMSETest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RMSE_TEST_KFOLD,k = kValue),formatStr)) )
            self.lORSquareTest.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SQUARE_TWO_TEST_KFOLD,k = kValue),formatStr)) )
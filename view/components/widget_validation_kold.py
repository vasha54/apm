from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_kold_ui import Ui_WidgetValidationKold


class WidgetValidationKold(QWidget,Ui_WidgetValidationKold):
    
    
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
        #self.sBK.valueChanged.connect(self.changeValueK)
    
    def calculate(self):
        kValue = int(self.sBK.value())
        print('keymodel',self.keyModel)
        self.lOCVNegRSMETE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TE_KFOLD,k = kValue)) )
        self.lOCVNegRSMETV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TV_KFOLD,k = kValue)) )
        self.lOCVRSquareTE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TE_KFOLD,k = kValue)) )
        self.lOCVRSquareTV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TV_KFOLD,k = kValue)) )
        self.lOMediaNegRSMETE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TE_KFOLD,k = kValue)) )
        self.lOMediaNegRSMETV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TV_KFOLD,k = kValue)) )
        self.lOMediaRSquareTE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TE_KFOLD,k = kValue)) )
        self.lOMediaRSquareTV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TV_KFOLD,k = kValue)) )
        self.lORMSETest.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RMSE_TEST_KFOLD,k = kValue)) )
        self.lORSquareTest.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SQUARE_TWO_TEST_KFOLD,k = kValue)) )
        
        self.gBResult.setVisible(True)
    
    def changeValueK(self,_value):
        kValue = int(_value)
        
        self.lOCVNegRSMETE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TE_KFOLD,k = kValue)) )
        self.lOCVNegRSMETV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_NEG_RMSE_TV_KFOLD,k = kValue)) )
        self.lOCVRSquareTE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TE_KFOLD,k = kValue)) )
        self.lOCVRSquareTV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CV_RSQUARE_TV_KFOLD,k = kValue)) )
        self.lOMediaNegRSMETE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TE_KFOLD,k = kValue)) )
        self.lOMediaNegRSMETV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_NEG_RMSE_TV_KFOLD,k = kValue)) )
        self.lOMediaRSquareTE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TE_KFOLD,k = kValue)) )
        self.lOMediaRSquareTV.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RSQUARE_TV_KFOLD,k = kValue)) )
        self.lORMSETest.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RMSE_TEST_KFOLD,k = kValue)) )
        self.lORSquareTest.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SQUARE_TWO_TEST_KFOLD,k = kValue)) )
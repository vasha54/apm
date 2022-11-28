from view.ui.widget_test_normal_residual_not_scale_ui import Ui_WidgetTestNormalResidualNotScale

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class WidgetTestNormalResidualNotScale(QWidget,Ui_WidgetTestNormalResidualNotScale):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
    def createWorkSpace(self):
        self.lOANDERSON_DARLING_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_PVALUE_RWS) )  )
        self.lOANDERSON_DARLING_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_RWS) )  )
        self.lOCHI_SQUARE_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_PVALUE_RWS) )  )
        self.lOCHI_SQUARE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_RWS) )  )
        self.lOCOEFF_ASYMETRY_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_ASYMETRY_RWS) )  )
        self.lOCOEFF_CURTOSIS_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_CURTOSIS_RWS) )  )
        self.lOJARQUE_BERA_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_PVALUE_RWS) )  )
        self.lOJARQUE_BERA_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_RWS) )  )
        self.lOK_CUAD_DANGOSTINO_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_PVALUE_RWS) )  )
        self.lOK_CUAD_DANGOSTINO_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_RWS) )  )
        self.lOKOLMOGOROV_SMIRNOV_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_PVALUE_RWS) )  )
        self.lOKOLMOGOROV_SMIRNOV_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_RWS) )  )
        self.lOLILLIEFORS_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_PVALUE_RWS) )  )
        self.lOLILLIEFORS_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_RWS) )  )
        self.lOSHAPIRO_WILK_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_RWS) )  )
        self.lOSHAPIRO_WILK_PVALUE_RWS.setText( str( AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_PVALUE_RWS) )  )
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
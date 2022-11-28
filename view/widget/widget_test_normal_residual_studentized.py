from view.ui.widget_test_normal_residual_studentized_ui import Ui_WidgetTestNormalResidualStudentized

from PyQt5.QtWidgets import (
    QWidget
)

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

class WidgetTestNormalResidualStudentized(QWidget,Ui_WidgetTestNormalResidualStudentized):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
    def createWorkSpace(self):
        self.lOANDERSON_DARLING_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_PVALUE_RE)) )
        self.lOANDERSON_DARLING_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_RE)) )
        self.lOCHI_SQUARE_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_PVALUE_RE)) )
        self.lOCHI_SQUARE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_RE)) )
        self.lOCOEFF_ASYMETRY_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_ASYMETRY_RE)) )
        self.lOCOEFF_CURTOSIS_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_CURTOSIS_RE)) )
        self.lOJARQUE_BERA_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_PVALUE_RE)) )
        self.lOJARQUE_BERA_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_RE)) )
        self.lOK_CUAD_DANGOSTINO_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_PVALUE_RE)) )
        self.lOK_CUAD_DANGOSTINO_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_RE)) )
        self.lOLILLIEFORS_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_PVALUE_RE)) )
        self.lOLILLIEFORS_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_RE)) )
        self.lOSHAPIRO_WILK_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_PVALUE_RE)) )
        self.lOSHAPIRO_WILK_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_RE)) )
        self.lOKOLMOGOROV_SMIRNOV_PVALUE_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_PVALUE_RE)) )
        self.lOKOLMOGOROV_SMIRNOV_RE.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_RE)) )
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
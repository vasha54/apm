from view.ui.widget_test_normal_residual_studentized_ui import Ui_WidgetTestNormalResidualStudentized

from PyQt5.QtWidgets import (
    QWidget,QVBoxLayout
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)


from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

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
        
        self.clearLayout(self.widgetGraphOne.layout())
        
        self.createChartQQTestNormalResidualStudentized()
        self.createChartDistributionResidualStudentized()
        
        
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
                
    def createChartQQTestNormalResidualStudentized(self):
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        styles = {'color':'b', 'font-size':'10px'}
        
        serie = AnalysisData().getDataModel(self.keyModel,ModelLMR.SERIE_CHART_QQ_TEST_NORMAL_RESIDUAL_STUDENTIZED)
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
        self.graphWidget.setBackground('w')
        
        brush = QBrush(QColor(0,0,0,255))
        brushLine = QBrush(QColor(255,0,0,255))
        
        penLine = pg.mkPen(color=(255, 0, 0), width=2)
        
        self.graphWidget.plot(xLine, yLine,pen=penLine ,symbol=None, symbolSize=5, symbolBrush=brushLine)
        self.graphWidget.plot(xs, ys,pen=None,symbol='o', symbolSize=5, symbolBrush=brush)
        
        self.widgetGraphOne.layout().addWidget(self.graphWidget)
    
    
    def createChartDistributionResidualStudentized(self):
        pass
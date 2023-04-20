from view.ui.widget_test_normal_residual_studentized_ui import Ui_WidgetTestNormalResidualStudentized

from PyQt5.QtWidgets import (
    QWidget,QVBoxLayout
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

from view.preferences.preferences import PreferenceGUI

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

from view.preferences.preferences import PreferenceGUI
from view.components.charts.chart_multiple import ChartMultiple


class WidgetTestNormalResidualStudentized(QWidget,Ui_WidgetTestNormalResidualStudentized):
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
        self.lOANDERSON_DARLING_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_PVALUE_RE),formatStr)) )
        self.lOANDERSON_DARLING_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ANDERSON_DARLING_RE),formatStr)) )
        self.lOCHI_SQUARE_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_PVALUE_RE),formatStr)) )
        self.lOCHI_SQUARE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.CHI_SQUARE_RE),formatStr)) )
        self.lOCOEFF_ASYMETRY_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_ASYMETRY_RE),formatStr)) )
        self.lOCOEFF_CURTOSIS_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COEFF_CURTOSIS_RE),formatStr)) )
        self.lOJARQUE_BERA_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_PVALUE_RE),formatStr)) )
        self.lOJARQUE_BERA_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.JARQUE_BERA_RE),formatStr)) )
        self.lOK_CUAD_DANGOSTINO_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_PVALUE_RE),formatStr)) )
        self.lOK_CUAD_DANGOSTINO_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.K_CUAD_DANGOSTINO_RE),formatStr)) )
        self.lOLILLIEFORS_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_PVALUE_RE),formatStr)) )
        self.lOLILLIEFORS_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LILLIEFORS_RE),formatStr)) )
        self.lOSHAPIRO_WILK_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_PVALUE_RE),formatStr)) )
        self.lOSHAPIRO_WILK_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SHAPIRO_WILK_RE),formatStr)) )
        self.lOKOLMOGOROV_SMIRNOV_PVALUE_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_PVALUE_RE),formatStr)) )
        self.lOKOLMOGOROV_SMIRNOV_RE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.KOLMOGOROV_SMIRNOV_RE),formatStr)) )
        
        self.clearLayout(self.widgetGraphOne.layout())
        self.clearLayout(self.widgetGraphTwo.layout())
        
        self.createChartQQTestNormalResidualStudentized()
        self.createChartDistributionResidualStudentized()
        
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
    
    def changePreference(self,_listChange):
        self.update()
    
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
                
    def createChartQQTestNormalResidualStudentized(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
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
        
        self.graphWidgetOne = ChartMultiple(self)
        self.graphWidgetOne.addPlot(xLine,yLine,color="#FF0000")
        self.graphWidgetOne.addScatter(xs,ys,c="#000000")
        
        
        self.graphWidgetOne.setNameChart("Gráfica Q-Q de distribución normal")
        self.graphWidgetOne.setTitleY("Cuartiles de los residuales")
        self.graphWidgetOne.setTitleX("Cuartiles teoricos")
        self.graphWidgetOne.setColorAxes(colorAxes)
        self.graphWidgetOne.setColorBackground(colorBackground)
        self.graphWidgetOne.setColorText(colorText)
        
        
        self.widgetGraphOne.layout().addWidget(self.graphWidgetOne)
        
        
    
    def createChartDistributionResidualStudentized(self):
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        series = AnalysisData().getDataModel(self.keyModel,ModelLMR.SERIE_CHART_DISTRIBUTION_RESIDUAL_STUDENTIZED)
        
        xKDE = []
        yKDE = []
        xNormal = []
        yNormal = [] 
        
        if series != None:
            xKDE = series[0]
            yKDE = series[1]
            xNormal = series[2]
            yNormal = series[3]
        
        self.graphWidgetTwo = ChartMultiple(self)
        self.graphWidgetTwo.addPlot(xNormal,yNormal,color="#FF0000",label="Distribución normal")
        self.graphWidgetTwo.addPlot(xKDE,yKDE,color="#000000",label="KDE")
        
        self.graphWidgetTwo.setNameChart("Distribución de los Residuales")
        self.graphWidgetTwo.setTitleY("Densidad")
        self.graphWidgetTwo.setTitleX("Residuales")
        self.graphWidgetTwo.setColorAxes(colorAxes)
        self.graphWidgetTwo.setColorBackground(colorBackground)
        self.graphWidgetTwo.setColorText(colorText)
        self.graphWidgetTwo.legend()
        
        self.widgetGraphTwo.layout().addWidget(self.graphWidgetTwo)
        
        
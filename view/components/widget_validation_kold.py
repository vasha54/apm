from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from PyQt5.QtGui import (
    QBrush, QColor, QPainter
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_validation_kold_ui import Ui_WidgetValidationKold

from view.preferences.preferences import PreferenceGUI
from view.components.charts.chart_multiple import ChartMultiple


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
        self.widgetChartNegRMSEKFold.setVisible(False)
        self.widgetChartRSquareKFold.setVisible(False)
        self.widgetChartValuesPredichosKFold.setVisible(False)
        
    def createChartValuesPredictedKFold(self):
        
        kValue = int(self.sBK.value())
        data =AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_VALUES_PREDICTED_KFOLD,k=kValue)
        
        xLine = [min(data['value-x'])-0.05,max(data['value-x'])+0.05]
        yLine = [min(data['value-y'])-0.05,max(data['value-y'])+0.05]
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        self.chartVPKFOLD = ChartMultiple(self)
        
        self.chartVPKFOLD.addPlot(xLine, yLine,color='#FF0000')
        self.chartVPKFOLD.addScatter(data['value-x'], data['value-y'],c='#0000FF')
        
        self.chartVPKFOLD.setTitleX('Valores predichos por el modelo (datos totales)')
        self.chartVPKFOLD.setTitleY('Valores predichos por K-Fold')
        self.chartVPKFOLD.setColorAxes(colorAxes)
        self.chartVPKFOLD.setColorBackground(colorBackground)
        self.chartVPKFOLD.setColorText(colorText)
        
        self.clearLayout(self.vLayoutChartValuesPredichosKFold)
        self.vLayoutChartValuesPredichosKFold.addWidget(self.chartVPKFOLD)
        
        
    def createChartNegRMSE(self):
        
        kValue = int(self.sBK.value())
        
        data =AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_NEG_RMSE_KFOLD,k=kValue)
        
        dataYTest=data['test_neg_mean']
        dataXTest=[1 * i for i in range(1, kValue + 1)]
        
        dataYTrain=data['train_neg_mean']
        dataXTrain=[1 * i for i in range(1, kValue + 1)]
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        self.chartNegRMSE = ChartMultiple(self)
        
        self.chartNegRMSE.addPlot(dataXTest, dataYTest,label='Test de validación',color='#0000FF',marker='o',markersize=2)
        self.chartNegRMSE.addPlot(dataXTrain, dataYTrain,label='Test de entrenamiento',color='#000000',marker='o',markersize=2)
        
        self.chartNegRMSE.setTitleX('K-Folds')
        self.chartNegRMSE.setTitleY('Neg-RMSE')
        self.chartNegRMSE.setColorAxes(colorAxes)
        self.chartNegRMSE.setColorBackground(colorBackground)
        self.chartNegRMSE.setColorText(colorText)
        self.chartNegRMSE.legend()
        
        self.clearLayout(self.vLayoutChartNegRMSEKFold)
        self.vLayoutChartNegRMSEKFold.addWidget(self.chartNegRMSE)
         
    
    def createChartRSquare(self):
        kValue = int(self.sBK.value())
        
        data =AnalysisData().getDataModel(self.keyModel,ModelLMR.CHART_R_SQUARE_KFOLD,k=kValue)
        
        dataYTest=data['test_r2']
        dataXTest=[1 * i for i in range(1, kValue + 1)]
        
        dataYTrain=data['train_r2']
        dataXTrain=[1 * i for i in range(1, kValue + 1)]
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        self.chartRSquare = ChartMultiple(self)
        
        self.chartRSquare.addPlot(dataXTest, dataYTest,label='Test de validación',color='#0000FF',marker='o',markersize=2)
        self.chartRSquare.addPlot(dataXTrain, dataYTrain,label='Test de entrenamiento',color='#000000',marker='o',markersize=2)
        
        self.chartRSquare.setTitleX('K-Folds')
        self.chartRSquare.setTitleY('R-cuadrado')
        self.chartRSquare.setColorAxes(colorAxes)
        self.chartRSquare.setColorBackground(colorBackground)
        self.chartRSquare.setColorText(colorText)
        self.chartRSquare.legend()
        
        self.clearLayout(self.vLayoutChartRSquareKFold)
        self.vLayoutChartRSquareKFold.addWidget(self.chartRSquare) 
          
        
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
        
        self.createChartNegRMSE()
        self.createChartRSquare()
        self.createChartValuesPredictedKFold()
        
        self.frameResult.setVisible(True)
        self.widgetChartNegRMSEKFold.setVisible(True)
        self.widgetChartRSquareKFold.setVisible(True)
        self.widgetChartValuesPredichosKFold.setVisible(True)
    
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
        
        self.createChartNegRMSE()
        self.createChartRSquare()
        self.createChartValuesPredictedKFold()
        
    def changePreference(self,_listChange):
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
        
        self.createChartNegRMSE()
        self.createChartRSquare()
        self.createChartValuesPredictedKFold()
        
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
        
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

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

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
        
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'Valores predichos por K-Fold', **styles)
        self.graphWidget.setLabel('bottom', 'Valores predichos por el modelo (datos totales)', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        penLine = pg.mkPen(color=(255, 0, 0), width=2)
        brushLine = QBrush(QColor(255,0,0,255))
        
        xLine = [0,1]
        yLine = [0,1]
        
        self.graphWidget.addLegend()
        
        self.graphWidget.plot(xLine, yLine,pen=penLine ,symbol=None, symbolSize=5, symbolBrush=brushLine)
        #self.graphWidget.plot(data['value-x'], data['value-y'], pen=None,symbol='o', symbolSize=5, symbolBrush=brush)
        #self.graphWidget.plot(dataXTrain, dataYTrain,name="Test de entrenamiento", pen=penLineTrain,symbol='o', symbolSize=5, symbolBrush=brushTrain)
        
        self.clearLayout(self.vLayoutChartValuesPredichosKFold)
        
        self.vLayoutChartValuesPredichosKFold.addWidget(self.graphWidget)
        
        
        
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
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'Neg-RMSE', **styles)
        self.graphWidget.setLabel('bottom', 'K-Folds', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brushTest = QtGui.QBrush(QtGui.QColor(0, 0, 255, 225))
        penLineTest = pg.mkPen(color=(0, 0, 255), width=2)
        brushTrain = QtGui.QBrush(QtGui.QColor(0, 0, 0, 255))
        penLineTrain = pg.mkPen(color=(0, 0, 0), width=2)
        
        self.graphWidget.addLegend()
        self.graphWidget.plot(dataXTest, dataYTest,name="Test de validación", pen=penLineTest,symbol='o', symbolSize=5, symbolBrush=brushTest)
        self.graphWidget.plot(dataXTrain, dataYTrain,name="Test de entrenamiento", pen=penLineTrain,symbol='o', symbolSize=5, symbolBrush=brushTrain)
        
        self.clearLayout(self.vLayoutChartNegRMSEKFold)
        
        self.vLayoutChartNegRMSEKFold.addWidget(self.graphWidget)
    
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
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'R-cuadrado', **styles)
        self.graphWidget.setLabel('bottom', 'K-Folds', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brushTest = QtGui.QBrush(QtGui.QColor(0, 0, 255, 225))
        penLineTest = pg.mkPen(color=(0, 0, 255), width=2)
        brushTrain = QtGui.QBrush(QtGui.QColor(0, 0, 0, 255))
        penLineTrain = pg.mkPen(color=(0, 0, 0), width=2)
        
        self.graphWidget.addLegend()
        self.graphWidget.plot(dataXTest, dataYTest,name="Test de validación", pen=penLineTest,symbol='o', symbolSize=5, symbolBrush=brushTest)
        self.graphWidget.plot(dataXTrain, dataYTrain,name="Test de entrenamiento", pen=penLineTrain,symbol='o', symbolSize=5, symbolBrush=brushTrain)
        
        self.clearLayout(self.vLayoutChartRSquareKFold)
        
        self.vLayoutChartRSquareKFold.addWidget(self.graphWidget)    
        
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
        
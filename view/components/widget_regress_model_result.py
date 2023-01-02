from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui
from view.preferences.preferences import PreferenceGUI
from view.ui.widget_regress_model_result_ui import Ui_WidgetRegressModelResult
from view.model.modelResultRegress_model import ModelResultRegressModel
from view.model.modelIntervalCoeffRegress_model import ModelIntervalCoeffRegressModel

class WidgetRegressModelResult(QWidget,Ui_WidgetRegressModelResult):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        PreferenceGUI.instance().subscribe(self)
    
    def changePreference(self,_listChange):
        if PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.createWorkSpace()
        
        
        
    def createWorkSpace(self):
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        self.lOVariableDependent.setText(AnalysisData().getDataModel(self.keyModel,ModelLMR.NAME_VD))
        self.lONumberObservations.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS),formatStr)))
        self.lOGLResidual.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.GL_RESIDUAL),formatStr)))
        self.lOGLModelo.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.GL_MODEL),formatStr)))
        
        self.lOAIC.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.AIC),formatStr)))
        self.lOBIC.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.BIC),formatStr)))
        self.lOLagLikeHead.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LOG_LIKELI_HEAD),formatStr)))
        
        self.lORcuad.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RCUAD),formatStr)))
        self.lORcuadAdjust.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RCUAD_ADJUST),formatStr)))
        self.lOFStadistic.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.FSTADISTIC),formatStr)))
        self.lOPValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.PVALUE),formatStr)))
        
        self.lOMSEModel.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_MODEL),formatStr)))
        self.lOMSEResidual.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_RESIDUAL),formatStr)))
        self.lOMSETotal.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_TOTAL),formatStr)))
        self.lORMSEModel.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RMSE_MODEL),formatStr)))
        
        self.modelResultRegress = ModelResultRegressModel(self.keyModel,self.tableViewResultRegress)
        self.modelIntervalCoeffRegress = ModelIntervalCoeffRegressModel(self.keyModel,self.tableViewIntervalEstimateCoeRegress)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewResultRegress.sizePolicy().hasHeightForWidth())
        
        self.tableViewResultRegress.setSizePolicy(sizePolicy)
        self.tableViewResultRegress.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewResultRegress.verticalHeader().hide()
        self.tableViewResultRegress.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewResultRegress.setModel(self.modelResultRegress)
        self.tableViewResultRegress.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewResultRegress.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        
        self.tableViewIntervalEstimateCoeRegress.setSizePolicy(sizePolicy)
        self.tableViewIntervalEstimateCoeRegress.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewIntervalEstimateCoeRegress.verticalHeader().hide()
        self.tableViewIntervalEstimateCoeRegress.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewIntervalEstimateCoeRegress.setModel(self.modelIntervalCoeffRegress)
        self.tableViewIntervalEstimateCoeRegress.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewIntervalEstimateCoeRegress.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        
        
        
        
        
        
        
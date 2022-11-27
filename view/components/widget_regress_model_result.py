from PyQt5.QtWidgets import (
    QWidget, QHeaderView
)

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtWidgets, QtGui

from view.ui.widget_regress_model_result_ui import Ui_WidgetRegressModelResult
from view.model.modelResultRegress_model import ModelResultRegressModel
from view.model.modelIntervalCoeffRegress_model import ModelIntervalCoeffRegressModel

class WidgetRegressModelResult(QWidget,Ui_WidgetRegressModelResult):
    
    
    def __init__(self,_keyModel='', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        
        
    def createWorkSpace(self):
        self.lOVariableDependent.setText(AnalysisData().getDataModel(self.keyModel,ModelLMR.NAME_VD))
        self.lONumberObservations.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS)))
        self.lOGLResidual.setText( str(AnalysisData().getDataModel(self.keyModel,ModelLMR.GL_RESIDUAL)))
        self.lOGLModelo.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.GL_MODEL)))
        
        self.lOAIC.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.AIC)))
        self.lOBIC.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.BIC)))
        self.lOLagLikeHead.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.LOG_LIKELI_HEAD)))
        
        self.lORcuad.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.RCUAD)))
        self.lORcuadAdjust.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.RCUAD_ADJUST)))
        self.lOFStadistic.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.FSTADISTIC)))
        self.lOPValue.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.PVALUE)))
        
        self.lOMSEModel.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_MODEL)))
        self.lOMSEResidual.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_RESIDUAL)))
        self.lOMSETotal.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.MSE_TOTAL)))
        self.lORMSEModel.setText(str(AnalysisData().getDataModel(self.keyModel,ModelLMR.RMSE_MODEL)))
        
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
        
        self.tableViewIntervalEstimateCoeRegress.setSizePolicy(sizePolicy)
        self.tableViewIntervalEstimateCoeRegress.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewIntervalEstimateCoeRegress.verticalHeader().hide()
        self.tableViewIntervalEstimateCoeRegress.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewIntervalEstimateCoeRegress.setModel(self.modelIntervalCoeffRegress)
        
        
        
        
        
        
        
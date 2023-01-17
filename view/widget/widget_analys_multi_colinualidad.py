from PyQt5.QtWidgets import (
    QWidget,QHeaderView
)

from PyQt5 import QtCore, QtWidgets

from view.model.modelVIFAnalysMultiColinualidad_model import ModelVIFAnalysMultiColinualidadModel
from view.ui.widget_analys_multi_colinualidad_ui import Ui_WidgetAnalysMultiColinualidad

from controller.analysis_data import AnalysisData
from view.preferences.preferences import PreferenceGUI
from model.modelLMR import ModelLMR
from exceptions.exceptions import NotFoundParameterExtraException
from view.components import message_box as MB

class WidgetAnalysMultiColinualidad(QWidget,Ui_WidgetAnalysMultiColinualidad):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.preference = PreferenceGUI.instance().subscribe(self)
        self.createWorkSpace()
        self.createConnects()
        
        
    def createWorkSpace(self):
        self.model = ModelVIFAnalysMultiColinualidadModel(self.keyModel)
        self.tableViewMultiColinealidad.setModel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewMultiColinealidad.sizePolicy().hasHeightForWidth())
        
        self.tableViewMultiColinealidad.setSizePolicy(sizePolicy)
        self.tableViewMultiColinealidad.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewMultiColinealidad.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewMultiColinealidad.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewMultiColinealidad.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        self.lOutputMeanResidualNotScaled.setText(str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RESIDUAL_NOT_SCALED),formatStr) ))
        self.lOutputMeanResidualStudentized.setText(str(format (AnalysisData().getDataModel(self.keyModel,ModelLMR.MEDIA_RESIDUAL_STUDENTIZED),formatStr)))
        self.lOutputTestWhiteWE.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SPECIFICATION_WHITE_WE),formatStr) ))
        self.lOutputTestWhitePValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_SPECIFICATION_WHITE_PVALUE),formatStr) ))
        self.lOutputTestHarveyCollierHC.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_HARVEY_COLLIER_LINEARITY_HC),formatStr)))
        self.lOutputTestHarveyCollierPValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_HARVEY_COLLIER_LINEARITY_PVALUE),formatStr)))
        self.lOutputTestRainbowF.setText(str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RAINBOW_LINEARITY_F),formatStr)))
        self.lOutputTestRainbowPValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RAINBOW_LINEARITY_PVALUE),formatStr)))
        try:
            self.lOutputLangrageF.setText(str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_MULTIPLIER_LAGRANGE_LINEARITY_F),formatStr) ))
            self.lOutputLangragePValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_MULTIPLIER_LAGRANGE_LINEARITY_PVALUE),formatStr)))
        except NotFoundParameterExtraException as e:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "Ha ocurrido error en la prueba de multiplicadores de Lagrange para linealidad",str(e))
            messageBox.exec()
        finally:
            self.calculateTestRamsey()
    
    def createConnects(self):
        self.pBCalculate.clicked.connect(self.calculateTestRamsey)
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.update()
            
    def calculateTestRamsey(self):
        powerInt = int(self.sBPower.value())
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        try:
            self.lOutputTestRamseyF.setText(str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RAMSEY_F,power=powerInt),formatStr) ))
            self.lOutputTestRamseyPValue.setText(str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.TEST_RAMSEY_PVALUE,power=powerInt),formatStr)))
        except NotFoundParameterExtraException as e:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "Ha ocurrido error en el Test de Ramsey ",str(e))
            messageBox.exec()
from PyQt5 import QtCore, QtGui, QtWidgets
from view.view.widget_tab.widget_tab import WidgetTab

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR
from view.preferences.preferences import PreferenceGUI
from exceptions.exceptions import EstadigrafoFisherCalFOException, RelationFOFTException, SumsNeighborsException

from view.components import message_box as MB

class WidgetQualityAdjustModel(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect() 
        PreferenceGUI.instance().subscribe(self)   
    
    def createUI(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetCentral)
        self.widget = QtWidgets.QWidget(self.widgetCentral)
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lORMSE = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lORMSE.sizePolicy().hasHeightForWidth())
        self.lORMSE.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.lORMSE, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.lORelationRangeValuesERRSTD = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lORelationRangeValuesERRSTD.sizePolicy().hasHeightForWidth())
        self.lORelationRangeValuesERRSTD.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.lORelationRangeValuesERRSTD, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout_2.addWidget(self.label_5)
        self.dSBLevelSignification = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dSBLevelSignification.sizePolicy().hasHeightForWidth())
        self.dSBLevelSignification.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dSBLevelSignification.setFont(font)
        self.dSBLevelSignification.setMaximum(1.0)
        self.dSBLevelSignification.setSingleStep(0.01)
        self.dSBLevelSignification.setProperty("value", 0.05)
        self.horizontalLayout_2.addWidget(self.dSBLevelSignification)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.pBCalculate = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pBCalculate.setFont(font)
        self.horizontalLayout_3.addWidget(self.pBCalculate)
        spacerItem3 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)
        self.horizontalLayout.addWidget(self.widget)
        self.widgetResult = QtWidgets.QWidget(self.widgetCentral)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetResult)
        self.label_6 = QtWidgets.QLabel(self.widgetResult)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lOSSfa = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOSSfa, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lOSSpe = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOSSpe, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.lOCountObsv = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOCountObsv, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.lOCountLevelVarInde = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOCountLevelVarInde, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.lOEstFisCalFO = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOEstFisCalFO, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)
        self.lOEstFisTabFO = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lOEstFisTabFO, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.gridLayout_2.addWidget(self.label_13, 7, 0, 1, 1)
        self.lORelationFOFt = QtWidgets.QLabel(self.widgetResult)
        self.gridLayout_2.addWidget(self.lORelationFOFt, 7, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widgetResult)
        
        self.label.setText(( "RMSE:"))
        self.lORMSE.setText("NA")
        self.label_3.setText("Relación entre el rango de los\n"
"valores ajustados y el error estándar\n"
"promedio estimado")
        self.lORelationRangeValuesERRSTD.setText("NA")
        self.groupBox.setTitle("Prueba de bondad de ajuste de Fisher")
        self.label_5.setText("Nivel de significación:")
        self.pBCalculate.setText("Calcular")
        self.label_6.setText("Resultado de la Prueba de bondad\n"
"de Ajuste de Fisher")
        self.label_7.setText("SSfa:")
        self.lOSSfa.setText("NA")
        self.label_8.setText("SSpe:")
        self.lOSSpe.setText("NA")
        self.label_9.setText("Cantidad de observaciones:")
        self.lOCountObsv.setText("NA")
        self.label_10.setText("Cantidad de niveles de las\n"
"variables independientes:")
        self.lOCountLevelVarInde.setText("NA")
        self.label_11.setText("Estadigráfo de Fisher calculado (Fo):")
        self.lOEstFisCalFO.setText("NA")
        self.label_12.setText("Estadigráfo de Fisher tabulado (Ft):")
        self.lOEstFisTabFO.setText("NA")
        self.label_13.setText("Relación (Fo/Ft):")
        self.lORelationFOFt.setText("NA")
    
    def createWorkspace(self):
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.hideShowComponentWidgetResult(False)
        self.lORMSE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RMSE_MODEL),formatStr)) )
        self.lORelationRangeValuesERRSTD.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RELATION_RANGE_VALUES_AND_ERROR_STD_MEAN),formatStr) ))
    
    def changePreference(self,_listChange):
        if PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.updateTab()
            placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
            formatStr = '.'+str(placeDecimal)+'f'
            levelSig = self.dSBLevelSignification.value()
            
            if self.lOSSfa.isVisible() == True:
                self.lOSSfa.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SSFA,alpha=float(levelSig)),formatStr) ) )
            
            if self.lOSSpe.isVisible() == True:
                self.lOSSpe.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SSPE,alpha=float(levelSig)),formatStr) ) )
            
            if self.lOCountObsv.isVisible() == True:
                self.lOCountObsv.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS,alpha=float(levelSig)),formatStr) ) )
            
            if self.lOCountLevelVarInde.isVisible() == True:
                self.lOCountLevelVarInde.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COUNT_LEVEL_VAR_IND,alpha=float(levelSig)),formatStr) ) )
            
            if self.lOEstFisCalFO.isVisible() == True:
                try:
                    self.lOEstFisCalFO.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ESTADIGRAFO_FISHER_CAL_FO,alpha=float(levelSig)),formatStr) ) )
                except EstadigrafoFisherCalFOException as e:
                    self.lOEstFisCalFO.setText("NA")
            
            if self.lOEstFisTabFO.isVisible() == True:
                self.lOEstFisTabFO.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ESTADIGRAFO_FISHER_TAB_FT,alpha=float(levelSig)),formatStr) ) )
            
            if self.lORelationFOFt.isVisible() == True:
                try:
                    self.lORelationFOFt.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RELATION_FOFT,alpha=float(levelSig)),formatStr) ) )
                except RelationFOFTException as f:
                    self.lORelationFOFt.setText("NA")
                
                
    
    def createConnect(self):
        self.pBCalculate.clicked.connect(self.calculate)
        super().createConnect()
        
    def updateTab(self):
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.lORMSE.setText( str(format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RMSE_MODEL),formatStr)) )
        try:
            self.lORelationRangeValuesERRSTD.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RELATION_RANGE_VALUES_AND_ERROR_STD_MEAN),formatStr) ))
        except SumsNeighborsException as f:
            self.lORelationRangeValuesERRSTD.setText("NA")
            errorMessage = str(f)
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       errorMessage)
            messageBox.exec()
             
            
    def calculate(self):
        levelSig = self.dSBLevelSignification.value()
        self.hideShowComponentWidgetResult(False)
        
        sumVecinos =0
        errorMessage=""
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
          
        try:
            sumVecinos = AnalysisData().getDataModel(self.keyModel, ModelLMR.SUMS_NEIGHBORS,alpha=float(levelSig))
        except SumsNeighborsException as f:
            errorMessage = errorMessage+str(f)
        
        if sumVecinos > 0 :
           self.lOSSfa.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SSFA,alpha=float(levelSig)),formatStr) ) )
           self.lOSSpe.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.SSPE,alpha=float(levelSig)),formatStr) ) )
           self.lOCountObsv.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.NUMBER_MEAS,alpha=float(levelSig)),formatStr) ) )
           self.lOCountLevelVarInde.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.COUNT_LEVEL_VAR_IND,alpha=float(levelSig)),formatStr) ) )
           try:
               self.lOEstFisCalFO.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ESTADIGRAFO_FISHER_CAL_FO,alpha=float(levelSig)),formatStr) ) )
           except EstadigrafoFisherCalFOException as e:
               errorMessage = errorMessage+str(e)
               self.lOEstFisCalFO.setText("NA")
           self.lOEstFisTabFO.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.ESTADIGRAFO_FISHER_TAB_FT,alpha=float(levelSig)),formatStr) ) )
           try:
               self.lORelationFOFt.setText( str( format(AnalysisData().getDataModel(self.keyModel,ModelLMR.RELATION_FOFT,alpha=float(levelSig)),formatStr) ) )   
           except RelationFOFTException as f:
               errorMessage = errorMessage+str(f)
               self.lORelationFOFt.setText("NA")
           self.hideShowComponentWidgetResult(True)
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "Error, debe contar con observaciones replicadas")
            messageBox.exec()
            
        if len(errorMessage)!=0:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       errorMessage)
            messageBox.exec()
        
        
    def hideShowComponentWidgetResult(self,_visible):
        self.label_6.setVisible(_visible)
        self.label_7.setVisible(_visible)
        self.label_8.setVisible(_visible)
        self.label_9.setVisible(_visible)
        self.label_10.setVisible(_visible)
        self.label_11.setVisible(_visible)
        self.label_12.setVisible(_visible)
        self.label_13.setVisible(_visible)
        self.lOSSfa.setVisible(_visible)
        self.lOSSpe.setVisible(_visible)
        self.lOCountObsv.setVisible(_visible)
        self.lOCountLevelVarInde.setVisible(_visible)
        self.lOEstFisCalFO.setVisible(_visible)
        self.lOEstFisTabFO.setVisible(_visible)
        self.lORelationFOFt.setVisible(_visible)
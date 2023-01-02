from view.view.widget_tab.widget_tab import WidgetTab

from controller.analysis_data import AnalysisData

from view.components.widget_validation_boot_stropping import  WidgetValidationBootStropping
from view.components.widget_validation_kold import WidgetValidationKold
from view.preferences.preferences import PreferenceGUI

from PyQt5 import QtCore, QtGui, QtWidgets
class WidgetValidate(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        self.gridLayout = QtWidgets.QGridLayout(self.widgetCentral)
        self.rBKFold = QtWidgets.QRadioButton(self.widgetCentral)
        self.gridLayout.addWidget(self.rBKFold, 0, 0, 1, 1)
        self.rbBootStro = QtWidgets.QRadioButton(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbBootStro.sizePolicy().hasHeightForWidth())
        self.rbBootStro.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.rbBootStro, 0, 1, 1, 1)
        self.subWidget = QtWidgets.QWidget(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subWidget.sizePolicy().hasHeightForWidth())
        self.subWidget.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.subWidget, 1, 0, 1, 2)
        self.pushButtonNext.setVisible(False)
        
        self.rBKFold.setText("Validación cruzada por K-Fold")
        self.rbBootStro.setText("Validación por bootsstropping")
    
    def createWorkspace(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.widgetValidationKold = WidgetValidationKold(self.keyModel)
        self.widgetValidationBootStropping = WidgetValidationBootStropping(self.keyModel)
    
    def createConnect(self):
        self.rBKFold.clicked.connect(self.changeMethodValidation)
        self.rbBootStro.clicked.connect(self.changeMethodValidation)
        super().createConnect()
        
    def updateTab(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.widgetValidationBootStropping.setKeyModel(self.keyModel)
        self.widgetValidationKold.setKeyModel(self.keyModel)
    
    def changeMethodValidation(self):
        if self.rBKFold.isChecked() == True and self.rbBootStro.isChecked() == False:
            self.gridLayout.replaceWidget(self.widgetValidationBootStropping,self.subWidget)
            self.gridLayout.replaceWidget(self.subWidget,self.widgetValidationKold)
            self.subWidget.setVisible(False)
            self.widgetValidationBootStropping.setVisible(False)
            self.widgetValidationKold.changePreference([PreferenceGUI.DECIMAL_PLACES])
            self.widgetValidationKold.setVisible(True)
        elif self.rBKFold.isChecked() == False and self.rbBootStro.isChecked() == True:
            self.gridLayout.replaceWidget(self.widgetValidationKold,self.subWidget)
            self.gridLayout.replaceWidget(self.subWidget,self.widgetValidationBootStropping)
            self.subWidget.setVisible(False)
            self.widgetValidationKold.setVisible(False)
            self.widgetValidationBootStropping.changePreference([PreferenceGUI.DECIMAL_PLACES])
            self.widgetValidationBootStropping.setVisible(True)
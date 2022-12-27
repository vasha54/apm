from PyQt5.QtWidgets import (
    QDialog, QColorDialog
)
from PyQt5 import QtCore, QtGui, QtWidgets
from view.ui.dialog_preference_ui import Ui_DialogPreference
from view.preferences.preferences import PreferenceGUI

class DialogPreference(QDialog,Ui_DialogPreference):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.createWorkSpace()
        self.createConnect()
        
    def createWorkSpace(self):
        self.prefence = PreferenceGUI.instance()
        self.tBColorBackgroundChart.setObjectName(self.prefence.COLOR_BACKGROUND_CHART)
        self.tBColorEjesChart.setObjectName(self.prefence.COLOR_AXES_CHART)
        self.tBColorTextChart.setObjectName(self.prefence.COLOR_TEXT_CHART)
        self.sBDecimalPlaces.setObjectName(self.prefence.DECIMAL_PLACES)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setText("Salvar")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Cancelar")
        
        self.keyPreference = dict()
        
        for key in self.prefence.LIST_PREFERENCES:
            self.keyPreference[key] = None
        self.updateValuesPreferences()
    
    def createConnect(self):
        self.tBColorBackgroundChart.clicked.connect(self.selectColorDialog)
        self.tBColorEjesChart.clicked.connect(self.selectColorDialog)
        self.tBColorTextChart.clicked.connect(self.selectColorDialog)
        self.sBDecimalPlaces.valueChanged.connect(self.changeValueDecimalPlaces)
        self.pBResetValue.clicked.connect(self.resetPreference)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def selectColorDialog(self):
        object_sender = self.sender()
        
        color = QColorDialog.getColor()

        if color.isValid():
            colorSelect=color.name()
            
            if object_sender.objectName() == self.tBColorBackgroundChart.objectName():
                self.tBColorBackgroundChart.setStyleSheet("background-color:"+colorSelect+";")
            elif object_sender.objectName() == self.tBColorEjesChart.objectName():
                self.tBColorEjesChart.setStyleSheet("background-color:"+colorSelect+";")
            elif object_sender.objectName() == self.tBColorTextChart.objectName():
                self.tBColorTextChart.setStyleSheet("background-color:"+colorSelect+";")
            
            self.keyPreference[object_sender.objectName()]=colorSelect
            
    def changeValueDecimalPlaces(self,_newValue):
        self.keyPreference[self.sBDecimalPlaces.objectName()]=_newValue
        
    def accept(self):
        self.prefence.updateValueSettings(self.keyPreference)
        return super().accept()
    
    def resetPreference(self):
        self.prefence.resetSettings()
        self.updateValuesPreferences()
    
    def updateValuesPreferences(self):
        value = self.prefence.getValueSettings(self.prefence.DECIMAL_PLACES)
        self.sBDecimalPlaces.setValue(int(value))
        value = self.prefence.getValueSettings(self.prefence.COLOR_AXES_CHART)
        self.tBColorEjesChart.setStyleSheet("background-color:"+value+";")
        value = self.prefence.getValueSettings(self.prefence.COLOR_BACKGROUND_CHART)
        self.tBColorBackgroundChart.setStyleSheet("background-color:"+value+";")
        value = self.prefence.getValueSettings(self.prefence.COLOR_TEXT_CHART)
        self.tBColorTextChart.setStyleSheet("background-color:"+value+";")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_validation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetValidation(object):
    def setupUi(self, WidgetValidation):
        WidgetValidation.setObjectName("WidgetValidation")
        WidgetValidation.resize(701, 300)
        self.gridLayout = QtWidgets.QGridLayout(WidgetValidation)
        self.gridLayout.setObjectName("gridLayout")
        self.rBKFold = QtWidgets.QRadioButton(WidgetValidation)
        self.rBKFold.setChecked(True)
        self.rBKFold.setObjectName("rBKFold")
        self.gridLayout.addWidget(self.rBKFold, 0, 0, 1, 1)
        self.rbBootStro = QtWidgets.QRadioButton(WidgetValidation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbBootStro.sizePolicy().hasHeightForWidth())
        self.rbBootStro.setSizePolicy(sizePolicy)
        self.rbBootStro.setObjectName("rbBootStro")
        self.gridLayout.addWidget(self.rbBootStro, 0, 1, 1, 1)
        self.subWidget = QtWidgets.QWidget(WidgetValidation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subWidget.sizePolicy().hasHeightForWidth())
        self.subWidget.setSizePolicy(sizePolicy)
        self.subWidget.setObjectName("subWidget")
        self.gridLayout.addWidget(self.subWidget, 1, 0, 1, 2)

        self.retranslateUi(WidgetValidation)
        QtCore.QMetaObject.connectSlotsByName(WidgetValidation)

    def retranslateUi(self, WidgetValidation):
        _translate = QtCore.QCoreApplication.translate
        WidgetValidation.setWindowTitle(_translate("WidgetValidation", "Form"))
        self.rBKFold.setText(_translate("WidgetValidation", "Validación cruzada por K-Fold"))
        self.rbBootStro.setText(_translate("WidgetValidation", "Validación por bootsstropping"))
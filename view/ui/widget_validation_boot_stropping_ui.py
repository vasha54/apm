# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_validation_boot_stropping.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetValidationBootStropping(object):
    def setupUi(self, WidgetValidationBootStropping):
        WidgetValidationBootStropping.setObjectName("WidgetValidationBootStropping")
        WidgetValidationBootStropping.resize(825, 516)
        self.gridLayout_4 = QtWidgets.QGridLayout(WidgetValidationBootStropping)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(WidgetValidationBootStropping)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sBCountBoot = QtWidgets.QSpinBox(WidgetValidationBootStropping)
        self.sBCountBoot.setMinimum(1)
        self.sBCountBoot.setMaximum(10000)
        self.sBCountBoot.setObjectName("sBCountBoot")
        self.horizontalLayout.addWidget(self.sBCountBoot)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(171, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(WidgetValidationBootStropping)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(376, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 448, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 3, 4, 1)
        self.pBAnalizar = QtWidgets.QPushButton(WidgetValidationBootStropping)
        self.pBAnalizar.setObjectName("pBAnalizar")
        self.gridLayout_4.addWidget(self.pBAnalizar, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(286, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 1, 1, 2)
        self.gBResult = QtWidgets.QGroupBox(WidgetValidationBootStropping)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gBResult.setFont(font)
        self.gBResult.setObjectName("gBResult")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gBResult)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gBResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lOMediaRSME = QtWidgets.QLabel(self.gBResult)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMediaRSME.setFont(font)
        self.lOMediaRSME.setObjectName("lOMediaRSME")
        self.gridLayout_3.addWidget(self.lOMediaRSME, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gBResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.lOCVRSME = QtWidgets.QLabel(self.gBResult)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOCVRSME.setFont(font)
        self.lOCVRSME.setObjectName("lOCVRSME")
        self.gridLayout_3.addWidget(self.lOCVRSME, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gBResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.lOMediaRSQUARE = QtWidgets.QLabel(self.gBResult)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMediaRSQUARE.setFont(font)
        self.lOMediaRSQUARE.setObjectName("lOMediaRSQUARE")
        self.gridLayout_3.addWidget(self.lOMediaRSQUARE, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gBResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.lOCVRSQUARE = QtWidgets.QLabel(self.gBResult)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOCVRSQUARE.setFont(font)
        self.lOCVRSQUARE.setObjectName("lOCVRSQUARE")
        self.gridLayout_3.addWidget(self.lOCVRSQUARE, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.gBResult, 2, 0, 1, 3)
        self.widgetChart = QtWidgets.QWidget(WidgetValidationBootStropping)
        self.widgetChart.setObjectName("widgetChart")
        self.gridLayout = QtWidgets.QGridLayout(self.widgetChart)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(383, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 247, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widgetChart, 3, 0, 1, 3)

        self.retranslateUi(WidgetValidationBootStropping)
        QtCore.QMetaObject.connectSlotsByName(WidgetValidationBootStropping)

    def retranslateUi(self, WidgetValidationBootStropping):
        _translate = QtCore.QCoreApplication.translate
        WidgetValidationBootStropping.setWindowTitle(_translate("WidgetValidationBootStropping", "Form"))
        self.label.setText(_translate("WidgetValidationBootStropping", "Cantidad de boot:"))
        self.pBAnalizar.setText(_translate("WidgetValidationBootStropping", "Analizar"))
        self.gBResult.setTitle(_translate("WidgetValidationBootStropping", "Resultado"))
        self.label_2.setText(_translate("WidgetValidationBootStropping", "Media del RSME:"))
        self.lOMediaRSME.setText(_translate("WidgetValidationBootStropping", "NA"))
        self.label_3.setText(_translate("WidgetValidationBootStropping", "CV del RSME:"))
        self.lOCVRSME.setText(_translate("WidgetValidationBootStropping", "NA"))
        self.label_4.setText(_translate("WidgetValidationBootStropping", "Media del R - Cuadrado:"))
        self.lOMediaRSQUARE.setText(_translate("WidgetValidationBootStropping", "NA"))
        self.label_5.setText(_translate("WidgetValidationBootStropping", "CV del R - Cuadrado:"))
        self.lOCVRSQUARE.setText(_translate("WidgetValidationBootStropping", "NA"))

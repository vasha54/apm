# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetTab(object):
    def setupUi(self, WidgetTab):
        WidgetTab.setObjectName("WidgetTab")
        sizePolicyWidget = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        WidgetTab.setSizePolicy(sizePolicyWidget)
        self.gridLayout = QtWidgets.QGridLayout(WidgetTab)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetCentral = QtWidgets.QWidget(WidgetTab)
        self.widgetCentral.setAutoFillBackground(True)
        self.widgetCentral.setObjectName("widgetCentral")
        self.gridLayout.addWidget(self.widgetCentral, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(697, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButtonNext = QtWidgets.QPushButton(WidgetTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonNext.sizePolicy().hasHeightForWidth())
        self.pushButtonNext.setSizePolicy(sizePolicy)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.gridLayout.addWidget(self.pushButtonNext, 1, 1, 1, 1)

        self.retranslateUi(WidgetTab)
        QtCore.QMetaObject.connectSlotsByName(WidgetTab)

    def retranslateUi(self, WidgetTab):
        _translate = QtCore.QCoreApplication.translate
        WidgetTab.setWindowTitle(_translate("WidgetTab", "Form"))
        self.pushButtonNext.setText(_translate("WidgetTab", "Siguiente paso"))

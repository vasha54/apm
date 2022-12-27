# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_preference.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from view.resource import resource

class Ui_DialogPreference(object):
    def setupUi(self, DialogPreference):
        DialogPreference.setObjectName("DialogPreference")
        DialogPreference.resize(458, 236)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogPreference.sizePolicy().hasHeightForWidth())
        DialogPreference.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogPreference.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DialogPreference)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sBDecimalPlaces = QtWidgets.QSpinBox(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBDecimalPlaces.sizePolicy().hasHeightForWidth())
        self.sBDecimalPlaces.setSizePolicy(sizePolicy)
        self.sBDecimalPlaces.setMinimumSize(QtCore.QSize(60, 35))
        self.sBDecimalPlaces.setMaximumSize(QtCore.QSize(60, 35))
        self.sBDecimalPlaces.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sBDecimalPlaces.setMaximum(21)
        self.sBDecimalPlaces.setObjectName("sBDecimalPlaces")
        self.verticalLayout.addWidget(self.sBDecimalPlaces)
        self.tBColorBackgroundChart = QtWidgets.QToolButton(DialogPreference)
        self.tBColorBackgroundChart.setMinimumSize(QtCore.QSize(60, 35))
        self.tBColorBackgroundChart.setMaximumSize(QtCore.QSize(60, 35))
        self.tBColorBackgroundChart.setAutoFillBackground(True)
        self.tBColorBackgroundChart.setText("")
        self.tBColorBackgroundChart.setCheckable(False)
        self.tBColorBackgroundChart.setChecked(False)
        self.tBColorBackgroundChart.setAutoExclusive(True)
        self.tBColorBackgroundChart.setAutoRaise(False)
        self.tBColorBackgroundChart.setObjectName("tBColorBackgroundChart")
        self.verticalLayout.addWidget(self.tBColorBackgroundChart)
        self.tBColorTextChart = QtWidgets.QToolButton(DialogPreference)
        self.tBColorTextChart.setMinimumSize(QtCore.QSize(60, 35))
        self.tBColorTextChart.setMaximumSize(QtCore.QSize(60, 35))
        self.tBColorTextChart.setAutoFillBackground(True)
        self.tBColorTextChart.setText("")
        self.tBColorTextChart.setAutoRaise(False)
        self.tBColorTextChart.setObjectName("tBColorTextChart")
        self.verticalLayout.addWidget(self.tBColorTextChart)
        self.tBColorEjesChart = QtWidgets.QToolButton(DialogPreference)
        self.tBColorEjesChart.setMinimumSize(QtCore.QSize(60, 35))
        self.tBColorEjesChart.setMaximumSize(QtCore.QSize(60, 35))
        self.tBColorEjesChart.setAutoFillBackground(True)
        self.tBColorEjesChart.setText("")
        self.tBColorEjesChart.setAutoRaise(False)
        self.tBColorEjesChart.setObjectName("tBColorEjesChart")
        self.verticalLayout.addWidget(self.tBColorEjesChart)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pBResetValue = QtWidgets.QPushButton(DialogPreference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBResetValue.sizePolicy().hasHeightForWidth())
        self.pBResetValue.setSizePolicy(sizePolicy)
        self.pBResetValue.setObjectName("pBResetValue")
        self.horizontalLayout.addWidget(self.pBResetValue)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogPreference)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogPreference)

    def retranslateUi(self, DialogPreference):
        _translate = QtCore.QCoreApplication.translate
        DialogPreference.setWindowTitle(_translate("DialogPreference", "Preferencias"))
        self.label.setText(_translate("DialogPreference", "Lugares decimales:"))
        self.label_2.setText(_translate("DialogPreference", "Color del fondo de los gráficos:"))
        self.label_3.setText(_translate("DialogPreference", "Color del texto de los gráficos:"))
        self.label_4.setText(_translate("DialogPreference", "Color de los ejes de los gráficos:"))
        self.pBResetValue.setText(_translate("DialogPreference", "Establecer valores por defecto"))


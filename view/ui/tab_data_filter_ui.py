# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_data_filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetDataFilter(object):
    def setupUi(self, WidgetDataFilter):
        WidgetDataFilter.setObjectName("WidgetDataFilter")
        WidgetDataFilter.resize(696, 471)
        self.gridLayout = QtWidgets.QGridLayout(WidgetDataFilter)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableViewDataFrame = QtWidgets.QTableView(WidgetDataFilter)
        self.tableViewDataFrame.setMinimumSize(QtCore.QSize(600, 0))
        self.tableViewDataFrame.setObjectName("tableViewDataFrame")
        self.verticalLayout.addWidget(self.tableViewDataFrame)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listViewVariable = QtWidgets.QListView(WidgetDataFilter)
        self.listViewVariable.setObjectName("listViewVariable")
        self.verticalLayout_2.addWidget(self.listViewVariable)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonNext = QtWidgets.QPushButton(WidgetDataFilter)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.retranslateUi(WidgetDataFilter)
        QtCore.QMetaObject.connectSlotsByName(WidgetDataFilter)

    def retranslateUi(self, WidgetDataFilter):
        _translate = QtCore.QCoreApplication.translate
        WidgetDataFilter.setWindowTitle(_translate("WidgetDataFilter", "Form"))
        self.label.setText(_translate("WidgetDataFilter", "Datos Iniciales"))
        self.label_2.setText(_translate("WidgetDataFilter", "Selecciones las variables del modelaje"))
        self.pushButtonNext.setText(_translate("WidgetDataFilter", "Siguiente paso"))

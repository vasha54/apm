# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_comparative_model.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetComparativeModel(object):
    def setupUi(self, WidgetComparativeModel):
        WidgetComparativeModel.setObjectName("WidgetComparativeModel")
        WidgetComparativeModel.resize(674, 421)
        self.gridLayout = QtWidgets.QGridLayout(WidgetComparativeModel)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(WidgetComparativeModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listViewModel = QtWidgets.QListView(WidgetComparativeModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewModel.sizePolicy().hasHeightForWidth())
        self.listViewModel.setSizePolicy(sizePolicy)
        self.listViewModel.setObjectName("listViewModel")
        self.verticalLayout.addWidget(self.listViewModel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pBCompare = QtWidgets.QPushButton(WidgetComparativeModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBCompare.sizePolicy().hasHeightForWidth())
        self.pBCompare.setSizePolicy(sizePolicy)
        self.pBCompare.setObjectName("pBCompare")
        self.horizontalLayout.addWidget(self.pBCompare)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(488, 5, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.widgetChartComparative = QtWidgets.QWidget(WidgetComparativeModel)
        self.widgetChartComparative.setStyleSheet("")
        self.widgetChartComparative.setObjectName("widgetChartComparative")
        self.vLayoutChartComparative = QtWidgets.QVBoxLayout(self.widgetChartComparative)
        self.vLayoutChartComparative.setObjectName("vLayoutChartComparative")
        self.gridLayout.addWidget(self.widgetChartComparative, 1, 1, 1, 1)
        self.tableViewModelCom = QtWidgets.QTableView(WidgetComparativeModel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewModelCom.sizePolicy().hasHeightForWidth())
        self.tableViewModelCom.setSizePolicy(sizePolicy)
        self.tableViewModelCom.setObjectName("tableViewModelCom")
        self.gridLayout.addWidget(self.tableViewModelCom, 2, 0, 1, 2)

        self.retranslateUi(WidgetComparativeModel)
        QtCore.QMetaObject.connectSlotsByName(WidgetComparativeModel)

    def retranslateUi(self, WidgetComparativeModel):
        _translate = QtCore.QCoreApplication.translate
        WidgetComparativeModel.setWindowTitle(_translate("WidgetComparativeModel", "Form"))
        self.label.setText(_translate("WidgetComparativeModel", "Modelos :"))
        self.pBCompare.setText(_translate("WidgetComparativeModel", "Comparar"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_charts_variable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetChartsVariables(object):
    def setupUi(self, WidgetChartsVariables):
        WidgetChartsVariables.setObjectName("WidgetChartsVariables")
        WidgetChartsVariables.resize(861, 471)
        self.gridLayout = QtWidgets.QGridLayout(WidgetChartsVariables)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetChart = QtWidgets.QTableWidget(WidgetChartsVariables)
        self.tableWidgetChart.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidgetChart.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidgetChart.setLineWidth(0)
        self.tableWidgetChart.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidgetChart.setShowGrid(False)
        self.tableWidgetChart.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidgetChart.setColumnCount(3)
        self.tableWidgetChart.setObjectName("tableWidgetChart")
        self.tableWidgetChart.setRowCount(0)
        self.tableWidgetChart.horizontalHeader().setVisible(False)
        self.tableWidgetChart.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidgetChart, 0, 0, 1, 2)

        self.retranslateUi(WidgetChartsVariables)
        QtCore.QMetaObject.connectSlotsByName(WidgetChartsVariables)

    def retranslateUi(self, WidgetChartsVariables):
        _translate = QtCore.QCoreApplication.translate
        WidgetChartsVariables.setWindowTitle(_translate("WidgetChartsVariables", "Form"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_data_filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetDataFilter(object):
    def setupUi(self, WidgetDataFilter):
        WidgetDataFilter.setObjectName("WidgetDataFilter")
        WidgetDataFilter.resize(882, 471)
        self.gridLayout_3 = QtWidgets.QGridLayout(WidgetDataFilter)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
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
        self.tableViewDataFrame = QtWidgets.QTableView(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewDataFrame.sizePolicy().hasHeightForWidth())
        self.tableViewDataFrame.setSizePolicy(sizePolicy)
        self.tableViewDataFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewDataFrame.setObjectName("tableViewDataFrame")
        self.verticalLayout.addWidget(self.tableViewDataFrame)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listViewVariable = QtWidgets.QListView(WidgetDataFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewVariable.sizePolicy().hasHeightForWidth())
        self.listViewVariable.setSizePolicy(sizePolicy)
        self.listViewVariable.setMinimumSize(QtCore.QSize(250, 0))
        self.listViewVariable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listViewVariable.setObjectName("listViewVariable")
        self.verticalLayout_2.addWidget(self.listViewVariable)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 158, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.gBVariable = QtWidgets.QGroupBox(WidgetDataFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gBVariable.setFont(font)
        self.gBVariable.setObjectName("gBVariable")
        self.gridLayout = QtWidgets.QGridLayout(self.gBVariable)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lOMedia = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMedia.setFont(font)
        self.lOMedia.setObjectName("lOMedia")
        self.gridLayout.addWidget(self.lOMedia, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.lOMedian = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOMedian.sizePolicy().hasHeightForWidth())
        self.lOMedian.setSizePolicy(sizePolicy)
        self.lOMedian.setObjectName("lOMedian")
        self.gridLayout.addWidget(self.lOMedian, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lOCV = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOCV.setFont(font)
        self.lOCV.setObjectName("lOCV")
        self.gridLayout.addWidget(self.lOCV, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.lOMax = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOMax.sizePolicy().hasHeightForWidth())
        self.lOMax.setSizePolicy(sizePolicy)
        self.lOMax.setObjectName("lOMax")
        self.gridLayout.addWidget(self.lOMax, 1, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.lOMin = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOMin.sizePolicy().hasHeightForWidth())
        self.lOMin.setSizePolicy(sizePolicy)
        self.lOMin.setObjectName("lOMin")
        self.gridLayout.addWidget(self.lOMin, 2, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.lONumberMeas = QtWidgets.QLabel(self.gBVariable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lONumberMeas.sizePolicy().hasHeightForWidth())
        self.lONumberMeas.setSizePolicy(sizePolicy)
        self.lONumberMeas.setObjectName("lONumberMeas")
        self.gridLayout.addWidget(self.lONumberMeas, 3, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gBVariable)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 4, 1, 1)
        self.gridLayout_2.addWidget(self.gBVariable, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(WidgetDataFilter)
        QtCore.QMetaObject.connectSlotsByName(WidgetDataFilter)

    def retranslateUi(self, WidgetDataFilter):
        _translate = QtCore.QCoreApplication.translate
        WidgetDataFilter.setWindowTitle(_translate("WidgetDataFilter", "Form"))
        self.label.setText(_translate("WidgetDataFilter", "Datos Iniciales"))
        self.label_2.setText(_translate("WidgetDataFilter", "Seleccione las variables para los gráficos de dispersión"))
        self.gBVariable.setTitle(_translate("WidgetDataFilter", "Detalles de la variable"))
        self.label_3.setText(_translate("WidgetDataFilter", "Media"))
        self.lOMedia.setText(_translate("WidgetDataFilter", "NA"))
        self.lOMedian.setText(_translate("WidgetDataFilter", "Mediana"))
        self.label_18.setText(_translate("WidgetDataFilter", "NA"))
        self.label_4.setText(_translate("WidgetDataFilter", "CV (%)"))
        self.lOCV.setText(_translate("WidgetDataFilter", "NA"))
        self.lOMax.setText(_translate("WidgetDataFilter", "Máximo"))
        self.label_13.setText(_translate("WidgetDataFilter", "NA"))
        self.label_5.setText(_translate("WidgetDataFilter", "Varianza"))
        self.label_9.setText(_translate("WidgetDataFilter", "NA"))
        self.lOMin.setText(_translate("WidgetDataFilter", "Mínimo"))
        self.label_16.setText(_translate("WidgetDataFilter", "NA"))
        self.label_6.setText(_translate("WidgetDataFilter", "Desviación Estándar"))
        self.label_10.setText(_translate("WidgetDataFilter", "NA"))
        self.lONumberMeas.setText(_translate("WidgetDataFilter", "Cant. Obser."))
        self.label_14.setText(_translate("WidgetDataFilter", "NA"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_test_quality_adjust.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetTestQualityAdjust(object):
    def setupUi(self, WidgetTestQualityAdjust):
        WidgetTestQualityAdjust.setObjectName("WidgetTestQualityAdjust")
        WidgetTestQualityAdjust.resize(803, 362)
        self.horizontalLayout = QtWidgets.QHBoxLayout(WidgetTestQualityAdjust)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(WidgetTestQualityAdjust)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
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
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lORMSE = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lORMSE.sizePolicy().hasHeightForWidth())
        self.lORMSE.setSizePolicy(sizePolicy)
        self.lORMSE.setObjectName("lORMSE")
        self.gridLayout.addWidget(self.lORMSE, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.dSBLevelSignification = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dSBLevelSignification.sizePolicy().hasHeightForWidth())
        self.dSBLevelSignification.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dSBLevelSignification.setFont(font)
        self.dSBLevelSignification.setMaximum(1.0)
        self.dSBLevelSignification.setSingleStep(0.01)
        self.dSBLevelSignification.setProperty("value", 0.05)
        self.dSBLevelSignification.setObjectName("dSBLevelSignification")
        self.horizontalLayout_2.addWidget(self.dSBLevelSignification)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pBCalculate = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pBCalculate.setFont(font)
        self.pBCalculate.setObjectName("pBCalculate")
        self.horizontalLayout_3.addWidget(self.pBCalculate)
        spacerItem3 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)
        self.horizontalLayout.addWidget(self.widget)
        self.widgetResult = QtWidgets.QWidget(WidgetTestQualityAdjust)
        self.widgetResult.setObjectName("widgetResult")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetResult)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widgetResult)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lOSSfa = QtWidgets.QLabel(self.widgetResult)
        self.lOSSfa.setObjectName("lOSSfa")
        self.gridLayout_2.addWidget(self.lOSSfa, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lOSSpe = QtWidgets.QLabel(self.widgetResult)
        self.lOSSpe.setObjectName("lOSSpe")
        self.gridLayout_2.addWidget(self.lOSSpe, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.lOCountObsv = QtWidgets.QLabel(self.widgetResult)
        self.lOCountObsv.setObjectName("lOCountObsv")
        self.gridLayout_2.addWidget(self.lOCountObsv, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.lOCountLevelVarInde = QtWidgets.QLabel(self.widgetResult)
        self.lOCountLevelVarInde.setObjectName("lOCountLevelVarInde")
        self.gridLayout_2.addWidget(self.lOCountLevelVarInde, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.lOEstFisCalFO = QtWidgets.QLabel(self.widgetResult)
        self.lOEstFisCalFO.setObjectName("lOEstFisCalFO")
        self.gridLayout_2.addWidget(self.lOEstFisCalFO, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)
        self.lOEstFisTabFO = QtWidgets.QLabel(self.widgetResult)
        self.lOEstFisTabFO.setObjectName("lOEstFisTabFO")
        self.gridLayout_2.addWidget(self.lOEstFisTabFO, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widgetResult)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 0, 1, 1)
        self.lORelationFOFt = QtWidgets.QLabel(self.widgetResult)
        self.lORelationFOFt.setObjectName("lORelationFOFt")
        self.gridLayout_2.addWidget(self.lORelationFOFt, 7, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widgetResult)

        self.retranslateUi(WidgetTestQualityAdjust)
        QtCore.QMetaObject.connectSlotsByName(WidgetTestQualityAdjust)

    def retranslateUi(self, WidgetTestQualityAdjust):
        _translate = QtCore.QCoreApplication.translate
        WidgetTestQualityAdjust.setWindowTitle(_translate("WidgetTestQualityAdjust", "Form"))
        self.label.setText(_translate("WidgetTestQualityAdjust", "RMSE:"))
        self.lORMSE.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_3.setText(_translate("WidgetTestQualityAdjust", "Relacion entre el rango de los\n"
"valores ajustados y el error estandar\n"
"promedio estimado"))
        self.label_4.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.groupBox.setTitle(_translate("WidgetTestQualityAdjust", "Prueba de bondad de ajuste de Fisher"))
        self.label_5.setText(_translate("WidgetTestQualityAdjust", "NIvel de significacion:"))
        self.pBCalculate.setText(_translate("WidgetTestQualityAdjust", "Calcular"))
        self.label_6.setText(_translate("WidgetTestQualityAdjust", "Resultado de la Prueba de bondad\n"
"de Ajuste de Fisher"))
        self.label_7.setText(_translate("WidgetTestQualityAdjust", "SSfa:"))
        self.lOSSfa.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_8.setText(_translate("WidgetTestQualityAdjust", "SSpe:"))
        self.lOSSpe.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_9.setText(_translate("WidgetTestQualityAdjust", "Cantidad de observaciones:"))
        self.lOCountObsv.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_10.setText(_translate("WidgetTestQualityAdjust", "Cantidad de niveles de las\n"
"variables independientes:"))
        self.lOCountLevelVarInde.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_11.setText(_translate("WidgetTestQualityAdjust", "Estadigráfo de Fisher calculado (Fo):"))
        self.lOEstFisCalFO.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_12.setText(_translate("WidgetTestQualityAdjust", "Estadigráfo de Fisher tabulado (Ft):"))
        self.lOEstFisTabFO.setText(_translate("WidgetTestQualityAdjust", "NA"))
        self.label_13.setText(_translate("WidgetTestQualityAdjust", "Relación (Fo/Ft):"))
        self.lORelationFOFt.setText(_translate("WidgetTestQualityAdjust", "NA"))

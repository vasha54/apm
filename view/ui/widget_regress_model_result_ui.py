# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_regress_model_result.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetRegressModelResult(object):
    def setupUi(self, WidgetRegressModelResult):
        WidgetRegressModelResult.setObjectName("WidgetRegressModelResult")
        WidgetRegressModelResult.resize(869, 541)
        self.gridLayout_2 = QtWidgets.QGridLayout(WidgetRegressModelResult)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(WidgetRegressModelResult)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtWidgets.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabGeneral)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBoxDetailGeneral = QtWidgets.QGroupBox(self.tabGeneral)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDetailGeneral.setFont(font)
        self.groupBoxDetailGeneral.setFlat(False)
        self.groupBoxDetailGeneral.setObjectName("groupBoxDetailGeneral")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxDetailGeneral)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lOVariableDependent = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOVariableDependent.setFont(font)
        self.lOVariableDependent.setObjectName("lOVariableDependent")
        self.gridLayout.addWidget(self.lOVariableDependent, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lONumberObservations = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lONumberObservations.setFont(font)
        self.lONumberObservations.setObjectName("lONumberObservations")
        self.gridLayout.addWidget(self.lONumberObservations, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lOGLResidual = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOGLResidual.setFont(font)
        self.lOGLResidual.setObjectName("lOGLResidual")
        self.gridLayout.addWidget(self.lOGLResidual, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lOGLModelo = QtWidgets.QLabel(self.groupBoxDetailGeneral)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOGLModelo.setFont(font)
        self.lOGLModelo.setObjectName("lOGLModelo")
        self.gridLayout.addWidget(self.lOGLModelo, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBoxDetailGeneral, 0, 0, 1, 1)
        self.groupBoxParameterGeneralOutput = QtWidgets.QGroupBox(self.tabGeneral)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxParameterGeneralOutput.setFont(font)
        self.groupBoxParameterGeneralOutput.setObjectName("groupBoxParameterGeneralOutput")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxParameterGeneralOutput)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.lORcuad = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lORcuad.setFont(font)
        self.lORcuad.setObjectName("lORcuad")
        self.gridLayout_4.addWidget(self.lORcuad, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.lORcuadAdjust = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lORcuadAdjust.setFont(font)
        self.lORcuadAdjust.setObjectName("lORcuadAdjust")
        self.gridLayout_4.addWidget(self.lORcuadAdjust, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.lOFStadistic = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOFStadistic.setFont(font)
        self.lOFStadistic.setObjectName("lOFStadistic")
        self.gridLayout_4.addWidget(self.lOFStadistic, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)
        self.lOPValue = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOPValue.setFont(font)
        self.lOPValue.setObjectName("lOPValue")
        self.gridLayout_4.addWidget(self.lOPValue, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)
        self.lOMSEModel = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMSEModel.setFont(font)
        self.lOMSEModel.setObjectName("lOMSEModel")
        self.gridLayout_4.addWidget(self.lOMSEModel, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 5, 0, 1, 1)
        self.lOMSEResidual = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMSEResidual.setFont(font)
        self.lOMSEResidual.setObjectName("lOMSEResidual")
        self.gridLayout_4.addWidget(self.lOMSEResidual, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 1)
        self.lOMSETotal = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOMSETotal.setFont(font)
        self.lOMSETotal.setObjectName("lOMSETotal")
        self.gridLayout_4.addWidget(self.lOMSETotal, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 7, 0, 1, 1)
        self.lORMSEModel = QtWidgets.QLabel(self.groupBoxParameterGeneralOutput)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lORMSEModel.setFont(font)
        self.lORMSEModel.setObjectName("lORMSEModel")
        self.gridLayout_4.addWidget(self.lORMSEModel, 7, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBoxParameterGeneralOutput, 0, 1, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tabGeneral)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lOAIC = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOAIC.setFont(font)
        self.lOAIC.setObjectName("lOAIC")
        self.gridLayout_3.addWidget(self.lOAIC, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.lOBIC = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOBIC.setFont(font)
        self.lOBIC.setObjectName("lOBIC")
        self.gridLayout_3.addWidget(self.lOBIC, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.lOLagLikeHead = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lOLagLikeHead.setFont(font)
        self.lOLagLikeHead.setObjectName("lOLagLikeHead")
        self.gridLayout_3.addWidget(self.lOLagLikeHead, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabResultRegress = QtWidgets.QWidget()
        self.tabResultRegress.setObjectName("tabResultRegress")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabResultRegress)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableViewResultRegress = QtWidgets.QTableView(self.tabResultRegress)
        self.tableViewResultRegress.setObjectName("tableViewResultRegress")
        self.verticalLayout.addWidget(self.tableViewResultRegress)
        self.tabWidget.addTab(self.tabResultRegress, "")
        self.tabIntervalEstimateCoefRegress = QtWidgets.QWidget()
        self.tabIntervalEstimateCoefRegress.setObjectName("tabIntervalEstimateCoefRegress")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabIntervalEstimateCoefRegress)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableViewIntervalEstimateCoeRegress = QtWidgets.QTableView(self.tabIntervalEstimateCoefRegress)
        self.tableViewIntervalEstimateCoeRegress.setObjectName("tableViewIntervalEstimateCoeRegress")
        self.verticalLayout_2.addWidget(self.tableViewIntervalEstimateCoeRegress)
        self.tabWidget.addTab(self.tabIntervalEstimateCoefRegress, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(WidgetRegressModelResult)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WidgetRegressModelResult)

    def retranslateUi(self, WidgetRegressModelResult):
        _translate = QtCore.QCoreApplication.translate
        WidgetRegressModelResult.setWindowTitle(_translate("WidgetRegressModelResult", "Form"))
        self.groupBoxDetailGeneral.setTitle(_translate("WidgetRegressModelResult", "Detalles generales"))
        self.label.setText(_translate("WidgetRegressModelResult", "Variable dependiente:"))
        self.lOVariableDependent.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_2.setText(_translate("WidgetRegressModelResult", "No. de observaciones:"))
        self.lONumberObservations.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_3.setText(_translate("WidgetRegressModelResult", "GL de los residuales:"))
        self.lOGLResidual.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_4.setText(_translate("WidgetRegressModelResult", "GL del modelo:"))
        self.lOGLModelo.setText(_translate("WidgetRegressModelResult", "NA"))
        self.groupBoxParameterGeneralOutput.setTitle(_translate("WidgetRegressModelResult", "Parámetros generales de salida"))
        self.label_8.setText(_translate("WidgetRegressModelResult", "R-cuad:"))
        self.lORcuad.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_9.setText(_translate("WidgetRegressModelResult", "R-cuad ajustada:"))
        self.lORcuadAdjust.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_10.setText(_translate("WidgetRegressModelResult", "F estadístico:"))
        self.lOFStadistic.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_11.setText(_translate("WidgetRegressModelResult", "P- valor:"))
        self.lOPValue.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_12.setText(_translate("WidgetRegressModelResult", "MSE modelo:"))
        self.lOMSEModel.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_13.setText(_translate("WidgetRegressModelResult", "MSE residuales:"))
        self.lOMSEResidual.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_14.setText(_translate("WidgetRegressModelResult", "MSE total:"))
        self.lOMSETotal.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_15.setText(_translate("WidgetRegressModelResult", "RMSE modelo"))
        self.lORMSEModel.setText(_translate("WidgetRegressModelResult", "NA"))
        self.groupBox.setTitle(_translate("WidgetRegressModelResult", "Otros parámetros de análisis"))
        self.label_5.setText(_translate("WidgetRegressModelResult", "AIC:"))
        self.lOAIC.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_6.setText(_translate("WidgetRegressModelResult", "BIC:"))
        self.lOBIC.setText(_translate("WidgetRegressModelResult", "NA"))
        self.label_7.setText(_translate("WidgetRegressModelResult", "Lag-likelihead:"))
        self.lOLagLikeHead.setText(_translate("WidgetRegressModelResult", "NA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("WidgetRegressModelResult", "General"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResultRegress), _translate("WidgetRegressModelResult", "Resultados de la regresión"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIntervalEstimateCoefRegress), _translate("WidgetRegressModelResult", "Intervalo de estimación de los coeficientes de regresión"))
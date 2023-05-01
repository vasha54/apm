# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_analys_multi_colinualidad.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetAnalysMultiColinualidad(object):
    def setupUi(self, WidgetAnalysMultiColinualidad):
        WidgetAnalysMultiColinualidad.setObjectName("WidgetAnalysMultiColinualidad")
        WidgetAnalysMultiColinualidad.resize(746, 504)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetAnalysMultiColinualidad)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableViewMultiColinealidad = QtWidgets.QTableView(WidgetAnalysMultiColinualidad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewMultiColinealidad.sizePolicy().hasHeightForWidth())
        self.tableViewMultiColinealidad.setSizePolicy(sizePolicy)
        self.tableViewMultiColinealidad.setMaximumSize(QtCore.QSize(16777215, 70))
        self.tableViewMultiColinealidad.setObjectName("tableViewMultiColinealidad")
        self.verticalLayout.addWidget(self.tableViewMultiColinealidad)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.sBPower = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sBPower.sizePolicy().hasHeightForWidth())
        self.sBPower.setSizePolicy(sizePolicy)
        self.sBPower.setMinimumSize(QtCore.QSize(0, 0))
        self.sBPower.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sBPower.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sBPower.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sBPower.setMinimum(2)
        self.sBPower.setMaximum(10)
        self.sBPower.setObjectName("sBPower")
        self.gridLayout_5.addWidget(self.sBPower, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 2, 1, 1)
        self.pBCalculate = QtWidgets.QPushButton(self.frame)
        self.pBCalculate.setObjectName("pBCalculate")
        self.gridLayout_5.addWidget(self.pBCalculate, 1, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
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
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lOutputTestRamseyF = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestRamseyF.sizePolicy().hasHeightForWidth())
        self.lOutputTestRamseyF.setSizePolicy(sizePolicy)
        self.lOutputTestRamseyF.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lOutputTestRamseyF.setObjectName("lOutputTestRamseyF")
        self.horizontalLayout_2.addWidget(self.lOutputTestRamseyF)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(126, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.lOutputTestRamseyPValue = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestRamseyPValue.sizePolicy().hasHeightForWidth())
        self.lOutputTestRamseyPValue.setSizePolicy(sizePolicy)
        self.lOutputTestRamseyPValue.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lOutputTestRamseyPValue.setObjectName("lOutputTestRamseyPValue")
        self.horizontalLayout.addWidget(self.lOutputTestRamseyPValue)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 3, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 5)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
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
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        self.lOutputTestHarveyCollierHC = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestHarveyCollierHC.sizePolicy().hasHeightForWidth())
        self.lOutputTestHarveyCollierHC.setSizePolicy(sizePolicy)
        self.lOutputTestHarveyCollierHC.setObjectName("lOutputTestHarveyCollierHC")
        self.gridLayout_4.addWidget(self.lOutputTestHarveyCollierHC, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(192, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 1, 3, 1, 1)
        self.lOutputTestHarveyCollierPValue = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestHarveyCollierPValue.sizePolicy().hasHeightForWidth())
        self.lOutputTestHarveyCollierPValue.setSizePolicy(sizePolicy)
        self.lOutputTestHarveyCollierPValue.setObjectName("lOutputTestHarveyCollierPValue")
        self.gridLayout_4.addWidget(self.lOutputTestHarveyCollierPValue, 1, 4, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lOutputMeanResidualNotScaled = QtWidgets.QLabel(self.frame_2)
        self.lOutputMeanResidualNotScaled.setObjectName("lOutputMeanResidualNotScaled")
        self.gridLayout.addWidget(self.lOutputMeanResidualNotScaled, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lOutputMeanResidualStudentized = QtWidgets.QLabel(self.frame_2)
        self.lOutputMeanResidualStudentized.setObjectName("lOutputMeanResidualStudentized")
        self.gridLayout.addWidget(self.lOutputMeanResidualStudentized, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 5)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.lOutputTestRainbowF = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestRainbowF.sizePolicy().hasHeightForWidth())
        self.lOutputTestRainbowF.setSizePolicy(sizePolicy)
        self.lOutputTestRainbowF.setObjectName("lOutputTestRainbowF")
        self.gridLayout_3.addWidget(self.lOutputTestRainbowF, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(204, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 1, 3, 1, 1)
        self.lOutputTestRainbowPValue = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestRainbowPValue.sizePolicy().hasHeightForWidth())
        self.lOutputTestRainbowPValue.setSizePolicy(sizePolicy)
        self.lOutputTestRainbowPValue.setObjectName("lOutputTestRainbowPValue")
        self.gridLayout_3.addWidget(self.lOutputTestRainbowPValue, 1, 4, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 5)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
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
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.lOutputLangrageF = QtWidgets.QLabel(self.frame_6)
        self.lOutputLangrageF.setObjectName("lOutputLangrageF")
        self.gridLayout_6.addWidget(self.lOutputLangrageF, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(204, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 1, 3, 1, 1)
        self.lOutputLangragePValue = QtWidgets.QLabel(self.frame_6)
        self.lOutputLangragePValue.setObjectName("lOutputLangragePValue")
        self.gridLayout_6.addWidget(self.lOutputLangragePValue, 1, 4, 1, 1)
        self.gridLayout_7.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(WidgetAnalysMultiColinualidad)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 5)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
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
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lOutputTestWhiteWE = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestWhiteWE.sizePolicy().hasHeightForWidth())
        self.lOutputTestWhiteWE.setSizePolicy(sizePolicy)
        self.lOutputTestWhiteWE.setObjectName("lOutputTestWhiteWE")
        self.gridLayout_2.addWidget(self.lOutputTestWhiteWE, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
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
        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)
        self.lOutputTestWhitePValue = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lOutputTestWhitePValue.sizePolicy().hasHeightForWidth())
        self.lOutputTestWhitePValue.setSizePolicy(sizePolicy)
        self.lOutputTestWhitePValue.setObjectName("lOutputTestWhitePValue")
        self.gridLayout_2.addWidget(self.lOutputTestWhitePValue, 1, 4, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        spacerItem6 = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(WidgetAnalysMultiColinualidad)
        QtCore.QMetaObject.connectSlotsByName(WidgetAnalysMultiColinualidad)

    def retranslateUi(self, WidgetAnalysMultiColinualidad):
        _translate = QtCore.QCoreApplication.translate
        WidgetAnalysMultiColinualidad.setWindowTitle(_translate("WidgetAnalysMultiColinualidad", "Form"))
        self.label.setText(_translate("WidgetAnalysMultiColinualidad", "Test Ramsey (Prueba de especificación)"))
        self.label_2.setText(_translate("WidgetAnalysMultiColinualidad", "Potencia:"))
        self.pBCalculate.setText(_translate("WidgetAnalysMultiColinualidad", "Calcular"))
        self.label_3.setText(_translate("WidgetAnalysMultiColinualidad", "F:"))
        self.lOutputTestRamseyF.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_16.setText(_translate("WidgetAnalysMultiColinualidad", "P-valor:"))
        self.lOutputTestRamseyPValue.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_8.setText(_translate("WidgetAnalysMultiColinualidad", "Prueba de Harvey-Collier de linealidad"))
        self.label_12.setText(_translate("WidgetAnalysMultiColinualidad", "HC:"))
        self.lOutputTestHarveyCollierHC.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_23.setText(_translate("WidgetAnalysMultiColinualidad", "P-valor:"))
        self.lOutputTestHarveyCollierPValue.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_4.setText(_translate("WidgetAnalysMultiColinualidad", "Media de los residuales sin escalamiento:"))
        self.lOutputMeanResidualNotScaled.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_5.setText(_translate("WidgetAnalysMultiColinualidad", "Media de los residuales estudentizados:"))
        self.lOutputMeanResidualStudentized.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_7.setText(_translate("WidgetAnalysMultiColinualidad", "Prueba de Rainbow de linealidad"))
        self.label_14.setText(_translate("WidgetAnalysMultiColinualidad", "F:"))
        self.lOutputTestRainbowF.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_22.setText(_translate("WidgetAnalysMultiColinualidad", "P-valor:"))
        self.lOutputTestRainbowPValue.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_9.setText(_translate("WidgetAnalysMultiColinualidad", "Prueba de los multiplicadores de Langrage \n"
"para linealidad"))
        self.label_13.setText(_translate("WidgetAnalysMultiColinualidad", "F:"))
        self.lOutputLangrageF.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_15.setText(_translate("WidgetAnalysMultiColinualidad", "P-valor:"))
        self.lOutputLangragePValue.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_6.setText(_translate("WidgetAnalysMultiColinualidad", "Prueba de especificación de White"))
        self.label_10.setText(_translate("WidgetAnalysMultiColinualidad", "WE:"))
        self.lOutputTestWhiteWE.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
        self.label_11.setText(_translate("WidgetAnalysMultiColinualidad", "P-valor:"))
        self.lOutputTestWhitePValue.setText(_translate("WidgetAnalysMultiColinualidad", "NA"))
